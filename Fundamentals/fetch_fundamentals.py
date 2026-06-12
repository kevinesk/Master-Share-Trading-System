"""
KLSE Fundamental Data Fetcher
==============================
Scrapes klsescreener.com for key financial metrics for every stock in
universe.txt and produces a ranked HTML report + JSON data file.

Metrics fetched per stock:
  PE, P/B, ROE, EPS, DPS, Dividend Yield, NTA, Revenue/share,
  Market Cap, 3Y EPS CAGR, 5Y EPS CAGR

Usage:
    Double-click run_fundamentals.bat
    OR: py fetch_fundamentals.py
"""

import sys
import re
import json
import time
import random
import datetime
import webbrowser
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# ── Dependencies ──────────────────────────────────────────────────────────────
try:
    from curl_cffi import requests as curl_requests
    SESSION = curl_requests.Session(verify=False, impersonate="chrome")
except ImportError:
    sys.exit("ERROR: Run:  pip install curl_cffi")

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("ERROR: Run:  pip install beautifulsoup4")

import warnings
warnings.filterwarnings("ignore")

# ── Config ────────────────────────────────────────────────────────────────────
SCRIPT_DIR    = Path(__file__).parent
UNIVERSE_FILE = SCRIPT_DIR.parent / "KLSE Screener" / "universe.txt"
OUTPUT_DIR    = SCRIPT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

TODAY       = datetime.date.today().strftime("%Y-%m-%d")
OUTPUT_HTML = OUTPUT_DIR / f"fundamentals_{TODAY}.html"
OUTPUT_JSON = OUTPUT_DIR / f"fundamentals_{TODAY}.json"

BASE_URL    = "https://www.klsescreener.com/v2/stocks/view"
MAX_WORKERS   = 1      # sequential — klsescreener rate-limits parallel requests
TIMEOUT       = 20
REQUEST_DELAY = 2.5    # seconds between requests (site rate-limits fast requests)
MAX_RETRIES   = 2      # retry count for HTTP 202
COOLDOWN_N    = 8      # take a longer break every N stocks
COOLDOWN_SEC  = 15     # break duration in seconds

# ── Helpers ───────────────────────────────────────────────────────────────────

def load_universe():
    stocks = []
    for line in UNIVERSE_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            ticker = parts[0]
            code   = ticker.replace(".KL", "").replace(".kl", "").lstrip("0") or "0"
            # Preserve meaningful leading zeros (e.g. 0097 → keep as "97" for URL but store raw)
            url_code = ticker.replace(".KL", "").replace(".kl", "")
            stocks.append((ticker, parts[1], url_code))
    return stocks


def _num(text: str) -> float | None:
    """Extract first float from a string, handling commas and units."""
    if not text:
        return None
    text = text.replace(",", "").replace("%", "").strip()
    m = re.search(r"[-+]?\d+\.?\d*", text)
    return float(m.group()) if m else None


def _find(soup, *labels) -> str:
    """Search for a metric value by its label text in the page."""
    for label in labels:
        # Try dt/dd pairs
        tag = soup.find(string=re.compile(re.escape(label), re.I))
        if tag:
            parent = tag.parent
            # Try next sibling or parent's next sibling
            for _ in range(4):
                if parent is None:
                    break
                nxt = parent.find_next_sibling()
                if nxt and nxt.get_text(strip=True):
                    val = nxt.get_text(strip=True)
                    if re.search(r"\d", val):
                        return val
                parent = parent.parent
    return ""


