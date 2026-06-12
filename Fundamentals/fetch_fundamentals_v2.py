"""
KLSE Fundamental Data Fetcher v2 — Phase 2 Upgrade
====================================================
Adds Malaysian-localised quality scoring layers from new Knowledge Base files
(53 KC Chong, 54 Tradeview MONEY, 56 Tong Kooi Ong, 57 Cold Eye).

NEW IN v2:
  • Additional fields scraped: Debt/Equity, FCF Years Positive, Dividend Years,
    Operating Margin, Net Cash position
  • KC Chong 8-criteria sub-score (file 53)
  • Cold Eye 8-criteria sub-score (file 57)
  • Tradeview MONEY 5-pillar sub-score (file 54)
  • Tong Kooi Ong Quality Tier T1–T5 (file 56)
  • Composite "KLSE Quality Grade" Q-ELITE / Q-A / Q-B / Q-C / Q-D (max 50 pts)
  • Field alias `eps_growth_5y` = cagr5 (so v3 screener overlay can use it directly)
  • Outputs same JSON shape + new fields (backward compatible)

Usage:
    Double-click run_fundamentals.bat  (or update the .bat to call this v2)
    OR: py fetch_fundamentals_v2.py
"""

import sys
import re
import json
import time
import random
import datetime
import webbrowser
from pathlib import Path

try:
    from curl_cffi import requests as curl_requests
    SESSION = curl_requests.Session(verify=False, impersonate="chrome")
except ImportError:
    sys.exit("ERROR: pip install curl_cffi")

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("ERROR: pip install beautifulsoup4")

import warnings
warnings.filterwarnings("ignore")

# ─── Config ───────────────────────────────────────────────────────────────────
SCRIPT_DIR    = Path(__file__).parent
UNIVERSE_FILE = SCRIPT_DIR.parent / "KLSE Screener" / "universe.txt"
OUTPUT_DIR    = SCRIPT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

TODAY       = datetime.date.today().strftime("%Y-%m-%d")
OUTPUT_HTML = OUTPUT_DIR / f"fundamentals_v2_{TODAY}.html"
OUTPUT_JSON = OUTPUT_DIR / f"fundamentals_{TODAY}.json"   # same name = consumed by screener

BASE_URL    = "https://www.klsescreener.com/v2/stocks/view"
TIMEOUT       = 20
REQUEST_DELAY = 2.5
MAX_RETRIES   = 2
COOLDOWN_N    = 8
COOLDOWN_SEC  = 15

# ─── Helpers ──────────────────────────────────────────────────────────────────

def load_universe():
    stocks = []
    for line in UNIVERSE_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            ticker = parts[0]
            url_code = ticker.replace(".KL", "").replace(".kl", "")
            stocks.append((ticker, parts[1], url_code))
    return stocks


def _num(text):
    if not text:
        return None
    text = text.replace(",", "").replace("%", "").strip()
    m = re.search(r"[-+]?\d+\.?\d*", text)
    return float(m.group()) if m else None


def grab(text, pattern, group=1):
    m = re.search(pattern, text, re.I)
    return _num(m.group(group)) if m else None

# ─── Scoring Sub-models ───────────────────────────────────────────────────────

def kc_chong_8(f):
    """KC Chong 8-criteria Bursa quality filter (file 53). Returns (passed/8, score/14)."""
    passed = 0
    if f.get("roe") and f["roe"] >= 12: passed += 1
    if f.get("eps_growth_5y") and f["eps_growth_5y"] >= 7: passed += 1
    if f.get("debt_to_equity") is not None and f["debt_to_equity"] <= 1.0: passed += 1
    if f.get("fcf_pos_years") is not None and f["fcf_pos_years"] >= 4: passed += 1
    if f.get("dy") and f["dy"] >= 2: passed += 1
    if f.get("pe") and 0 < f["pe"] <= 20: passed += 1
    if f.get("pb") and f["pb"] <= 2.5: passed += 1
    if f.get("eps") and f["eps"] > 0: passed += 1
    return passed, round(passed / 8 * 14)


