"""
US News Filter v1
=================
US sibling of the KLSE news filter. Pulls recent headlines per ticker via
yfinance, classifies each by catalyst type (BULLISH / BEARISH / EARNINGS /
NEUTRAL) using keyword matching, and writes an HTML report grouped by ticker.

Why catalysts matter for swing trades: a downgrade or guidance cut overnight
can gap a stock against you at the US open. Reviewing this report during your
Malaysia day BEFORE placing pre-open orders helps you avoid event landmines.

SETUP (one time):
    pip install yfinance
USAGE:
    Double-click run_news_us.bat   OR   py us_news_filter.py

Watchlist: us_watchlist.txt in this folder, one TICKER per line (# = comment).
"""

import sys
import datetime
import webbrowser
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    sys.exit("ERROR: pip install yfinance")

SCRIPT_DIR     = Path(__file__).parent
WATCHLIST_FILE = SCRIPT_DIR / "us_watchlist.txt"
OUTPUT_DIR     = SCRIPT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
TODAY          = datetime.date.today().strftime("%Y-%m-%d")
OUTPUT_HTML    = OUTPUT_DIR / f"us_news_{TODAY}.html"

MAX_AGE_DAYS   = 5     # only show headlines newer than this

# --- Catalyst keyword maps ---------------------------------------------------
BULLISH = ["upgrade", "raised", "beats", "beat estimates", "record", "approval",
           "approved", "buyback", "repurchase", "dividend increase", "hikes dividend",
           "contract", "partnership", "wins", "breakthrough", "outperform",
           "price target raised", "all-time high", "surge", "soars", "acquire", "guidance raise"]
BEARISH = ["downgrade", "cut", "miss", "misses", "lawsuit", "investigation", "probe",
           "recall", "layoff", "sec ", "delay", "warning", "warns", "bankruptcy",
           "fraud", "halts", "plunge", "slumps", "sinks", "guidance cut", "subpoena",
           "short seller", "underperform", "price target cut"]
EARNINGS = ["earnings", "q1 ", "q2 ", "q3 ", "q4 ", "quarter", "results", "revenue", "eps"]


def load_watchlist():
    if not WATCHLIST_FILE.exists():
        sys.exit(f"ERROR: missing {WATCHLIST_FILE}. Add one TICKER per line.")
    out = []
    for line in WATCHLIST_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line.split()[0].upper())
    return out


def classify(title):
    t = title.lower()
    if any(k in t for k in BEARISH):
        return "BEARISH", "#dc3545"
    if any(k in t for k in BULLISH):
        return "BULLISH", "#198754"
    if any(k in t for k in EARNINGS):
        return "EARNINGS", "#6610f2"
    return "NEUTRAL", "#6c757d"


def parse_item(it):
    """yfinance news items come in two shapes (old flat / new nested 'content')."""
    c = it.get("content") if isinstance(it.get("content"), dict) else it
    title = c.get("title") or it.get("title") or ""
    publisher = it.get("publisher")
    if not publisher and isinstance(c.get("provider"), dict):
        publisher = c["provider"].get("displayName")
    publisher = publisher or "-"
    # link
    link = it.get("link")
    if not link and isinstance(c.get("canonicalUrl"), dict):
        link = c["canonicalUrl"].get("url")
    if not link and isinstance(c.get("clickThroughUrl"), dict):
        link = c["clickThroughUrl"].get("url")
    link = link or "#"
    # time
    dt = None
    if it.get("providerPublishTime"):
        try:
            dt = datetime.datetime.fromtimestamp(it["providerPublishTime"])
        except Exception:
            dt = None
    if dt is None:
        raw = c.get("pubDate") or c.get("displayTime")
        if raw:
            try:
                dt = datetime.datetime.fromisoformat(str(raw).replace("Z", "+00:00")).replace(tzinfo=None)
            except Exception:
                dt = None
    return title, publisher, link, dt


def fetch_news(ticker):
    items = []
    try:
        raw = yf.Ticker(ticker).news or []
    except Exception:
        raw = []
    cutoff = datetime.datetime.now() - datetime.timedelta(days=MAX_AGE_DAYS)
    for it in raw:
        title, publisher, link, dt = parse_item(it)
        if not title:
            continue
        if dt and dt < cutoff:
            continue
        cat, col = classify(title)
        items.append({"title": title, "publisher": publisher, "link": link,
                      "dt": dt, "cat": cat, "col": col})
    # newest first
    items.sort(key=lambda x: x["dt"] or datetime.datetime.min, reverse=True)
    return items


