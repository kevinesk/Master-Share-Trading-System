"""
KLSE Screener Backtester  (validates the VCP-breakout edge)
============================================================
Walks 5 years of history for every stock in universe.txt and simulates the
exact strategy the screener flags:

    ENTRY   : price closes above the PIVOT_LOOKBACK-day high (the VCP pivot)
              on a volume surge (>=1.5x 20-day avg), while above EMA50
    STOP    : the lower of  (coil low)  or  (entry - MAX_STOP_PCT)
    MANAGE  : raise stop to breakeven once the trade is +1R
    EXIT    : hard stop hit, OR daily close falls below EMA20 (trend break)

It runs the SAME signals twice to measure the cost of being a latecomer:
    ON-PIVOT : enter on the breakout day's close          (what the screener wants)
    LATE     : enter LATE_BARS days after the breakout     (chasing an extended stock)

The gap between the two expectancy numbers is the price of buying STAGE 3
instead of STAGE 2 — the exact mistake the staged screener now prevents.

Requirements:  pip install yfinance pandas numpy curl_cffi
Usage:         double-click run_backtest.bat   OR   python backtest_screener.py
"""

import sys
import datetime
import webbrowser
import warnings
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

warnings.filterwarnings("ignore")

try:
    import yfinance as yf
    import pandas as pd
    import numpy as np
except ImportError:
    sys.exit("ERROR: Run:  pip install yfinance pandas numpy")

try:
    from curl_cffi import requests as curl_requests
    _SESSION = curl_requests.Session(verify=False, impersonate="chrome")
except ImportError:
    _SESSION = None

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════════════
SCRIPT_DIR    = Path(__file__).parent
UNIVERSE_FILE = SCRIPT_DIR / "universe.txt"
OUTPUT_DIR    = SCRIPT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

TODAY        = datetime.date.today().strftime("%Y-%m-%d")
OUTPUT_HTML  = OUTPUT_DIR / f"backtest_{TODAY}.html"
OUTPUT_CSV   = OUTPUT_DIR / f"backtest_{TODAY}.csv"

BACKTEST_YEARS = 5
MAX_WORKERS    = 8

# strategy parameters — kept identical to klse_screener.py
PIVOT_LOOKBACK = 15        # trading days — base whose high is the pivot
VOL_SURGE_X    = 1.5       # breakout volume vs 20-day avg
MAX_STOP_PCT   = 8.0       # hard stop never wider than this
EMA_SHORT      = 20
EMA_MID        = 50

LATE_BARS      = 3         # "latecomer" entry = this many days after breakout

# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def ema(series: pd.Series, n: int) -> pd.Series:
    return series.ewm(span=n, adjust=False).mean()


def load_universe(path: Path) -> list[tuple[str, str]]:
    stocks = []
    if not path.exists():
        sys.exit(f"Universe file not found: {path}")
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        stocks.append((parts[0].upper(), parts[1].strip() if len(parts) > 1 else parts[0]))
    return stocks

# ═══════════════════════════════════════════════════════════════════════════════
# SINGLE-STOCK SIMULATION
# ═══════════════════════════════════════════════════════════════════════════════

