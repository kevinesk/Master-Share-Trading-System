"""
US Fundamental Data Fetcher v1
==============================
US sibling of the KLSE fundamentals scraper. Instead of scraping
klsescreener.com (Malaysia-only), this uses yfinance (free, no API key,
reliable US data). KLSE-specific scoring (KC Chong / Cold Eye / Tong Kooi /
MONEY) is replaced with US quality frameworks:

  - Buffett Quality 8     (replaces KC Chong)      -> /14
  - Dividend Compounder 8 (replaces Cold Eye)      -> /14
  - Quality Tier T1-T5    (replaces Tong Kooi Ong) -> /10
  - Magic Formula score   (replaces MONEY equation)-> /12
  - Composite "US Quality Grade" Q-ELITE / Q-A / Q-B / Q-C / Q-D (max 50)

Outputs JSON + an HTML report (same shape/style as the KLSE tool).

SETUP (one time):
    pip install yfinance
USAGE:
    Double-click run_fundamentals_us.bat   OR   py fetch_fundamentals_us.py

Universe file: us_universe.txt in this folder, one per line: "TICKER Name"
e.g.   AAPL  Apple
       MSFT  Microsoft
Lines starting with # are ignored.
"""

import sys
import json
import time
import datetime
import webbrowser
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    sys.exit("ERROR: pip install yfinance")

# --- Config ------------------------------------------------------------------
SCRIPT_DIR    = Path(__file__).parent
UNIVERSE_FILE = SCRIPT_DIR / "us_universe.txt"
OUTPUT_DIR    = SCRIPT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

TODAY       = datetime.date.today().strftime("%Y-%m-%d")
OUTPUT_HTML = OUTPUT_DIR / f"fundamentals_us_{TODAY}.html"
OUTPUT_JSON = OUTPUT_DIR / f"fundamentals_us_{TODAY}.json"

REQUEST_DELAY = 0.6   # polite pause between tickers


# --- Helpers -----------------------------------------------------------------

def load_universe():
    if not UNIVERSE_FILE.exists():
        sys.exit(f"ERROR: missing {UNIVERSE_FILE}. Create it with one 'TICKER Name' per line.")
    stocks = []
    for line in UNIVERSE_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        ticker = parts[0].upper()
        name = parts[1] if len(parts) > 1 else ticker
        stocks.append((ticker, name))
    return stocks


def pct(v):
    """Convert a yfinance decimal (0.25) to a percent (25.0). None-safe."""
    return round(v * 100, 2) if v is not None else None


# --- US Scoring Sub-models ---------------------------------------------------

def buffett_quality_8(f):
    """Buffett-style 8-criteria quality (replaces KC Chong). Returns (passed/8, score/14)."""
    p = 0
    if f.get("roe") and f["roe"] >= 15: p += 1
    if f.get("eps") and f["eps"] > 0: p += 1
    if f.get("debt_to_equity") is not None and f["debt_to_equity"] <= 1.0: p += 1
    if f.get("op_margin") and f["op_margin"] >= 15: p += 1
    if f.get("fcf") is not None and f["fcf"] > 0: p += 1
    if f.get("pe") and 0 < f["pe"] <= 25: p += 1
    if f.get("pb") and f["pb"] <= 6: p += 1
    if f.get("growth") and f["growth"] > 0: p += 1
    return p, round(p / 8 * 14)


def dividend_compounder_8(f):
    """Dividend compounder 8-criteria (replaces Cold Eye). Returns (passed/8, score/14)."""
    p = 0
    tot_ret = (f.get("dy") or 0) + (f.get("growth") or 0)
    if tot_ret >= 8: p += 1
    if f.get("roe") and f["roe"] >= 12: p += 1
    if f.get("dy") and f["dy"] >= 2: p += 1
    if f.get("payout") is not None and 0 < f["payout"] <= 70: p += 1
    if f.get("debt_to_equity") is not None and f["debt_to_equity"] <= 0.8: p += 1
    if f.get("dy") and f["dy"] > 0: p += 1
    if f.get("pe") and 0 < f["pe"] <= 20: p += 1
    if f.get("op_margin") and f["op_margin"] >= 10: p += 1
    return p, round(p / 8 * 14)


