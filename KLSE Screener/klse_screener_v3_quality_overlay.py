"""
KLSE Quality Overlay (v3 — Phase 2 Upgrade)
============================================
Adds KLSE-specific quality + sizing layers on top of v2's CSV output.

NEW LAYERS ADDED IN v3 (from Knowledge Base files 43–57 + Operational Foundations):
  1. WEINSTEIN STAGE (file 44) — stock-level 1/2/3/4 via 30-week MA slope/cross
  2. KC CHONG 8-CRITERIA (file 53) — Bursa-localised value+quality screen
  3. COLD EYE 8 CRITERIA (file 57) — 冷眼 long-term compounder check
  4. TONG KOOI ONG QUALITY TIER (file 56) — corporate insider quality 1–5
  5. TRADEVIEW MONEY EQUATION (file 54) — M-O-N-E-Y composite
  6. DUAL-STYLE BUCKET (DUAL_STYLE_PLAYBOOK.md) — A (momentum) / B (yield) / —
  7. POSITION SIZE SUGGESTION (POSITION_SIZE_CALCULATOR.md) — uses --portfolio arg
  8. ANTI-FOMO WARNING (STICKY_NOTE_Anti_FOMO.md) — chase-extension flag
  9. COMPOSITE QUALITY SCORE (50 pts) — Cold Eye 14 + KC Chong 14 + Tong Kooi 10 + MONEY 12

USAGE:
    python klse_screener_v3_quality_overlay.py                # uses default portfolio = 30000
    python klse_screener_v3_quality_overlay.py --portfolio 50000
    python klse_screener_v3_quality_overlay.py --csv watchlist_2026-05-21.csv --portfolio 30000

REQUIRES: v2 has already been run today (CSV present in ./output/).
          fetch_fundamentals.py has been run (JSON present in ../Fundamentals/output/).
"""

import os
import sys
import json
import glob
import argparse
import datetime
import webbrowser
from pathlib import Path
from typing import Optional

try:
    import pandas as pd
except ImportError:
    sys.exit("ERROR: pip install pandas")

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════════════
SCRIPT_DIR    = Path(__file__).parent
OUTPUT_DIR    = SCRIPT_DIR / "output"
FUND_DIR      = SCRIPT_DIR.parent / "Fundamentals" / "output"
TODAY         = datetime.date.today().strftime("%Y-%m-%d")

DEFAULT_PORTFOLIO = 30000   # RM — override with --portfolio
MAX_POSITION_PCT  = 0.10    # 10% hard cap
TARGET_PCT        = 0.07    # 7% normal sizing target
RISK_PER_TRADE    = 0.01    # 1% risk rule
BURSA_LOT         = 100     # round down to nearest 100

# ═══════════════════════════════════════════════════════════════════════════════
# LOAD V2 OUTPUT + FUNDAMENTALS
# ═══════════════════════════════════════════════════════════════════════════════

def load_v2_csv(csv_arg: Optional[str]) -> pd.DataFrame:
    if csv_arg:
        path = OUTPUT_DIR / csv_arg if not Path(csv_arg).is_absolute() else Path(csv_arg)
    else:
        files = sorted(glob.glob(str(OUTPUT_DIR / "watchlist_*.csv")))
        if not files:
            sys.exit(f"ERROR: No v2 CSV in {OUTPUT_DIR}. Run klse_screener.py first.")
        path = Path(files[-1])
    print(f"Loading v2 output: {path.name}")
    return pd.read_csv(path)


def load_fundamentals() -> dict:
    files = sorted(glob.glob(str(FUND_DIR / "fundamentals_*.json")))
    if not files:
        print("  WARNING: No fundamentals JSON. Quality scores will be limited.")
        return {}
    latest = files[-1]
    data = json.loads(Path(latest).read_text(encoding="utf-8"))
    print(f"Loading fundamentals: {os.path.basename(latest)} ({len(data)} stocks)")
    return {(r.get("ticker") or "").upper(): r for r in data}