def fetch_stock_fundamentals(ticker: str, name: str, code: str) -> dict:
    time.sleep(REQUEST_DELAY + random.uniform(0, 0.8))
    base = {
        "ticker": ticker, "name": name, "code": code,
        "pe": None, "pb": None, "roe": None, "eps": None,
        "dps": None, "dy": None, "nta": None, "rps": None,
        "mkt_cap_b": None, "cagr3": None, "cagr5": None,
        "score": 0, "grade": "—", "error": None,
    }
    try:
        url  = f"{BASE_URL}/{code}"
        resp = None
        for attempt in range(MAX_RETRIES):
            # Fresh session on retry to bypass session-based rate tracking
            sess = SESSION if attempt == 0 else curl_requests.Session(verify=False, impersonate="chrome")
            resp = sess.get(url, timeout=TIMEOUT)
            if resp.status_code == 200:
                break
            if resp.status_code == 202:
                wait = 8 + attempt * 5 + random.uniform(0, 3)
                time.sleep(wait)
            else:
                base["error"] = f"HTTP {resp.status_code}"
                return base
        if resp is None or resp.status_code != 200:
            base["error"] = f"HTTP {resp.status_code} after {MAX_RETRIES} retries"
            return base

        soup = BeautifulSoup(resp.text, "html.parser")
        text = soup.get_text(" ", strip=True)

        # ── Extract metrics via regex on page text ────────────────────────────
        def grab(pattern, group=1):
            m = re.search(pattern, text, re.I)
            return _num(m.group(group)) if m else None

        base["pe"]       = grab(r"P[/.]E\s*[:\s]*([0-9,.N/A]+)")
        base["pb"]       = grab(r"P[/.]B\s*[:\s]*([0-9,.N/A]+)")
        base["roe"]      = grab(r"ROE\s*[:\s]*([0-9,.+-]+)")
        base["eps"]      = grab(r"EPS\s*[:\s]*([0-9,.+-]+)")
        base["dps"]      = grab(r"DPS\s*[:\s]*([0-9,.]+)")
        base["dy"]       = grab(r"D[Yy][:\s]*([0-9,.]+)\s*%")
        base["nta"]      = grab(r"NTA\s*[:\s]*([0-9,.]+)")
        base["rps"]      = grab(r"RPS\s*[:\s]*([0-9,.]+)")

        # Market cap — look for pattern like "134.0B" or "Market Cap: 134.0B"
        mc = re.search(r"Market\s*Cap\s*[:\s]*([0-9,.]+)\s*([BMK])", text, re.I)
        if mc:
            val  = float(mc.group(1).replace(",", ""))
            unit = mc.group(2).upper()
            base["mkt_cap_b"] = val if unit == "B" else (val / 1000 if unit == "M" else val / 1_000_000)

        # CAGR
        base["cagr3"] = grab(r"3[Yy]\s*CAGR\s*[:\s]*([0-9,.+-]+)")
        base["cagr5"] = grab(r"5[Yy]\s*CAGR\s*[:\s]*([0-9,.+-]+)")

        # ── Fundamental scoring (0–10) ────────────────────────────────────────
        score = 0
        pe, roe, eps, dy, cagr5 = base["pe"], base["roe"], base["eps"], base["dy"], base["cagr5"]

        if pe  and 0 < pe  <= 20: score += 2
        elif pe and 20 < pe <= 30: score += 1

        if roe and roe >= 15:  score += 2
        elif roe and roe >= 10: score += 1

        if eps and eps > 0:   score += 1

        if dy  and dy  >= 4:   score += 2
        elif dy and dy >= 2:   score += 1

        if cagr5 and cagr5 >= 10: score += 2
        elif cagr5 and cagr5 >= 5: score += 1

        base["score"] = score
        base["grade"] = ("A" if score >= 8 else
                         "B" if score >= 6 else
                         "C" if score >= 4 else "D")

    except Exception as e:
        base["error"] = str(e)[:80]

    return base

# ── HTML Report ───────────────────────────────────────────────────────────────

GRADE_STYLE = {
    "A": ("#198754", "#d4edda"),
    "B": ("#0d6efd", "#d0e4ff"),
    "C": ("#fd7e14", "#fff3cd"),
    "D": ("#dc3545", "#fde8e8"),
    "—": ("#6c757d", "#f8f9fa"),
}

def _f(v, fmt=".1f", suffix=""):
    return f"{v:{fmt}}{suffix}" if v is not None else "—"


