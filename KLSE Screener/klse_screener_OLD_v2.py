"""
KLSE Daily Screener  (v2 — VCP-staged, fundamental-merged, 100-point model)
===========================================================================
Scores every stock in universe.txt and outputs a ranked HTML watchlist + CSV.

WHAT CHANGED IN v2
------------------
1. VCP STAGING (fixes the "latecomer" problem)
   The old screener flagged a buy only when the volume SQUEEZE and the volume
   SURGE were both green — but a surge only happens AFTER the breakout, so by
   then the price was already extended and you were chasing.
   v2 separates the trade into stages:
       COILING   — tight VCP, volume dried up, NOT yet broken out  -> WATCH, set alert
       BREAKOUT  — cleared the pivot today, still <=3% past it     -> BUY ZONE
       EXTENDED  — >3% past the pivot                              -> TOO LATE, skip
       BASING    — above EMA50 but no tight coil yet               -> developing
       WEAK      — below EMA50 or fails liquidity                  -> ignore
   You buy STAGE 2 (or take a 1/3 starter in late STAGE 1) — never STAGE 3.

2. FUNDAMENTAL MERGE
   Reads the latest fundamentals_*.json from ..\\Fundamentals\\output so every
   stock shows its Grade A/B/C/D + ROE + DY alongside the technical stage.

3. 100-POINT COMPOSITE MODEL (Knowledge Base file 27)
   Momentum 40  +  Quality 30  +  Value 20  +  Liquidity 10  = 100
   Grade: >=75 Elite | >=60 A | >=50 B | >=40 C | <40 D

4. MARKET BREADTH GATE (Knowledge Base file 26)
   Macro layer now also reports % of the universe trading above its EMA50.

Requirements:  pip install yfinance pandas numpy curl_cffi
Usage:         double-click run_screener.bat   OR   python klse_screener.py
"""

import os
import sys
import glob
import json
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

# Fundamentals JSON produced by ..\Fundamentals\fetch_fundamentals.py
FUND_OUTPUT_DIR = SCRIPT_DIR.parent / "Fundamentals" / "output"

TODAY         = datetime.date.today().strftime("%Y-%m-%d")
OUTPUT_HTML   = OUTPUT_DIR / f"watchlist_{TODAY}.html"
OUTPUT_CSV    = OUTPUT_DIR / f"watchlist_{TODAY}.csv"

HISTORY_DAYS  = 420          # calendar days (~300 trading days, need 252 for RS rating)
MAX_WORKERS   = 8            # parallel download threads

# ── Layer 2 — Liquidity thresholds ───────────────────────────────────────────
MIN_PRICE     = 0.50         # RM
MIN_AVG_VOL   = 200_000      # shares (20-day avg)
MIN_MKT_CAP   = 100_000_000  # RM 100M

# ── Layer 3 — Fundamental thresholds (yfinance fallback) ─────────────────────
MAX_PE        = 35.0
MIN_PE        = 0.0          # must be profitable

# ── Layer 4 — Technical ──────────────────────────────────────────────────────
RSI_LOW       = 35
RSI_HIGH      = 75
EMA_SHORT     = 20
EMA_MID       = 50
EMA_LONG      = 200
VOL_SURGE_X   = 1.5          # volume >= 1.5x 20-day avg = breakout-confirming surge
VCP_BB_PCT    = 20           # BB width in bottom 20th pct = coiling

# ── VCP STAGING ──────────────────────────────────────────────────────────────
PIVOT_LOOKBACK   = 15        # trading days — the base whose HIGH is the pivot
BUY_ZONE_PCT     = 3.0       # <=3% above pivot = still a valid (non-extended) entry
EXTENDED_PCT     = 3.0       # >this above pivot = EXTENDED, too late to chase
VOL_DRYUP_PCT    = 35        # recent 5-day vol <= 35th pct of 60-day vol = dried up
TIGHT_COIL_PCT   = 10        # BB width in bottom 10th pct = tightest coil (starter zone)
STARTER_RANGE    = 4.0       # price within 4% of coil low = starter-tranche zone
IMMINENT_PCT     = 3.0       # COILING price within 3% BELOW pivot = breakout imminent

# ── Macro tickers ────────────────────────────────────────────────────────────
KLCI_TICKER   = "^KLSE"
DOW_TICKER    = "^DJI"

# ═══════════════════════════════════════════════════════════════════════════════
# TECHNICAL HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def ema(series: pd.Series, n: int) -> pd.Series:
    return series.ewm(span=n, adjust=False).mean()


def rsi(series: pd.Series, n: int = 14) -> float:
    delta = series.diff().dropna()
    gain  = delta.clip(lower=0).rolling(n).mean()
    loss  = (-delta.clip(upper=0)).rolling(n).mean()
    rs    = gain / loss.replace(0, float("nan"))
    r     = 100 - (100 / (1 + rs))
    return float(r.iloc[-1]) if not r.empty else float("nan")


def bb_width(series: pd.Series, n: int = 20) -> pd.Series:
    mid = series.rolling(n).mean()
    std = series.rolling(n).std()
    return (2 * std) / mid.replace(0, float("nan"))


def atr(df: pd.DataFrame, n: int = 14) -> float:
    hi, lo, cl = df["High"], df["Low"], df["Close"]
    tr = pd.concat([hi - lo, (hi - cl.shift()).abs(), (lo - cl.shift()).abs()], axis=1).max(axis=1)
    return float(tr.rolling(n).mean().iloc[-1])


def percentile(series: pd.Series, pct: float) -> float:
    return float(series.quantile(pct / 100))

# ═══════════════════════════════════════════════════════════════════════════════
# FUNDAMENTAL DATA  (merged from fetch_fundamentals.py output)
# ═══════════════════════════════════════════════════════════════════════════════

def load_fundamentals() -> tuple[dict, str | None]:
    """Load the most recent fundamentals_*.json. Returns ({ticker: row}, filename)."""
    if not FUND_OUTPUT_DIR.exists():
        return {}, None
    files = sorted(glob.glob(str(FUND_OUTPUT_DIR / "fundamentals_*.json")))
    if not files:
        return {}, None
    latest = files[-1]
    try:
        data = json.loads(Path(latest).read_text(encoding="utf-8"))
    except Exception:
        return {}, None
    by_ticker = {}
    for row in data:
        tk = (row.get("ticker") or "").upper()
        if tk:
            by_ticker[tk] = row
    return by_ticker, os.path.basename(latest)