# ═══════════════════════════════════════════════════════════════════════════════
# LAYER 1 — WEINSTEIN STAGE ANALYSIS (file 44)
# ═══════════════════════════════════════════════════════════════════════════════
# Stage 1 = base (flat 30W MA, price oscillating around)
# Stage 2 = uptrend (price > 30W MA rising)
# Stage 3 = topping (price flat/choppy above flat 30W MA)
# Stage 4 = downtrend (price < 30W MA falling)
#
# We approximate using the v2 row's EMA20/50/200 + above_ema50 + tt_score.
# True Weinstein needs 30-week MA — substitute with EMA150 ≈ 30W on daily data.

def weinstein_stage(row: dict) -> str:
    above50  = bool(row.get("AboveEMA50", False))
    above200 = bool(row.get("AboveEMA200", False))
    tt       = int(row.get("TrendTemplate") or 0)
    rs       = row.get("RS_vs_KLCI")
    from_hi  = row.get("DistPivot%")  # proxy

    if not above50 and not above200:
        return "4-DOWNTREND"
    if not above200 and above50:
        return "1-BASE"            # recovering through 50, not yet 200
    if above200 and not above50:
        return "3-TOPPING"          # broke 50, still above 200
    # Both above
    if tt >= 7 and (rs is None or rs >= 0):
        return "2-UPTREND"
    if tt >= 4:
        return "1-BASE"
    return "3-TOPPING"

# ═══════════════════════════════════════════════════════════════════════════════
# LAYER 2 — KC CHONG 8-CRITERIA (file 53)  — max 14 pts
# ═══════════════════════════════════════════════════════════════════════════════
# Each pass = ~1.75 pts (round to 14 max). Degrades if data missing.

def kc_chong_score(fund: dict) -> tuple[int, int, str]:
    """Returns (score 0-14, criteria passed 0-8, note)."""
    if not fund:
        return 0, 0, "no-fund-data"
    passed = 0
    notes = []
    roe   = fund.get("roe")
    eps_g = fund.get("eps_growth_5y") or fund.get("eps_cagr")  # 5y CAGR
    de    = fund.get("debt_to_equity") or fund.get("de")
    fcf_y = fund.get("fcf_years_positive") or fund.get("fcf_pos_years")
    dy    = fund.get("dy")
    pe    = fund.get("pe")
    pb    = fund.get("pb")
    grade = fund.get("grade")

    if roe is not None and roe >= 12:    passed += 1; notes.append("ROE≥12")
    if eps_g is not None and eps_g >= 7: passed += 1; notes.append("EPSg≥7")
    if de is not None and de <= 1.0:     passed += 1; notes.append("DE≤1")
    if fcf_y is not None and fcf_y >= 4: passed += 1; notes.append("FCF4/5")
    if dy is not None and dy >= 2:       passed += 1; notes.append("DY≥2")
    if pe is not None and 0 < pe <= 20:  passed += 1; notes.append("PE≤20")
    if pb is not None and pb <= 2.5:     passed += 1; notes.append("PB≤2.5")
    if grade in ("A", "B"):              passed += 1; notes.append(f"Grd{grade}")

    score = round(passed / 8 * 14)
    return score, passed, "+".join(notes) if notes else "0/8"

# ═══════════════════════════════════════════════════════════════════════════════
# LAYER 3 — COLD EYE 8 CRITERIA (file 57)  — max 14 pts
# ═══════════════════════════════════════════════════════════════════════════════
# Cold Eye (冷眼) long-term compounder: 8% min total return, stable DY, no fancy
# debt, high CAGR, simple business. We approximate from available fields.

