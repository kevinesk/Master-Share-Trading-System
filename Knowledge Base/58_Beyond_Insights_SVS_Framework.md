# 58 — Beyond Insights (Kathlyn Toh) — SVS Framework & Curriculum

**Source:** Beyond Insights Investment & Trading Education (Asia)
**Founder:** Kathlyn Toh
**Core philosophy:** Make the market **Systematic, Versatile, Safe (SVS)** — eliminate guesswork, preserve capital, master psychology.

This file integrates the full Beyond Insights curriculum into the KLSE Trading Mastery system. It maps each Beyond Insights teaching to the existing knowledge base files and TradingView scripts so the principles become operational, not just theoretical.

---

## 0. The SVS Framework — The Anchor

| Pillar | Meaning | Where it lives in our system |
|---|---|---|
| **S — Systematic** | Repeatable rules, no intuition | [PRE_TRADE_CHECKLIST.md](PRE_TRADE_CHECKLIST.md), [MASTER_DECISION_TREE.md](MASTER_DECISION_TREE.md) |
| **V — Versatile** | Multiple styles & timeframes (LT growth, trend, swing, intraday) | [DUAL_STYLE_PLAYBOOK.md](DUAL_STYLE_PLAYBOOK.md), [05_Intraday_Trading_KLSE.md](05_Intraday_Trading_KLSE.md) |
| **S — Safe** | Capital preservation first, predefined risk | [06_Risk_Management_and_Position_Sizing.md](06_Risk_Management_and_Position_Sizing.md), [POSITION_SIZE_CALCULATOR.md](POSITION_SIZE_CALCULATOR.md) |

**Operating rule:** No trade is allowed unless it scores 🟢 on **all three** SVS pillars. If any pillar is missing — skip the trade.

---

## TIER 1 — Foundation: Growth Investing eXpress (GIX)

### Module 1.1 — Fundamental Analysis & Valuation
**Beyond Insights teaches:** ROE, ROA, EPS, institutional ownership, intrinsic value, dividend yield screening.

**Our integration:**
- Fundamental scoring already lives in `Fundamentals/` folder (per-ticker JSON v2)
- Cross-reference with [KLSE_QUALITY_SCORE.md](KLSE_QUALITY_SCORE.md) — 50-pt grade includes ROE, debt, FCF
- Use [29_Reading_Financial_Statements.md](29_Reading_Financial_Statements.md) for 15-min analysis checklist
- Valuation methods → [35_Stock_Valuation_Methods.md](35_Stock_Valuation_Methods.md)

**Beyond Insights "eXpress Screener" → our equivalent:**
- KLSE: `KLSE Screener/` + `27_Quantitative_Stock_Screening.md` 4-factor model
- US: `US Market System/` mirror
- Bargain bucket: [KLSE_BARGAIN_HUNTING_SCREENERS.md](KLSE_BARGAIN_HUNTING_SCREENERS.md)

### Module 1.2 — Core Technical Analysis
**Beyond Insights teaches:** Uptrend/downtrend/sideways structure, S/R zones, candlestick basics, max safe buy price.