def magic_formula(f):
    """Greenblatt-style quality+value score (replaces MONEY). Returns (score 0-12, breakdown)."""
    pts = 0
    brk = []
    roe = f.get("roe") or 0
    if roe >= 20: pts += 3; brk.append("Q:3")
    elif roe >= 12: pts += 2; brk.append("Q:2")
    elif roe >= 6: pts += 1; brk.append("Q:1")
    om = f.get("op_margin") or 0
    if om >= 20: pts += 3; brk.append("M:3")
    elif om >= 12: pts += 2; brk.append("M:2")
    elif om >= 6: pts += 1; brk.append("M:1")
    g = f.get("growth") or 0
    if g >= 15: pts += 2; brk.append("G:2")
    elif g >= 7: pts += 1; brk.append("G:1")
    if f.get("eps") and f["eps"] > 0: pts += 2; brk.append("E:2")
    pe = f.get("pe")
    if pe and 0 < pe <= 15: pts += 2; brk.append("V:2")
    elif pe and 15 < pe <= 25: pts += 1; brk.append("V:1")
    return min(pts, 12), "/".join(brk)


def quality_tier(f):
    """Generic quality tier T1-T5 (replaces Tong Kooi). Returns (label, score/10)."""
    roe = f.get("roe") or 0
    mc = f.get("mkt_cap") or 0
    de = f.get("debt_to_equity")
    g = f.get("growth") or 0
    if roe >= 18 and mc >= 10e9 and g >= 7 and (de is None or de <= 0.5):
        return "T1-Elite", 10
    if roe >= 12 and mc >= 2e9 and g >= 5:
        return "T2-Strong", 8
    if roe >= 8:
        return "T3-Decent", 5
    if roe >= 0:
        return "T4-Cyclical", 3
    return "T5-Spec", 1


def composite_quality(b_s, d_s, t_s, m_s):
    total = b_s + d_s + t_s + m_s   # max 14+14+10+12 = 50
    if   total >= 40: return total, "Q-ELITE"
    elif total >= 30: return total, "Q-A"
    elif total >= 20: return total, "Q-B"
    elif total >= 10: return total, "Q-C"
    return total, "Q-D"


# --- Stock Fetcher -----------------------------------------------------------

def fetch_stock(ticker, name):
    base = {
        "ticker": ticker, "name": name,
        "price": None, "pe": None, "pb": None, "roe": None, "eps": None,
        "dy": None, "payout": None, "growth": None, "op_margin": None,
        "debt_to_equity": None, "fcf": None, "mkt_cap": None,
        "buffett_passed": None, "buffett_score": 0,
        "divcomp_passed": None, "divcomp_score": 0,
        "magic_score": 0, "magic_breakdown": None,
        "tier": None, "tier_score": 0,
        "quality_score": 0, "quality_grade": "Q-D",
        "error": None,
    }
    try:
        info = yf.Ticker(ticker).info or {}
        if not info or info.get("regularMarketPrice") is None and info.get("currentPrice") is None:
            base["error"] = "no data"
            return base

        price = info.get("currentPrice") or info.get("regularMarketPrice")
        base["price"]   = price
        base["pe"]      = info.get("trailingPE")
        base["pb"]      = info.get("priceToBook")
        base["roe"]     = pct(info.get("returnOnEquity"))
        base["eps"]     = info.get("trailingEps")
        base["op_margin"] = pct(info.get("operatingMargins"))
        base["growth"]  = pct(info.get("earningsGrowth"))
        if base["growth"] is None:
            base["growth"] = pct(info.get("revenueGrowth"))
        base["payout"]  = pct(info.get("payoutRatio"))
        base["fcf"]     = info.get("freeCashflow")
        base["mkt_cap"] = info.get("marketCap")

        # Debt/Equity: yfinance returns it as a percent number (e.g. 199.4) -> ratio
        de = info.get("debtToEquity")
        base["debt_to_equity"] = round(de / 100, 2) if de is not None else None

        # Dividend yield: prefer dividendRate / price, fall back to trailing yield
        if info.get("dividendRate") and price:
            base["dy"] = round(info["dividendRate"] / price * 100, 2)
        elif info.get("trailingAnnualDividendYield"):
            base["dy"] = pct(info["trailingAnnualDividendYield"])
        else:
            base["dy"] = 0.0

        # US quality sub-scores
        b_p, b_s = buffett_quality_8(base)
        d_p, d_s = dividend_compounder_8(base)
        m_s, m_b = magic_formula(base)
        t_lbl, t_s = quality_tier(base)
        q_tot, q_g = composite_quality(b_s, d_s, t_s, m_s)

        base["buffett_passed"] = b_p
        base["buffett_score"]  = b_s
        base["divcomp_passed"] = d_p
        base["divcomp_score"]  = d_s
        base["magic_score"]    = m_s
        base["magic_breakdown"] = m_b
        base["tier"]           = t_lbl
        base["tier_score"]     = t_s
        base["quality_score"]  = q_tot
        base["quality_grade"]  = q_g

    except Exception as e:
        base["error"] = str(e)[:80]
    return base