def build_html(data, generated_at):
    # data = list of (ticker, items)
    total = sum(len(items) for _, items in data)
    bear = sum(1 for _, items in data for x in items if x["cat"] == "BEARISH")
    bull = sum(1 for _, items in data for x in items if x["cat"] == "BULLISH")
    earn = sum(1 for _, items in data for x in items if x["cat"] == "EARNINGS")

    chips = (f'<span style="background:#dc354533;color:#dc3545;padding:4px 10px;border-radius:5px;font-weight:600;">BEARISH {bear}</span>'
             f'<span style="background:#19875433;color:#198754;padding:4px 10px;border-radius:5px;font-weight:600;">BULLISH {bull}</span>'
             f'<span style="background:#6610f233;color:#6610f2;padding:4px 10px;border-radius:5px;font-weight:600;">EARNINGS {earn}</span>')

    blocks = []
    for ticker, items in data:
        if not items:
            continue
        rows = []
        for x in items:
            when = x["dt"].strftime("%d %b %H:%M") if x["dt"] else "-"
            rows.append(
                f'<tr style="border-bottom:1px solid #eee;">'
                f'<td style="padding:6px 8px;white-space:nowrap;"><span style="background:{x["col"]};color:#fff;padding:1px 7px;border-radius:4px;font-size:10px;font-weight:700;">{x["cat"]}</span></td>'
                f'<td style="padding:6px 8px;"><a href="{x["link"]}" target="_blank" style="color:#1a1a2e;text-decoration:none;">{x["title"]}</a></td>'
                f'<td style="padding:6px 8px;font-size:11px;color:#888;white-space:nowrap;">{x["publisher"]}</td>'
                f'<td style="padding:6px 8px;font-size:11px;color:#888;white-space:nowrap;">{when}</td>'
                f'</tr>'
            )
        blocks.append(
            f'<div style="background:#fff;border-radius:8px;margin:14px 0;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.08);">'
            f'<div style="background:#1a1a2e;color:#fff;padding:8px 14px;font-weight:700;">{ticker} '
            f'<span style="font-size:11px;color:#adb5bd;font-weight:400;">({len(items)} headlines)</span></div>'
            f'<table style="width:100%;border-collapse:collapse;">{"".join(rows)}</table></div>'
        )

    no_news = "".join(f"{t} " for t, items in data if not items)
    no_news_html = (f'<div style="font-size:11px;color:#aaa;margin-top:10px;">No recent news: {no_news}</div>'
                    if no_news else "")

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>US News - {generated_at}</title>
<style>body{{font-family:-apple-system,Segoe UI,Roboto,sans-serif;background:#f8f9fa;margin:0;}}
.header{{background:#1a1a2e;color:#fff;padding:18px 28px;}}
.container{{max-width:1100px;margin:0 auto;padding:20px 16px;}}
tr:hover{{background:#f6f8fa;}}</style></head>
<body><div class="header"><h1 style="margin:0;font-size:20px;">US Watchlist News
<span style="font-size:12px;color:#6610f2;">v1 - catalyst filter</span></h1>
<div style="font-size:12px;color:#adb5bd;margin-top:4px;">Generated: {generated_at} -
{total} headlines &lt;{MAX_AGE_DAYS}d - review before placing pre-open orders</div></div>
<div class="container"><div style="display:flex;gap:8px;margin:10px 0;">{chips}</div>
{"".join(blocks)}{no_news_html}
<div style="margin-top:16px;font-size:11px;color:#888;">Source: yfinance (Yahoo Finance). Catalyst tags are keyword-based - read the headline before acting.</div>
</div></body></html>"""


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    tickers = load_watchlist()
    print(f"\nUS News Filter v1 - {len(tickers)} tickers, <{MAX_AGE_DAYS}d window")
    print("-" * 50)
    data = []
    for i, t in enumerate(tickers, 1):
        items = fetch_news(t)
        data.append((t, items))
        flags = sum(1 for x in items if x["cat"] in ("BEARISH", "BULLISH", "EARNINGS"))
        print(f"  [{i:3d}/{len(tickers)}] {t:8s}  {len(items):2d} headlines  ({flags} catalysts)", flush=True)

    generated_at = datetime.datetime.now().strftime("%d %b %Y  %H:%M")
    OUTPUT_HTML.write_text(build_html(data, generated_at), encoding="utf-8")
    print(f"\nHTML : {OUTPUT_HTML}")
    try:
        webbrowser.open(OUTPUT_HTML.as_uri())
    except Exception:
        pass
    print("Done.")


if __name__ == "__main__":
    main()
