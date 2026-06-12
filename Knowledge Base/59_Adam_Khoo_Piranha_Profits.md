# 59 — Adam Khoo / Piranha Profits — VMI™, Profit Snapper, Market Snapper, PAM

**Source:** Piranha Profits (online academy) + Wealth Academy live seminars
**Founder:** Adam Khoo (with co-developer Alson Chew for PAM)
**Core split:** Two clean tracks — **Investing** (Whale Investor™, hybrid fundamental + technical) and **Trading** (Profit Snapper™ → Market Snapper™ → PAM, pure price action).

This file integrates the full Adam Khoo curriculum into the KLSE Trading Mastery system. Each Khoo lesson is mapped to existing KB files and TradingView scripts so the methods are operationalised, not catalogued.

---

## 0. The Two-Track Mental Model

Adam Khoo's organising principle is that **investing and trading are different jobs requiring different brains** — don't blur them.

| Track | Style | Hold | Analysis weight | Our system home |
|---|---|---|---|---|
| **Whale Investor™** | LT compounding | Months–years | 70% F / 30% T | [DUAL_STYLE_PLAYBOOK.md](DUAL_STYLE_PLAYBOOK.md) "Bucket B" (yield/quality) |
| **Profit Snapper™** | Swing | Days–weeks | 100% T (trend retrace) | KLSE MSS v6 + V8/V9 Pro Quant Desk |
| **Market Snapper™** | Adv swing + day | Min–days | 100% T (mean rev + scalp) | Intraday Sniper + Bollinger module |
| **PAM™** (Alson Chew) | Institutional footprint | Hours–weeks | Price + volume | Wyckoff/VSA + order flow files |

**Operating rule:** any individual trade must be tagged to ONE track. No bucket-jumping mid-trade ("it was a swing, now it's a long-term hold because it dropped").

---

## TRACK 1 — Whale Investor™ (Value Momentum Investing™)

VMI™ = buy fundamentally strong companies that are also showing positive technical momentum. Hybrid of Buffett valuation + O'Neil/Minervini trend.

### Lesson 1 — Long-run vs short-run price drivers
- LT: earnings growth + multiple expansion
- ST: sentiment, flows, news
- **Our mapping:** This is already the spine of [35_Stock_Valuation_Methods.md](35_Stock_Valuation_Methods.md) + [10_CAN_SLIM_KLSE.md](10_CAN_SLIM_KLSE.md). VMI is essentially **CAN SLIM with valuation discipline added**.

### Lesson 2 — ETFs as structural safety net
- Index/sector ETFs for entry/exit timing
- **Our mapping:** KLSE has limited ETF depth (FBMKLCI-EA, MyETF series). For US side, this is core — see `project_us_ecosystem.md`. **Action:** when KLCI macro is Red, route 30–50% of capital to a US S&P ETF rather than sit in 100% cash.

### Lesson 3 — Pillars of profitable investing
- Buy premier companies at discount
- Distinguish **value traps** from real bargains
- **Our mapping:** [KLSE_BARGAIN_HUNTING_SCREENERS.md](KLSE_BARGAIN_HUNTING_SCREENERS.md) is your falling-knife filter — Adam Khoo's "value trap" warning is exactly what these screeners protect against. Cross-ref [53_KC_Chong_Bursa_Value_Investing.md](53_KC_Chong_Bursa_Value_Investing.md) for the 7 KLSE value trap signs.

### Lesson 4 — Fundamental analysis (moat businesses)
- IS / BS / CF mechanics, ROE, ROA, D/E, EPS growth
- **Our mapping:** [29_Reading_Financial_Statements.md](29_Reading_Financial_Statements.md) + [KLSE_QUALITY_SCORE.md](KLSE_QUALITY_SCORE.md) 50-pt grade already mechanises this.

### Lesson 5 — Stock valuation models (4 methods)
- PEG, DCF, Discounted Earnings, P/B
- **Our mapping:** [35_Stock_Valuation_Methods.md](35_Stock_Valuation_Methods.md) covers P/E, PEG, P/B, EV/EBITDA, DCF, DDM. **Khoo's 4-method convergence rule:** if 3 of 4 methods say "undervalued by ≥20%", that's a real margin of safety. Add this as a tiebreaker when [KLSE_QUALITY_SCORE.md](KLSE_QUALITY_SCORE.md) gives ambiguous reads.

