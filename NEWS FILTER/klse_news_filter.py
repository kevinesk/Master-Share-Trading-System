"""
KLSE News Filter
================
Sources (in priority order):
  1. klsescreener.com — News articles  (stock-specific, today's KLSE news)
  2. klsescreener.com — Announcements  (official Bursa Malaysia filings)
  3. Yahoo Finance (yfinance)           — fallback, sparse for KLSE

Classifies each headline as POSITIVE / NEGATIVE / NEUTRAL using:
  - Claude Haiku API (if ANTHROPIC_API_KEY is set)
  - Keyword rules (fallback, no API key needed)

Requirements:
    pip install yfinance anthropic beautifulsoup4 certifi

Usage:
    Double-click run_daily.bat
    OR: python klse_news_filter.py
"""

import os
import re
import sys
import time
import datetime
import webbrowser
from pathlib import Path

# ── third-party ───────────────────────────────────────────────────────────────
try:
    from curl_cffi import requests as curl_requests
    _curl_ok = True
except ImportError:
    _curl_ok = False

try:
    from bs4 import BeautifulSoup
    _bs4_ok = True
except ImportError:
    _bs4_ok = False

try:
    import yfinance as yf
    _yf_ok = True
except ImportError:
    _yf_ok = False

try:
    import anthropic
    _anthropic_available = True
except ImportError:
    _anthropic_available = False

if not _curl_ok or not _bs4_ok:
    sys.exit("ERROR: Missing packages. Run:  pip install beautifulsoup4 curl_cffi")

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════════════
SCRIPT_DIR     = Path(__file__).parent
WATCHLIST_FILE = SCRIPT_DIR / "watchlist.txt"
OUTPUT_FILE    = SCRIPT_DIR / "klse_news_report.html"

NEWS_DAYS      = 7           # look back this many calendar days
MAX_NEWS       = 5           # max news articles to fetch per stock
MAX_ANN        = 5           # max announcements per stock
API_MODEL      = "claude-haiku-4-5-20251001"
API_DELAY_S    = 0.5
REQUEST_DELAY  = 0.3         # seconds between HTTP requests (polite scraping)

KLSESCREENER   = "https://www.klsescreener.com/v2"

# Shared curl_cffi session (SSL verify disabled — Windows cert store issue)
SESSION = curl_requests.Session(verify=False, impersonate="chrome")
SESSION.headers.update({"Accept-Language": "en-US,en;q=0.9"})

# ── keyword classifier ────────────────────────────────────────────────────────
POSITIVE_KW = [
    "profit", "earnings beat", "record revenue", "dividend", "contract win",
    "new order", "expansion", "upgrade", "buy rating", "outperform",
    "strong growth", "surge", "rally", "breakthrough", "acquisition target",
    "privatisation", "buyback", "special dividend", "bonus issue",
    "rights issue at premium", "joint venture", "export deal",
    "record high", "exceeds expectations", "revenue growth",
]
NEGATIVE_KW = [
    "loss", "deficit", "revenue miss", "earnings miss", "lawsuit",
    "fraud", "investigation", "fine", "penalty", "downgrade", "sell rating",
    "underperform", "warning", "restructuring", "layoff", "default",
    "debt", "recall", "regulatory action", "suspended", "de-listed",
    "profit warning", "impairment", "write-off", "write-down",
    "net loss", "lower profit", "revenue fell", "earnings fell",
]

# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def load_watchlist(path: Path) -> list[tuple[str, str, str]]:
    """Return list of (ticker, short_name, search_terms) from watchlist file.
    Watchlist format:  TICKER.KL  SHORT_NAME  [optional extra search words...]
    """
    stocks = []
    if not path.exists():
        print(f"[WARN] Watchlist not found: {path}")
        return stocks
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 2)
        ticker = parts[0].upper()
        name   = parts[1].strip() if len(parts) > 1 else ticker
        extra  = parts[2].strip() if len(parts) > 2 else ""
        stocks.append((ticker, name, extra))
    return stocks


def bursa_code(ticker: str) -> str:
    """'1155.KL' → '1155'"""
    return ticker.replace(".KL", "").replace(".kl", "").strip()


def get_page(url: str) -> "BeautifulSoup | None":
    try:
        r = SESSION.get(url, timeout=12)
        if r.status_code == 200:
            return BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        print(f"    [FETCH ERR] {url[-60:]}: {e}")
    return None