# --- HTML Report -------------------------------------------------------------

QUALITY_STYLE = {"Q-ELITE": "#6610f2", "Q-A": "#198754", "Q-B": "#0d6efd",
                 "Q-C": "#fd7e14", "Q-D": "#dc3545"}


def _f(v, fmt=".1f", suffix=""):
    return f"{v:{fmt}}{suffix}" if v is not None else "-"


def _cap(v):
    if not v:
        return "-"
    if v >= 1e12:
        return f"${v/1e12:.2f}T"
    if v >= 1e9:
        return f"${v/1e9:.1f}B"
    return f"${v/1e6:.0f}M"


def build_html(results, generated_at):
    results_sorted = sorted(results, key=lambda x: -(x.get("quality_score") or 0))
    q_counts = {g: sum(1 for r in results if r.get("quality_grade") == g)
                for g in ["Q-ELITE", "Q-A", "Q-B", "Q-C", "Q-D"]}

    counts_html = "".join(
        f'<div style="background:{QUALITY_STYLE[g]}33;border-radius:6px;padding:10px 16px;text-align:center;min-width:90px;">'
        f'<div style="font-size:22px;font-weight:700;color:{QUALITY_STYLE[g]};">{q_counts[g]}</div>'
        f'<div style="font-size:10px;color:{QUALITY_STYLE[g]};font-weight:600;">{g}</div></div>'
        for g in ["Q-ELITE", "Q-A", "Q-B", "Q-C", "Q-D"]
    )

    th = lambda t: f'<th style="padding:8px;text-align:left;font-size:11px;color:#555;white-space:nowrap;background:#f1f3f5;border-bottom:2px solid #dee2e6;">{t}</th>'
    header = (f'<tr>{th("#")}{th("Stock")}{th("Quality")}{th("Buffett")}'
              f'{th("Div Comp")}{th("Tier")}{th("Magic")}{th("PE")}{th("ROE %")}'
              f'{th("DY %")}{th("Growth %")}{th("D/E")}{th("OpMgn %")}{th("Mkt Cap")}</tr>')

    rows = []
    for i, r in enumerate(results_sorted, 1):
        q = r.get("quality_grade", "Q-D")
        qc = QUALITY_STYLE.get(q, "#aaa")
        tv_url = f"https://www.tradingview.com/chart/?symbol={r['ticker']}"
        rows.append(
            f'<tr style="background:#fff;border-bottom:1px solid #dee2e6;">'
            f'<td style="padding:7px 8px;font-size:11px;color:#888;">{i}</td>'
            f'<td style="padding:7px 8px;"><a href="{tv_url}" target="_blank" '
            f'style="font-weight:700;color:#1a1a2e;text-decoration:none;">{r["name"]}</a><br>'
            f'<span style="font-size:10px;color:#888;">{r["ticker"]}</span></td>'
            f'<td style="padding:7px 8px;text-align:center;">'
            f'<span style="background:{qc};color:#fff;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:700;">{q}</span><br>'
            f'<span style="font-size:10px;color:#666;">{r.get("quality_score",0)}/50</span></td>'
            f'<td style="padding:7px 8px;font-size:11px;text-align:center;">'
            f'<b>{r.get("buffett_passed","-")}</b>/8<br>'
            f'<span style="font-size:9px;color:#888;">{r.get("buffett_score",0)}/14</span></td>'
            f'<td style="padding:7px 8px;font-size:11px;text-align:center;">'
            f'<b>{r.get("divcomp_passed","-")}</b>/8<br>'
            f'<span style="font-size:9px;color:#888;">{r.get("divcomp_score",0)}/14</span></td>'
            f'<td style="padding:7px 8px;font-size:11px;">{r.get("tier","-")}</td>'
            f'<td style="padding:7px 8px;font-size:10px;">{r.get("magic_breakdown","-")}<br>'
            f'<b>{r.get("magic_score",0)}/12</b></td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r.get("pe"))}</td>'
            f'<td style="padding:7px 8px;font-size:12px;color:{"#198754" if r.get("roe") and r["roe"]>=15 else "#fd7e14" if r.get("roe") and r["roe"]>=10 else "#dc3545" if r.get("roe") else "#aaa"};">{_f(r.get("roe"))}</td>'
            f'<td style="padding:7px 8px;font-size:12px;color:{"#198754" if r.get("dy") and r["dy"]>=4 else "#0d6efd" if r.get("dy") and r["dy"]>=2 else "#888"};">{_f(r.get("dy"), suffix="%")}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r.get("growth"), suffix="%")}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r.get("debt_to_equity"))}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r.get("op_margin"), suffix="%")}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_cap(r.get("mkt_cap"))}</td>'
            f'</tr>'
        )

    table_html = (f'<div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;">'
                  f'{header}{"".join(rows)}</table></div>')

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>US Fundamentals - {generated_at}</title>
<style>body{{font-family:-apple-system,Segoe UI,Roboto,sans-serif;background:#f8f9fa;margin:0;}}
.header{{background:#1a1a2e;color:#fff;padding:18px 28px;}}
.container{{max-width:1500px;margin:0 auto;padding:20px 16px;}}
tr:hover{{filter:brightness(0.97);}}th{{position:sticky;top:0;z-index:2;}}</style></head>
<body><div class="header"><h1 style="margin:0;font-size:20px;">US Fundamentals
<span style="font-size:12px;color:#6610f2;">v1 - Buffett + Div Compounder + Tier + Magic Formula</span></h1>
<div style="font-size:12px;color:#adb5bd;margin-top:4px;">Generated: {generated_at}
&nbsp;-&nbsp; Composite quality (max 50): Buffett 14 + Div Compounder 14 + Tier 10 + Magic 12 &nbsp;-&nbsp; Source: yfinance</div>
</div><div class="container">
<div style="display:flex;gap:10px;flex-wrap:wrap;margin:16px 0;">{counts_html}</div>
{table_html}
<div style="margin-top:16px;font-size:11px;color:#888;">
Buffett Quality - Dividend Compounder - Quality Tier - Magic Formula. Data via yfinance (Yahoo Finance).
Growth = earnings growth (YoY) where available, else revenue growth. Verify before trading.
</div></div></body></html>"""


# --- Main --------------------------------------------------------------------

def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    universe = load_universe()
    print(f"\nUS Fundamental Data Fetcher v1")
    print(f"Universe : {len(universe)} stocks  -  Source : yfinance")
    print("-" * 60)

    results = []
    total = len(universe)
    for i, (ticker, name) in enumerate(universe, 1):
        res = fetch_stock(ticker, name)
        results.append(res)
        q = res.get("quality_grade", "Q-D")
        bp = res.get("buffett_passed")
        dp = res.get("divcomp_passed")
        err = f"  [{res['error']}]" if res.get("error") else ""
        print(f"  [{i:3d}/{total}] {res['ticker']:8s} {res['name'][:16]:16s}  "
              f"{q:8s}  Buf:{bp}/8  Div:{dp}/8  ROE:{res.get('roe') or '-':>5}"
              f"  DY:{(str(res.get('dy'))+'%' if res.get('dy') else '-'):>6}{err}", flush=True)
        time.sleep(REQUEST_DELAY)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str)

    generated_at = datetime.datetime.now().strftime("%d %b %Y  %H:%M")
    html = build_html(results, generated_at)
    OUTPUT_HTML.write_text(html, encoding="utf-8")

    qe = sum(1 for r in results if r.get("quality_grade") == "Q-ELITE")
    qa = sum(1 for r in results if r.get("quality_grade") == "Q-A")
    qb = sum(1 for r in results if r.get("quality_grade") == "Q-B")
    print(f"\n{'='*60}")
    print(f"Q-ELITE  : {qe}")
    print(f"Q-A      : {qa}")
    print(f"Q-B      : {qb}")
    print(f"{'='*60}")
    print(f"\nHTML : {OUTPUT_HTML}")
    print(f"JSON : {OUTPUT_JSON}")
    try:
        webbrowser.open(OUTPUT_HTML.as_uri())
    except Exception:
        pass
    print("Done.")


if __name__ == "__main__":
    main()
