"""
KLSE 7-Light Macro Regime Board  (automates KLSE_MASTER_SYSTEM.md section 3)
============================================================================
Scores the weekly macro regime that drives bucket mix (section 2) and
per-trade risk (section 6). Run every Sunday before WEEKLY_ROUTINE.md,
then copy the score into MACRO_DASHBOARD.md.

Automated lights (6 of 7):
  1. KLCI trend          — close vs EMA50/EMA200 + slopes
  2. S&P 500 trend       — close vs EMA50/EMA200 + RSI zone
  3. McClellan (proxy)   — ratio-adjusted A/D oscillator over the
                           100-stock universe (universe.txt), NOT the full
                           exchange; same +/-50 thresholds apply
  4. Breadth             — % of universe above EMA50
  5. USD/MYR             — 4.20-4.40 band + 20-session rate of change
  6. Distribution days   — KLCI down >=0.2% on rising volume, last 25
                           sessions (manual fallback if volume feed empty)

Manual light (1 of 7):
  7. Foreign net flow    — no free feed; read MIDF Fund Flow report and
                           answer the prompt (or pass --flow G|Y|R)

Score -> regime -> bucket mix, exactly per the master doc tables.
OVERRIDE: Light 1 red = NO new Bucket A entries regardless of total score.

Usage:  double-click run_macro_lights.bat
        py macro_lights.py [--flow G|Y|R] [--auto]
                            --auto skips the prompt (light 7 = Yellow/0)
"""

import argparse
import csv
import datetime
import sys
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

warnings.filterwarnings("ignore")

try:
    import yfinance as yf
    import pandas as pd
except ImportError:
    sys.exit("ERROR: Run:  pip install yfinance pandas")

try:
    from curl_cffi import requests as curl_requests
    _SESSION = curl_requests.Session(verify=False, impersonate="chrome")
except ImportError:
    _SESSION = None

SCRIPT_DIR    = Path(__file__).parent
UNIVERSE_FILE = SCRIPT_DIR / "universe.txt"
HISTORY_CSV   = SCRIPT_DIR / "output" / "macro_lights_history.csv"

KLCI_TICKER   = "^KLSE"
SPX_TICKER    = "^GSPC"
USDMYR_TICKER = "MYR=X"
MAX_WORKERS   = 8

GREEN, YELLOW, RED = 1, 0, -1
LABEL = {GREEN: "GREEN  (+1)", YELLOW: "YELLOW ( 0)", RED: "RED    (-1)"}


# ── data fetch (same session pattern as klse_screener.py) ────────────────────

def fetch_history(ticker: str, period: str = "9mo") -> pd.DataFrame:
    try:
        df = yf.Ticker(ticker, session=_SESSION).history(period=period)
        return df if not df.empty else pd.DataFrame()
    except Exception:
        return pd.DataFrame()


def load_universe() -> list[str]:
    tickers = []
    for line in UNIVERSE_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            tickers.append(line.split()[0])
    return tickers


def fetch_universe_closes(tickers: list[str]) -> pd.DataFrame:
    """Daily close per ticker (columns), aligned on date index."""
    closes = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(fetch_history, t, "9mo"): t for t in tickers}
        done = 0
        for fut in as_completed(futures):
            t = futures[fut]
            df = fut.result()
            done += 1
            print(f"\r  universe download {done}/{len(tickers)}", end="")
            if not df.empty and "Close" in df:
                s = df["Close"]
                s.index = s.index.tz_localize(None).normalize()
                closes[t] = s
    print()
    return pd.DataFrame(closes)


# ── indicator helpers ────────────────────────────────────────────────────────

def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def rsi(s: pd.Series, n: int = 14) -> float:
    delta = s.diff()
    gain  = delta.clip(lower=0).rolling(n).mean()
    loss  = (-delta.clip(upper=0)).rolling(n).mean()
    rs    = gain / loss.replace(0, 1e-10)
    return float((100 - 100 / (1 + rs)).iloc[-1])


# ── the seven lights ─────────────────────────────────────────────────────────