def parse_klsc_date(date_str: str) -> "datetime.datetime | None":
    """Parse 'Tue, May 19, 2026 03:57pm' → datetime (local)."""
    clean = re.sub(r'\s*-\s*\d+\s+\w+\s+ago$', '', date_str).strip()
    clean = re.sub(r'\s*-\s*\d+\s+\w+$', '', clean).strip()
    for fmt in ("%a, %b %d, %Y %I:%M%p", "%a, %b %d, %Y %I:%M %p",
                "%b %d, %Y %I:%M%p", "%b %d, %Y"):
        try:
            return datetime.datetime.strptime(clean, fmt)
        except ValueError:
            pass
    return None


def days_ago_cutoff(days: int) -> datetime.datetime:
    return datetime.datetime.now() - datetime.timedelta(days=days)


# ═══════════════════════════════════════════════════════════════════════════════
# SOURCE 1 — klsescreener NEWS
# ═══════════════════════════════════════════════════════════════════════════════

def _name_tokens(name: str, extra: str = "") -> list[str]:
    """
    Build search tokens from the watchlist name + optional extra column.
    The extra column in the watchlist file holds additional search words.
    Always includes the short name itself as a token.
    """
    tokens = [name.lower()]
    if extra:
        tokens.extend([w.lower() for w in extra.split() if len(w) > 2])
    return list(dict.fromkeys(tokens))  # deduplicate, preserve order


def _matches_stock(text: str, tokens: list[str]) -> bool:
    t = text.lower()
    return any(tok in t for tok in tokens)


def fetch_klsc_news(stock_code: str, name: str, extra: str = "") -> list[dict]:
    """
    Fetch news articles from klsescreener. Only returns articles where the
    stock name (or a known alias) appears in the headline or URL slug.
    """
    soup = get_page(f"{KLSESCREENER}/news?code={stock_code}")
    if soup is None:
        return []

    cutoff  = days_ago_cutoff(NEWS_DAYS)
    tokens  = _name_tokens(name, extra)

    # Collect article links that specifically mention this stock
    candidates = []
    for a in soup.find_all("a", href=True):
        href = a.get("href", "")
        txt  = a.get_text(strip=True)
        if "/v2/news/view/" not in href:
            continue
        if _matches_stock(txt, tokens) or _matches_stock(href, tokens):
            full_url = f"https://www.klsescreener.com{href}" if href.startswith("/") else href
            candidates.append((full_url, txt))

    results = []
    for url, title in candidates[:MAX_NEWS]:
        time.sleep(REQUEST_DELAY)
        art = get_page(url)
        if art is None:
            continue

        # Extract date: "Tue, May 19, 2026 03:57pm"
        text_lines = [l.strip() for l in art.get_text("\n", strip=True).split("\n") if l.strip()]
        pub_dt  = None
        source  = ""
        content = ""
        for i, line in enumerate(text_lines):
            if re.search(r'\w+,\s+\w+\s+\d+,\s+\d{4}', line):
                pub_dt = parse_klsc_date(line)
                if i > 0:
                    source = text_lines[i - 1]
                # content starts after date line
                content = " ".join(text_lines[i+1:i+8])
                break

        if pub_dt and pub_dt < cutoff:
            continue

        results.append({
            "source":  "klsescreener-news",
            "title":   title,
            "summary": content[:300],
            "url":     url,
            "provider": source or "KLSE Screener",
            "ts":      pub_dt.timestamp() if pub_dt else time.time(),
        })

    return results


# ═══════════════════════════════════════════════════════════════════════════════
# SOURCE 2 — klsescreener ANNOUNCEMENTS
# ═══════════════════════════════════════════════════════════════════════════════

# Categories to keep (filter out routine shareholding changes)
IMPORTANT_ANN_TYPES = {
    "Financial Results", "Dividend", "General Announcement",
    "Quarterly Results", "Annual Results", "Rights Issue",
    "Bonus Issue", "Private Placement", "Change in Boardroom",
    "Change in Audit Committee", "Listing Circular",
}
SKIP_ANN_TYPES = {"Changes in Shareholdings"}

MONTH_MAP = {m: i+1 for i, m in enumerate(
    ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])}