# ═══════════════════════════════════════════════════════════════════════════════
# MACRO GATE (Layer 1)
# ═══════════════════════════════════════════════════════════════════════════════

# Global KLCI close series for RS Rating — populated in check_macro()
_KLCI_CLOSE: pd.Series = pd.Series(dtype=float)


def check_macro() -> dict:
    global _KLCI_CLOSE
    result = {"klci_bull": False, "dow_bull": False, "klci_val": None, "dow_val": None,
              "klci_ema50": None, "dow_ema20": None,
              "breadth_pct": None, "breadth_label": "—"}
    try:
        klci = yf.Ticker(KLCI_TICKER, session=_SESSION)
        kdf  = klci.history(period="14mo")   # 14 months for 12-month RS calculation
        if not kdf.empty:
            kclose = kdf["Close"]
            _KLCI_CLOSE = kclose
            result["klci_val"]   = round(float(kclose.iloc[-1]), 2)
            result["klci_ema50"] = round(float(ema(kclose, 50).iloc[-1]), 2)
            result["klci_bull"]  = kclose.iloc[-1] > ema(kclose, 50).iloc[-1]
    except Exception as e:
        print(f"  [MACRO] KLCI fetch error: {e}")

    try:
        dow  = yf.Ticker(DOW_TICKER, session=_SESSION)
        ddf  = dow.history(period="3mo")
        if not ddf.empty:
            dclose = ddf["Close"]
            result["dow_val"]   = round(float(dclose.iloc[-1]), 2)
            result["dow_ema20"] = round(float(ema(dclose, 20).iloc[-1]), 2)
            result["dow_bull"]  = dclose.iloc[-1] > ema(dclose, 20).iloc[-1]
    except Exception as e:
        print(f"  [MACRO] Dow fetch error: {e}")

    return result


def rs_rating(stock_close: pd.Series) -> float | None:
    """Relative Strength vs KLCI over 12 months. Positive = outperforming KLCI."""
    if _KLCI_CLOSE.empty or len(stock_close) < 60:
        return None
    try:
        lookback = min(252, len(stock_close) - 1, len(_KLCI_CLOSE) - 1)
        stock_ret = float(stock_close.iloc[-1] / stock_close.iloc[-lookback] - 1) * 100
        klci_ret  = float(_KLCI_CLOSE.iloc[-1] / _KLCI_CLOSE.iloc[-lookback] - 1) * 100
        return round(stock_ret - klci_ret, 1)
    except Exception:
        return None

# ═══════════════════════════════════════════════════════════════════════════════
# 100-POINT COMPOSITE MODEL  (Knowledge Base file 27)
#   Momentum 40  +  Quality 30  +  Value 20  +  Liquidity 10
# ═══════════════════════════════════════════════════════════════════════════════

def score_momentum(rs: float | None, tt: int, above_ema50: bool,
                    from_hi_pct: float | None) -> int:
    """Max 40 points."""
    pts = 0
    # RS Rating vs KLCI — 15 pts
    if rs is not None:
        if   rs >= 20: pts += 15
        elif rs >= 10: pts += 12
        elif rs >= 0:  pts += 8
        elif rs >= -10: pts += 4
    # Trend Template score — 16 pts (tt is 0-8)
    pts += round(tt / 8 * 16)
    # Above EMA50 — 5 pts
    if above_ema50: pts += 5
    # Proximity to 52-week high — 4 pts
    if from_hi_pct is not None:
        if   from_hi_pct >= -10: pts += 4
        elif from_hi_pct >= -20: pts += 3
        elif from_hi_pct >= -30: pts += 2
    return min(pts, 40)


def score_quality(fund: dict | None, eps: float | None) -> int:
    """Max 30 points. Uses merged fundamentals; degrades gracefully if absent."""
    pts = 0
    roe   = (fund or {}).get("roe")
    grade = (fund or {}).get("grade")
    # ROE — 12 pts
    if roe is not None:
        if   roe >= 20: pts += 12
        elif roe >= 15: pts += 10
        elif roe >= 10: pts += 7
        elif roe >= 5:  pts += 3
    # Fundamental Grade from fetch_fundamentals.py — 12 pts
    gmap = {"A": 12, "B": 9, "C": 5, "D": 2}
    if grade in gmap:
        pts += gmap[grade]
    # Positive EPS — 6 pts
    eps_val = eps if eps is not None else (fund or {}).get("eps")
    if eps_val is not None and eps_val > 0:
        pts += 6
    return min(pts, 30)


def score_value(fund: dict | None, pe: float | None) -> int:
    """Max 20 points."""
    pts = 0
    dy = (fund or {}).get("dy")
    pb = (fund or {}).get("pb")
    pe_val = pe if pe is not None else (fund or {}).get("pe")
    # Dividend yield — 10 pts
    if dy is not None:
        if   dy >= 6: pts += 10
        elif dy >= 4: pts += 7
        elif dy >= 2: pts += 4
        elif dy >  0: pts += 2
    # P/E — 6 pts
    if pe_val is not None and pe_val > 0:
        if   pe_val <= 15: pts += 6
        elif pe_val <= 25: pts += 4
        elif pe_val <= 35: pts += 2
    # P/B — 4 pts
    if pb is not None and pb > 0:
        if   pb <= 1: pts += 4
        elif pb <= 2: pts += 3
        elif pb <= 3: pts += 2
    return min(pts, 20)


def score_liquidity(price: float | None, avg_vol: float | None,
                     mkt_cap: float | None) -> int:
    """Max 10 points."""
    pts = 0
    turnover = (price or 0) * (avg_vol or 0)   # RM daily turnover
    if   turnover >= 5_000_000: pts += 6
    elif turnover >= 2_000_000: pts += 4
    elif turnover >= 500_000:   pts += 2
    if   (mkt_cap or 0) >= 1_000_000_000: pts += 4
    elif (mkt_cap or 0) >= 300_000_000:   pts += 3
    elif (mkt_cap or 0) >= 100_000_000:   pts += 2
    return min(pts, 10)