def simulate(ticker: str, name: str, late_bars: int) -> list[dict]:
    """Return a list of completed trades for one stock."""
    trades: list[dict] = []
    try:
        stock = yf.Ticker(ticker, session=_SESSION)
        df = stock.history(period=f"{BACKTEST_YEARS}y")
        if df.empty or len(df) < 120:
            return trades

        close  = df["Close"].to_numpy(dtype=float)
        high   = df["High"].to_numpy(dtype=float)
        low    = df["Low"].to_numpy(dtype=float)
        vol    = df["Volume"].to_numpy(dtype=float)
        dates  = df.index
        e20    = ema(df["Close"], EMA_SHORT).to_numpy(dtype=float)
        e50    = ema(df["Close"], EMA_MID).to_numpy(dtype=float)
        avg20  = pd.Series(vol).rolling(20).mean().to_numpy(dtype=float)

        n = len(close)
        i = 60
        while i < n - 1:
            # ── breakout signal at bar i ─────────────────────────────────────
            lo_slice = max(0, i - PIVOT_LOOKBACK)
            pivot    = high[lo_slice:i].max()
            coil_low = low[lo_slice:i].min()
            signal = (close[i] > pivot and close[i - 1] <= pivot
                      and not np.isnan(avg20[i]) and avg20[i] > 0
                      and vol[i] >= VOL_SURGE_X * avg20[i]
                      and close[i] > e50[i])
            if not signal:
                i += 1
                continue

            # ── entry (on-pivot or late) ─────────────────────────────────────
            entry_idx = i + late_bars
            if entry_idx >= n - 1:
                break
            entry = close[entry_idx]
            stop  = max(coil_low, entry * (1 - MAX_STOP_PCT / 100))
            if stop >= entry:                       # safety
                stop = entry * (1 - MAX_STOP_PCT / 100)
            risk = entry - stop
            if risk <= 0:
                i += 1
                continue

            # ── walk the trade forward ───────────────────────────────────────
            exit_price = None
            exit_idx   = None
            be_moved   = False
            for j in range(entry_idx + 1, n):
                if low[j] <= stop:                  # hard / breakeven stop hit
                    exit_price, exit_idx = stop, j
                    break
                if not be_moved and high[j] >= entry + risk:   # +1R -> breakeven
                    stop = max(stop, entry)
                    be_moved = True
                if close[j] < e20[j]:               # trend break -> exit
                    exit_price, exit_idx = close[j], j
                    break
            if exit_price is None:                  # still open at data end
                exit_price, exit_idx = close[-1], n - 1

            r_mult   = (exit_price - entry) / risk
            hold     = exit_idx - entry_idx
            trades.append({
                "ticker": ticker, "name": name,
                "entry_date": dates[entry_idx].strftime("%Y-%m-%d"),
                "exit_date":  dates[exit_idx].strftime("%Y-%m-%d"),
                "entry": round(entry, 4), "stop": round(stop, 4),
                "exit": round(exit_price, 4),
                "R": round(r_mult, 3), "hold_days": hold,
                "win": r_mult > 0,
            })
            i = exit_idx + 1                        # no overlapping trades
    except Exception:
        return trades
    return trades

# ═══════════════════════════════════════════════════════════════════════════════
# AGGREGATE METRICS
# ═══════════════════════════════════════════════════════════════════════════════

def metrics(trades: list[dict]) -> dict:
    m = {"trades": 0, "win_rate": 0.0, "avg_win": 0.0, "avg_loss": 0.0,
         "expectancy": 0.0, "profit_factor": 0.0, "total_R": 0.0,
         "max_dd": 0.0, "max_consec_loss": 0, "avg_hold": 0.0}
    if not trades:
        return m
    Rs   = [t["R"] for t in trades]
    wins = [r for r in Rs if r > 0]
    loss = [r for r in Rs if r <= 0]
    m["trades"]     = len(Rs)
    m["win_rate"]   = len(wins) / len(Rs) * 100
    m["avg_win"]    = sum(wins) / len(wins) if wins else 0.0
    m["avg_loss"]   = sum(loss) / len(loss) if loss else 0.0
    m["expectancy"] = sum(Rs) / len(Rs)
    m["total_R"]    = sum(Rs)
    m["profit_factor"] = (sum(wins) / abs(sum(loss))) if loss and sum(loss) != 0 else float("inf")
    m["avg_hold"]   = sum(t["hold_days"] for t in trades) / len(trades)

    # equity curve drawdown (in R)
    equity, peak, dd = 0.0, 0.0, 0.0
    for r in Rs:
        equity += r
        peak = max(peak, equity)
        dd = min(dd, equity - peak)
    m["max_dd"] = dd

    # max consecutive losses
    streak = best = 0
    for r in Rs:
        if r <= 0:
            streak += 1
            best = max(best, streak)
        else:
            streak = 0
    m["max_consec_loss"] = best
    return m