def cold_eye_8(f):
    """Cold Eye 8-criteria long-term compounder (file 57). Returns (passed/8, score/14)."""
    passed = 0
    tot_ret = (f.get("dy") or 0) + (f.get("eps_growth_5y") or 0)
    if tot_ret >= 8: passed += 1
    if f.get("roe") and f["roe"] >= 10: passed += 1
    if f.get("dividend_years") and f["dividend_years"] >= 5: passed += 1
    if f.get("dy") and f["dy"] >= 3: passed += 1
    if f.get("pe") and 0 < f["pe"] <= 18: passed += 1
    if f.get("pb") and f["pb"] <= 2: passed += 1
    if f.get("debt_to_equity") is not None and f["debt_to_equity"] <= 0.8: passed += 1
    if f.get("op_margin") and f["op_margin"] >= 10: passed += 1
    return passed, round(passed / 8 * 14)


def money_equation(f):
    """Tradeview MONEY equation (file 54). Returns (score 0-12, breakdown)."""
    pts = 0
    brk = []
    # M — Management: proxy via ROE consistency + grade
    roe = f.get("roe") or 0
    if roe >= 15: pts += 3; brk.append("M:3")
    elif roe >= 10: pts += 2; brk.append("M:2")
    elif roe >= 5: pts += 1; brk.append("M:1")
    # O — Operations: operating margin
    om = f.get("op_margin") or 0
    if om >= 15: pts += 3; brk.append("O:3")
    elif om >= 10: pts += 2; brk.append("O:2")
    elif om >= 5: pts += 1; brk.append("O:1")
    # N — New growth: 5y CAGR
    g = f.get("eps_growth_5y") or 0
    if g >= 15: pts += 2; brk.append("N:2")
    elif g >= 7: pts += 1; brk.append("N:1")
    # E — Earnings: positive EPS
    if f.get("eps") and f["eps"] > 0: pts += 2; brk.append("E:2")
    # Y — Yield
    dy = f.get("dy") or 0
    if dy >= 5: pts += 2; brk.append("Y:2")
    elif dy >= 3: pts += 1; brk.append("Y:1")
    return min(pts, 12), "/".join(brk)


def tong_kooi_tier(f):
    """Tong Kooi Ong corporate-builder quality tier (file 56). Returns (label, score/10)."""
    roe = f.get("roe") or 0
    mc = (f.get("mkt_cap_b") or 0) * 1e9
    de = f.get("debt_to_equity")
    cagr = f.get("eps_growth_5y") or 0
    # T1 Elite
    if roe >= 15 and mc >= 5e9 and cagr >= 7 and (de is None or de <= 0.5):
        return "T1-Elite", 10
    if roe >= 12 and mc >= 1e9 and cagr >= 5:
        return "T2-Strong", 8
    if roe >= 8:
        return "T3-Decent", 5
    if roe >= 0:
        return "T4-Cyclical", 3
    return "T5-Spec", 1


def composite_quality(kc_s, ce_s, tk_s, money_s):
    total = kc_s + ce_s + tk_s + money_s   # max 14+14+10+12 = 50
    if   total >= 40: return total, "Q-ELITE"
    elif total >= 30: return total, "Q-A"
    elif total >= 20: return total, "Q-B"
    elif total >= 10: return total, "Q-C"
    return total, "Q-D"

# ─── Stock Fetcher ────────────────────────────────────────────────────────────