**Our integration:**
- Trend structure → [02_Minervini_SEPA_KLSE.md](02_Minervini_SEPA_KLSE.md) Trend Template (8 criteria)
- Candlesticks → [52_Fred_Tam_KLSE_Patterns_Candlesticks.md](52_Fred_Tam_KLSE_Patterns_Candlesticks.md)
- **Max safe buy price** (don't chase): we enforce via **≤ 2–3% above pivot** rule in [12_Perfect_Entry_Exit.md](12_Perfect_Entry_Exit.md). This is the same anti-chasing discipline Kathlyn Toh teaches.

### Module 1.3 — The Golden Rule: 1% Risk
**Beyond Insights teaches:** Never risk more than 1% of capital per trade. Cut-loss defined BEFORE entry.

**Our integration:**
- US system: 1% sizing (per [project_us_ecosystem.md])
- KLSE system: 2% rule baseline (per `06_Risk_Management_and_Position_Sizing.md`) — but Beyond Insights' 1% is the tighter discipline. **Decision:** for new positions during a weak macro (KLCI < EMA50), step down to 1% per BI's rule. Strong macro = 2% allowed.
- Cut-loss BEFORE entry → enforced by Gate 6 of [PRE_TRADE_CHECKLIST.md](PRE_TRADE_CHECKLIST.md)

---

## TIER 2 — Advanced: Technical Acceleration & Intraday

### Module 2.1 — Early Trend Reversals
**Beyond Insights teaches:** Catch structural shift points to ride macro/swing moves early.

**Our integration:**
- Stage 1→2 transition detection → [44_Weinstein_Industry_Stage_Analysis.md](44_Weinstein_Industry_Stage_Analysis.md)
- **COIL pre-surge signal** already shipped in V8 Sniper + KLSE MSS v6 (commit `cdc1a41`) — this IS the early-reversal detector
- Cup-handle / double-bottom / VCP early entries → [39_ONeil_Greatest_Winners_Templates.md](39_ONeil_Greatest_Winners_Templates.md) + [42_Momentum_Masters_Advanced_VCP.md](42_Momentum_Masters_Advanced_VCP.md) ("the cheat")

### Module 2.2 — Pyramiding & Compounding
**Beyond Insights teaches:** Only add to winners AFTER the trend strengthens AND the initial position is protected (stop moved to breakeven).

**Our integration:**
- Tranche entry rules → [06_Risk_Management_and_Position_Sizing.md](06_Risk_Management_and_Position_Sizing.md)
- **Pyramiding rule (BI-aligned):** add Tranche 2 only when (a) price +5% above first entry, (b) stop on Tranche 1 moved to breakeven, (c) volume confirms continuation. NEVER pyramid into a losing position.

### Module 2.3 — Intraday Trading (Zero Overnight Risk)
**Beyond Insights teaches:** Open and close within a single session — eliminate gapping & overnight news shocks.

**Our integration:**
- Full intraday playbook → [05_Intraday_Trading_KLSE.md](05_Intraday_Trading_KLSE.md)
- Indicator: `Intraday Sniper/V9 Intraday Sniper — Phase 2 Filters.pine`
- US intraday: `Intraday Sniper (US)/`
- **BI rule to enforce:** any position opened on the intraday timeframe MUST be closed by the last 15-min auction. No "let it run overnight just this once."

### Module 2.4 — CFDs (Leverage with Defined Risk)
**Beyond Insights teaches:** Use CFDs for short/mid-term leverage, both long and short, with strict risk control.

**Our integration:**
- Not currently in our KB. KLSE retail doesn't have native CFDs — closest equivalents:
  - **Structured warrants** → [15_Structured_Warrants_Bursa.md](15_Structured_Warrants_Bursa.md) (gearing + defined max loss = premium paid)
  - **US side:** options and margin available — see project_us_ecosystem.md
- **Rule:** any leveraged instrument inherits the **1% capital risk cap** — the leverage does not increase risk, it reduces capital required for the same risk.

---

## TIER 3 — Professional/Mastery: Macro & Options

### Module 3.1 — Options for Income & Protection
**Beyond Insights teaches:** Options as leverage AND portfolio insurance. Profit in sideways markets via time decay.

**Our integration:**
- KLSE has no liquid equity options — applies to US side only
- **Defensive use:** when US portfolio macro score drops (VIX > 25, SPX < EMA50), buy SPY puts as portfolio hedge (0.5–1% of capital, 30–60 DTE)
- **Income use:** covered calls on stalled positions in late-cycle
- Build out: dedicated `61_Options_Strategies.md` (placeholder — not yet written)

### Module 3.2 — Megatrends & Supply Chain Analysis
**Beyond Insights teaches:** 8 core global industries, supply chain mapping, 5 stages of emerging stocks, buyback analysis.

**Our integration:**
- Supply chains → [18_Supply_Chain_Analysis.md](18_Supply_Chain_Analysis.md) (semi, plantation, construction, healthcare, etc.)
- 5 stages of emerging stocks ≈ Weinstein 4 stages + accumulation footprint → [44_Weinstein_Industry_Stage_Analysis.md](44_Weinstein_Industry_Stage_Analysis.md) + [39_ONeil_Greatest_Winners_Templates.md](39_ONeil_Greatest_Winners_Templates.md)
- Buyback analysis → covered in [28_Corporate_Actions_Bursa.md](28_Corporate_Actions_Bursa.md) + Tong Kooi Ong corporate-insider lens in [56_Tong_Kooi_Ong_Corporate_Insider.md](56_Tong_Kooi_Ong_Corporate_Insider.md)
- Capital cycle (overcapacity → starvation) → [48_Chancellor_Capital_Cycle.md](48_Chancellor_Capital_Cycle.md)

### Module 3.3 — Inter-Market & Macro Event Navigation
**Beyond Insights teaches:** Stocks ↔ FX ↔ crypto ↔ bonds ↔ commodities; manage risk through FOMC, central bank events, geopolitics.

**Our integration:**
- Intermarket → [32_Intermarket_Analysis.md](32_Intermarket_Analysis.md) (USD/MYR master variable, SOX → semis, CPO → planters)
- Global macro → [20_Global_Macro_for_KLSE.md](20_Global_Macro_for_KLSE.md)
- Dalio liquidity cycles → [47_Dalio_Debt_Crises_Liquidity.md](47_Dalio_Debt_Crises_Liquidity.md)
- **Event navigation rule (BI):** No new entries 24h before FOMC, BNM MPC, or major Bursa company results. Existing positions: tighten stops by 50%.

---

## TIER 4 — Trading Psychology Bootcamp ★ Highest Weight

Kathlyn Toh's central tenet: **A 90% win-rate strategy + bad psychology = losses. A 50% win-rate strategy + ironclad discipline = profits.**

### Module 4.1 — Behavioral Bias Correction
**Targeted:** FOMO, panic-selling, greed, revenge trading, ego.

**Our integration:**
- [09_Trading_Psychology.md](09_Trading_Psychology.md) — 7 cognitive biases
- [33_Fear_FOMO_Confidence_Mastery.md](33_Fear_FOMO_Confidence_Mastery.md) — Mark Douglas 5 truths, FOMO dopamine cycle, 3-step interrupt
- [STICKY_NOTE_Anti_FOMO.md](STICKY_NOTE_Anti_FOMO.md) — physical pre-buy emotional checks

### Module 4.2 — Multi-Decade Market Lifecycle Simulation
**Beyond Insights teaches:** Experience 30 years of market conditions via simulation to build emotional fortitude.

**Our integration:**
- Backtesting framework → [14_Backtesting_Framework.md](14_Backtesting_Framework.md)
- Crisis case studies → 47_Dalio + 55_Tan_Chong_Koay (1997 AFC, 2000 dot-com, 2008 GFC, 2020 COVID)
- **Action:** run Pine Script backtests across 1997, 2008, 2020 KLCI/SPX data on every new strategy BEFORE live deployment

### Module 4.3 — BiTS Journaling Ecosystem
**Beyond Insights teaches:** Log technical trade details + emotional/mental state at execution to map and eliminate recurring errors.

**Our integration:**
- [TRADE_JOURNAL.md](TRADE_JOURNAL.md) — already in place
- **Upgrade:** add three emotion fields to every journal entry:
  1. **Pre-trade emotion** (calm / FOMO / revenge / confident / fearful)
  2. **In-trade emotion** (during the hold)
  3. **Exit emotion** (disciplined / panic / greed-extended)
- Weekly review: pattern-match losing trades against emotion tags. If 60%+ of losses tag "FOMO" or "revenge" — institute a 24h cooling-off rule.

---

## Beyond Insights vs Our System — Gap Analysis

| BI Component | Status in our system | Action |
|---|---|---|
| SVS Framework anchor | ✅ Embedded via existing checklists | Reference in MASTER_DECISION_TREE header |
| 1% cut-loss before entry | ✅ Gate 6 of pre-trade checklist | Step down to 1% in weak macro |
| eXpress screener | ✅ KLSE Screener + US Screener | Done |
| Trend Template | ✅ Minervini SEPA file 02 | Done |
| VCP / early reversal | ✅ Files 04, 42; COIL signal shipped | Done |
| Intraday zero-overnight | ✅ Intraday Sniper scripts | Enforce close-by-auction rule |
| CFDs | ⚠️ KLSE = warrants substitute | US side needs options module |
| Options (income + hedge) | ❌ Not yet built | **TODO: 61_Options_Strategies.md** |
| Supply chain / megatrends | ✅ Files 18, 21, 48 | Done |
| Intermarket | ✅ File 32 | Done |
| Event navigation | ⚠️ Scattered | **TODO: add 24h-before-event rule to DAILY_ROUTINE** |
| Psychology bootcamp | ✅ Files 09, 33 + Sticky Note | Upgrade journal with 3 emotion fields |
| BiTS journaling | ⚠️ Technical only | **TODO: add emotion tags to TRADE_JOURNAL** |
| 30-year simulation | ⚠️ Manual backtests | Run 1997/2008/2020 backtests on all strategies |

---

## The Single Most Important BI Quote to Internalise

> *"You can have a 90% win-rate strategy and still lose money without psychological discipline. Conversely, a 50% win-rate with ironclad risk management is highly profitable."*

This is mathematically true via the [25_Probability_Edge_Calculation.md](25_Probability_Edge_Calculation.md) R-multiple system:
- 50% win-rate × 3R winners vs 1R losers = **+1R per trade** (expectancy)
- 90% win-rate × 1R winners vs 10R losers (no stop discipline) = **0R expectancy** — ruin guaranteed

**Conclusion:** the edge lives in **payoff ratio × discipline**, not in win rate. This is why every Beyond Insights module circles back to the 1% rule and pre-defined cut-loss.

---

## Three Things to Operationalise This Week

1. **Add SVS triple-check** to the top of [MASTER_DECISION_TREE.md](MASTER_DECISION_TREE.md): every trade must be 🟢 Systematic + 🟢 Versatile (right style for cycle) + 🟢 Safe (1–2% risk capped).
2. **Add 3 emotion fields** to [TRADE_JOURNAL.md](TRADE_JOURNAL.md): pre-trade / in-trade / exit emotion.
3. **Add event-blackout rule** to [DAILY_ROUTINE.md](DAILY_ROUTINE.md): no new entries 24h before FOMC / BNM MPC / major results.

---

*See also:* [09_Trading_Psychology.md](09_Trading_Psychology.md), [33_Fear_FOMO_Confidence_Mastery.md](33_Fear_FOMO_Confidence_Mastery.md), [06_Risk_Management_and_Position_Sizing.md](06_Risk_Management_and_Position_Sizing.md), [DUAL_STYLE_PLAYBOOK.md](DUAL_STYLE_PLAYBOOK.md), [MASTER_DECISION_TREE.md](MASTER_DECISION_TREE.md)