def composite_grade(score: int) -> str:
    if   score >= 75: return "ELITE"
    elif score >= 60: return "A"
    elif score >= 50: return "B"
    elif score >= 40: return "C"
    return "D"

# ═══════════════════════════════════════════════════════════════════════════════
# SINGLE STOCK ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

def analyse_stock(ticker: str, name: str, fundamentals: dict) -> dict:
    base = {
        "ticker": ticker, "name": name,
        "price": None, "rt_price": False, "avg_vol": None, "mkt_cap": None,
        "pe": None, "eps": None,
        "ema20": None, "ema50": None, "ema200": None,
        "rsi14": None, "bb_pct": None,
        "vol_ratio": None, "atr_pct": None,
        "week52_hi": None, "week52_lo": None, "from_hi_pct": None,
        "rs_rating": None, "tt_score": 0,
        # VCP staging
        "pivot": None, "dist_pivot_pct": None, "stage": "WEAK",
        "coil": False, "vol_dryup": False, "vol_surge": False,
        "broke_out_today": False, "starter_zone": False,
        "imminent": False, "coil_wait": None,
        "buy_lo": None, "buy_hi": None,
        # fundamentals (merged)
        "fund_grade": None, "roe": None, "dy": None, "pb": None,
        # 100-point model
        "mom": 0, "qual": 0, "val": 0, "liq": 0,
        "score": 0, "grade": "D",
        # gate results
        "pass_liq": False,
        "above_ema20": False, "above_ema50": False, "above_ema200": False,
        "rsi_ok": False,
        "error": None,
    }
    try:
        stock = yf.Ticker(ticker, session=_SESSION)
        end   = datetime.date.today()
        start = end - datetime.timedelta(days=HISTORY_DAYS)
        df    = stock.history(start=start.isoformat(), end=end.isoformat())

        if df.empty or len(df) < 50:
            base["error"] = "Insufficient history"
            return base

        # ── Real-time intraday price ─────────────────────────────────────────
        rt_price = None
        try:
            intra = stock.history(period="1d", interval="1m", auto_adjust=True)
            if not intra.empty:
                last_ts = intra.index[-1]
                if hasattr(last_ts, "date") and last_ts.date() == end:
                    rt_price     = float(intra["Close"].iloc[-1])
                    intra_volume = float(intra["Volume"].sum())
                    df.iloc[-1, df.columns.get_loc("Close")]  = rt_price
                    df.iloc[-1, df.columns.get_loc("Volume")] = intra_volume
        except Exception:
            pass

        close  = df["Close"]
        high   = df["High"]
        low    = df["Low"]
        volume = df["Volume"]
        price  = float(close.iloc[-1])
        avg_v  = float(volume.rolling(20).mean().iloc[-1])

        base["price"]    = round(price, 4)
        base["rt_price"] = rt_price is not None
        base["avg_vol"]  = int(avg_v)

        # 52-week range
        w52_hi = float(close.rolling(252).max().iloc[-1])
        w52_lo = float(close.rolling(252).min().iloc[-1])
        base["week52_hi"]   = round(w52_hi, 4)
        base["week52_lo"]   = round(w52_lo, 4)
        base["from_hi_pct"] = round((price / w52_hi - 1) * 100, 1) if w52_hi else None

        # ── Layer 2 — Liquidity ──────────────────────────────────────────────
        info = {}
        try:
            info = stock.info or {}
        except Exception:
            pass
        mkt_cap = info.get("marketCap") or 0
        base["mkt_cap"] = mkt_cap
        liq_ok = (price >= MIN_PRICE and avg_v >= MIN_AVG_VOL and mkt_cap >= MIN_MKT_CAP)
        base["pass_liq"] = liq_ok

        # ── Layer 3 — Fundamental (yfinance fallback) ────────────────────────
        pe  = info.get("trailingPE") or info.get("forwardPE")
        eps = info.get("trailingEps")
        base["pe"]  = round(float(pe), 2)  if pe  else None
        base["eps"] = round(float(eps), 4) if eps else None

        # Merge fundamentals from fetch_fundamentals.py
        fund = fundamentals.get(ticker.upper())
        if fund:
            base["fund_grade"] = fund.get("grade")
            base["roe"]        = fund.get("roe")
            base["dy"]         = fund.get("dy")
            base["pb"]         = fund.get("pb")
            if base["pe"] is None and fund.get("pe"):
                base["pe"] = fund.get("pe")

        # ── Layer 4 — Technical ──────────────────────────────────────────────
        e20  = ema(close, EMA_SHORT)
        e50  = ema(close, EMA_MID)
        e150 = ema(close, 150)
        e200 = ema(close, EMA_LONG)
        base["ema20"]  = round(float(e20.iloc[-1]), 4)
        base["ema50"]  = round(float(e50.iloc[-1]), 4)
        base["ema200"] = round(float(e200.iloc[-1]), 4)

        above_ema20  = price > float(e20.iloc[-1])
        above_ema50  = price > float(e50.iloc[-1])
        above_ema200 = price > float(e200.iloc[-1])
        base["above_ema20"]  = above_ema20
        base["above_ema50"]  = above_ema50
        base["above_ema200"] = above_ema200

        rsi14 = rsi(close, 14)
        base["rsi14"]  = round(rsi14, 1) if not pd.isna(rsi14) else None
        rsi_ok = not pd.isna(rsi14) and RSI_LOW <= rsi14 <= RSI_HIGH
        base["rsi_ok"] = rsi_ok

        # Volume ratio (surge = breakout confirmation)
        vol_ratio = float(volume.iloc[-1]) / avg_v if avg_v > 0 else 0
        base["vol_ratio"] = round(vol_ratio, 2)
        base["vol_surge"] = vol_ratio >= VOL_SURGE_X

        # Bollinger Band width percentile — the COIL / squeeze indicator
        bbw = bb_width(close, 20)
        coil = tight_coil = False
        bbw_pct = None
        if bbw.notna().sum() >= 60:
            bbw_clean  = bbw.dropna()
            thr_coil   = percentile(bbw_clean, VCP_BB_PCT)
            thr_tight  = percentile(bbw_clean, TIGHT_COIL_PCT)
            cur_bbw    = float(bbw.iloc[-1])
            coil       = cur_bbw <= thr_coil
            tight_coil = cur_bbw <= thr_tight
            bbw_pct    = round(cur_bbw * 100, 2)
        base["bb_pct"] = bbw_pct
        base["coil"]   = coil

        # Volume dry-up — recent 5-day avg volume vs 60-day distribution.
        # A genuine VCP coil has volume DRYING UP (sellers exhausted), which is
        # the opposite of a surge. This is the STAGE 1 confirmation.
        vol_dryup = False
        if len(volume) >= 60:
            vol5  = float(volume.iloc[-5:].mean())
            vthr  = percentile(volume.iloc[-60:], VOL_DRYUP_PCT)
            vol_dryup = vol5 <= vthr
        base["vol_dryup"] = vol_dryup

        # ATR %
        try:
            atr_val = atr(df, 14)
            base["atr_pct"] = round(atr_val / price * 100, 2) if price else None
        except Exception:
            pass

        # RS Rating vs KLCI
        rs = rs_rating(close)
        base["rs_rating"] = rs

        # Minervini Trend Template (8 criteria)
        tt = 0
        if price > float(e150.iloc[-1]):                                       tt += 1
        if price > float(e200.iloc[-1]):                                       tt += 1
        if float(e150.iloc[-1]) > float(e200.iloc[-1]):                        tt += 1
        if len(e200) >= 20 and float(e200.iloc[-1]) > float(e200.iloc[-20]):   tt += 1
        if float(e50.iloc[-1]) > float(e150.iloc[-1]):                         tt += 1
        if price > float(e50.iloc[-1]):                                        tt += 1
        if w52_lo > 0 and (price / w52_lo - 1) >= 0.30:                        tt += 1
        if w52_hi > 0 and (price / w52_hi - 1) >= -0.25:                       tt += 1
        base["tt_score"] = tt

        # ── VCP STAGING ──────────────────────────────────────────────────────
        # Pivot = highest HIGH of the prior PIVOT_LOOKBACK days (excluding today).
        # The coil tops out at the pivot; clearing it on volume is the breakout.
        if len(high) > PIVOT_LOOKBACK + 1:
            pivot = float(high.iloc[-(PIVOT_LOOKBACK + 1):-1].max())
        else:
            pivot = float(high.iloc[:-1].max()) if len(high) > 1 else price
        base["pivot"] = round(pivot, 4)
        dist = (price / pivot - 1) * 100 if pivot > 0 else 0
        base["dist_pivot_pct"] = round(dist, 2)
        base["buy_lo"] = round(pivot, 4)
        base["buy_hi"] = round(pivot * (1 + BUY_ZONE_PCT / 100), 4)

        prev_close = float(close.iloc[-2]) if len(close) > 1 else price
        base["broke_out_today"] = prev_close <= pivot < price

        # coil low — bottom of the recent base, used for starter-tranche stop
        coil_low = float(low.iloc[-(PIVOT_LOOKBACK + 1):-1].min()) if len(low) > PIVOT_LOOKBACK + 1 else float(low.min())

        # Stage classification
        if not liq_ok or not above_ema50:
            stage = "WEAK"
        elif price > pivot:
            stage = "BREAKOUT" if dist <= EXTENDED_PCT else "EXTENDED"
        else:  # price at/below pivot — inside a base
            if coil and vol_dryup:
                stage = "COILING"
            else:
                stage = "BASING"
        base["stage"] = stage

        # Starter-tranche zone: tightest coil + price near the base low.
        # This is the only legitimate "before the breakout" entry — 1/3 size,
        # stop just below the coil low.
        if stage == "COILING" and tight_coil and coil_low > 0:
            near_low = (price / coil_low - 1) * 100 <= STARTER_RANGE
            base["starter_zone"] = bool(near_low)

        # Breakout imminence: a COILING stock pinned just below its pivot on
        # dried-up volume is about to resolve — minimal "locked funds" wait.
        # A coil sitting deep below the pivot may take many more days/weeks.
        if stage == "COILING":
            if -IMMINENT_PCT <= dist <= 0 and vol_dryup:
                base["imminent"]   = True
                base["coil_wait"]  = "IMMINENT"      # near pivot — breaks soon
            elif dist <= -IMMINENT_PCT:
                base["coil_wait"]  = "DEEP"          # far from pivot — long wait
            else:
                base["coil_wait"]  = "MID"

        # ── 100-POINT COMPOSITE SCORE ────────────────────────────────────────
        mom  = score_momentum(rs, tt, above_ema50, base["from_hi_pct"])
        qual = score_quality(fund, base["eps"])
        val  = score_value(fund, base["pe"])
        liq  = score_liquidity(price, avg_v, mkt_cap)
        total = mom + qual + val + liq
        base["mom"], base["qual"], base["val"], base["liq"] = mom, qual, val, liq
        base["score"] = total
        base["grade"] = composite_grade(total)

    except Exception as e:
        base["error"] = str(e)[:80]

    return base