def light_klci_trend(close: pd.Series) -> tuple[int, str]:
    e50, e200 = ema(close, 50), ema(close, 200)
    px = close.iloc[-1]
    above_both  = px > e50.iloc[-1] and px > e200.iloc[-1]
    sloping_up  = (e50.iloc[-1] > e50.iloc[-11]) and (e200.iloc[-1] > e200.iloc[-11])
    detail = (f"KLCI {px:,.2f} | EMA50 {e50.iloc[-1]:,.2f} | "
              f"EMA200 {e200.iloc[-1]:,.2f}")
    if px < e200.iloc[-1] or e50.iloc[-1] < e200.iloc[-1]:
        return RED, detail
    if above_both and sloping_up:
        return GREEN, detail
    return YELLOW, detail


def light_spx_trend(close: pd.Series) -> tuple[int, str]:
    e50, e200 = ema(close, 50), ema(close, 200)
    px, r = close.iloc[-1], rsi(close)
    detail = f"SPX {px:,.0f} | EMA50 {e50.iloc[-1]:,.0f} | RSI {r:.0f}"
    if px < e200.iloc[-1]:
        return RED, detail
    if px > e50.iloc[-1] and 50 <= r <= 70:
        return GREEN, detail
    return YELLOW, detail


def light_mcclellan(universe_close: pd.DataFrame) -> tuple[int, str]:
    chg  = universe_close.diff()
    adv  = (chg > 0).sum(axis=1)
    dec  = (chg < 0).sum(axis=1)
    tot  = (adv + dec).replace(0, 1)
    rana = 1000 * (adv - dec) / tot                  # ratio-adjusted net adv
    mcc  = (ema(rana, 19) - ema(rana, 39)).iloc[-1]
    detail = f"McClellan (universe proxy) {mcc:+.0f}"
    if mcc > 50:
        return GREEN, detail
    if mcc < -50:
        return RED, detail
    return YELLOW, detail


def light_breadth(universe_close: pd.DataFrame) -> tuple[int, str]:
    above = total = 0
    for col in universe_close:
        s = universe_close[col].dropna()
        if len(s) >= 60:
            total += 1
            if s.iloc[-1] > ema(s, 50).iloc[-1]:
                above += 1
    pct = above / total * 100 if total else 0.0
    detail = f"{above}/{total} universe stocks above EMA50 = {pct:.0f}%"
    if pct > 60:
        return GREEN, detail
    if pct < 30:
        return RED, detail
    return YELLOW, detail


def light_usdmyr(close: pd.Series) -> tuple[int, str]:
    px    = close.iloc[-1]
    chg20 = (px / close.iloc[-21] - 1) * 100 if len(close) > 21 else 0.0
    detail = f"USD/MYR {px:.4f} | 20-session change {chg20:+.1f}%"
    if chg20 >= 2.0:                                  # ringgit weakening fast
        return RED, detail
    if 4.20 <= px <= 4.40 and abs(chg20) <= 1.5:      # firm and stable
        return GREEN, detail
    return YELLOW, detail


def light_distribution(kdf: pd.DataFrame) -> tuple[int, str]:
    if kdf.empty or "Volume" not in kdf or kdf["Volume"].fillna(0).sum() == 0:
        return YELLOW, "NO VOLUME DATA - count manually on TradingView (KLCI daily)"
    last = kdf.tail(26)
    ret  = last["Close"].pct_change() * 100
    vol_up = last["Volume"] > last["Volume"].shift(1)
    n = int(((ret <= -0.2) & vol_up).tail(25).sum())
    detail = f"{n} distribution days in last 25 sessions"
    if n <= 2:
        return GREEN, detail
    if n >= 5:
        return RED, detail
    return YELLOW, detail


def light_foreign_flow(flow_arg: str | None, auto: bool) -> tuple[int, str]:
    mapping = {"G": (GREEN, "net buying"), "Y": (YELLOW, "mixed"),
               "R": (RED, "net selling 3+ days")}
    if flow_arg and flow_arg.upper() in mapping:
        v, note = mapping[flow_arg.upper()]
        return v, f"manual input: {note}"
    if auto:
        return YELLOW, "SKIPPED - check MIDF Fund Flow report, rerun with --flow G|Y|R"
    print("\nLight 7 - Foreign net flow (5-day). Source: MIDF Fund Flow weekly report.")
    ans = input("  Net buying [G], mixed [Y], net selling 3+ days [R]? (Enter=Y) ").strip().upper()
    v, note = mapping.get(ans, (YELLOW, "mixed (default)"))
    return v, f"manual input: {note}"