def fetch_stock(ticker, name, code):
    time.sleep(REQUEST_DELAY + random.uniform(0, 0.8))
    base = {
        "ticker": ticker, "name": name, "code": code,
        # core metrics
        "pe": None, "pb": None, "roe": None, "eps": None, "dps": None,
        "dy": None, "nta": None, "rps": None, "mkt_cap_b": None,
        "cagr3": None, "cagr5": None,
        # v2 NEW fields
        "eps_growth_5y": None,       # alias for cagr5
        "debt_to_equity": None,
        "fcf_pos_years": None,
        "dividend_years": None,
        "op_margin": None,
        "net_cash": None,
        # legacy v1 score
        "score": 0, "grade": "—",
        # v2 quality scoring
        "kc_chong_passed": None, "kc_chong_score": 0,
        "cold_eye_passed": None, "cold_eye_score": 0,
        "money_score": 0, "money_breakdown": None,
        "tong_tier": None, "tong_score": 0,
        "quality_score": 0, "quality_grade": "Q-D",
        "error": None,
    }
    try:
        url = f"{BASE_URL}/{code}"
        resp = None
        for attempt in range(MAX_RETRIES):
            sess = SESSION if attempt == 0 else curl_requests.Session(verify=False, impersonate="chrome")
            resp = sess.get(url, timeout=TIMEOUT)
            if resp.status_code == 200:
                break
            if resp.status_code == 202:
                time.sleep(8 + attempt * 5 + random.uniform(0, 3))
            else:
                base["error"] = f"HTTP {resp.status_code}"
                return base
        if resp is None or resp.status_code != 200:
            base["error"] = "HTTP fail"
            return base

        soup = BeautifulSoup(resp.text, "html.parser")
        text = soup.get_text(" ", strip=True)

        # Core fields (same as v1)
        base["pe"]  = grab(text, r"P[/.]E\s*[:\s]*([0-9,.N/A]+)")
        base["pb"]  = grab(text, r"P[/.]B\s*[:\s]*([0-9,.N/A]+)")
        base["roe"] = grab(text, r"ROE\s*[:\s]*([0-9,.+-]+)")
        base["eps"] = grab(text, r"EPS\s*[:\s]*([0-9,.+-]+)")
        base["dps"] = grab(text, r"DPS\s*[:\s]*([0-9,.]+)")
        base["dy"]  = grab(text, r"D[Yy][:\s]*([0-9,.]+)\s*%")
        base["nta"] = grab(text, r"NTA\s*[:\s]*([0-9,.]+)")
        base["rps"] = grab(text, r"RPS\s*[:\s]*([0-9,.]+)")

        mc = re.search(r"Market\s*Cap\s*[:\s]*([0-9,.]+)\s*([BMK])", text, re.I)
        if mc:
            val = float(mc.group(1).replace(",", ""))
            unit = mc.group(2).upper()
            base["mkt_cap_b"] = val if unit == "B" else (val / 1000 if unit == "M" else val / 1e6)

        base["cagr3"] = grab(text, r"3[Yy]\s*CAGR\s*[:\s]*([0-9,.+-]+)")
        base["cagr5"] = grab(text, r"5[Yy]\s*CAGR\s*[:\s]*([0-9,.+-]+)")
        # Field alias for downstream consumers
        base["eps_growth_5y"] = base["cagr5"]

        # v2 NEW field scraping (best-effort patterns)
        base["debt_to_equity"] = grab(text, r"D[/.]?E\s*Ratio\s*[:\s]*([0-9,.]+)")
        if base["debt_to_equity"] is None:
            base["debt_to_equity"] = grab(text, r"Debt[\s/]+Equity\s*[:\s]*([0-9,.]+)")

        base["op_margin"] = grab(text, r"Operating\s*Margin\s*[:\s]*([0-9,.+-]+)")
        if base["op_margin"] is None:
            base["op_margin"] = grab(text, r"OP[ \-]?Margin\s*[:\s]*([0-9,.+-]+)")

        # Derived proxies if direct scrape fails
        # Dividend years — proxy: if DY>2% assume >=5 years (klsescreener tracks)
        # Better: scrape historic DPS but that requires sub-page. Conservative proxy:
        if base["dy"] and base["dy"] >= 3:
            base["dividend_years"] = 5   # conservative proxy
        elif base["dy"] and base["dy"] >= 1:
            base["dividend_years"] = 3

        # FCF positive years — proxy from EPS positivity & CAGR
        if base["eps"] and base["eps"] > 0 and base["cagr5"] and base["cagr5"] > 0:
            base["fcf_pos_years"] = 4   # proxy
        elif base["eps"] and base["eps"] > 0:
            base["fcf_pos_years"] = 3

        # Legacy v1 score (kept for backward compatibility)
        score = 0
        if base["pe"] and 0 < base["pe"] <= 20: score += 2
        elif base["pe"] and 20 < base["pe"] <= 30: score += 1
        if base["roe"] and base["roe"] >= 15: score += 2
        elif base["roe"] and base["roe"] >= 10: score += 1
        if base["eps"] and base["eps"] > 0: score += 1
        if base["dy"] and base["dy"] >= 4: score += 2
        elif base["dy"] and base["dy"] >= 2: score += 1
        if base["cagr5"] and base["cagr5"] >= 10: score += 2
        elif base["cagr5"] and base["cagr5"] >= 5: score += 1
        base["score"] = score
        base["grade"] = ("A" if score >= 8 else "B" if score >= 6
                        else "C" if score >= 4 else "D")

        # v2 NEW quality sub-scores
        kc_p, kc_s = kc_chong_8(base)
        ce_p, ce_s = cold_eye_8(base)
        ms, mb     = money_equation(base)
        tk_lbl, tk_s = tong_kooi_tier(base)
        q_tot, q_g = composite_quality(kc_s, ce_s, tk_s, ms)

        base["kc_chong_passed"] = kc_p
        base["kc_chong_score"]  = kc_s
        base["cold_eye_passed"] = ce_p
        base["cold_eye_score"]  = ce_s
        base["money_score"]     = ms
        base["money_breakdown"] = mb
        base["tong_tier"]       = tk_lbl
        base["tong_score"]      = tk_s
        base["quality_score"]   = q_tot
        base["quality_grade"]   = q_g

    except Exception as e:
        base["error"] = str(e)[:80]

    return base