def parse_ann_date(day: str, month_str: str) -> "datetime.datetime | None":
    """Turn '18' + 'May' → datetime for current/previous year."""
    try:
        day_n   = int(day)
        month_n = MONTH_MAP.get(month_str[:3].capitalize(), 0)
        if not month_n:
            return None
        now  = datetime.datetime.now()
        year = now.year
        dt   = datetime.datetime(year, month_n, day_n)
        if dt > now + datetime.timedelta(days=1):
            dt = datetime.datetime(year - 1, month_n, day_n)
        return dt
    except Exception:
        return None


def fetch_klsc_announcements(stock_code: str) -> list[dict]:
    """Parse Bursa Malaysia announcements from klsescreener."""
    soup = get_page(f"{KLSESCREENER}/announcements?code={stock_code}")
    if soup is None:
        return []

    cutoff = days_ago_cutoff(NEWS_DAYS)
    results = []

    for a in soup.find_all("a", href=True):
        href = a.get("href", "")
        if "/v2/announcements/view/" not in href:
            continue
        txt = a.get_text(" ", strip=True)
        if not txt:
            continue

        # Pattern: "18MayCOMPANY NAMECategory HH:MM amTitle..."
        m = re.match(
            r'(\d{1,2})(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
            r'(.+?)(Financial Results|Dividend|General Announcement|Quarterly|Annual|'
            r'Rights Issue|Bonus Issue|Private Placement|Change in Boardroom|'
            r'Changes in Shareholdings|Listing Circular|Others)'
            r'(.*)',
            txt
        )
        if not m:
            continue

        day, month_str, _company, category, rest = m.groups()
        category = category.strip()

        if category in SKIP_ANN_TYPES:
            continue

        pub_dt = parse_ann_date(day, month_str)
        if pub_dt and pub_dt < cutoff:
            continue

        # Extract time + title from remainder
        time_m = re.search(r'(\d+:\d+\s*[ap]m)', rest, re.IGNORECASE)
        time_str = time_m.group(1).strip() if time_m else ""
        title = rest.replace(time_str, "").strip() if time_str else rest.strip()
        title = re.sub(r'^OTHERS\s*', '', title).strip()

        full_url = f"https://www.klsescreener.com{href}" if href.startswith("/") else href
        display_title = f"[{category}] {title}" if title else f"[{category}]"

        results.append({
            "source":   "klsescreener-ann",
            "title":    display_title,
            "summary":  f"Official Bursa Malaysia announcement — {category}.",
            "url":      full_url,
            "provider": "Bursa Malaysia via KLSE Screener",
            "ts":       pub_dt.timestamp() if pub_dt else time.time(),
        })

        if len(results) >= MAX_ANN:
            break

    return results


# ═══════════════════════════════════════════════════════════════════════════════
# SOURCE 3 — Yahoo Finance (fallback)
# ═══════════════════════════════════════════════════════════════════════════════

_yf_session = None
if _yf_ok:
    try:
        _yf_session = curl_requests.Session(verify=False, impersonate="chrome")
    except Exception:
        pass


def fetch_yfinance(ticker: str) -> list[dict]:
    if not _yf_ok or _yf_session is None:
        return []
    cutoff = time.time() - NEWS_DAYS * 86400
    try:
        stock = yf.Ticker(ticker, session=_yf_session)
        raw   = stock.news or []
    except Exception:
        return []

    results = []
    for article in raw:
        c = article.get("content", article)
        if isinstance(c, dict):
            pub = c.get("pubDate", "")
            try:
                dt      = datetime.datetime.fromisoformat(pub.replace("Z", "+00:00"))
                ts_unix = dt.timestamp()
            except Exception:
                ts_unix = float(article.get("providerPublishTime", 0))
            title    = c.get("title", "")
            summary  = c.get("summary", "")[:300]
            url      = c.get("canonicalUrl", {}).get("url", "")
            provider = c.get("provider", {}).get("displayName", "Yahoo Finance")
        else:
            ts_unix  = float(article.get("providerPublishTime", 0))
            title    = article.get("title", "")
            summary  = article.get("summary", "")[:300]
            url      = article.get("link", "")
            provider = article.get("publisher", "Yahoo Finance")

        if ts_unix < cutoff:
            continue

        results.append({
            "source":   "yfinance",
            "title":    title,
            "summary":  summary,
            "url":      url,
            "provider": provider,
            "ts":       ts_unix,
        })

    results.sort(key=lambda x: x["ts"], reverse=True)
    return results


# ═══════════════════════════════════════════════════════════════════════════════
# COMBINED FETCHER
# ═══════════════════════════════════════════════════════════════════════════════

