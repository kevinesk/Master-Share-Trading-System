"""
KLSE Annual Report Analyzer
============================
Downloads the latest annual report PDF for a KLSE stock from Bursa Malaysia
(via klsescreener.com), extracts the text, and sends it to Claude AI for a
trading-focused fundamental analysis. Saves the result to the Knowledge Base.

Usage:
    py annual_report.py 1023          (CIMB by Bursa code)
    py annual_report.py MAYBANK       (by name — searches universe.txt)
    py annual_report.py 1023 --year 2023   (force a specific year)

Output:
    Knowledge Base\AR_1023_CIMB_2024.md   (trading analysis in Markdown)
    Fundamentals\ar_cache\1023_2024.pdf    (cached PDF)

Requirements:
    pip install curl_cffi beautifulsoup4 pdfplumber anthropic
"""

import sys
import re
import os
import time
import json
import random
import argparse
import datetime
from pathlib import Path

# ── Dependency checks ─────────────────────────────────────────────────────────
try:
    from curl_cffi import requests as curl_requests
    SESSION = curl_requests.Session(verify=False, impersonate="chrome")
except ImportError:
    sys.exit("ERROR: Run:  pip install curl_cffi")

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("ERROR: Run:  pip install beautifulsoup4")

try:
    import pdfplumber
except ImportError:
    sys.exit("ERROR: Run:  pip install pdfplumber")

try:
    import anthropic
except ImportError:
    sys.exit("ERROR: Run:  pip install anthropic")

# ── API Key setup ──────────────────────────────────────────────────────────────
# Load from environment OR from a local key file (api_key.txt in this folder)
def _load_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key:
        key_file = Path(__file__).parent / "api_key.txt"
        if key_file.exists():
            key = key_file.read_text(encoding="utf-8").strip()
    if not key:
        print("\nERROR: ANTHROPIC_API_KEY not found.")
        print("To fix, do ONE of:")
        print("  Option A — Set environment variable (PowerShell):")
        print("    $env:ANTHROPIC_API_KEY = 'sk-ant-...'")
        print("    setx ANTHROPIC_API_KEY 'sk-ant-...'   (permanent)")
        print()
        print("  Option B — Create a key file:")
        print(f"    {Path(__file__).parent / 'api_key.txt'}")
        print("    Paste your key (sk-ant-...) as the only line in that file.")
        print()
        print("Get your API key at: https://console.anthropic.com/")
        sys.exit(1)
    return key

import warnings
warnings.filterwarnings("ignore")

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR     = Path(__file__).parent
UNIVERSE_FILE  = SCRIPT_DIR.parent / "KLSE Screener" / "universe.txt"
KNOWLEDGE_DIR  = SCRIPT_DIR.parent / "Knowledge Base"
CACHE_DIR      = SCRIPT_DIR / "ar_cache"
CACHE_DIR.mkdir(exist_ok=True)

BASE_SCREENER  = "https://www.klsescreener.com"
TIMEOUT        = 30
CLAUDE_MODEL   = "claude-opus-4-7"    # best model for document analysis
MAX_PDF_CHARS  = 180_000              # ~45k tokens — enough for full AR

# ── Universe helpers ──────────────────────────────────────────────────────────

def load_universe() -> dict[str, tuple[str, str]]:
    """Returns {ticker_code: (name, url_code)} e.g. {'1023': ('CIMB', '1023')}"""
    mapping = {}
    for line in UNIVERSE_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            ticker   = parts[0]           # e.g. "1023.KL"
            code     = ticker.replace(".KL", "").replace(".kl", "")
            name     = parts[1]
            mapping[code] = (name, code)
            mapping[name.upper()] = (name, code)
    return mapping


def resolve_stock(query: str) -> tuple[str, str]:
    """Resolve user input (code or name) to (name, url_code)."""
    universe = load_universe()
    key = query.upper().replace(".KL", "")
    if key in universe:
        return universe[key]
    # Try prefix match on name
    for k, v in universe.items():
        if k.startswith(key) or key.startswith(k):
            return v
    sys.exit(f"ERROR: '{query}' not found in universe.txt — check the code or name.")

# ── Bursa announcement search ─────────────────────────────────────────────────