def cold_eye_score(fund: dict, row: dict) -> tuple[int, int]:
    """Returns (score 0-14, criteria passed 0-8)."""
    if not fund and not row:
        return 0, 0
    passed = 0
    dy    = (fund or {}).get("dy")
    roe   = (fund or {}).get("roe")
    eps_g = (fund or {}).get("eps_growth_5y") or (fund or {}).get("eps_cagr")
    pe    = (fund or {}).get("pe")
    pb    = (fund or {}).get("pb")
    grade = (fund or {}).get("grade")
    de    = (fund or {}).get("debt_to_equity") or (fund or {}).get("de")
    yrs_div  = (fund or {}).get("dividend_years") or (fund or {}).get("div_years")

    # 1. 8% min total return (DY + EPS growth ≥ 8%)
    tot_ret = (dy or 0) + (eps_g or 0)
    if tot_ret >= 8: passed += 1
    # 2. ROE consistent ≥ 10%
    if roe is not None and roe >= 10: passed += 1
    # 3. Dividend track record (≥ 5 years)
    if yrs_div is not None and yrs_div >= 5: passed += 1
    elif dy is not None and dy >= 3: passed += 1   # proxy
    # 4. DY ≥ 3% (income compounding)
    if dy is not None and dy >= 3: passed += 1
    # 5. P/E reasonable (≤ 18)
    if pe is not None and 0 < pe <= 18: passed += 1
    # 6. P/B reasonable (≤ 2)
    if pb is not None and pb <= 2: passed += 1
    # 7. Low debt (D/E ≤ 0.8)
    if de is not None and de <= 0.8: passed += 1
    # 8. Quality grade A or B
    if grade in ("A", "B"): passed += 1

    score = round(passed / 8 * 14)
    return score, passed

# ═══════════════════════════════════════════════════════════════════════════════
# LAYER 4 — TONG KOOI ONG QUALITY TIER (file 56)  — max 10 pts
# ═══════════════════════════════════════════════════════════════════════════════
# Tier 1 = Best-in-class moat + management (e.g. PBBANK, NESTLE)
# Tier 2 = Strong moat, niche leader
# Tier 3 = Decent business, average moat
# Tier 4 = Cyclical / commodity
# Tier 5 = Speculative / poor governance
#
# Heuristic based on grade, ROE, mkt cap, and stage.

def tong_kooi_tier(fund: dict, row: dict) -> tuple[str, int]:
    """Returns (tier label, score 0-10)."""
    grade = (fund or {}).get("grade")
    roe   = (fund or {}).get("roe") or 0
    mc    = row.get("MktCap") or 0

    # Tier logic
    if grade == "A" and roe >= 15 and mc >= 5_000_000_000:
        return "T1-Elite", 10
    if grade in ("A", "B") and roe >= 12 and mc >= 1_000_000_000:
        return "T2-Strong", 8
    if grade in ("A", "B", "C") and roe >= 8:
        return "T3-Decent", 5
    if grade in ("C", "D"):
        return "T4-Cyclical", 3
    return "T5-Spec", 1

# ═══════════════════════════════════════════════════════════════════════════════
# LAYER 5 — TRADEVIEW MONEY EQUATION (file 54)  — max 12 pts
# ═══════════════════════════════════════════════════════════════════════════════
# M = Management   (proxy: grade)
# O = Operations   (proxy: ROE)
# N = New growth   (proxy: EPS growth)
# E = Earnings     (proxy: positive EPS)
# Y = Yield        (proxy: DY)

def money_equation(fund: dict, row: dict) -> tuple[int, str]:
    if not fund:
        return 0, "no-fund"
    pts = 0
    breakdown = []
    grade = fund.get("grade")
    if grade == "A":  pts += 3; breakdown.append("M:A=3")
    elif grade == "B": pts += 2; breakdown.append("M:B=2")
    elif grade == "C": pts += 1; breakdown.append("M:C=1")

    roe = fund.get("roe")
    if roe is not None:
        if roe >= 20:   pts += 3; breakdown.append("O:20+=3")
        elif roe >= 15: pts += 2; breakdown.append("O:15+=2")
        elif roe >= 10: pts += 1; breakdown.append("O:10+=1")

    eps_g = fund.get("eps_growth_5y") or fund.get("eps_cagr")
    if eps_g is not None:
        if eps_g >= 15:  pts += 2; breakdown.append("N:15+=2")
        elif eps_g >= 7: pts += 1; breakdown.append("N:7+=1")

    eps = fund.get("eps")
    if eps is not None and eps > 0:
        pts += 2; breakdown.append("E:+=2")

    dy = fund.get("dy")
    if dy is not None:
        if dy >= 5:   pts += 2; breakdown.append("Y:5+=2")
        elif dy >= 3: pts += 1; breakdown.append("Y:3+=1")

    return min(pts, 12), "/".join(breakdown) if breakdown else "—"