# ═══════════════════════════════════════════════════════════════════════════════
# HTML REPORT
# ═══════════════════════════════════════════════════════════════════════════════

def _mcell(label, val, good=None, fmt="{:.2f}"):
    color = "#212529"
    if good is not None:
        color = "#198754" if good else "#dc3545"
    return (f'<div style="background:#fff;border:1px solid #dee2e6;border-radius:8px;'
            f'padding:12px 18px;text-align:center;min-width:120px;">'
            f'<div style="font-size:22px;font-weight:700;color:{color};">'
            f'{fmt.format(val) if isinstance(val,(int,float)) else val}</div>'
            f'<div style="font-size:11px;color:#666;">{label}</div></div>')


def build_html(on_m: dict, late_m: dict, on_trades: list[dict],
               generated_at: str) -> str:
    verdict_ok = on_m["expectancy"] > 0
    verdict = (f'EDGE CONFIRMED — on-pivot entry expectancy is +{on_m["expectancy"]:.3f}R per trade'
               if verdict_ok else
               f'NO EDGE — on-pivot expectancy is {on_m["expectancy"]:.3f}R; do not trade this as-is')
    verdict_bg = "#d4edda" if verdict_ok else "#f8d7da"
    verdict_col = "#198754" if verdict_ok else "#dc3545"

    edge_loss = on_m["expectancy"] - late_m["expectancy"]

    on_cards = "".join([
        _mcell("Trades", on_m["trades"], fmt="{:.0f}"),
        _mcell("Win Rate %", on_m["win_rate"], on_m["win_rate"] >= 40),
        _mcell("Expectancy (R)", on_m["expectancy"], on_m["expectancy"] > 0, "{:+.3f}"),
        _mcell("Profit Factor", on_m["profit_factor"], on_m["profit_factor"] >= 1.5),
        _mcell("Avg Win (R)", on_m["avg_win"], True, "{:+.2f}"),
        _mcell("Avg Loss (R)", on_m["avg_loss"], False, "{:+.2f}"),
        _mcell("Total (R)", on_m["total_R"], on_m["total_R"] > 0, "{:+.1f}"),
        _mcell("Max DD (R)", on_m["max_dd"], on_m["max_dd"] > -15, "{:.1f}"),
        _mcell("Max Consec Loss", on_m["max_consec_loss"], on_m["max_consec_loss"] <= 8, "{:.0f}"),
        _mcell("Avg Hold (days)", on_m["avg_hold"], None, "{:.0f}"),
    ])

    # comparison table
    def row(label, a, b, fmt="{:.3f}", higher_better=True):
        better = "#198754"
        a_col = better if ((a > b) == higher_better and a != b) else "#212529"
        b_col = better if ((b > a) == higher_better and a != b) else "#212529"
        return (f'<tr><td style="padding:7px 12px;">{label}</td>'
                f'<td style="padding:7px 12px;text-align:right;font-weight:700;color:{a_col};">{fmt.format(a)}</td>'
                f'<td style="padding:7px 12px;text-align:right;font-weight:700;color:{b_col};">{fmt.format(b)}</td></tr>')

    cmp_rows = "".join([
        row("Expectancy (R / trade)", on_m["expectancy"], late_m["expectancy"], "{:+.3f}"),
        row("Win Rate (%)",           on_m["win_rate"],   late_m["win_rate"],   "{:.1f}"),
        row("Profit Factor",          on_m["profit_factor"], late_m["profit_factor"], "{:.2f}"),
        row("Total (R)",              on_m["total_R"],    late_m["total_R"],    "{:+.1f}"),
        row("Avg Win (R)",            on_m["avg_win"],    late_m["avg_win"],    "{:+.2f}"),
        row("Avg Loss (R)",           on_m["avg_loss"],   late_m["avg_loss"],   "{:+.2f}", higher_better=True),
        row("Max Drawdown (R)",       on_m["max_dd"],     late_m["max_dd"],     "{:.1f}", higher_better=True),
    ])

    # best & worst trades
    s_trades = sorted(on_trades, key=lambda t: t["R"], reverse=True)
    sample = s_trades[:8] + [{"name": "...", "ticker": "", "entry_date": "", "exit_date": "",
                              "entry": "", "exit": "", "R": "", "hold_days": "", "win": True}] \
             + s_trades[-8:] if len(s_trades) > 16 else s_trades
    tr_rows = ""
    for t in sample:
        if t["name"] == "...":
            tr_rows += '<tr><td colspan="7" style="padding:5px;text-align:center;color:#aaa;">···</td></tr>'
            continue
        rcol = "#198754" if (isinstance(t["R"], (int, float)) and t["R"] > 0) else "#dc3545"
        tr_rows += (
            f'<tr style="border-bottom:1px solid #eee;">'
            f'<td style="padding:6px 10px;font-weight:600;">{t["name"]}</td>'
            f'<td style="padding:6px 10px;font-size:11px;color:#666;">{t["entry_date"]}</td>'
            f'<td style="padding:6px 10px;font-size:11px;color:#666;">{t["exit_date"]}</td>'
            f'<td style="padding:6px 10px;text-align:right;">{t["entry"]}</td>'
            f'<td style="padding:6px 10px;text-align:right;">{t["exit"]}</td>'
            f'<td style="padding:6px 10px;text-align:right;font-weight:700;color:{rcol};">'
            f'{t["R"]:+.2f}R</td>' if isinstance(t["R"], (int, float)) else
            f'<td style="padding:6px 10px;text-align:right;">{t["R"]}</td>')
        tr_rows += f'<td style="padding:6px 10px;text-align:right;color:#666;">{t["hold_days"]}d</td></tr>'

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>KLSE Screener Backtest — {generated_at}</title>
<style>
 body {{ font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
        background:#f8f9fa;margin:0;color:#212529; }}
 .header {{ background:#1a1a2e;color:#fff;padding:18px 28px; }}
 .header h1 {{ margin:0;font-size:20px; }}
 .container {{ max-width:1100px;margin:0 auto;padding:20px 16px; }}
 table {{ width:100%;border-collapse:collapse;background:#fff;border-radius:8px;overflow:hidden; }}
 th {{ background:#f1f3f5;padding:8px 12px;text-align:left;font-size:12px;color:#555; }}
</style></head><body>
<div class="header">
  <h1>KLSE Screener Backtest — VCP Breakout Strategy</h1>
  <div style="font-size:12px;color:#adb5bd;margin-top:4px;">
    {BACKTEST_YEARS}-year history · entry = pivot breakout on volume · stop = coil low / -{MAX_STOP_PCT:.0f}% ·
    exit = stop or close below EMA20 · Generated {generated_at}</div>
</div>
<div class="container">

  <div style="background:{verdict_bg};border-radius:8px;padding:16px 20px;margin:16px 0;
              font-size:15px;font-weight:700;color:{verdict_col};">{verdict}</div>

  <h3 style="margin:18px 0 8px;">On-Pivot Entry — full results</h3>
  <div style="display:flex;gap:10px;flex-wrap:wrap;">{on_cards}</div>

  <h3 style="margin:24px 0 8px;">The Latecomer Cost — On-Pivot vs Entering {LATE_BARS} Days Late</h3>
  <p style="font-size:12px;color:#555;margin:0 0 8px;">
    Same breakout signals, same stops. The only difference is WHEN you buy.
    This is the measured cost of buying an extended stock (Stage 3) instead of
    at the pivot (Stage 2).</p>
  <table>
    <thead><tr><th>Metric</th><th style="text-align:right;">On-Pivot (Stage 2)</th>
    <th style="text-align:right;">{LATE_BARS} Days Late (Stage 3)</th></tr></thead>
    <tbody>{cmp_rows}</tbody>
  </table>
  <div style="background:#fff3cd;border-radius:8px;padding:12px 18px;margin:12px 0;font-size:13px;">
    <strong>Latecomer penalty:</strong> entering {LATE_BARS} days late costs
    <strong style="color:#dc3545;">{edge_loss:+.3f}R per trade</strong> in expectancy.
    Over {on_m['trades']} trades that is {edge_loss*on_m['trades']:+.0f}R of performance
    handed away purely by chasing.
  </div>

  <h3 style="margin:24px 0 8px;">Sample Trades (best & worst, on-pivot)</h3>
  <table>
    <thead><tr><th>Stock</th><th>Entry Date</th><th>Exit Date</th>
    <th style="text-align:right;">Entry</th><th style="text-align:right;">Exit</th>
    <th style="text-align:right;">R</th><th style="text-align:right;">Hold</th></tr></thead>
    <tbody>{tr_rows}</tbody>
  </table>

  <p style="font-size:11px;color:#888;margin-top:20px;">
    Note: backtest assumes one position per stock at a time, no commissions/slippage,
    fills at the close. Real expectancy will be slightly lower — size positions so a
    string of {on_m['max_consec_loss']}+ losses (the worst run seen here) is survivable.</p>
</div></body></html>"""

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    generated_at = datetime.datetime.now().strftime("%d %b %Y  %H:%M")
    universe = load_universe(UNIVERSE_FILE)

    print(f"\nKLSE Screener Backtester")
    print(f"Universe : {len(universe)} stocks · {BACKTEST_YEARS}-year history")
    print("-" * 60)

    on_trades: list[dict]   = []
    late_trades: list[dict] = []
    done = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {}
        for t, n in universe:
            futures[ex.submit(simulate, t, n, 0)] = (t, n, "on")
            futures[ex.submit(simulate, t, n, LATE_BARS)] = (t, n, "late")
        for fut in as_completed(futures):
            t, n, kind = futures[fut]
            try:
                res = fut.result()
            except Exception:
                res = []
            if kind == "on":
                on_trades.extend(res)
            else:
                late_trades.extend(res)
            done += 1
            if done % 40 == 0:
                print(f"  ... {done}/{len(futures)} simulations done")

    on_m   = metrics(on_trades)
    late_m = metrics(late_trades)

    print(f"\n{'='*60}")
    print(f"ON-PIVOT ENTRY  (Stage 2 — what the screener wants)")
    print(f"  Trades        : {on_m['trades']}")
    print(f"  Win rate      : {on_m['win_rate']:.1f}%")
    print(f"  Expectancy    : {on_m['expectancy']:+.3f} R / trade")
    print(f"  Profit factor : {on_m['profit_factor']:.2f}")
    print(f"  Total         : {on_m['total_R']:+.1f} R")
    print(f"  Max drawdown  : {on_m['max_dd']:.1f} R")
    print(f"  Max consec L  : {on_m['max_consec_loss']}")
    print(f"\n{LATE_BARS}-DAY-LATE ENTRY  (Stage 3 — the latecomer trap)")
    print(f"  Win rate      : {late_m['win_rate']:.1f}%")
    print(f"  Expectancy    : {late_m['expectancy']:+.3f} R / trade")
    print(f"  Profit factor : {late_m['profit_factor']:.2f}")
    print(f"\nLatecomer penalty: {on_m['expectancy']-late_m['expectancy']:+.3f} R per trade")
    print(f"{'='*60}")

    # CSV — all on-pivot trades
    if on_trades:
        pd.DataFrame(on_trades).to_csv(OUTPUT_CSV, index=False)

    html = build_html(on_m, late_m, on_trades, generated_at)
    OUTPUT_HTML.write_text(html, encoding="utf-8")
    print(f"\nHTML report : {OUTPUT_HTML}")
    print(f"CSV trades  : {OUTPUT_CSV}")
    webbrowser.open(OUTPUT_HTML.as_uri())
    print("Browser opened.")


if __name__ == "__main__":
    main()