def find_annual_report_url(code: str, year: int | None = None) -> tuple[str, int]:
    """
    Searches klsescreener.com for the latest annual report announcement for
    the given stock code. Returns (download_url, report_year).
    """
    print(f"  Searching for annual report on klsescreener.com ...")
    ann_url = f"{BASE_SCREENER}/v2/stocks/view/{code}#announcement"
    resp    = SESSION.get(ann_url, timeout=TIMEOUT)
    if resp.status_code != 200:
        raise RuntimeError(f"Cannot load stock page: HTTP {resp.status_code}")

    soup = BeautifulSoup(resp.text, "html.parser")

    # Find all announcement links that look like annual reports
    candidates = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        text = a.get_text(" ", strip=True)
        if "annual report" in text.lower() or "laporan tahunan" in text.lower():
            # Extract year from text if present
            yr_match = re.search(r"20[12]\d", text)
            yr = int(yr_match.group()) if yr_match else 0
            if "FileAccess" in href or "apbursaweb" in href or "download" in href.lower():
                candidates.append((yr, href))
            elif href.startswith("/"):
                candidates.append((yr, BASE_SCREENER + href))

    if not candidates:
        # Fallback: search for Bursa EDGAR-style download links
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "FileAccess" in href and "EA_DS" in href:
                yr_match = re.search(r"20[12]\d", a.get_text(" ", strip=True))
                yr = int(yr_match.group()) if yr_match else 0
                candidates.append((yr, href))

    if not candidates:
        raise RuntimeError(
            "No annual report links found on klsescreener.com for this stock.\n"
            "The stock may not have filed yet, or the page structure has changed."
        )

    # Sort by year descending
    candidates.sort(key=lambda x: x[0], reverse=True)

    if year:
        filtered = [(y, h) for y, h in candidates if y == year]
        if not filtered:
            available = sorted({y for y, _ in candidates}, reverse=True)
            raise RuntimeError(f"Year {year} not found. Available years: {available}")
        candidates = filtered

    report_year, url = candidates[0]
    if not report_year:
        report_year = datetime.date.today().year - 1

    # Make absolute URL if needed
    if url.startswith("/"):
        url = BASE_SCREENER + url

    print(f"  Found: Annual Report {report_year}  →  {url[:80]}...")
    return url, report_year

# ── PDF download ──────────────────────────────────────────────────────────────

def download_pdf(url: str, cache_path: Path) -> Path:
    if cache_path.exists():
        size_kb = cache_path.stat().st_size // 1024
        print(f"  Using cached PDF: {cache_path.name} ({size_kb} KB)")
        return cache_path

    print(f"  Downloading PDF ...")
    resp = SESSION.get(url, timeout=60)
    if resp.status_code != 200:
        raise RuntimeError(f"PDF download failed: HTTP {resp.status_code}")

    content_type = resp.headers.get("content-type", "")
    if "pdf" not in content_type.lower() and not url.lower().endswith(".pdf"):
        # Might be a redirect page — look for a direct PDF link
        soup = BeautifulSoup(resp.text, "html.parser")
        pdf_link = soup.find("a", href=re.compile(r"\.pdf", re.I))
        if pdf_link:
            pdf_url = pdf_link["href"]
            if not pdf_url.startswith("http"):
                pdf_url = BASE_SCREENER + pdf_url
            print(f"  Redirected to: {pdf_url[:80]}")
            resp = SESSION.get(pdf_url, timeout=60)
            if resp.status_code != 200:
                raise RuntimeError(f"PDF redirect download failed: HTTP {resp.status_code}")
        else:
            raise RuntimeError(
                "Response is not a PDF and no PDF link found. "
                "The annual report may require manual download from Bursa Malaysia."
            )

    cache_path.write_bytes(resp.content)
    size_kb = len(resp.content) // 1024
    print(f"  Downloaded: {size_kb} KB → {cache_path.name}")
    return cache_path

# ── PDF text extraction ───────────────────────────────────────────────────────

def extract_pdf_text(pdf_path: Path) -> str:
    print(f"  Extracting text from PDF ...")
    pages_text = []
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        print(f"  PDF has {total} pages")
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                pages_text.append(text)
            if sum(len(t) for t in pages_text) > MAX_PDF_CHARS:
                print(f"  Text limit reached at page {i+1}/{total} — truncating")
                break

    full_text = "\n\n".join(pages_text)
    print(f"  Extracted {len(full_text):,} characters from {len(pages_text)} pages")
    return full_text

# ── Claude analysis ───────────────────────────────────────────────────────────