### Lesson 6 — Technical timing for investors
- Dow Theory + Moving Averages for macro trend
- **Our mapping:** [02_Minervini_SEPA_KLSE.md](02_Minervini_SEPA_KLSE.md) Trend Template (EMA50 > EMA150 > EMA200) IS the Khoo investor-timing filter.

### Lesson 7 — The 7-Step VMI™ Formula (Khoo's signature checklist)

Khoo's exact sequence — adopt as a per-stock investor scorecard:

| # | Check | Pass criterion |
|---|---|---|
| 1 | Wonderful business with moat | Quality Score ≥ 35/50 |
| 2 | Consistent earnings growth | EPS up 5 of last 7 years |
| 3 | Strong ROE | ROE ≥ 15% for 3+ years |
| 4 | Low debt | D/E ≤ 0.5 (or net cash) |
| 5 | Trading below intrinsic value | ≥20% discount on 3 of 4 valuation methods |
| 6 | Uptrend confirmed | Price > 200 EMA, EMA50 > EMA200 |
| 7 | Momentum entry trigger | Bounce off EMA50 OR breakout from base on volume |

**Pass = ≥6 of 7.** This becomes the **Whale Investor pre-buy gate** — runs BEFORE [PRE_TRADE_CHECKLIST.md](PRE_TRADE_CHECKLIST.md) for any position tagged "investing bucket".

### Lesson 8 — Portfolio design
- 8 structural stock classifications, defensive vs cyclical balance
- **Our mapping:** [DUAL_STYLE_PLAYBOOK.md](DUAL_STYLE_PLAYBOOK.md) two-bucket model + [16_Sector_Playbooks.md](16_Sector_Playbooks.md). Khoo's 8 classes mirror Lynch's 6 ([46_Lynch_Six_Categories.md](46_Lynch_Six_Categories.md)) — use Lynch as the working schema, Khoo as cross-check.

### Lesson 9 — Screeners + exit rules
- Global screener setup, hard exit rules
- **Our mapping:** `KLSE Screener/` + `US Market System/` + [27_Quantitative_Stock_Screening.md](27_Quantitative_Stock_Screening.md). **Khoo's investor exit rules** (adopt verbatim):
  1. Fundamentals deteriorate (2 consecutive quarters EPS down)
  2. Price closes below 200 EMA on weekly + holds 4 weeks
  3. Original thesis broken (regulatory shock, moat erosion)
  4. Better opportunity with materially higher VMI score appears (relative replacement)

### Lesson 10 — Investor psychology (NLP-based)
- Defeat panic-selling, FOMO via anchoring techniques
- **Our mapping:** [09_Trading_Psychology.md](09_Trading_Psychology.md) + [33_Fear_FOMO_Confidence_Mastery.md](33_Fear_FOMO_Confidence_Mastery.md). Already covered.

### Lesson 11 — Broker navigation
- Selecting international brokers, order types
- **Our mapping:** You already use MooMoo (KLSE) + IBKR or similar (US). Already operational.

### Lesson 12 — Portfolio turbocharging
- Margin (cautiously), covered calls, protective puts
- **Our mapping:** US side only (KLSE has no liquid options). Slated for the future `61_Options_Strategies.md` placeholder noted in file 58.

---

## TRACK 2 — Profit Snapper™ (Foundational Swing Trading)