# ═══════════════════════════════════════════════════════════════════════════════
# LAYER 6 — DUAL-STYLE BUCKET ASSIGNMENT
# ═══════════════════════════════════════════════════════════════════════════════
# Bucket A — Momentum/Growth: high TT, RS, low DY, growth-stage
# Bucket B — Yield/Defensive: high DY, lower RS, stable, banks/REITs/utilities
# —       — Neither (skip or special)

def assign_bucket(row: dict, fund: dict) -> str:
    tt = int(row.get("TrendTemplate") or 0)
    rs = row.get("RS_vs_KLCI") or 0
    dy = (fund or {}).get("dy") or 0
    stage = row.get("Stage") or ""

    # Bucket A — Growth/Momentum
    if tt >= 7 and rs >= 5 and dy < 3:
        return "A-Momentum"
    # Bucket B — Yield/Defensive
    if dy >= 4 and tt >= 4:
        return "B-Yield"
    # Hybrid
    if tt >= 6 and dy >= 3:
        return "AB-Hybrid"
    return "—"

# ═══════════════════════════════════════════════════════════════════════════════
# LAYER 7 — POSITION SIZE CALCULATION
# ═══════════════════════════════════════════════════════════════════════════════

def position_size(price: float, portfolio: float,
                   stop_distance_pct: float = 5.0) -> dict:
    """Calculate suggested units using 10% cap + 1% risk rule + Bursa lot rounding."""
    if not price or price <= 0:
        return {"max_units": 0, "target_units": 0, "risk_units": 0,
                "final_units": 0, "final_cost": 0, "final_pct": 0}

    max_units    = int((portfolio * MAX_POSITION_PCT) / price // BURSA_LOT * BURSA_LOT)
    target_units = int((portfolio * TARGET_PCT)       / price // BURSA_LOT * BURSA_LOT)

    risk_rm    = portfolio * RISK_PER_TRADE
    risk_per_share = price * (stop_distance_pct / 100)
    risk_units = int((risk_rm / risk_per_share) // BURSA_LOT * BURSA_LOT) if risk_per_share > 0 else 0

    final = min(max_units, target_units if target_units > 0 else max_units,
                risk_units if risk_units > 0 else max_units)
    if final < BURSA_LOT:
        final = 0
    return {
        "max_units":    max_units,
        "target_units": target_units,
        "risk_units":   risk_units,
        "final_units":  final,
        "final_cost":   round(final * price, 2),
        "final_pct":    round(final * price / portfolio * 100, 2) if portfolio else 0,
    }

# ═══════════════════════════════════════════════════════════════════════════════
# LAYER 8 — ANTI-FOMO WARNING
# ═══════════════════════════════════════════════════════════════════════════════

def fomo_warning(row: dict) -> str:
    dist = row.get("DistPivot%")
    stage = row.get("Stage") or ""
    if dist is None:
        return ""
    if dist > 3:
        return "🔴 EXTENDED — DO NOT CHASE"
    if dist > 1 and stage == "BREAKOUT":
        return "🟡 LATE — small tranche only"
    if -1 <= dist <= 1:
        return "🟢 BUY ZONE"
    if stage == "COILING" and dist <= 0:
        return "⏳ WAIT for pivot break"
    return ""

# ═══════════════════════════════════════════════════════════════════════════════
# COMPOSITE QUALITY SCORE (50 PTS)
# ═══════════════════════════════════════════════════════════════════════════════

def composite_quality(kc: int, cold: int, tong: int, money: int) -> tuple[int, str]:
    total = kc + cold + tong + money   # max 14+14+10+12 = 50
    if   total >= 40: return total, "Q-ELITE"
    elif total >= 30: return total, "Q-A"
    elif total >= 20: return total, "Q-B"
    elif total >= 10: return total, "Q-C"
    return total, "Q-D"

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN PROCESSING
# ═══════════════════════════════════════════════════════════════════════════════

def enhance(df: pd.DataFrame, fundamentals: dict, portfolio: float) -> pd.DataFrame:
    new_cols = []
    for _, row in df.iterrows():
        row_d = row.to_dict()
        ticker = (row_d.get("Ticker") or "").upper()
        fund = fundamentals.get(ticker, {})

        stage_w = weinstein_stage(row_d)
        kc_s, kc_p, kc_note = kc_chong_score(fund)
        ce_s, ce_p = cold_eye_score(fund, row_d)
        tk_label, tk_s = tong_kooi_tier(fund, row_d)
        money_s, money_brk = money_equation(fund, row_d)
        bucket = assign_bucket(row_d, fund)
        sizing = position_size(row_d.get("Price") or 0, portfolio)
        fomo = fomo_warning(row_d)
        q_total, q_grade = composite_quality(kc_s, ce_s, tk_s, money_s)

        new_cols.append({
            "WeinsteinStage": stage_w,
            "KC_Chong_8":     f"{kc_p}/8",
            "KC_Score":       kc_s,
            "ColdEye_8":      f"{ce_p}/8",
            "ColdEye_Score":  ce_s,
            "Tong_Tier":      tk_label,
            "Tong_Score":     tk_s,
            "MONEY":          money_brk,
            "MONEY_Score":    money_s,
            "QualityScore":   q_total,
            "QualityGrade":   q_grade,
            "Bucket":         bucket,
            "MaxUnits":       sizing["max_units"],
            "FinalUnits":     sizing["final_units"],
            "FinalCost_RM":   sizing["final_cost"],
            "Final_Pct":      sizing["final_pct"],
            "FOMO_Flag":      fomo,
        })

    enhanced = pd.concat([df.reset_index(drop=True),
                          pd.DataFrame(new_cols)], axis=1)
    return enhanced

# ═══════════════════════════════════════════════════════════════════════════════
# HTML REPORT (quality-focused, complements v2 momentum-focused HTML)
# ═══════════════════════════════════════════════════════════════════════════════

QUALITY_COLOR = {"Q-ELITE": "#6610f2", "Q-A": "#198754", "Q-B": "#0d6efd",
                 "Q-C": "#fd7e14", "Q-D": "#dc3545"}
BUCKET_COLOR  = {"A-Momentum": "#0d6efd", "B-Yield": "#198754",
                 "AB-Hybrid": "#6610f2", "—": "#adb5bd"}
STAGE_COLOR   = {"2-UPTREND": "#198754", "1-BASE": "#fd7e14",
                 "3-TOPPING": "#dc3545", "4-DOWNTREND": "#6c757d"}


def build_html(df: pd.DataFrame, portfolio: float, generated_at: str) -> str:
    # Top picks: Stage 2 + Quality >= Q-B + FOMO not red
    actionable = df[
        (df["WeinsteinStage"] == "2-UPTREND") &
        (df["QualityScore"]  >= 20) &
        (~df["FOMO_Flag"].astype(str).str.contains("EXTENDED", na=False))
    ].sort_values(["QualityScore", "Score100"], ascending=[False, False])

    coiling_quality = df[
        (df["Stage"] == "COILING") &
        (df["QualityScore"] >= 15)
    ].sort_values("QualityScore", ascending=False)

    def render_row(s: dict, i: int) -> str:
        q_col = QUALITY_COLOR.get(s.get("QualityGrade"), "#aaa")
        b_col = BUCKET_COLOR.get(s.get("Bucket"), "#aaa")
        st_col = STAGE_COLOR.get(s.get("WeinsteinStage"), "#aaa")

        price = s.get("Price")
        price_str = f"RM {price:.4f}" if price and not pd.isna(price) else "—"

        sizing = (f"<b>{int(s.get('FinalUnits') or 0)}</b> units<br>"
                  f"<span style='font-size:10px;color:#666;'>"
                  f"RM {s.get('FinalCost_RM') or 0:,.0f} · {s.get('Final_Pct') or 0:.1f}%</span>")

        return (
            f'<tr style="border-bottom:1px solid #dee2e6;">'
            f'<td style="padding:6px 8px;font-size:11px;color:#888;">{i}</td>'
            f'<td style="padding:6px 8px;"><b>{s.get("Name","")}</b><br>'
            f'  <span style="font-size:10px;color:#888;">{s.get("Ticker","")}</span></td>'
            f'<td style="padding:6px 8px;"><span style="background:{st_col};color:#fff;padding:1px 5px;'
            f'border-radius:3px;font-size:10px;">{s.get("WeinsteinStage","")}</span></td>'
            f'<td style="padding:6px 8px;font-size:12px;">{price_str}</td>'
            f'<td style="padding:6px 8px;text-align:center;">'
            f'  <span style="font-size:14px;font-weight:700;color:{q_col};">{s.get("QualityScore")}</span>'
            f'  <span style="font-size:9px;color:#888;">/50</span><br>'
            f'  <span style="background:{q_col};color:#fff;padding:0 5px;border-radius:3px;font-size:10px;">'
            f'{s.get("QualityGrade","")}</span></td>'
            f'<td style="padding:6px 8px;font-size:11px;">'
            f'  KC: <b>{s.get("KC_Chong_8")}</b><br>'
            f'  Cold: <b>{s.get("ColdEye_8")}</b><br>'
            f'  Tong: <b>{s.get("Tong_Tier")}</b><br>'
            f'  MONEY: <b>{s.get("MONEY_Score")}</b>/12</td>'
            f'<td style="padding:6px 8px;"><span style="background:{b_col};color:#fff;padding:2px 8px;'
            f'border-radius:4px;font-size:11px;font-weight:600;">{s.get("Bucket","")}</span></td>'
            f'<td style="padding:6px 8px;">{sizing}</td>'
            f'<td style="padding:6px 8px;font-size:11px;">{s.get("FOMO_Flag","")}</td>'
            f'</tr>'
        )

    def render_table(rows_df: pd.DataFrame, title: str, sub: str) -> str:
        if rows_df.empty:
            return f'<div style="background:#fff3cd;padding:14px;border-radius:8px;margin:12px 0;">{title}: none</div>'
        rows = "".join(render_row(s.to_dict(), i + 1)
                       for i, (_, s) in enumerate(rows_df.head(30).iterrows()))
        return f"""
        <div style="background:#fff;border:1px solid #dee2e6;border-radius:8px;margin:16px 0;overflow:hidden;">
          <div style="background:#1F2937;color:#fff;padding:10px 16px;">
            <span style="font-size:14px;font-weight:600;">{title}</span>
            <span style="font-size:11px;color:#adb5bd;margin-left:10px;">{sub}</span>
          </div>
          <div style="overflow-x:auto;">
            <table style="width:100%;border-collapse:collapse;">
              <thead><tr style="background:#f1f3f5;">
                <th style="padding:8px;font-size:11px;text-align:left;">#</th>
                <th style="padding:8px;font-size:11px;text-align:left;">Stock</th>
                <th style="padding:8px;font-size:11px;text-align:left;">Weinstein</th>
                <th style="padding:8px;font-size:11px;text-align:left;">Price</th>
                <th style="padding:8px;font-size:11px;text-align:center;">Quality /50</th>
                <th style="padding:8px;font-size:11px;text-align:left;">Detail</th>
                <th style="padding:8px;font-size:11px;text-align:left;">Bucket</th>
                <th style="padding:8px;font-size:11px;text-align:left;">Position Size</th>
                <th style="padding:8px;font-size:11px;text-align:left;">FOMO</th>
              </tr></thead>
              <tbody>{rows}</tbody>
            </table>
          </div>
        </div>"""

    summary = f"""
    <div style="background:#e7d9ff;border-left:4px solid #6610f2;border-radius:6px;padding:14px 20px;margin:12px 0;font-size:13px;">
      <b style="color:#6610f2;">Quality Overlay v3 — Phase 2 Upgrade</b><br>
      <span style="font-size:11px;color:#333;">
        Portfolio sizing basis: <b>RM {portfolio:,.0f}</b> &nbsp;|&nbsp;
        Per-position cap: <b>{MAX_POSITION_PCT*100:.0f}%</b> &nbsp;|&nbsp;
        Target size: <b>{TARGET_PCT*100:.0f}%</b> &nbsp;|&nbsp;
        Risk per trade: <b>{RISK_PER_TRADE*100:.0f}%</b><br>
        New layers: Weinstein Stage · KC Chong 8-criteria · Cold Eye 8 · Tong Kooi Tier · MONEY Equation · Dual-Style Bucket · Position Size · Anti-FOMO Flag
      </span>
    </div>"""

    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>KLSE Quality Overlay v3 — {generated_at}</title>
<style>body{{font-family:-apple-system,Segoe UI,Roboto,sans-serif;background:#f8f9fa;margin:0;}}
.header{{background:#1a1a2e;color:#fff;padding:18px 28px;}}
.container{{max-width:1280px;margin:0 auto;padding:20px 16px;}}
tr:hover{{filter:brightness(0.97);}}</style></head>
<body>
<div class="header">
  <h1 style="margin:0;font-size:20px;">KLSE Quality Overlay
    <span style="font-size:12px;color:#6610f2;">v3 · KC Chong + Cold Eye + Tong Kooi + MONEY + Sizing</span></h1>
  <div style="font-size:12px;color:#adb5bd;margin-top:4px;">Generated: {generated_at}</div>
</div>
<div class="container">
  {summary}
  {render_table(actionable, "🎯 Top Quality + Stage 2 Buys",
                "Stage 2 uptrend × Quality ≥ Q-B × not extended")}
  {render_table(coiling_quality, "⏳ High-Quality Coiling Setups",
                "Currently COILING with Quality ≥ Q-C — set alerts at pivot")}
</div></body></html>"""

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="KLSE Quality Overlay v3")
    parser.add_argument("--portfolio", type=float, default=DEFAULT_PORTFOLIO,
                        help="Portfolio value in RM (default 30000)")
    parser.add_argument("--csv", type=str, default=None,
                        help="v2 watchlist CSV filename (default: latest in output/)")
    args = parser.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    generated_at = datetime.datetime.now().strftime("%d %b %Y  %H:%M")
    print(f"\nKLSE Quality Overlay v3 — Phase 2 Upgrade")
    print(f"Portfolio basis : RM {args.portfolio:,.0f}")
    print("-" * 60)

    df = load_v2_csv(args.csv)
    fundamentals = load_fundamentals()

    print(f"\nEnhancing {len(df)} stocks with quality + sizing layers...")
    enhanced = enhance(df, fundamentals, args.portfolio)

    # Outputs
    out_csv  = OUTPUT_DIR / f"watchlist_v3_{TODAY}.csv"
    out_html = OUTPUT_DIR / f"watchlist_v3_{TODAY}.html"

    enhanced.to_csv(out_csv, index=False)
    html = build_html(enhanced, args.portfolio, generated_at)
    out_html.write_text(html, encoding="utf-8")

    # Summary
    elite  = (enhanced["QualityGrade"] == "Q-ELITE").sum()
    qa     = (enhanced["QualityGrade"] == "Q-A").sum()
    stage2 = (enhanced["WeinsteinStage"] == "2-UPTREND").sum()
    actionable = enhanced[
        (enhanced["WeinsteinStage"] == "2-UPTREND") &
        (enhanced["QualityScore"] >= 20)
    ]

    print(f"\n{'='*60}")
    print(f"Q-ELITE         : {elite}")
    print(f"Q-A             : {qa}")
    print(f"Stage 2 uptrend : {stage2}")
    print(f"Actionable picks: {len(actionable)} (Stage 2 + Quality ≥ Q-B)")
    print(f"{'='*60}")
    print(f"\nCSV  : {out_csv}")
    print(f"HTML : {out_html}")
    webbrowser.open(out_html.as_uri())
    print("Browser opened.")


if __name__ == "__main__":
    main()