ANALYSIS_PROMPT = """You are a professional Malaysian stock analyst specialising in KLSE (Bursa Malaysia).

You have been given the full text of an annual report for {name} ({code}.KL) for the financial year {year}.

Analyse this annual report and produce a structured trading-focused fundamental analysis in Markdown format.

Cover the following sections in order:

## 1. Business Overview
- Core business activities and revenue streams
- Market position and competitive advantages (moat)
- Key risks (operational, regulatory, currency, sector-specific)

## 2. Financial Performance
- Revenue trend (3-year if data available): growing / flat / declining
- Net profit margin and trend
- Return on Equity (ROE) and whether it is improving
- Debt level: net debt/equity ratio, interest coverage
- Free cash flow: positive or negative?
- Dividend history: consistent, growing, or cut?

## 3. Management & Governance
- Any red flags: related-party transactions, frequent auditor changes, qualified audit opinion?
- Management track record: did they deliver on stated targets?
- Capital allocation: buybacks, dividends, acquisitions?

## 4. KLSE Trading Signals
Based on fundamentals from this annual report, rate each criterion:
- Stage 2 candidate? (Is the business growing and profitable enough to support a price uptrend?)
- VCP suitability: Is the business stable enough for swing trading setups?
- RS (Relative Strength) expectation: Is this company likely to outperform KLCI? Why?
- Minervini quality score (1–10): Based on ROE, EPS growth, competitive position

## 5. Key Numbers to Watch
A table of the most important metrics extracted from this report:
| Metric | Value | Assessment |
|--------|-------|------------|
(Include: Revenue, Net Profit, EPS, ROE, Net Debt/Equity, DPS, Dividend Yield, Free Cash Flow)

## 6. Conclusion & Trading Verdict
- **Buy candidate?** Yes / Watchlist / Avoid — and why
- **Ideal entry context**: What macro/technical setup would make this a high-conviction buy?
- **Key catalyst to watch**: What upcoming event could re-rate this stock?
- **Main risk**: What could make the thesis wrong?

Be specific and direct. Use actual numbers from the report. Avoid vague statements. Write for a trader, not an academic.

---

ANNUAL REPORT TEXT:
{text}
"""


def analyse_with_claude(name: str, code: str, year: int, text: str) -> str:
    print(f"  Sending to Claude AI for analysis ({len(text):,} chars) ...")
    client  = anthropic.Anthropic(api_key=_load_api_key())
    prompt  = ANALYSIS_PROMPT.format(name=name, code=code, year=year, text=text[:MAX_PDF_CHARS])

    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    analysis = message.content[0].text
    print(f"  Claude analysis complete: {len(analysis):,} chars")
    return analysis

# ── Save to Knowledge Base ────────────────────────────────────────────────────

def save_to_knowledge_base(name: str, code: str, year: int, analysis: str) -> Path:
    filename  = f"AR_{code}_{name}_{year}.md"
    out_path  = KNOWLEDGE_DIR / filename
    header    = (
        f"# Annual Report Analysis: {name} ({code}.KL) — FY{year}\n\n"
        f"*Generated: {datetime.datetime.now().strftime('%d %b %Y %H:%M')} "
        f"by Claude AI ({CLAUDE_MODEL})*  \n"
        f"*Source: Bursa Malaysia Annual Report FY{year}*\n\n"
        f"---\n\n"
    )
    out_path.write_text(header + analysis, encoding="utf-8")
    print(f"\n  Saved: {out_path}")
    return out_path

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Download and analyse a KLSE stock's annual report with Claude AI."
    )
    parser.add_argument("stock", help="Stock code (e.g. 1023) or name (e.g. CIMB)")
    parser.add_argument("--year", type=int, default=None, help="Force a specific report year")
    parser.add_argument("--no-cache", action="store_true", help="Re-download even if PDF is cached")
    args = parser.parse_args()

    name, code = resolve_stock(args.stock)
    print(f"\nKLSE Annual Report Analyzer")
    print(f"Stock : {name} ({code}.KL)")
    print(f"=" * 50)

    # 1. Find annual report URL on klsescreener
    try:
        pdf_url, report_year = find_annual_report_url(code, args.year)
    except RuntimeError as e:
        print(f"\nERROR: {e}")
        print("\nAlternative: Download the annual report manually from:")
        print(f"  https://www.bursamalaysia.com/market_information/announcements/company_announcement")
        print(f"  Search for: {name} annual report")
        sys.exit(1)

    # 2. Download PDF (with cache)
    cache_path = CACHE_DIR / f"{code}_{report_year}.pdf"
    if args.no_cache and cache_path.exists():
        cache_path.unlink()
    try:
        pdf_path = download_pdf(pdf_url, cache_path)
    except RuntimeError as e:
        print(f"\nERROR: {e}")
        sys.exit(1)

    # 3. Extract text
    try:
        text = extract_pdf_text(pdf_path)
    except Exception as e:
        print(f"\nERROR extracting PDF text: {e}")
        sys.exit(1)

    if len(text) < 500:
        print("\nWARNING: Very little text extracted from PDF (may be scanned/image-based).")
        print("OCR is not supported. Try a different annual report year.")
        sys.exit(1)

    # 4. Claude analysis
    try:
        analysis = analyse_with_claude(name, code, report_year, text)
    except anthropic.AuthenticationError:
        print("\nERROR: Invalid or missing ANTHROPIC_API_KEY.")
        print("Set it with:  $env:ANTHROPIC_API_KEY = 'sk-ant-...'")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR calling Claude API: {e}")
        sys.exit(1)

    # 5. Save
    out_path = save_to_knowledge_base(name, code, report_year, analysis)

    print(f"\n{'='*50}")
    print(f"DONE: Annual report analysis saved to:")
    print(f"  {out_path}")
    print(f"\nOpen it in VS Code or Notepad to read the full analysis.")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