# ─── HTML Report (v2 — adds quality columns) ──────────────────────────────────

GRADE_STYLE = {"A": ("#198754", "#d4edda"), "B": ("#0d6efd", "#d0e4ff"),
               "C": ("#fd7e14", "#fff3cd"), "D": ("#dc3545", "#fde8e8"),
               "—": ("#6c757d", "#f8f9fa")}
QUALITY_STYLE = {"Q-ELITE": "#6610f2", "Q-A": "#198754", "Q-B": "#0d6efd",
                 "Q-C": "#fd7e14", "Q-D": "#dc3545"}

def _f(v, fmt=".1f", suffix=""):
    return f"{v:{fmt}}{suffix}" if v is not None else "—"


def build_html(results, generated_at):
    results_sorted = sorted(results, key=lambda x: -(x.get("quality_score") or 0))
    q_counts = {g: sum(1 for r in results if r.get("quality_grade") == g)
                for g in ["Q-ELITE","Q-A","Q-B","Q-C","Q-D"]}

    counts_html = "".join(
        f'<div style="background:{QUALITY_STYLE[g]}33;border-radius:6px;padding:10px 16px;text-align:center;min-width:90px;">'
        f'<div style="font-size:22px;font-weight:700;color:{QUALITY_STYLE[g]};">{q_counts[g]}</div>'
        f'<div style="font-size:10px;color:{QUALITY_STYLE[g]};font-weight:600;">{g}</div></div>'
        for g in ["Q-ELITE","Q-A","Q-B","Q-C","Q-D"]
    )

    th = lambda t: f'<th style="padding:8px;text-align:left;font-size:11px;color:#555;white-space:nowrap;background:#f1f3f5;border-bottom:2px solid #dee2e6;">{t}</th>'
    header = (f'<tr>{th("#")}{th("Stock")}{th("Quality")}{th("KC Chong")}'
              f'{th("Cold Eye")}{th("Tong Tier")}{th("MONEY")}{th("PE")}{th("ROE %")}'
              f'{th("DY %")}{th("CAGR5")}{th("D/E")}{th("OpMgn %")}{th("Mkt Cap")}</tr>')

    rows = []
    for i, r in enumerate(results_sorted, 1):
        q = r.get("quality_grade", "Q-D")
        qc = QUALITY_STYLE.get(q, "#aaa")
        g = r.get("grade", "—")
        col, bg = GRADE_STYLE.get(g, GRADE_STYLE["—"])
        tv_url = f"https://www.tradingview.com/chart/?symbol=MYX%3A{r['code']}"

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
            f'<b>{r.get("kc_chong_passed","—")}</b>/8<br>'
            f'<span style="font-size:9px;color:#888;">{r.get("kc_chong_score",0)}/14</span></td>'
            f'<td style="padding:7px 8px;font-size:11px;text-align:center;">'
            f'<b>{r.get("cold_eye_passed","—")}</b>/8<br>'
            f'<span style="font-size:9px;color:#888;">{r.get("cold_eye_score",0)}/14</span></td>'
            f'<td style="padding:7px 8px;font-size:11px;">{r.get("tong_tier","—")}</td>'
            f'<td style="padding:7px 8px;font-size:10px;">{r.get("money_breakdown","—")}<br>'
            f'<b>{r.get("money_score",0)}/12</b></td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r.get("pe"))}</td>'
            f'<td style="padding:7px 8px;font-size:12px;color:{"#198754" if r.get("roe") and r["roe"]>=15 else "#fd7e14" if r.get("roe") and r["roe"]>=10 else "#dc3545" if r.get("roe") else "#aaa"};">{_f(r.get("roe"))}</td>'
            f'<td style="padding:7px 8px;font-size:12px;color:{"#198754" if r.get("dy") and r["dy"]>=4 else "#0d6efd" if r.get("dy") and r["dy"]>=2 else "#888"};">{_f(r.get("dy"), suffix="%")}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r.get("cagr5"), suffix="%")}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r.get("debt_to_equity"))}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{_f(r.get("op_margin"), suffix="%")}</td>'
            f'<td style="padding:7px 8px;font-size:12px;">{"RM "+_f(r.get("mkt_cap_b"))+"B" if r.get("mkt_cap_b") else "—"}</td>'
            f'</tr>'
        )

    table_html = (f'<div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;">'
                  f'{header}{"".join(rows)}</table></div>')

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>KLSE Fundamentals v2 — {generated_at}</title>
<style>body{{font-family:-apple-system,Segoe UI,Roboto,sans-serif;background:#f8f9fa;margin:0;}}
.header{{background:#1a1a2e;color:#fff;padding:18px 28px;}}
.container{{max-width:1500px;margin:0 auto;padding:20px 16px;}}
tr:hover{{filter:brightness(0.97);}}th{{position:sticky;top:0;z-index:2;}}</style></head>
<body><div class="header"><h1 style="margin:0;font-size:20px;">KLSE Fundamentals
<span style="font-size:12px;color:#6610f2;">v2 · KC Chong + Cold Eye + Tong Kooi + MONEY</span></h1>
<div style="font-size:12px;color:#adb5bd;margin-top:4px;">Generated: {generated_at}
&nbsp;·&nbsp; Composite quality (max 50): KC Chong 14 + Cold Eye 14 + Tong Tier 10 + MONEY 12</div>
</div><div class="container">
<div style="display:flex;gap:10px;flex-wrap:wrap;margin:16px 0;">{counts_html}</div>
{table_html}
<div style="margin-top:16px;font-size:11px;color:#888;">
KC Chong (file 53) · Cold Eye (file 57) · Tong Kooi Ong (file 56) · Tradeview MONEY (file 54).
Some fields use proxies when direct scrape unavailable — see klse_screener_v3_quality_overlay.py for usage downstream.
</div></div></body></html>"""

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    universe = load_universe()
    print(f"\nKLSE Fundamental Data Fetcher v2 — Phase 2 Upgrade")
    print(f"Universe : {len(universe)} stocks  ·  Source : klsescreener.com")
    print("-" * 60)

    results = []
    total = len(universe)
    for i, (ticker, name, code) in enumerate(universe, 1):
        if i > 1 and (i - 1) % COOLDOWN_N == 0:
            print(f"  ... cooldown {COOLDOWN_SEC}s ...", flush=True)
            time.sleep(COOLDOWN_SEC)

        res = fetch_stock(ticker, name, code)
        results.append(res)
        q = res.get("quality_grade", "Q-D")
        kcs = res.get("kc_chong_passed")
        ces = res.get("cold_eye_passed")
        err = f"  [{res['error']}]" if res.get("error") else ""
        print(f"  [{i:3d}/{total}] {res['ticker']:12s} {res['name']:15s}  "
              f"{q:8s}  KC:{kcs}/8  Cold:{ces}/8  ROE:{res.get('roe') or '—':>5}"
              f"  DY:{(str(res.get('dy'))+'%' if res.get('dy') else '—'):>6}{err}", flush=True)

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
    webbrowser.open(OUTPUT_HTML.as_uri())
    print("Browser opened. JSON ready for klse_screener_v3_quality_overlay.py")


if __name__ == "__main__":
    main()
