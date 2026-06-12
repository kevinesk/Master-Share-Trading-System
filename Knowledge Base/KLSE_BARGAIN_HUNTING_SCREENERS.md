# KLSE Bargain Hunting Screeners — Reference

**Purpose:** Two TradingView Stock Screeners for buying quality KLSE blue chips during broad market weakness (KLCI < EMA50). Avoids "falling knife" traps that the naive oversold-RSI approach catches.

**When to use:** Only when **FBMKLCI closes below its daily EMA50**. Set an alert on KLCI for "Price crossing down EMA(50)" — when it fires, run these screeners. Otherwise the macro context is wrong.

**Related KB references:** [43_Marks_Market_Cycles.md](43_Marks_Market_Cycles.md), [53_KC_Chong_Bursa_Value_Investing.md](53_KC_Chong_Bursa_Value_Investing.md), [55_Tan_Chong_Koay_Never_Fully_Invested.md](55_Tan_Chong_Koay_Never_Fully_Invested.md), [57_Cold_Eye_Local_Value_Compounding.md](57_Cold_Eye_Local_Value_Compounding.md), [MARKET_REGIME_FILTER.md](MARKET_REGIME_FILTER.md)

---

## Screener 1: KLSE Quality Pullback Buy

**Thesis:** Top-50 quality names that are oversold on the short timeframe but still in long-term uptrend. Catches pullbacks within bull structure, not collapses.

| Filter | Value | Rationale |
|---|---|---|
| Market | MY | KLSE only |
| Market cap | > 3B MYR | Top ~50, institutional liquidity |
| **Price > SMA(200)** | ✅ | **Critical — still in long-term uptrend** |
| Price < EMA(20) | ✅ | Short-term oversold |
| RSI (14) | 30 to 45 | Oversold, not freefall |
| Average volume 30D | > 300,000 | Real exit liquidity |
| P/E TTM | 5 to 25 | Reasonable valuation |
| ROE TTM | > 10% | Quality threshold |
| Debt/Equity | < 1 | Survives the downturn |
| Net income growth TTM YoY | > 0% | Fundamentals improving |
| Dividend yield TTM | > 2% | Paid to wait |
| Price vs 52-week high | -10% to -25% | Meaningful pullback, not collapse |

**Expected hit count:** 8–15 stocks during normal pullbacks; 20–30 during deeper corrections.

---

## Screener 2: KLSE Deep Value + Dividend Safety

**Thesis:** True deep value with sustainable dividends — for income-focused bargain hunting during bear phases. Wider net than Screener 1.

| Filter | Value | Rationale |
|---|---|---|
| Market | MY | KLSE only |
| Market cap | > 500M MYR | Mid+ cap, still tradable |
| P/E | 4 to 12 | Real value zone |
| P/B | 0.5 to 1.8 | Below to slight premium of book |
| Dividend yield TTM | > 4% | Income mandate |
| **Payout ratio** | < 80% | **Dividend is sustainable** |
| ROE TTM | > 10% | Capital efficiency |
| Debt/Equity | < 0.7 | Conservative balance sheet |
| Revenue growth TTM YoY | > 0% | Not a melting ice cube |
| Average volume 30D | > 150,000 | Tradable liquidity |
| Recent earnings date | Last 90 days | Fresh fundamentals |

**Expected hit count:** 5–12 stocks.

---

## Manual Confirmation Checklist (apply to EVERY screener result)

Before buying any candidate:

- [ ] **Higher low forming on daily chart** — at least one swing low above the most recent swing low
- [ ] **Volume drying up on red bars** — sellers exhausted (use OBV or just visual)
- [ ] **Sector RS not in bottom 2** of your KLSE Market Regime Dashboard
- [ ] **No earnings scheduled in next 14 days** — avoid binary surprise risk
- [ ] **News check** — confirm decline is macro/sentiment-driven, NOT fundamental (fraud, downgrade, missed guidance, accounting issue)
- [ ] **SmartMCDX shows ≥ 5–10% banker accumulation** (Pro Quant Desk indicator) — institutional footprint of a real bottom
- [ ] **Stock is not in a Stage 4 decline** (Weinstein — see [44_Weinstein_Industry_Stage_Analysis.md](44_Weinstein_Industry_Stage_Analysis.md))

If any box unchecked → skip the trade.

---

## Phased Entry Rules (mandatory for bargain hunts)

Never lump-sum into a bargain pick. Use a 3-tranche scale-in:

| Tranche | Size | Trigger |
|---|---|---|
| 1 | ⅓ of intended position | First screener hit + manual checklist passes |
| 2 | ⅓ | Confirmed higher low on daily chart (1-3 weeks later) |
| 3 | ⅓ | Price reclaims EMA(20) with volume |

**Hard stop:** -15% from average cost across all 3 tranches. If thesis breaks before Tranche 2, you've only lost on ⅓ position.

---

## Risk Warning (read every time)

Bargain hunting in a downtrend has the worst risk-reward of any KLSE strategy without discipline:

- ~70% of "quality at discount" picks decline another **10–15% before basing**
- The remaining ~30% deliver **30–60% in 6–12 months** (math still works)
- **Only if you size small, scale in, and respect the stop**

**Position sizing:** Cap individual bargain-hunt positions at **5%** of portfolio (vs 10% for trend-following swing trades). Cap total bargain-hunt allocation at **30%** of portfolio — always hold dry powder for the next leg lower. See [POSITION_SIZE_CALCULATOR.md](POSITION_SIZE_CALCULATOR.md) and [55_Tan_Chong_Koay_Never_Fully_Invested.md](55_Tan_Chong_Koay_Never_Fully_Invested.md).

---

## Common Traps to Avoid

| Trap | Symptom | Defense |
|---|---|---|
| Falling knife | Already down 30%+, RSI < 30, no base | Require Price > SMA(200) **or** 52w-low proximity confirmed |
| Yield trap | Dividend yield > 8% screams danger | Add Payout ratio < 80% filter |
| Value trap | Low P/E because earnings collapsing | Require Net income growth > 0% |
| Liquidity trap | Cheap because no one trades it | Require avg vol 30D > 150K |
| Cigar butt | One-time bargain, no growth runway | Require ROE > 10% (real returns on capital) |

---

## Quick Setup in TradingView

1. Open Stock Screener
2. Filters → add each row from the tables above
3. Save as: **"KLSE Quality Pullback Buy"** and **"KLSE Deep Value Income"**
4. Set FBMKLCI alert: Price crossing down EMA(50) — title "MACRO BARGAIN HUNT WINDOW OPEN"
5. Only run screeners when that alert has fired in the last 30 days

---

*Last updated: 2026-05-26*