# ── score -> regime (master doc section 3 + section 6 tables) ────────────────

REGIMES = [
    (5,  "STRONG BULL", "A 55% | B 15% | C 10% | Cash 20%", "2.0% risk/trade, 10% max position"),
    (1,  "NEUTRAL",     "A 40% | B 25% | C 15% | Cash 20%", "1.5% risk/trade, 10% max position"),
    (-2, "WEAK",        "A 20% | B 35% | C 15% | Cash 30%", "1.0% risk/trade, 8% max position"),
    (-5, "BEAR",        "A  5% | B 15% | C 10% | Cash 70%", "0.5% risk/trade (capitulation only), 5% max"),
    (-7, "CRISIS",      "Cash 70%+ | capitulation watch",   "NO new entries"),
]


def classify(score: int):
    for floor, name, mix, sizing in REGIMES:
        if score >= floor:
            return name, mix, sizing
    return REGIMES[-1][1:]


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--flow", choices=list("GYRgyr"), help="foreign flow light: G, Y or R")
    ap.add_argument("--auto", action="store_true", help="no prompts (light 7 defaults to Yellow)")
    args = ap.parse_args()

    print("\nKLSE 7-LIGHT MACRO REGIME BOARD  (KLSE_MASTER_SYSTEM.md section 3)")
    print(f"Run date: {datetime.date.today()}")
    print("-" * 78)

    print("Downloading index data (KLCI, S&P 500, USD/MYR)...")
    kdf  = fetch_history(KLCI_TICKER)
    sdf  = fetch_history(SPX_TICKER)
    fxdf = fetch_history(USDMYR_TICKER, "6mo")
    print("Downloading universe (for McClellan proxy + breadth)...")
    uni  = fetch_universe_closes(load_universe())

    lights: list[tuple[str, int, str]] = []

    def add(name, fn, *fa):
        try:
            v, detail = fn(*fa)
        except Exception as e:
            v, detail = YELLOW, f"DATA ERROR ({str(e)[:40]}) - score manually"
        lights.append((name, v, detail))

    add("1. KLCI trend",          light_klci_trend,   kdf["Close"] if not kdf.empty else pd.Series(dtype=float))
    add("2. S&P 500 trend",       light_spx_trend,    sdf["Close"] if not sdf.empty else pd.Series(dtype=float))
    add("3. McClellan (proxy)",   light_mcclellan,    uni)
    add("4. Breadth >EMA50",      light_breadth,      uni)
    add("5. USD/MYR",             light_usdmyr,       fxdf["Close"] if not fxdf.empty else pd.Series(dtype=float))
    add("6. Distribution days",   light_distribution, kdf)
    add("7. Foreign net flow",    light_foreign_flow, args.flow, args.auto)

    score = sum(v for _, v, _ in lights)
    regime, mix, sizing = classify(score)

    print()
    for name, v, detail in lights:
        print(f"  {name:<24} {LABEL[v]:<12} {detail}")
    print("-" * 78)
    print(f"  SCORE   : {score:+d}  ->  REGIME: {regime}")
    print(f"  BUCKETS : {mix}")
    print(f"  SIZING  : {sizing}")
    if lights[0][1] == RED:
        print("  OVERRIDE: Light 1 is RED -> NO new Bucket A entries, regardless of score.")
    print("-" * 78)
    print("  Next: copy this score into Knowledge Base/MACRO_DASHBOARD.md,")
    print("  then continue WEEKLY_ROUTINE.md (sector breadth, bucket rebalance).")

    # history log
    HISTORY_CSV.parent.mkdir(exist_ok=True)
    new = not HISTORY_CSV.exists()
    with open(HISTORY_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["Date", "KLCI", "SPX", "McClellan", "Breadth",
                        "USDMYR", "Distribution", "ForeignFlow", "Score", "Regime"])
        w.writerow([datetime.date.today()] + [v for _, v, _ in lights] + [score, regime])
    print(f"  Logged to {HISTORY_CSV}")


if __name__ == "__main__":
    main()