# ═══════════════════════════════════════════════════════════════════════════════
# HTML REPORT
# ═══════════════════════════════════════════════════════════════════════════════

STAGE_STYLE = {
    "COILING":  ("COILING — WATCH",   "#6610f2", "#e7d9ff"),
    "BREAKOUT": ("BREAKOUT — BUY",    "#198754", "#d4edda"),
    "EXTENDED": ("EXTENDED — TOO LATE","#dc3545", "#f8d7da"),
    "BASING":   ("BASING",            "#fd7e14", "#fff3cd"),
    "WEAK":     ("WEAK",              "#6c757d", "#f8f9fa"),
}
GRADE_COLOR = {"ELITE": "#6610f2", "A": "#198754", "B": "#0d6efd",
               "C": "#fd7e14", "D": "#dc3545"}
FUND_COLOR  = {"A": "#198754", "B": "#0d6efd", "C": "#fd7e14", "D": "#dc3545"}


def _tv_url(ticker: str, name: str) -> str:
    code = ticker.replace(".KL", "").replace(".kl", "").strip()
    return f"https://www.tradingview.com/chart/?symbol=MYX%3A{code}"


def _tick(val: bool) -> str:
    return ('<span style="color:#198754;font-weight:700;">✓</span>' if val
            else '<span style="color:#dc3545;">✗</span>')