100% technical. Hold days–weeks. Built on **Trend Retracement** (Khoo's signature setup).

### Lesson 1 — Trading as a business
- Systematic, not emotional
- **Our mapping:** [DAILY_ROUTINE.md](DAILY_ROUTINE.md) + [WEEKLY_ROUTINE.md](WEEKLY_ROUTINE.md) already enforce this.

### Lesson 2 — The Casino Math (Positive Expectancy)
- Random individual outcomes, consistent edge via expectancy
- **Our mapping:** [25_Probability_Edge_Calculation.md](25_Probability_Edge_Calculation.md) full coverage of R-multiples + Kelly + ruin probability. Khoo's "casino" framing matches our **Beyond Insights anchor** — see [58_Beyond_Insights_SVS_Framework.md](58_Beyond_Insights_SVS_Framework.md): edge = payoff ratio × discipline, not win rate.

### Lesson 3 — Technical Analysis I (Structure)
- Trend structure, macro S/R as supply/demand zones
- **Our mapping:** [34_Advanced_Technical_Analysis.md](34_Advanced_Technical_Analysis.md) covers HH/HL, BOS, CHoCH.

### Lesson 4 — Technical Analysis II (Indicators)
- Trend indicators + momentum oscillators + divergences + candles
- **Our mapping:** [13_Bollinger_Bands_Oscillator.md](13_Bollinger_Bands_Oscillator.md) + [52_Fred_Tam_KLSE_Patterns_Candlesticks.md](52_Fred_Tam_KLSE_Patterns_Candlesticks.md) + Pro Quant Desk SmartMCDX overlay.

### Lesson 5 — Risk & position sizing (1–2% rule)
- **Identical to Beyond Insights' 1% rule** — confirms it as universal pro standard
- **Our mapping:** [POSITION_SIZE_CALCULATOR.md](POSITION_SIZE_CALCULATOR.md) + [06_Risk_Management_and_Position_Sizing.md](06_Risk_Management_and_Position_Sizing.md). Already enforced.

### Lessons 6–10 — Trend Retracement System (Khoo's signature)

**The setup (adopt as a named pattern in our library):**

1. **Stage 2 uptrend confirmed** — price > 50 EMA > 150 EMA > 200 EMA, all sloping up
2. **Retracement to dynamic support** — pullback to 20 EMA or 50 EMA (depending on trend strength)
3. **Volume contraction during pullback** — dry-up like VCP final contraction
4. **Reversal signal at the EMA** — bullish engulfing, hammer, or inside-bar break
5. **Entry** — buy on the close of the reversal bar or open of the next bar
6. **Stop** — below the swing low of the pullback (typically 4–8% away)
7. **Target** — prior swing high (T1), then trailing on 20 EMA

**Why this matters for KLSE:** the existing V8/V9 Pro Quant Desk and KLSE MSS v6 detect Stage 2 + VCP breakouts. **Trend Retracement is the complementary entry** — for when you missed the breakout and want to add on the first healthy pullback. Less risk than a chase-buy at the breakout extended +5%.

**Khoo's journaling protocol (lessons 6–10):**
- Automated transaction log — flag execution flaws weekly
- We already have [TRADE_JOURNAL.md](TRADE_JOURNAL.md) with the BiTS emotion tags from file 58 — combine the two.

---

## TRACK 3 — Market Snapper™ (Advanced Swing + Day)

Adam's "all-weather" playbook — profit in bull, bear, or chop.

### Lesson 1 — Breakout Within Base
- Tight consolidation inside a larger trend; screen for high/low momentum profiles
- **Our mapping:** This is exactly the **VCP "cheat" entry** ([42_Momentum_Masters_Advanced_VCP.md](42_Momentum_Masters_Advanced_VCP.md)) + the COIL pre-surge signal already shipped in V8 Sniper + KLSE MSS v6 (commit `cdc1a41`). **Direct overlap — no new build needed.**

### Lessons 2 & 3 — Impulse Pullback (hyper-growth scaling)
- After an impulse leg up, scale into the first shallow pullback
- **Our mapping:** Extension of Profit Snapper's Trend Retracement, applied to higher-beta names. Use [41_Ryan_Zanger_Methods.md](41_Ryan_Zanger_Methods.md) — Zanger's bull flag pattern is the same idea.

### Lesson 4 — Momentum Value Reversal (MVR)
- Strong stocks → oscillator hits extreme overbought → fade for a quick reversal trade
- **Counter-intuitive for momentum traders** — Khoo's lesson: even in an uptrend, RSI > 80 + bearish divergence = high-probability short-term mean revert
- **Our mapping:** [13_Bollinger_Bands_Oscillator.md](13_Bollinger_Bands_Oscillator.md) + divergence section of [34_Advanced_Technical_Analysis.md](34_Advanced_Technical_Analysis.md). New rule: **MVR is only for trim-the-runner sizing**, not new shorts (KLSE has limited short access anyway).

### Lessons 5 & 6 — Counter-Trend + Divergence
- Safe structural turning points to fade overextensions
- **Our mapping:** Wyckoff distribution → [08_Wyckoff_Method_VSA.md](08_Wyckoff_Method_VSA.md). Combine with breadth divergence from [26_Market_Breadth_Sentiment.md](26_Market_Breadth_Sentiment.md).

### Lesson 7 — Bollinger Mean Reversion (BMR)
- Long/short at ±2σ band extremes
- **Our mapping:** [13_Bollinger_Bands_Oscillator.md](13_Bollinger_Bands_Oscillator.md) %B + Bandwidth squeeze module already documents this. Add Khoo's **filter:** only take BMR on stocks with ADX < 20 (ranging market), never in ADX > 30 (strong trend = bands ride).

### Lesson 8 — The Capitulation Setup
- High-prob bottoms during panic washouts
- **Signal stack:** (a) VIX or volatility spike, (b) volume 3× average, (c) wide-range down bar, (d) close in upper third of bar (hammer/dragonfly), (e) breadth panic (95% down volume day)
- **Our mapping:** Cross-ref Tan Chong Koay's "never fully invested → deploy in crisis" ([55_Tan_Chong_Koay_Never_Fully_Invested.md](55_Tan_Chong_Koay_Never_Fully_Invested.md)). **Capitulation = the cash you preserved gets deployed.**

### Lessons 9 & 10 — Gap Up News Scalp (GUNS) + Intraday execution
- Catch volatile moves within 3–5 minutes of open on positive gap-up news
- Bracket orders, direct routing
- **Our mapping:** [05_Intraday_Trading_KLSE.md](05_Intraday_Trading_KLSE.md) + Intraday Sniper scripts. **KLSE caveat:** Bursa retail brokerage doesn't have IBKR-style direct-routing; bracket orders limited. GUNS is more applicable to US side. For KLSE, adapt to the **opening 30-min observation rule** in [DAILY_ROUTINE.md](DAILY_ROUTINE.md) — observe, don't scalp.

---

## TRACK 4 — Price Action Manipulation™ (PAM, by Alson Chew)

Institutional footprint reading. Decode market-maker engineered moves.

### Modules 1 & 2 — Market Flow & Big Player Footprints
- Identify when supply/demand is being falsified by market makers
- **Our mapping:** [54_Tradeview_MONEY_Equation.md](54_Tradeview_MONEY_Equation.md) covers exactly this for KLSE — 5 manipulation patterns (pump-dump, rumour mill, rights issue trap, surprise director sale, synthetic demand). PAM is the global equivalent.

### Modules 3 & 4 — Stop-Loss Hunting / Liquidity Pools
- Big players clear retail stops below obvious S/R before reversing
- **Practical rule (adopt):** never place stop at the EXACT round number or visible swing low. Place it **0.5–1 ATR below** to avoid the hunt.
- **Our mapping:** This is a stop-placement upgrade — apply across [06_Risk_Management_and_Position_Sizing.md](06_Risk_Management_and_Position_Sizing.md) and the stop rules in [12_Perfect_Entry_Exit.md](12_Perfect_Entry_Exit.md).

### Modules 5 & 6 — Force Strike Bar Analysis
- Reduce chart to 3 standard bar formations for entries
- **The 3 bars Alson Chew uses:** wide-range absorption bar, narrow-range coiled bar, false-break reversal bar
- **Our mapping:** Maps directly onto VSA bar types in [08_Wyckoff_Method_VSA.md](08_Wyckoff_Method_VSA.md). Add as a quick-decode cheat sheet.

### Modules 7 & 8 — DR1/UR1 reversal & continuation patterns
- Trade alongside institutional accumulation/distribution
- **DR1** = down-reversal pattern #1 (failed breakdown + strong close)
- **UR1** = up-reversal pattern #1 (failed breakout + strong drop)
- **Our mapping:** Equivalent to Wyckoff "spring" (DR1) and "upthrust" (UR1) in [08_Wyckoff_Method_VSA.md](08_Wyckoff_Method_VSA.md). Same idea, different naming. Use Wyckoff vocabulary as the master schema; PAM as cross-reference.

---

## Adam Khoo vs Our System — Gap Analysis

| Khoo Component | Status in our system | Action |
|---|---|---|
| VMI™ 7-step formula | ⚠️ Partial (in KLSE_QUALITY_SCORE + 35_Valuation) | **Adopted above** — use as Whale Investor pre-buy gate |
| Value-trap discrimination | ✅ Bargain screeners + 53_KC_Chong | Done |
| 4-method valuation convergence | ✅ File 35 | Add Khoo's "3-of-4 ≥20% discount" tiebreaker |
| Whale exit rules (4) | ⚠️ Scattered | **Adopted above** — codify in Whale bucket exits |
| Trend Retracement (Profit Snapper) | ⚠️ Not named as its own setup | **Add to V9 KLSE Swing scanner as a separate signal** |
| Casino math / positive expectancy | ✅ File 25 | Done |
| 1–2% risk rule | ✅ Beyond Insights anchor (file 58) | Done |
| Breakout-Within-Base | ✅ COIL signal + VCP cheat | Done |
| Impulse Pullback | ⚠️ Implicit in flags | Tag explicitly in trade journal |
| MVR (overbought fade) | ⚠️ Trimming only, not new shorts | Rule added above |
| BMR (Bollinger mean rev) | ✅ File 13 | Add ADX<20 filter |
| Capitulation setup | ⚠️ Concept in 55_TCK | Build 5-signal scoring card |
| GUNS intraday | ⚠️ US-side applicable | Limited KLSE relevance |
| PAM stop-hunting | ⚠️ Generic stops only | **Add 0.5–1 ATR offset rule to stop placement** |
| PAM force-strike bars | ✅ Maps to VSA file 08 | Add quick-decode card |
| DR1/UR1 = spring/upthrust | ✅ Wyckoff file 08 | Done — cross-reference naming |

---

## The Single Most Important Khoo Insight to Internalise

> *"Investing and trading are different jobs. The same chart can be a 'no' for the trader and a 'yes' for the investor — or the reverse. Pick which job you're doing on this trade BEFORE you click buy."*

This locks in the bucket discipline that prevents the most common retail mistake: a **swing trade that goes wrong and gets "promoted" to a long-term investment** to avoid taking the loss. Once a trade is tagged Profit Snapper, it lives and dies by Profit Snapper rules — never reclassified.

---

## Three Things to Operationalise From This File

1. **VMI™ 7-Step Whale gate** — add a "Whale Investor Pre-Buy" section to [PRE_TRADE_CHECKLIST.md](PRE_TRADE_CHECKLIST.md) for investing-bucket positions.
2. **Trend Retracement named setup** — add as an explicit signal in the V9 KLSE Swing scanner (separate from breakout-of-base), with the 7-criteria spec from Lessons 6–10 above.
3. **Stop-placement ATR offset** — update [06_Risk_Management_and_Position_Sizing.md](06_Risk_Management_and_Position_Sizing.md) and [12_Perfect_Entry_Exit.md](12_Perfect_Entry_Exit.md) so stops are placed **0.5–1 ATR below** the obvious swing low (PAM anti-stop-hunt rule), not AT it.

---

*See also:* [58_Beyond_Insights_SVS_Framework.md](58_Beyond_Insights_SVS_Framework.md) (sister academy file), [10_CAN_SLIM_KLSE.md](10_CAN_SLIM_KLSE.md), [25_Probability_Edge_Calculation.md](25_Probability_Edge_Calculation.md), [35_Stock_Valuation_Methods.md](35_Stock_Valuation_Methods.md), [42_Momentum_Masters_Advanced_VCP.md](42_Momentum_Masters_Advanced_VCP.md), [54_Tradeview_MONEY_Equation.md](54_Tradeview_MONEY_Equation.md), [DUAL_STYLE_PLAYBOOK.md](DUAL_STYLE_PLAYBOOK.md), [KLSE_QUALITY_SCORE.md](KLSE_QUALITY_SCORE.md)