def build_html(results: list[dict], generated_at: str) -> str:
    results_sorted = sorted(results, key=lambda x: -(x["score"]))

    grade_counts = {g: sum(1 for r in results if r["grade"] == g) for g in "ABCD"}

    counts_html = "".join(
        f'<div style="background:{GRADE_STYLE[g][1]};border-radius:6px;padding:10px 18px;text-align:center;">'
        f'<div style="font-size:22px;font-weight:700;color:{GRADE_STYLE[g][0]};">{grade_counts[g]}</div>'
        f'<div style="font-size:11px;color:{GRADE_STYLE[g][0]};">Grade {g}</div>'
        f'</div>'
        for g in "ABCD"
    )

    th = lambda t: f'<th style="padding:8px;text-align:left;font-size:11px;color:#555;white-space:nowrap;background:#f1f3f5;border-bottom:2px solid #dee2e6;">{t}</th>'

    header = (f'<tr>{th("#")}{th("Stock")}{th("Grade")}{th("PE")}{th("P/B")}'
              f'{th("ROE %")}{th("EPS")}{th("DPS")}{th("Div Yield")}{th("NTA")}'
              f'{th("Mkt Cap")}{th("5Y CAGR")}{th("3Y CAGR")}{th("Score")}</tr>')

    rows = []
    for i, r in enumerate(results_sorted, 1):
        col, bg = GRADE_STYLE.get(r["grade"], GRADE_STYLE["—"])
        err = f'<span style="color:#dc3545;font-size:10px;">{r["error"]}</span>' if r.get("error") else ""
        tv_url = f"https://www.tradingview.com/chart/?symbol=MYX%3A{r['code']}"
        rows.append(
            f'<tr style="background:{bg};border-bottom:1px solid #dee2e6;">'
            f'<td style="padding:7px 8px;font-size:12px;color:#888;">{i}</td>'
            f'<td style="padding:7px 8px;">'
            f'  <a href="{tv_url}" target="_blank" style="font-weight:700;font-size:13px;color:#1a1a2e;text-decoration:none;">{r["name"]}</a><br>'
            f'  <span style="font-size:10px;color:#888;">{r["ticker"]}</span>'
            f'</td>'
            f'<td style="padding:7px 8px;"><span style="background:{col};color:#fff;padding:3px 10px;border-radius:4px;font-weight:700;">{r["grade"]}</span></td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r["pe"])}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r["pb"])}</td>'
            f'<td style="padding:7px 8px;font-size:12px;color:{"#198754" if r["roe"] and r["roe"]>=15 else "#fd7e14" if r["roe"] and r["roe"]>=10 else "#dc3545"};">{_f(r["roe"])}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r["eps"])}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r["dps"])}</td>'
            f'<td style="padding:7px 8px;font-size:12px;color:{"#198754" if r["dy"] and r["dy"]>=4 else "#0d6efd" if r["dy"] and r["dy"]>=2 else ""};">{_f(r["dy"], suffix="%")}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r["nta"])}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{"RM "+_f(r["mkt_cap_b"])+"B" if r["mkt_cap_b"] else "—"}</td>'
            f'<td style="padding:7px 8px;font-size:12px;color:{"#198754" if r["cagr5"] and r["cagr5"]>=10 else "#fd7e14" if r["cagr5"] and r["cagr5"]>=5 else "#dc3545"};">{_f(r["cagr5"], suffix="%")}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r["cagr3"], suffix="%")}</td>'
            f'<td style="padding:7px 8px;font-size:12px;font-weight:700;color:{col};">{r["score"]}/10</td>'
            f'{f"<td>{err}</td>" if err else ""}'
            f'</tr>'
        )

    table_html = (
        f'<div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;">'
        f'{header}{"".join(rows)}</table></div>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>KLSE Fundamentals — {generated_at}</title>
  <style>
    body {{ font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
           background:#f8f9fa;margin:0;padding:0; }}
    .header {{ background:#1a1a2e;color:#fff;padding:18px 28px; }}
    .header h1 {{ margin:0;font-size:20px; }}
    .header .meta {{ font-size:12px;color:#adb5bd;margin-top:4px; }}
    .container {{ max-width:1400px;margin:0 auto;padding:20px 16px; }}
    tr:hover {{ filter:brightness(0.96); }}
    th {{ position:sticky;top:0;z-index:2; }}
  </style>
</head>
<body>
  <div class="header">
    <h1>KLSE Fundamental Analysis</h1>
    <div class="meta">Generated: {generated_at} &nbsp;·&nbsp; Source: klsescreener.com &nbsp;·&nbsp;
      Grade A = Score 8–10 &nbsp;·&nbsp; Grade B = 6–7 &nbsp;·&nbsp; Grade C = 4–5 &nbsp;·&nbsp; Grade D = 0–3</div>
  </div>
  <div class="container">
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin:16px 0;">
      {counts_html}
      <div style="background:#fff;border:1px solid #dee2e6;border-radius:6px;padding:10px 18px;flex:1;font-size:12px;color:#555;">
        <strong>Scoring:</strong>
        PE ≤20 = +2, PE 20–30 = +1 &nbsp;|&nbsp;
        ROE ≥15% = +2, ≥10% = +1 &nbsp;|&nbsp;
        EPS &gt; 0 = +1 &nbsp;|&nbsp;
        Div Yield ≥4% = +2, ≥2% = +1 &nbsp;|&nbsp;
        5Y EPS CAGR ≥10% = +2, ≥5% = +1
      </div>
    </div>
    {table_html}
    <div style="margin-top:16px;font-size:11px;color:#888;">
      Data source: klsescreener.com (Bursa Malaysia quarterly filings) &nbsp;·&nbsp;
      For deeper analysis of any stock, run: <code>py annual_report.py [CODE]</code>
    </div>
  </div>
</body>
</html>"""

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    universe = load_universe()
    print(f"\nKLSE Fundamental Data Fetcher")
    print(f"Universe : {len(universe)} stocks")
    print(f"Source   : klsescreener.com")
    print("-" * 50)

    results = []
    total   = len(universe)

    for i, (ticker, name, code) in enumerate(universe, 1):
        # Cooldown break every COOLDOWN_N stocks to avoid session-based blocking
        if i > 1 and (i - 1) % COOLDOWN_N == 0:
            print(f"  ... cooldown {COOLDOWN_SEC}s (avoiding rate limit) ...", flush=True)
            time.sleep(COOLDOWN_SEC)

        res = fetch_stock_fundamentals(ticker, name, code)
        results.append(res)
        g   = res["grade"]
        err = f"  [{res['error']}]" if res.get("error") else ""
        print(f"  [{i:3d}/{total}] {res['ticker']:12s} {res['name']:15s}  "
              f"Grade:{g}  PE:{res['pe'] or '—':>6}  ROE:{res['roe'] or '—':>5}  "
              f"DY:{str(res['dy'])+'%' if res['dy'] else '—':>6}{err}", flush=True)

    # Save JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str)

    # Save HTML
    generated_at = datetime.datetime.now().strftime("%d %b %Y  %H:%M")
    html = build_html(results, generated_at)
    OUTPUT_HTML.write_text(html, encoding="utf-8")

    # Summary
    a = sum(1 for r in results if r["grade"] == "A")
    b = sum(1 for r in results if r["grade"] == "B")
    c = sum(1 for r in results if r["grade"] == "C")
    d = sum(1 for r in results if r["grade"] == "D")
    print(f"\n{'='*50}")
    print(f"Grade A (Strong fundamentals) : {a}")
    print(f"Grade B (Good fundamentals)   : {b}")
    print(f"Grade C (Average)             : {c}")
    print(f"Grade D (Weak/no data)        : {d}")
    print(f"{'='*50}")
    print(f"\nHTML report : {OUTPUT_HTML}")
    print(f"JSON data   : {OUTPUT_JSON}")

    webbrowser.open(OUTPUT_HTML.as_uri())
    print("Browser opened.")

if __name__ == "__main__":
    main()