def _fmt_vol(v) -> str:
    if v is None: return "—"
    if v >= 1_000_000: return f"{v/1_000_000:.1f}M"
    if v >= 1_000:     return f"{v/1_000:.0f}K"
    return str(v)


def _fmt_cap(v) -> str:
    if v is None or v == 0: return "N/A"
    if v >= 1_000_000_000: return f"RM {v/1_000_000_000:.2f}B"
    if v >= 1_000_000:     return f"RM {v/1_000_000:.0f}M"
    return f"RM {v:,.0f}"


def build_html(macro: dict, stocks: list[dict], generated_at: str,
               fund_file: str | None) -> str:
    # ── Macro banner (now includes breadth) ──────────────────────────────────
    klci_color = "#198754" if macro["klci_bull"] else "#dc3545"
    dow_color  = "#198754" if macro["dow_bull"]  else "#dc3545"
    macro_ok   = macro["klci_bull"] and macro["dow_bull"]
    macro_bg   = "#d4edda" if macro_ok else "#f8d7da"

    bp = macro.get("breadth_pct")
    breadth_color = ("#198754" if (bp is not None and bp >= 60)
                     else "#fd7e14" if (bp is not None and bp >= 40)
                     else "#dc3545")
    breadth_str = f"{bp:.0f}%" if bp is not None else "—"

    macro_html = f"""
    <div style="background:{macro_bg};border:1px solid #dee2e6;border-radius:8px;padding:14px 20px;margin:16px 0;display:flex;gap:36px;flex-wrap:wrap;">
      <div>
        <div style="font-size:11px;color:#555;text-transform:uppercase;font-weight:600;">KLCI Index</div>
        <div style="font-size:20px;font-weight:700;color:{klci_color};">{macro['klci_val'] or '—'}</div>
        <div style="font-size:11px;color:#555;">EMA50: {macro['klci_ema50'] or '—'} &nbsp;
          {'▲ BULL' if macro['klci_bull'] else '▼ BEAR'}</div>
      </div>
      <div>
        <div style="font-size:11px;color:#555;text-transform:uppercase;font-weight:600;">Dow Jones</div>
        <div style="font-size:20px;font-weight:700;color:{dow_color};">{macro['dow_val'] or '—'}</div>
        <div style="font-size:11px;color:#555;">EMA20: {macro['dow_ema20'] or '—'} &nbsp;
          {'▲ BULL' if macro['dow_bull'] else '▼ BEAR'}</div>
      </div>
      <div>
        <div style="font-size:11px;color:#555;text-transform:uppercase;font-weight:600;">Market Breadth</div>
        <div style="font-size:20px;font-weight:700;color:{breadth_color};">{breadth_str}</div>
        <div style="font-size:11px;color:#555;">of universe above EMA50 &nbsp; {macro.get('breadth_label','—')}</div>
      </div>
      <div style="align-self:center;font-size:13px;font-weight:700;color:{'#198754' if macro_ok else '#dc3545'};">
        Macro: {'✓ FAVOURABLE' if macro_ok else '⚠ CAUTION — raise your bar'}
      </div>
    </div>"""

    # ── Info bar ─────────────────────────────────────────────────────────────
    tv_screener_url = "https://www.tradingview.com/screener/?exchange=MYX"
    rt_count = sum(1 for s in stocks if s.get("rt_price"))
    rt_note  = (f"{rt_count}/{len(stocks)} live intraday prices"
                if rt_count else "market closed — last session close")
    fund_note = f"Fundamentals merged from {fund_file}" if fund_file else \
                "Fundamentals NOT merged — run fetch_fundamentals.py first"
    tv_bar_html = f"""
    <div style="background:#fff;border:1px solid #dee2e6;border-radius:8px;padding:10px 16px;margin:12px 0;
                display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
      <span style="font-size:12px;color:#555;font-weight:600;">TradingView:</span>
      <a href="{tv_screener_url}" target="_blank"
         style="background:#1565C0;color:#fff;padding:5px 14px;border-radius:4px;
                text-decoration:none;font-size:12px;font-weight:600;">Open KLSE Screener</a>
      <span style="font-size:11px;color:#888;">{fund_note}</span>
      <span style="font-size:11px;margin-left:auto;color:#555;">
        <span style="display:inline-block;width:8px;height:8px;border-radius:50%;
              background:{'#22c55e' if rt_count else '#f59e0b'};vertical-align:middle;margin-right:4px;"></span>
        {rt_note} &nbsp;·&nbsp; Generated: {generated_at}
      </span>
    </div>"""

    # ── How-to-use banner (the VCP staging explainer) ────────────────────────
    howto_html = """
    <div style="background:#fff;border:1px solid #6610f2;border-left:5px solid #6610f2;
                border-radius:8px;padding:12px 18px;margin:12px 0;font-size:12px;color:#333;">
      <strong style="color:#6610f2;">How to trade these stages — avoid the latecomer trap:</strong><br>
      <span style="color:#6610f2;font-weight:700;">COILING</span> = tight VCP, volume dried up, not yet broken out.
      <em>Action:</em> add to watchlist, set a TradingView alert AT the pivot.
      An <strong style="color:#e8590c;">IMMINENT</strong> tag = price is pinned just below the pivot —
      breakout is close, minimal waiting; <strong>DEEP COIL</strong> = far below pivot, expect a long wait.
      A <strong>STARTER</strong> tag means price sits near the coil low — you may take a 1/3 position
      with a stop just below it. &nbsp;|&nbsp;
      <span style="color:#198754;font-weight:700;">BREAKOUT</span> = cleared the pivot today on volume, still in the buy zone.
      <em>Action:</em> buy now / add tranche — but ONLY within the buy zone shown. &nbsp;|&nbsp;
      <span style="color:#dc3545;font-weight:700;">EXTENDED</span> = already >3% past the pivot.
      <em>Action:</em> do NOT chase — wait for the next base.
    </div>"""

    # ── Summary counts ───────────────────────────────────────────────────────
    def cnt(stage): return sum(1 for s in stocks if s["stage"] == stage)
    counts_html = f"""
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin:12px 0;">
      <div style="background:#e7d9ff;border-radius:6px;padding:10px 18px;text-align:center;">
        <div style="font-size:22px;font-weight:700;color:#6610f2;">{cnt('COILING')}</div>
        <div style="font-size:11px;color:#4b0082;">COILING (watch)</div></div>
      <div style="background:#d4edda;border-radius:6px;padding:10px 18px;text-align:center;">
        <div style="font-size:22px;font-weight:700;color:#198754;">{cnt('BREAKOUT')}</div>
        <div style="font-size:11px;color:#155724;">BREAKOUT (buy)</div></div>
      <div style="background:#f8d7da;border-radius:6px;padding:10px 18px;text-align:center;">
        <div style="font-size:22px;font-weight:700;color:#dc3545;">{cnt('EXTENDED')}</div>
        <div style="font-size:11px;color:#721c24;">EXTENDED (skip)</div></div>
      <div style="background:#fff3cd;border-radius:6px;padding:10px 18px;text-align:center;">
        <div style="font-size:22px;font-weight:700;color:#fd7e14;">{cnt('BASING')}</div>
        <div style="font-size:11px;color:#664d03;">BASING</div></div>
      <div style="background:#f8f9fa;border-radius:6px;padding:10px 18px;text-align:center;">
        <div style="font-size:22px;font-weight:700;color:#6c757d;">{cnt('WEAK')}</div>
        <div style="font-size:11px;color:#6c757d;">WEAK</div></div>
    </div>"""

    # ── Table rows ───────────────────────────────────────────────────────────
    def make_row(i: int, s: dict, dim: bool = False) -> str:
        stage = s["stage"]
        st_lbl, st_col, st_bg = STAGE_STYLE.get(stage, STAGE_STYLE["WEAK"])
        row_bg = "#fff" if dim else st_bg

        price_str = f"RM {s['price']:.4f}" if s["price"] else "—"
        if s.get("rt_price"):
            price_str += ('<span title="Live" style="display:inline-block;width:7px;height:7px;'
                          'border-radius:50%;background:#22c55e;margin-left:4px;vertical-align:middle;"></span>')

        # Pivot / buy-zone cell
        if s["pivot"]:
            dp = s["dist_pivot_pct"]
            dp_col = "#198754" if (dp is not None and dp <= 0) else "#dc3545" if (dp is not None and dp > EXTENDED_PCT) else "#fd7e14"
            pivot_cell = (f'<span style="font-size:11px;">Pivot RM {s["pivot"]:.3f}</span><br>'
                          f'<span style="font-size:10px;color:#666;">Buy {s["buy_lo"]:.3f}–{s["buy_hi"]:.3f}</span><br>'
                          f'<span style="font-size:10px;color:{dp_col};font-weight:700;">{dp:+.1f}% vs pivot</span>')
        else:
            pivot_cell = "—"

        # Stage flags
        flags = ""
        if s.get("imminent"):
            flags += '<span style="background:#e8590c;color:#fff;padding:1px 5px;border-radius:3px;font-size:10px;margin-right:3px;">IMMINENT</span>'
        elif s.get("coil_wait") == "DEEP":
            flags += '<span style="background:#adb5bd;color:#fff;padding:1px 5px;border-radius:3px;font-size:10px;margin-right:3px;">DEEP COIL</span>'
        if s.get("starter_zone"):
            flags += '<span style="background:#6610f2;color:#fff;padding:1px 5px;border-radius:3px;font-size:10px;margin-right:3px;">STARTER 1/3</span>'
        if s.get("broke_out_today"):
            flags += '<span style="background:#198754;color:#fff;padding:1px 5px;border-radius:3px;font-size:10px;margin-right:3px;">BROKE TODAY</span>'
        if s.get("vol_dryup"):
            flags += '<span style="background:#6c757d;color:#fff;padding:1px 5px;border-radius:3px;font-size:10px;margin-right:3px;">VOL DRY</span>'
        if s.get("vol_surge"):
            flags += '<span style="background:#0d6efd;color:#fff;padding:1px 5px;border-radius:3px;font-size:10px;margin-right:3px;">VOL↑</span>'
        if s.get("error"):
            flags += f'<span style="color:#dc3545;font-size:10px;">{s["error"]}</span>'

        # Fundamental grade
        fg = s.get("fund_grade")
        fg_cell = (f'<span style="background:{FUND_COLOR.get(fg,"#aaa")};color:#fff;'
                   f'padding:1px 6px;border-radius:3px;font-size:11px;font-weight:700;">{fg}</span>'
                   if fg else '<span style="color:#aaa;font-size:11px;">—</span>')
        roe_str = f'{s["roe"]:.0f}%' if s.get("roe") is not None else "—"
        dy_str  = f'{s["dy"]:.1f}%'  if s.get("dy")  is not None else "—"

        # 100-point score
        g       = s["grade"]
        g_col   = GRADE_COLOR.get(g, "#aaa")
        score_cell = (f'<span style="font-size:15px;font-weight:700;color:{g_col};">{s["score"]}</span>'
                      f'<span style="font-size:10px;color:#888;">/100</span><br>'
                      f'<span style="background:{g_col};color:#fff;padding:0 5px;border-radius:3px;font-size:10px;font-weight:700;">{g}</span>')
        pillars = (f'<span style="font-size:9px;color:#888;">'
                   f'M{s["mom"]} Q{s["qual"]} V{s["val"]} L{s["liq"]}</span>')

        rs = s.get("rs_rating")
        rs_str = (f'{rs:+.0f}%' if rs is not None else "—")
        tt = s.get("tt_score", 0)

        tv_url = _tv_url(s["ticker"], s["name"])
        tv_btn = (f'<a href="{tv_url}" target="_blank" style="display:inline-block;margin-top:3px;'
                  f'padding:1px 6px;background:#1565C0;color:#fff;border-radius:3px;font-size:9px;'
                  f'text-decoration:none;font-weight:600;">TV Chart</a>')

        return (
            f'<tr style="background:{row_bg};border-bottom:1px solid #dee2e6;">'
            f'<td style="padding:7px 8px;font-size:12px;color:#888;">{i}</td>'
            f'<td style="padding:7px 8px;min-width:120px;">'
            f'  <a href="{tv_url}" target="_blank" style="font-weight:700;font-size:13px;color:#1a1a2e;text-decoration:none;">{s["name"]}</a><br>'
            f'  <span style="font-size:10px;color:#888;">{s["ticker"]}</span><br>{tv_btn}</td>'
            f'<td style="padding:7px 8px;">'
            f'  <span style="background:{st_bg};color:{st_col};padding:2px 8px;border-radius:4px;font-size:11px;font-weight:700;">{st_lbl}</span></td>'
            f'<td style="padding:7px 8px;font-size:12px;">{price_str}</td>'
            f'<td style="padding:7px 8px;">{pivot_cell}</td>'
            f'<td style="padding:7px 8px;text-align:center;">{score_cell}<br>{pillars}</td>'
            f'<td style="padding:7px 8px;text-align:center;">{fg_cell}<br>'
            f'  <span style="font-size:9px;color:#888;">ROE {roe_str} · DY {dy_str}</span></td>'
            f'<td style="padding:7px 8px;text-align:center;font-size:11px;">RS {rs_str}<br>'
            f'  <span style="font-size:10px;color:#888;">TT {tt}/8</span></td>'
            f'<td style="padding:7px 8px;text-align:center;">'
            f'  {_tick(s["above_ema20"])} {_tick(s["above_ema50"])} {_tick(s["above_ema200"])}'
            f'  <br><span style="font-size:9px;color:#aaa;">20 50 200</span></td>'
            f'<td style="padding:7px 8px;">{flags}</td>'
            f'</tr>'
        )

    th = lambda t: (f'<th style="padding:8px;text-align:left;font-size:11px;color:#555;'
                    f'white-space:nowrap;background:#f1f3f5;border-bottom:2px solid #dee2e6;">{t}</th>')
    header = (f'<tr>{th("#")}{th("Stock")}{th("Stage")}{th("Price")}'
              f'{th("Pivot / Buy Zone")}{th("Score /100")}{th("Fundamental")}'
              f'{th("RS / TT")}{th("EMA")}{th("Flags")}</tr>')

    # Order: COILING -> BREAKOUT -> BASING -> EXTENDED -> WEAK.
    # Within COILING, IMMINENT coils come first (shortest wait). Then by score.
    stage_order = {"COILING": 0, "BREAKOUT": 1, "BASING": 2, "EXTENDED": 3, "WEAK": 4}
    ordered = sorted(stocks, key=lambda x: (stage_order.get(x["stage"], 5),
                                            0 if x.get("imminent") else 1,
                                            -(x["score"] or 0)))
    actionable = [s for s in ordered if s["stage"] in ("COILING", "BREAKOUT", "BASING", "EXTENDED")]
    weak       = [s for s in ordered if s["stage"] == "WEAK"]

    rows = "".join(make_row(i + 1, s) for i, s in enumerate(actionable))
    if weak:
        rows += (f'<tr><td colspan="10" style="padding:8px 10px;background:#f8f9fa;'
                 f'font-size:11px;color:#888;font-style:italic;">'
                 f'— WEAK: below EMA50 or fails liquidity ({len(weak)}) —</td></tr>'
                 + "".join(make_row(0, s, dim=True) for s in weak))

    table_html = f"""
    <div style="background:#fff;border:1px solid #dee2e6;border-radius:8px;margin:16px 0;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.08);">
      <div style="background:#1F2937;color:#fff;padding:10px 16px;font-size:14px;font-weight:600;">
        Screener Results — {generated_at}</div>
      <div style="overflow-x:auto;">
        <table style="width:100%;border-collapse:collapse;">
          <thead>{header}</thead><tbody>{rows}</tbody>
        </table>
      </div>
    </div>"""

    legend_html = """
    <div style="background:#fff;border:1px solid #dee2e6;border-radius:8px;padding:14px 20px;margin:16px 0;font-size:11px;color:#555;">
      <strong>Legend:</strong> &nbsp;
      <span style="background:#e8590c;color:#fff;padding:1px 6px;border-radius:3px;">IMMINENT</span> coil pinned &lt;3% below pivot — breaks soon &nbsp;|&nbsp;
      <span style="background:#adb5bd;color:#fff;padding:1px 6px;border-radius:3px;">DEEP COIL</span> far below pivot — long wait &nbsp;|&nbsp;
      <span style="background:#6610f2;color:#fff;padding:1px 6px;border-radius:3px;">STARTER 1/3</span> tightest coil + near base low — optional 1/3 entry &nbsp;|&nbsp;
      <span style="background:#198754;color:#fff;padding:1px 6px;border-radius:3px;">BROKE TODAY</span> crossed the pivot today &nbsp;|&nbsp;
      <span style="background:#6c757d;color:#fff;padding:1px 6px;border-radius:3px;">VOL DRY</span> volume dried up (real coil) &nbsp;|&nbsp;
      <span style="background:#0d6efd;color:#fff;padding:1px 6px;border-radius:3px;">VOL↑</span> volume surge (breakout confirm) &nbsp;|&nbsp;
      Score = Momentum 40 + Quality 30 + Value 20 + Liquidity 10 (M/Q/V/L shown) &nbsp;|&nbsp;
      Fundamental grade merged from fetch_fundamentals.py &nbsp;|&nbsp;
      RS = 12-mth return vs KLCI; TT = Minervini Trend Template /8
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>KLSE Screener — {generated_at}</title>
  <style>
    body {{ font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
           background:#f8f9fa;margin:0;padding:0;color:#212529; }}
    .header {{ background:#1a1a2e;color:#fff;padding:18px 28px; }}
    .header h1 {{ margin:0;font-size:20px; }}
    .header .meta {{ font-size:12px;color:#adb5bd;margin-top:4px; }}
    .container {{ max-width:1280px;margin:0 auto;padding:20px 16px; }}
    tr:hover {{ filter:brightness(0.96); }}
    th {{ position:sticky;top:0;z-index:2; }}
  </style>
</head>
<body>
  <div class="header">
    <h1>KLSE Daily Screener <span style="font-size:12px;color:#6610f2;">v2 · VCP-staged</span></h1>
    <div class="meta">Generated: {generated_at} &nbsp;·&nbsp;
      Macro+Breadth → Liquidity → Fundamental merge → VCP staging → 100-pt model</div>
  </div>
  <div class="container">
    {macro_html}
    {tv_bar_html}
    {howto_html}
    {counts_html}
    {table_html}
    {legend_html}
  </div>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════════════════════════
# CSV EXPORT
# ═══════════════════════════════════════════════════════════════════════════════

def export_csv(stocks: list[dict], path: Path) -> None:
    rows = []
    for s in stocks:
        rows.append({
            "Ticker": s["ticker"], "Name": s["name"], "Stage": s["stage"],
            "Score100": s["score"], "Grade": s["grade"],
            "Mom": s["mom"], "Qual": s["qual"], "Val": s["val"], "Liq": s["liq"],
            "Price": s["price"], "Pivot": s["pivot"],
            "DistPivot%": s["dist_pivot_pct"], "BuyLo": s["buy_lo"], "BuyHi": s["buy_hi"],
            "StarterZone": s["starter_zone"], "BrokeToday": s["broke_out_today"],
            "Imminent": s["imminent"], "CoilWait": s["coil_wait"],
            "Coil": s["coil"], "VolDryUp": s["vol_dryup"], "VolSurge": s["vol_surge"],
            "FundGrade": s["fund_grade"], "ROE": s["roe"], "DY": s["dy"], "PB": s["pb"],
            "RS_vs_KLCI": s["rs_rating"], "TrendTemplate": s["tt_score"],
            "RSI14": s["rsi14"], "AvgVol": s["avg_vol"], "MktCap": s["mkt_cap"],
            "AboveEMA50": s["above_ema50"], "AboveEMA200": s["above_ema200"],
        })
    pd.DataFrame(rows).to_csv(path, index=False)

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

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


def main():
    try:                                   # Windows console: avoid cp1252 crashes
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    generated_at = datetime.datetime.now().strftime("%d %b %Y  %H:%M")
    universe = load_universe(UNIVERSE_FILE)

    print(f"\nKLSE Daily Screener v2 (VCP-staged)")
    print(f"Universe    : {len(universe)} stocks")
    print(f"Generated   : {generated_at}")
    print("-" * 60)

    # Fundamentals merge
    fundamentals, fund_file = load_fundamentals()
    if fund_file:
        print(f"Fundamentals: merged {len(fundamentals)} stocks from {fund_file}")
    else:
        print("Fundamentals: none found — run fetch_fundamentals.py for full scoring")

    # Layer 1 — Macro
    print("\n[Layer 1] Checking macro conditions...")
    macro = check_macro()
    print(f"  KLCI : {macro['klci_val']} (EMA50 {macro['klci_ema50']}) — "
          f"{'BULL ^' if macro['klci_bull'] else 'BEAR v'}")
    print(f"  Dow  : {macro['dow_val']} (EMA20 {macro['dow_ema20']}) — "
          f"{'BULL ^' if macro['dow_bull'] else 'BEAR v'}")

    # Layers 2–4 — parallel stock screening
    print(f"\n[Layers 2-4] Screening {len(universe)} stocks ({MAX_WORKERS} threads)...")
    results = []
    done = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(analyse_stock, t, n, fundamentals): (t, n)
                   for t, n in universe}
        for fut in as_completed(futures):
            ticker, name = futures[fut]
            try:
                res = fut.result()
            except Exception as e:
                res = {"ticker": ticker, "name": name, "stage": "WEAK",
                       "score": 0, "grade": "D", "error": str(e)[:60]}
            results.append(res)
            done += 1
            print(f"  [{done:3d}/{len(universe)}] {ticker:12s} {name:15s} "
                  f"{res.get('stage','—'):9s} Score:{res.get('score',0)}"
                  f"{(' ['+res['error']+']') if res.get('error') else ''}")

    # ── Market breadth (Layer 1 extension) ───────────────────────────────────
    valid = [s for s in results if s.get("above_ema50") is not None and s.get("price")]
    if valid:
        above = sum(1 for s in valid if s.get("above_ema50"))
        bp = above / len(valid) * 100
        macro["breadth_pct"] = round(bp, 1)
        macro["breadth_label"] = ("STRONG (risk-on)" if bp >= 60
                                  else "NEUTRAL" if bp >= 40
                                  else "WEAK (risk-off)")
        print(f"\n[Breadth] {above}/{len(valid)} stocks above EMA50 = "
              f"{bp:.0f}% — {macro['breadth_label']}")

    # Summary
    def cnt(st): return sum(1 for s in results if s.get("stage") == st)
    print(f"\n{'='*60}")
    print(f"COILING  (watch) : {cnt('COILING')}")
    print(f"BREAKOUT (buy)   : {cnt('BREAKOUT')}")
    print(f"BASING           : {cnt('BASING')}")
    print(f"EXTENDED (skip)  : {cnt('EXTENDED')}")
    print(f"WEAK             : {cnt('WEAK')}")
    print(f"{'='*60}")

    # Output
    html = build_html(macro, results, generated_at, fund_file)
    OUTPUT_HTML.write_text(html, encoding="utf-8")
    export_csv(results, OUTPUT_CSV)
    print(f"\nHTML report : {OUTPUT_HTML}")
    print(f"CSV export  : {OUTPUT_CSV}")
    webbrowser.open(OUTPUT_HTML.as_uri())
    print("Browser opened.")


if __name__ == "__main__":
    main()