def fetch_all_news(ticker: str, name: str, extra: str = "") -> list[dict]:
    code  = bursa_code(ticker)
    items = []

    news = fetch_klsc_news(code, name, extra)
    items.extend(news)
    time.sleep(REQUEST_DELAY)

    anns = fetch_klsc_announcements(code)
    items.extend(anns)
    time.sleep(REQUEST_DELAY)

    if not items:
        items.extend(fetch_yfinance(ticker))

    items.sort(key=lambda x: x["ts"], reverse=True)
    return items


# ═══════════════════════════════════════════════════════════════════════════════
# CLASSIFIER
# ═══════════════════════════════════════════════════════════════════════════════

def _extract_key_sentence(text: str, keywords: list[str]) -> str:
    """Return the first sentence in text that contains any keyword."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    for sent in sentences:
        if any(kw in sent.lower() for kw in keywords):
            sent = sent.strip()
            return sent[:200] + ("..." if len(sent) > 200 else "")
    return ""


def classify_keyword(title: str, summary: str) -> tuple[str, str]:
    text = (title + " " + summary).lower()
    full_text = title + " " + summary

    pos_hits = [kw for kw in POSITIVE_KW if kw in text]
    neg_hits = [kw for kw in NEGATIVE_KW if kw in text]

    if len(pos_hits) > len(neg_hits):
        key_sent = _extract_key_sentence(full_text, pos_hits)
        reason = key_sent if key_sent else f"Positive signals detected: {', '.join(pos_hits[:3])}."
        return "POSITIVE", reason
    if len(neg_hits) > len(pos_hits):
        key_sent = _extract_key_sentence(full_text, neg_hits)
        reason = key_sent if key_sent else f"Negative signals detected: {', '.join(neg_hits[:3])}."
        return "NEGATIVE", reason

    # Neutral — extract first substantive sentence from summary as context
    if summary:
        sentences = re.split(r'(?<=[.!?])\s+', summary.strip())
        for sent in sentences:
            if len(sent) > 30:
                sent = sent.strip()
                return "NEUTRAL", (sent[:200] + "..." if len(sent) > 200 else sent)
    return "NEUTRAL", title[:200]


_api_client = None

def _get_api_client():
    global _api_client
    if _api_client is None:
        key = os.environ.get("ANTHROPIC_API_KEY", "")
        if key and _anthropic_available:
            _api_client = anthropic.Anthropic(api_key=key)
    return _api_client


def classify_ai(ticker: str, name: str, title: str, summary: str) -> tuple[str, str]:
    client = _get_api_client()
    if client is None:
        return classify_keyword(title, summary)
    prompt = (
        f"You are a KLSE stock analyst. Analyse this news about {name} ({ticker}).\n\n"
        f"Headline: {title}\n"
        f"Summary: {summary}\n\n"
        "Respond with exactly this format — one line only:\n"
        "CLASSIFICATION | One-sentence reason focused on share price impact.\n"
        "Where CLASSIFICATION is one of: POSITIVE, NEGATIVE, NEUTRAL"
    )
    try:
        msg = client.messages.create(
            model=API_MODEL, max_tokens=120,
            messages=[{"role": "user", "content": prompt}],
        )
        response = msg.content[0].text.strip()
        time.sleep(API_DELAY_S)
        if "|" in response:
            label, reason = response.split("|", 1)
            label = label.strip().upper()
            if label not in ("POSITIVE", "NEGATIVE", "NEUTRAL"):
                label = "NEUTRAL"
            return label, reason.strip()
        for lbl in ("POSITIVE", "NEGATIVE", "NEUTRAL"):
            if lbl in response.upper():
                return lbl, response
        return "NEUTRAL", response
    except Exception as e:
        print(f"    [API WARN] {e} — keyword fallback")
        return classify_keyword(title, summary)


def classify(ticker: str, name: str, title: str, summary: str) -> tuple[str, str]:
    if os.environ.get("ANTHROPIC_API_KEY") and _anthropic_available:
        return classify_ai(ticker, name, title, summary)
    return classify_keyword(title, summary)


def assess_stock_overall(ticker: str, name: str, items: list[dict]) -> tuple[str, str]:
    """
    Ask Claude to read ALL articles for this stock and give a single
    overall POSITIVE / NEUTRAL / NEGATIVE verdict + one-sentence assessment.
    Used for the summary table row. Falls back to keyword majority vote.
    """
    if not items:
        return "—", "No recent news."

    use_ai = bool(os.environ.get("ANTHROPIC_API_KEY")) and _anthropic_available

    if use_ai:
        client = _get_api_client()
        if client:
            news_block = ""
            for i, it in enumerate(items, 1):
                src = SOURCE_LABEL.get(it["source"], ("News", ""))[0]
                news_block += f"{i}. [{src}] {it['title']}\n"
                if it.get("summary"):
                    news_block += f"   {it['summary'][:400]}\n"
                news_block += "\n"

            prompt = (
                f"You are a KLSE equity analyst. Analyze the following recent news about "
                f"{name} ({ticker}) listed on Bursa Malaysia.\n\n"
                f"{news_block}"
                f"Based on ALL the above, assess the likely short-term (1–5 day) share price impact on {name}.\n"
                f"Respond in exactly this format — one line only:\n"
                f"CLASSIFICATION | Your one-sentence assessment.\n"
                f"Where CLASSIFICATION is: POSITIVE, NEGATIVE, or NEUTRAL\n"
                f"Do NOT copy the headline. Write your own analytical conclusion."
            )
            try:
                msg = client.messages.create(
                    model=API_MODEL, max_tokens=160,
                    messages=[{"role": "user", "content": prompt}],
                )
                response = msg.content[0].text.strip()
                time.sleep(API_DELAY_S)
                if "|" in response:
                    label, reason = response.split("|", 1)
                    label = label.strip().upper()
                    if label not in ("POSITIVE", "NEGATIVE", "NEUTRAL"):
                        label = "NEUTRAL"
                    return label, reason.strip()
                for lbl in ("POSITIVE", "NEGATIVE", "NEUTRAL"):
                    if lbl in response.upper():
                        return lbl, response
                return "NEUTRAL", response
            except Exception as e:
                print(f"    [AI ERR] {e}")

    # Keyword majority vote fallback
    votes = [classify_keyword(it["title"], it.get("summary", ""))[0] for it in items]
    pos = votes.count("POSITIVE")
    neg = votes.count("NEGATIVE")
    if pos > neg:
        return "POSITIVE", f"Majority positive signals across {len(items)} article(s)."
    if neg > pos:
        return "NEGATIVE", f"Majority negative signals across {len(items)} article(s)."
    return "NEUTRAL", f"Mixed or neutral coverage across {len(items)} article(s)."


# ═══════════════════════════════════════════════════════════════════════════════
# HTML REPORT
# ═══════════════════════════════════════════════════════════════════════════════

SOURCE_LABEL = {
    "klsescreener-news": ("KLSE Screener", "#1565C0"),
    "klsescreener-ann":  ("Bursa Announcement", "#6A1B9A"),
    "yfinance":          ("Yahoo Finance", "#E65100"),
}

def _label_style(label: str) -> tuple[str, str]:
    return {
        "POSITIVE": ("#d4edda", "#155724"),
        "NEGATIVE": ("#f8d7da", "#721c24"),
        "NEUTRAL":  ("#e2e3e5", "#383d41"),
    }.get(label, ("#e2e3e5", "#383d41"))


def ts_to_str(ts: float) -> str:
    if not ts:
        return "—"
    return datetime.datetime.fromtimestamp(ts).strftime("%d %b %Y  %H:%M")


def _sentiment_badge(label: str) -> tuple[str, str]:
    """Return (badge_html, row_bg) for a sentiment label."""
    if label == "POSITIVE":
        return '<span style="background:#198754;color:#fff;padding:2px 10px;border-radius:3px;font-size:11px;font-weight:700;">POSITIVE</span>', "#f0fff4"
    if label == "NEGATIVE":
        return '<span style="background:#dc3545;color:#fff;padding:2px 10px;border-radius:3px;font-size:11px;font-weight:700;">NEGATIVE</span>', "#fff5f5"
    if label == "NEUTRAL":
        return '<span style="background:#0d6efd;color:#fff;padding:2px 10px;border-radius:3px;font-size:11px;font-weight:700;">NEUTRAL</span>', "#f0f4ff"
    return '<span style="color:#aaa;">—</span>', "#fff"


def build_html(results: list[dict], generated_at: str, mode: str, wl_label: str = "WATCHLIST") -> str:

    # ── Summary table ────────────────────────────────────────────────────────
    table_rows = []
    for i, stock in enumerate(results, 1):
        ticker  = stock["ticker"]
        name    = stock["name"]
        items   = stock["items"]
        sent_lbl = stock.get("overall_label", "—")
        top_rsn  = stock.get("overall_remark", "—")
        sent_badge, row_bg = _sentiment_badge(sent_lbl)
        n_items = len(items)
        anchor  = f"stock-{ticker.replace('.','')}"
        table_rows.append(
            f'<tr style="background:{row_bg};border-bottom:1px solid #dee2e6;">'
            f'<td style="padding:7px 10px;font-size:13px;color:#555;">{i}</td>'
            f'<td style="padding:7px 10px;font-size:13px;font-weight:700;">'
            f'<a href="#{anchor}" style="color:#212529;text-decoration:none;">{name}</a></td>'
            f'<td style="padding:7px 10px;font-size:12px;color:#888;">{ticker}</td>'
            f'<td style="padding:7px 10px;text-align:center;">{sent_badge}</td>'
            f'<td style="padding:7px 10px;font-size:12px;color:#555;">{top_rsn}</td>'
            f'<td style="padding:7px 10px;text-align:center;font-size:12px;color:#888;">{n_items}</td>'
            f'</tr>'
        )

    summary_table = f"""
    <div style="background:#fff;border:1px solid #dee2e6;border-radius:8px;margin:16px 0;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.08);">
      <div style="background:#1F2937;color:#fff;padding:10px 16px;font-size:14px;font-weight:600;">
        {wl_label} — Summary Table &nbsp;·&nbsp; {generated_at}
      </div>
      <div style="overflow-x:auto;">
      <table style="width:100%;border-collapse:collapse;">
        <thead>
          <tr style="background:#f1f3f5;border-bottom:2px solid #dee2e6;">
            <th style="padding:8px 10px;text-align:left;font-size:12px;color:#555;width:30px;">#</th>
            <th style="padding:8px 10px;text-align:left;font-size:12px;color:#555;">Stock</th>
            <th style="padding:8px 10px;text-align:left;font-size:12px;color:#555;">Ticker</th>
            <th style="padding:8px 10px;text-align:center;font-size:12px;color:#555;width:110px;">Sentiment</th>
            <th style="padding:8px 10px;text-align:left;font-size:12px;color:#555;">Key Remark</th>
            <th style="padding:8px 10px;text-align:center;font-size:12px;color:#555;width:60px;">Items</th>
          </tr>
        </thead>
        <tbody>
          {"".join(table_rows)}
        </tbody>
      </table>
      </div>
    </div>"""

    # ── Per-stock detail sections ────────────────────────────────────────────
    stock_sections = []
    for stock in results:
        ticker = stock["ticker"]
        name   = stock["name"]
        items  = stock["items"]
        anchor = f"stock-{ticker.replace('.','')}"
        sent_lbl = stock.get("overall_label", "—")
        sent_badge, _ = _sentiment_badge(sent_lbl)

        if not items:
            article_html = '<p style="color:#888;font-style:italic;margin:0;">No news in the last 7 days.</p>'
        else:
            rows = []
            for it in items:
                label   = it["label"]
                reason  = it.get("reason", "")
                bg, fg  = _label_style(label)
                url     = it["url"]
                title   = it["title"] or "(no title)"
                src_lbl, src_col = SOURCE_LABEL.get(it["source"], ("News", "#555"))
                link = (f'<a href="{url}" target="_blank" style="color:#1a73e8;text-decoration:none;">{title}</a>'
                        if url else title)
                badge_bg = {"POSITIVE": "#198754", "NEGATIVE": "#dc3545"}.get(label, "#6c757d")
                rows.append(
                    f'<div style="background:{bg};border-left:4px solid {fg};padding:10px 14px;margin:8px 0;border-radius:4px;">'
                    f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:5px;flex-wrap:wrap;">'
                    f'<span style="background:{badge_bg};color:#fff;padding:2px 8px;border-radius:3px;font-size:11px;font-weight:700;">{label}</span>'
                    f'<span style="background:{src_col};color:#fff;padding:2px 7px;border-radius:3px;font-size:10px;">{src_lbl}</span>'
                    f'<span style="font-size:13px;font-weight:600;">{link}</span></div>'
                    f'<div style="font-size:12px;color:{fg};margin-bottom:3px;line-height:1.5;">{reason}</div>'
                    f'<div style="font-size:11px;color:#888;">{it["provider"]} &nbsp;·&nbsp; {ts_to_str(it["ts"])}</div>'
                    f'</div>'
                )
            article_html = "\n".join(rows)

        stock_sections.append(
            f'<div id="{anchor}" style="background:#fff;border:1px solid #dee2e6;border-radius:8px;'
            f'padding:16px 20px;margin:16px 0;box-shadow:0 1px 3px rgba(0,0,0,.08);">'
            f'<h2 style="margin:0 0 12px;font-size:15px;color:#212529;display:flex;align-items:center;gap:8px;">'
            f'{name} <span style="color:#6c757d;font-size:12px;font-weight:400;">({ticker})</span>'
            f'&nbsp;{sent_badge}</h2>'
            f'{article_html}</div>'
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>KLSE News Filter — {generated_at}</title>
  <style>
    body {{ font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
           background:#f8f9fa;margin:0;padding:0;color:#212529; }}
    .header {{ background:#1a1a2e;color:#fff;padding:18px 28px; }}
    .header h1 {{ margin:0;font-size:20px; }}
    .header .meta {{ font-size:12px;color:#adb5bd;margin-top:4px; }}
    .container {{ max-width:960px;margin:0 auto;padding:20px 16px; }}
    a:hover {{ text-decoration:underline !important; }}
    tr:hover {{ filter:brightness(0.97); }}
  </style>
</head>
<body>
  <div class="header">
    <h1>KLSE News Filter</h1>
    <div class="meta">Generated: {generated_at} &nbsp;·&nbsp; Mode: {mode} &nbsp;·&nbsp;
      Last {NEWS_DAYS} days &nbsp;·&nbsp;
      Sources: <span style="color:#90CAF9;">KLSE Screener</span> +
      <span style="color:#CE93D8;">Bursa Announcements</span></div>
  </div>
  <div class="container">
    {summary_table}
    {"".join(stock_sections)}
  </div>
</body>
</html>"""


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    # Accept optional watchlist filename as first argument
    if len(sys.argv) > 1:
        wl_path = SCRIPT_DIR / sys.argv[1]
    else:
        wl_path = WATCHLIST_FILE

    stocks = load_watchlist(wl_path)
    if not stocks:
        sys.exit(f"No stocks loaded — check {wl_path}")

    use_ai = bool(os.environ.get("ANTHROPIC_API_KEY")) and _anthropic_available
    mode   = f"Claude Haiku AI ({API_MODEL})" if use_ai else "Keyword rules (set ANTHROPIC_API_KEY for AI analysis)"
    wl_label = wl_path.stem.upper().replace("_", " ")
    generated_at = datetime.datetime.now().strftime("%d %b %Y  %H:%M")

    print(f"\nKLSE News Filter - {wl_label}")
    print(f"Mode        : {mode}")
    print(f"Stocks      : {len(stocks)}")
    print(f"Lookback    : last {NEWS_DAYS} days")
    print(f"Sources     : KLSE Screener news + Bursa announcements + Yahoo Finance")
    print(f"Generated   : {generated_at}")
    print("-" * 60)

    all_results = []
    for ticker, name, extra in stocks:
        print(f"  {ticker:12s} {name} ...", end=" ", flush=True)
        raw_items = fetch_all_news(ticker, name, extra)

        # Per-article classification
        classified = []
        for it in raw_items:
            label, reason = classify(ticker, name, it["title"], it["summary"])
            classified.append({**it, "label": label, "reason": reason})

        # Stock-level overall assessment (Claude reads ALL articles together)
        overall_label, overall_remark = assess_stock_overall(ticker, name, classified)

        pos = sum(1 for i in classified if i["label"] == "POSITIVE")
        neg = sum(1 for i in classified if i["label"] == "NEGATIVE")
        print(f"{len(classified)} items  (+{pos} / -{neg})  [{overall_label}]")
        all_results.append({
            "ticker": ticker, "name": name,
            "items": classified,
            "overall_label": overall_label,
            "overall_remark": overall_remark,
        })

    html = build_html(all_results, generated_at, mode, wl_label)
    out_file = SCRIPT_DIR / f"klse_news_{wl_path.stem}.html"
    out_file.write_text(html, encoding="utf-8")
    print(f"\nReport saved: {out_file}")
    webbrowser.open(out_file.as_uri())
    print("Browser opened.")


if __name__ == "__main__":
    main()
