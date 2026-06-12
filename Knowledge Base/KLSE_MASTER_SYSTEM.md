# KLSE Master Trading System (v1.0)
**Date authored:** 2026-05-30
**Owner:** Kevin (KLSE, starting capital basis RM 30,000, MooMoo + TradingView)
**Status:** The single operating doc. Everything else in this KB is a reference for this system.

> **The principle**: Profitability comes from **edge × discipline × survival**. Edge alone loses to bad discipline. Discipline alone loses to no edge. Both lose to ruin. This document maximises all three.

---

## 0. WHY THIS DOCUMENT EXISTS

The KB now has 59 files + 17 operational templates + 4 active Pine scripts. That is too much to navigate mid-trade. This file is the single executable system that:

1. **Decides what to trade** (regime + bucket + stock selection)
2. **Decides how much** (sizing math, never violated)
3. **Decides when in / out** (entry triggers, stop placement, exit ladder)
4. **Decides when to do nothing** (the most under-used skill)

Everything below is a rule. Theory lives in files 01–59; this document only states the rules and links to the file when you need the "why."

---

## 1. THE FOUR ANCHOR PRINCIPLES (non-negotiable)

| # | Principle | Source | Why |
|---|---|---|---|
| 1 | **Capital preservation > return maximisation** | Memory; [06](06_Risk_Management_and_Position_Sizing.md); [55](55_Tan_Chong_Koay_Never_Fully_Invested.md) | A 50% loss requires 100% gain to recover. Survival compounds; aggression doesn't. |
| 2 | **System over conviction** | [58_Beyond_Insights_SVS_Framework.md](58_Beyond_Insights_SVS_Framework.md); [59_Adam_Khoo_Piranha_Profits.md](59_Adam_Khoo_Piranha_Profits.md) | Conviction is hindsight in disguise. Rules survive bear markets; convictions don't. |
| 3 | **Buckets don't bleed** | [59](59_Adam_Khoo_Piranha_Profits.md) Khoo 2-track | A swing trade gone wrong is NEVER reclassified to "long-term hold". Bucket at entry = bucket at exit. |
| 4 | **Cash is a position** | [55](55_Tan_Chong_Koay_Never_Fully_Invested.md) Tan Chong Koay | Sitting out is an active choice. Forced deployment loses more than empty seats. |

If any future "improvement" violates one of these four, the improvement is rejected.

---

## 2. THE THREE-BUCKET PORTFOLIO

Forget single-style trading. KLSE rewards a **3-bucket portfolio** matched to its cycle structure.

| Bucket | % of capital (default) | Style | Hold | Entry source | KB anchor |
|---|---|---|---|---|---|
| **A — Momentum / Leaders** | 40% | Stage 2 breakouts, VCP, Trend Retracement | 2–12 weeks | V10 Swing Sniper + KLSE MSS v6 + V8 Sniper | [02](02_Minervini_SEPA_KLSE.md), [10](10_CAN_SLIM_KLSE.md), [42](42_Momentum_Masters_Advanced_VCP.md), [59](59_Adam_Khoo_Piranha_Profits.md) |
| **B — Value-Bargain** | 25% | Quality at discount during weakness | 6 weeks – 18 months | [KLSE Bargain Hunting Screeners](KLSE_BARGAIN_HUNTING_SCREENERS.md) | [53](53_KC_Chong_Bursa_Value_Investing.md), [57](57_Cold_Eye_Local_Value_Compounding.md), bargain memory |
| **C — Whale / Yield Compound** | 15% | VMI™ 7-step gate passes; high-quality compounders | 1–5 years | Whale Investor pre-buy gate ([PRE_TRADE_CHECKLIST](PRE_TRADE_CHECKLIST.md)) | [46](46_Lynch_Six_Categories.md), [59](59_Adam_Khoo_Piranha_Profits.md), [KLSE_QUALITY_SCORE](KLSE_QUALITY_SCORE.md) |
| **D — Cash / T-bills floor** | **20% MINIMUM** | Capital preservation reserve | Always | — | Anchor principle 4 |

**Bucket A + B + C ≤ 80%. Always. No exceptions.**

### Bucket-mix shift by macro regime (auto-rebalance):

| Macro state (see §3) | A | B | C | Cash | Logic |
|---|---|---|---|---|---|
| **Strong bull** (KLCI > EMA50, breadth >70%, McClellan>+50) | **55%** | 15% | 10% | 20% | Press momentum, scale back bargain-hunting |
| **Neutral / chop** (mixed signals) | 40% | 25% | 15% | 20% | Default mix |
| **Weak / corrective** (KLCI < EMA50 but >EMA200, breadth 40–60%) | 20% | 35% | 15% | 30% | Quality + bargain bias, raise cash |
| **Bear** (KLCI < EMA200, breadth <30%, McClellan<-50) | 5% | 15% | 10% | **70%** | Capitulation watch only; reserve dry powder per [55](55_Tan_Chong_Koay_Never_Fully_Invested.md) |
| **Capitulation event** (panic washout fires per [59](59_Adam_Khoo_Piranha_Profits.md) signal stack) | Deploy bear cash into B+C only | up to 35% B | up to 25% C | 40% | "The cash you preserved gets deployed" |

The bucket weights are **targets, not constraints**. You can be 0% in any bucket if no qualified candidate exists. You can NEVER be below the cash floor.

---

## 3. THE 7-LIGHT MACRO REGIME LIGHT BOARD

Run every **Sunday** during [WEEKLY_ROUTINE.md](WEEKLY_ROUTINE.md). Updates in [MACRO_DASHBOARD.md](MACRO_DASHBOARD.md). Scoring:

| # | Light | Green (+1) | Yellow (0) | Red (−1) | Source |
|---|---|---|---|---|---|
| 1 | **KLCI trend** | > EMA50 & EMA200, all sloping up | Mixed | < EMA200 or EMA50 < EMA200 | [02](02_Minervini_SEPA_KLSE.md) |
| 2 | **Dow / S&P trend** | > EMA50, RSI 50–70 | Mixed | < EMA200 | [20](20_Global_Macro_for_KLSE.md) |
| 3 | **McClellan KLSE** | > +50 | −50 to +50 | < −50 | [26](26_Market_Breadth_Sentiment.md) |
| 4 | **% KLCI stocks > EMA50** | > 60% | 40–60% | < 30% | [26](26_Market_Breadth_Sentiment.md), [50](50_Morris_Sector_Breadth_Indicators.md) |
| 5 | **USD/MYR** | Firming (4.20–4.40) | Stable | Weakening rapidly | [32](32_Intermarket_Analysis.md), [51](51_Pauline_Yong_Malaysian_Macro_Execution.md) |
| 6 | **Distribution days (last 25 sessions)** | ≤ 2 | 3–4 | ≥ 5 | [10](10_CAN_SLIM_KLSE.md) |
| 7 | **Foreign net flow (5-day)** | Net buying | Mixed | Net selling 3+ days | [23](23_Local_Institutional_Investors.md), [26](26_Market_Breadth_Sentiment.md) |

**Score → regime:**

| Sum | Regime | Action |
|---|---|---|
| +5 to +7 | Strong bull | Press momentum (Bucket A shift to 55%) |
| +1 to +4 | Neutral / chop | Default mix |
| −2 to 0 | Weak / corrective | Shift to value, raise cash |
| −5 to −3 | Bear | Defence mode |
| −7 to −6 | Crisis | Cash 70%+; watch for capitulation |

**Override**: Light 1 (KLCI trend) red = no new Bucket A entries. Period. Even if score is positive due to other lights.

---

## 4. ENTRY DECISION FLOW (per trade)

```
┌─────────────────────────────────────────────────────────┐
│ Step 0: Which BUCKET is this trade?                     │
│         A=Momentum, B=Bargain, C=Whale                  │
│         → Lock the bucket. No reclassification later.  │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ Step 1: Macro pass?                                     │
│   Bucket A: requires regime ≥ Neutral                  │
│   Bucket B: any regime except Crisis                   │
│   Bucket C: any regime (long horizon absorbs cycle)    │
│   → If fail: STOP. Cash is the trade.                  │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ Step 2: SVS Triple-Check (Beyond Insights, file 58)    │
│   Systematic + Versatile + Safe — ALL THREE 🟢         │
│   → If any 🔴: STOP                                     │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ Step 3: Bucket-specific stock selection (see §5)       │
│   → Output: single ticker + entry price + stop         │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ Step 4: PRE_TRADE_CHECKLIST 12 gates                   │
│   (Whale gate first if Bucket C)                       │
│   → All 12 🟢 = proceed; any 🔴 = STOP                  │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ Step 5: POSITION_SIZE_CALCULATOR                        │
│   risk% per §6, ATR-offset stop, cap at 10% portfolio  │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ Step 6: Execute → log in TRADE_JOURNAL                 │
│   Tag bucket. Tag emotion. Set broker stop.            │
└─────────────────────────────────────────────────────────┘
```

---

## 5. STOCK SELECTION BY BUCKET

### Bucket A — Momentum (40%)

**Sources (in order of priority):**
1. V10 Swing Sniper EXECUTE NOW alert (highest priority — all signals aligned + coil released)
2. V10 Swing Sniper SWING BUY alert
3. V10 Khoo Trend Retracement BUY (Profit Snapper pullback to EMA20/50)
4. KLSE MSS v6 COIL pre-surge signal
5. Manual scan: Pro Quant Desk v9 dashboard top of heatmap + Trend Template 8/8

**Must clear:**
- Trend Template ≥ 7/8 (rare: 6/8 with elite RS rating)
- ADV ≥ RM 500K (liquidity floor for KLSE)
- Not in 4th+ stage base (count bases per [39](39_ONeil_Greatest_Winners_Templates.md))
- Sector light in [SECTOR_BREADTH_TRACKER.md](SECTOR_BREADTH_TRACKER.md) is Green or improving

**Reject if:**
- Recent gap-down on volume in last 5 sessions
- Insider selling cluster (per [56](56_Tong_Kooi_Ong_Corporate_Insider.md))
- News-driven pop without underlying base ([54](54_Tradeview_MONEY_Equation.md) pump-dump watch)

### Bucket B — Value-Bargain (25%)

**Sources:**
1. [KLSE_BARGAIN_HUNTING_SCREENERS.md](KLSE_BARGAIN_HUNTING_SCREENERS.md) weekly run
2. Quality-Score ≥ 35/50 stocks within 15% of 52-week low

**Must clear (the falling-knife filter — non-negotiable for bargain bucket):**
1. Quality Score ≥ 35/50 ([KLSE_QUALITY_SCORE.md](KLSE_QUALITY_SCORE.md))
2. ROE ≥ 12% for ≥3 of last 5 years
3. Net cash OR D/E ≤ 0.5
4. **NO** Cold Eye value-trap signs ([53](53_KC_Chong_Bursa_Value_Investing.md) 7 warnings)
5. Stock has stopped making lower lows for ≥3 weeks (basing, not falling)
6. Either: (a) on EMA200 with bullish reversal candle, OR (b) at prior multi-year support tested ≥2× before

**Why this list matters:** the bargain bucket is where retail accounts die. The 6 filters above are the difference between "buying quality cheap" and "catching a falling knife."

### Bucket C — Whale / Yield Compound (15%)

**The gate:** Whale Investor pre-buy gate at top of [PRE_TRADE_CHECKLIST.md](PRE_TRADE_CHECKLIST.md) — VMI™ 7-step, ≥6/7 to pass.

**Names to watch:** the historical KLSE compounders — banks, REITs, defensive consumer, GLC quality (PBBank, Maybank, Tenaga, Genting Plantation, Nestle MY, F&N, IGB REIT, Sunway REIT). Not as "always buy" but as the persistent watchlist; entry only on VMI pass.

**Exit triggers (Khoo Whale, codified):**
1. 2 consecutive quarters EPS decline → review
2. Weekly close < EMA200 held 4 weeks → exit
3. Original thesis broken (moat erosion, regulatory shock, accounting concern) → exit immediately
4. Materially better VMI candidate emerges → replace

---

## 6. POSITION SIZING — THE MATH

### The dynamic 1%/2% rule (combines BI + 06_Risk + Khoo)

| Macro regime | Per-trade risk | Max position | Notes |
|---|---|---|---|
| Strong bull | **2%** | 10% portfolio | Press momentum |
| Neutral | 1.5% | 10% portfolio | Default |
| Weak / corrective | 1% | 8% portfolio | Tighten |
| Bear | 0.5% (only for capitulation entries) | 5% portfolio | Reserve cash |
| Crisis | 0% (no new entries) | — | Cash floor protects |

### Position size formula

```
1. ATR(14) = current 14-day average true range
2. ATR_offset = 0.7 × ATR(14)  (use 0.5× for low-vol, 1.0× for high-vol)
3. Stop_price = (logical support) − ATR_offset  ← PAM anti-stop-hunt rule
4. Risk_per_share = Entry_price − Stop_price
5. Risk_budget_RM = Portfolio × Risk%_from_table_above
6. Shares_by_risk = Risk_budget_RM / Risk_per_share
7. Shares_by_cap = (Portfolio × 0.10) / Entry_price   ← 10% hard cap
8. Final_shares = MIN(Shares_by_risk, Shares_by_cap), round down to 100 lot

Validate: Final_shares × Risk_per_share ≤ Risk_budget_RM ✓
Validate: Final_shares × Entry_price ≤ Portfolio × 0.10 ✓
```

### Portfolio heat ceiling

**Σ(open risk per all positions) ≤ 5% of portfolio at any time.**

If 5 positions each risking 1% are open, no new entries until one closes or a stop tightens. This stops you from waking up to a coordinated drawdown.

---

## 7. EXIT LADDER (one ladder, all buckets)

### Stop progression — universal

| Trade state | Stop level |
|---|---|
| Entry | Initial ATR-offset stop (§6 step 3) |
| +5% gain | Tighten to entry − 2% (de-risk) |
| +10% gain | Move to entry (breakeven) — this trade can no longer lose |
| +15% gain | Trail under EMA21 (daily close) |
| +25% gain | Trail under EMA10 (daily close) |
| +35% gain | Trail under EMA10 + climax-top watch ([12](12_Perfect_Entry_Exit.md)) |

### Tranche exit (default for Bucket A; optional for B; rare for C)

| Tranche | Trigger | % sold |
|---|---|---|
| T1 | +15% OR first resistance (whichever first) | 1/3 |
| T2 | +25–30% OR 2× ATR extension above pivot | 1/3 |
| T3 | Trail per stop progression above; no fixed target | 1/3 |

### Hard "exit immediately" triggers (apply to ALL buckets)

1. Initial stop hit — no hesitation
2. Distribution day cluster on the stock (3 of last 5 sessions: down on volume > 1.5× avg)
3. Daily close 7% below pivot from a fresh breakout (failed breakout = exit)
4. Macro regime drops to Bear (§3) — close half of all Bucket A positions, tighten remainder to breakeven
5. Bucket-specific thesis break (Whale: see §5 Bucket C; Bargain: stops making lower lows)

---

## 8. THE OPERATING CALENDAR

### Daily ([DAILY_ROUTINE.md](DAILY_ROUTINE.md))
- **08:00–08:55**: Macro sweep + event blackout check (Beyond Insights rule, §2b in Daily Routine) + position review + watchlist refresh + write daily plan
- **09:00–09:30**: Observe only — no trades
- **09:30–12:30**: Triggered entries, manage profits
- **12:30–14:30**: Step away — Bursa is closed; YOU must close too
- **14:30–17:00**: Re-engage, manage, no chasing in final 30 min
- **17:00–18:00**: Journal, EOD screener, plan tomorrow

### Weekly ([WEEKLY_ROUTINE.md](WEEKLY_ROUTINE.md))
- **Sunday 2.5 hrs**: 7-light macro update → [MACRO_DASHBOARD.md](MACRO_DASHBOARD.md), sector breadth → [SECTOR_BREADTH_TRACKER.md](SECTOR_BREADTH_TRACKER.md), bucket rebalance check, top-down review per [TOP_DOWN_FRAMEWORK.md](TOP_DOWN_FRAMEWORK.md), build the week's watchlist (5 names per bucket max)

### Monthly
- Bucket allocation review: are we within ±5% of regime-default mix?
- Performance review: win rate, average R, expectancy ([24](24_Trading_Statistics_Essentials.md))
- Emotion-tag pattern check: any losing-trade cluster on FOMO/revenge? → apply 24h cooling-off rule
- One-page month summary into [TRADE_JOURNAL.md](TRADE_JOURNAL.md)

### Quarterly
- Drawdown review: any drawdown > 8% → cut all sizes in half for next 30 days
- KB drift check: any rule violated more than twice? → either revise the rule (with rationale) or institute a tighter check

### Annual
- Full system audit: does each rule still pay rent? Remove rules that haven't fired in 12 months. Add rules to plug holes from the year's losses.

---

## 9. CIRCUIT BREAKERS (drawdown defence)

Capital preservation is anchor principle 1. The circuit breakers below override every other rule.

| Drawdown from peak | Action |
|---|---|
| −3% | Review: any rule violated? Note in journal. |
| −5% | Cut all new-entry sizing by **50%** for next 10 trades |
| −8% | Stop all new entries for 1 full trading week. Manage existing only. |
| −12% | **Hard stop**: close all Bucket A. Hold only Bucket C (whales) and cash. Re-enter only after macro regime returns to Neutral+. |
| −20% | System failure. Stop trading for 30 days. Audit every losing trade. Do not return without written rule changes. |

These are not suggestions. The −12% level is where retail accounts spiral; the rule above is the seatbelt.

---

## 10. THE FAILURE MODES TO WATCH (Kevin-specific)

From the journal record and KLSE retail patterns, the recurring failure modes are:

| Failure mode | Source incident | Guard rule |
|---|---|---|
| **Oversizing** | RHB trade 2026-05-20: 32.9% vs 10% cap | Calculate max units BEFORE clicking buy (PRE_TRADE Gate 9) |
| **Bucket bleed** | Hypothetical: swing trade going wrong "becomes" long-term hold | Tag bucket at entry; locked. Anchor principle 3. |
| **Anticipating breakouts** | Buying base before pivot break ("I'll get a better price") | PRE_TRADE Gate 7 requires trigger met within 1% |
| **Falling-knife in B-bucket** | Buying quality "cheap" that becomes cheaper | §5 Bucket B 6-filter list; no exceptions |
| **FOMO post-loss** | Revenge trading after a stop hit | Gate 11 anti-FOMO + emotion tags in journal + 24h cooling rule |
| **Macro denial** | Holding Stage 2 longs after KLCI turns Stage 4 | §7 hard trigger #4 + §9 circuit breakers |
| **Event surprise** | Position into FOMC / BNM / earnings without size reduction | Daily Step 2b event blackout check |
| **Stop-hunt sweep** | Stop placed AT obvious swing low gets cleared | §6 ATR-offset rule + PRE_TRADE Gate 8 |

Each guard rule above is already live somewhere in the system. This table is the index of which rule guards which failure.

---

## 11. THE PERFORMANCE TARGETS (realistic, KLSE-tuned)

| Metric | Target Year 1 | Target Year 3 | Notes |
|---|---|---|---|
| Win rate | 45–55% | 50–60% | Don't chase higher — payoff matters more |
| Average R (winner) | +2.0R | +2.5R | T2 = +2R; T3 trail adds 0.5R |
| Average R (loser) | −0.9R | −0.8R | Stops fire cleanly; not −1.5R |
| Expectancy per trade | +0.4R | +0.7R | (Win% × WinR) − (Loss% × LossR) |
| Max drawdown | < 12% | < 10% | Circuit breakers in §9 |
| Trades per month | 4–8 | 6–10 | Quality, not turnover |
| Annual return | +15 to +25% | +20 to +35% | Net of costs; KLSE long-run real return is ~6%, so this is 2.5–5× index |
| KLCI beta | < 0.7 | < 0.7 | We compound, not surf |

These are targets, not promises. Anchor principle 1 says: hitting 0% in a bear year by holding cash is a WIN.

---

## 12. THE ONE-PAGE DAILY DECISION CARD

Print this. Tape to monitor.

```
┌──────────────────────────────────────────────────────────────┐
│  KLSE MASTER SYSTEM — DAILY DECISION CARD                    │
├──────────────────────────────────────────────────────────────┤
│  PRE-MARKET                                                  │
│  [ ] Macro 7-light score: ____ → regime: ____________        │
│  [ ] Event blackout next 24h?   YES / NO                     │
│  [ ] Current drawdown from peak: ____%                       │
│  [ ] Circuit breaker active?    ____________                 │
│  [ ] Bucket weights vs target:  A__% B__% C__% Cash__%       │
├──────────────────────────────────────────────────────────────┤
│  PER-TRADE                                                   │
│  Bucket (lock):  A / B / C                                   │
│  Ticker:         ____________                                │
│  Entry:          RM ______    ATR(14):  ______               │
│  Stop (logical): RM ______    Offset:   ______               │
│  Stop (broker):  RM ______  ← logical − 0.7×ATR              │
│  T1 / T2:        RM ______ / RM ______                       │
│  Net R:R:        ______ : 1  (must be ≥ 2:1)                 │
│  Risk %:         ______  (per §6 table)                      │
│  Size (units):   ______  (MIN of risk & cap)                 │
│  Portfolio %:    ______  (≤ 10%)                             │
│  Open risk Σ:    ______  (≤ 5% across all positions)         │
│  SVS check:      🟢 S  🟢 V  🟢 S                             │
│  12 gates:       _______/12 green                            │
│  Whale gate (if C): _______/7                                │
│  Emotion (pre):  calm/confident/fomo/revenge/fearful/bored   │
├──────────────────────────────────────────────────────────────┤
│  POST-TRADE / EOD                                            │
│  [ ] Stop placed in broker                                   │
│  [ ] Logged in TRADE_JOURNAL with all fields                 │
│  [ ] Mental state 1-10: ____                                 │
│  [ ] Followed plan today? Y / N — if N, why?                 │
└──────────────────────────────────────────────────────────────┘
```

---

## 13. WHAT THIS SYSTEM EXPLICITLY DOES NOT DO

Saying no to things is part of the edge.

1. **No leverage / no margin** until 24 months of profitable journal at consistent positive expectancy
2. **No naked options / no shorts** on KLSE (limited access + asymmetric tail risk)
3. **No intraday trading** during weak / bear / crisis regimes (zero-overnight rule from Beyond Insights is for normal regimes)
4. **No averaging down**: scaling in is allowed ONLY after a position is profitable and the trend strengthens (Khoo pyramiding rule)
5. **No "just this once" exceptions** to size, stop, or bucket rules
6. **No tips, no rumours, no Telegram groups** as a primary entry source
7. **No new strategies bolted on** without 30 trades of paper-test data
8. **No checking P&L during the session** more than 4 times per day (per Daily Routine)

---

## 14. THE 10-LINE EXECUTIVE SUMMARY

1. Three buckets: Momentum 40 / Value-Bargain 25 / Whale 15 / Cash floor 20 minimum.
2. Bucket mix shifts with the 7-light macro score (§3); cash rises to 70% in bear.
3. SVS triple-check + macro gate + bucket-specific filters + 12-gate PRE_TRADE checklist + (Whale gate if C).
4. Sizing: 0.5%–2% risk per trade by regime, ATR-offset stop (PAM rule), 10% position cap, 5% portfolio heat ceiling.
5. Exit ladder: tighten at +5, breakeven at +10, EMA21 trail at +15, EMA10 trail at +25.
6. Hard exits: stop hit, distribution cluster, failed breakout, regime turn to Bear, bucket thesis broken.
7. Daily Routine + Weekly Routine + monthly emotion-pattern check + quarterly drawdown review + annual audit.
8. Circuit breakers at −5%, −8%, −12%, −20% drawdown — non-negotiable.
9. Failure-mode index (§10) maps each Kevin-specific risk to a guard rule.
10. No leverage, no naked options, no averaging down, no exception trades. Ever.

---

## APPENDIX A — FILE LOOKUP BY DECISION NEED

| When you need to... | Open... |
|---|---|
| Score macro regime | [MACRO_DASHBOARD.md](MACRO_DASHBOARD.md), [03](03_KLSE_Sectors_and_Macro.md), [20](20_Global_Macro_for_KLSE.md), [47](47_Dalio_Debt_Crises_Liquidity.md) |
| Score sectors | [SECTOR_BREADTH_TRACKER.md](SECTOR_BREADTH_TRACKER.md), [16](16_Sector_Playbooks.md), [44](44_Weinstein_Industry_Stage_Analysis.md), [45](45_Stovall_Sector_Rotation_Model.md), [49](49_Cane_Sector_Rotation_Mechanics.md) |
| Score stock quality | [KLSE_QUALITY_SCORE.md](KLSE_QUALITY_SCORE.md), [29](29_Reading_Financial_Statements.md), [35](35_Stock_Valuation_Methods.md), [53](53_KC_Chong_Bursa_Value_Investing.md), [57](57_Cold_Eye_Local_Value_Compounding.md) |
| Confirm momentum setup | [02](02_Minervini_SEPA_KLSE.md), [04](04_VCP_Pattern_Playbook.md), [10](10_CAN_SLIM_KLSE.md), [39](39_ONeil_Greatest_Winners_Templates.md), [42](42_Momentum_Masters_Advanced_VCP.md) |
| Run bargain screen | [KLSE_BARGAIN_HUNTING_SCREENERS.md](KLSE_BARGAIN_HUNTING_SCREENERS.md) |
| Size a position | [POSITION_SIZE_CALCULATOR.md](POSITION_SIZE_CALCULATOR.md), [06](06_Risk_Management_and_Position_Sizing.md), [25](25_Probability_Edge_Calculation.md) |
| Place a stop | [06](06_Risk_Management_and_Position_Sizing.md) ATR-offset rule, [12](12_Perfect_Entry_Exit.md) |
| Handle psychology | [09](09_Trading_Psychology.md), [33](33_Fear_FOMO_Confidence_Mastery.md), [STICKY_NOTE_Anti_FOMO.md](STICKY_NOTE_Anti_FOMO.md), [58](58_Beyond_Insights_SVS_Framework.md) |
| Decide an exit | [12](12_Perfect_Entry_Exit.md), [38](38_Pit_Bull_Schwartz_Method.md), [55](55_Tan_Chong_Koay_Never_Fully_Invested.md) |
| Audit performance | [24](24_Trading_Statistics_Essentials.md), [25](25_Probability_Edge_Calculation.md), [14](14_Backtesting_Framework.md), [TRADE_JOURNAL.md](TRADE_JOURNAL.md) |
| Pre-buy gate (Whale) | [PRE_TRADE_CHECKLIST.md](PRE_TRADE_CHECKLIST.md) top section, [59](59_Adam_Khoo_Piranha_Profits.md) |
| Indicator on TradingView | `KLSE Momentum Swing Screener/V10 Swing Sniper (KLSE).pine`, `Pro Quant Desk (KLSE)/...v9.pine`, `Minervini VCP + SmartMCDX Backtest/...v9.pine` |

---

## APPENDIX B — VERSION HISTORY

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-05-30 | Initial system spec synthesising KB files 01–59 + operational templates + V10 indicators. Three-bucket portfolio, 7-light regime, dynamic 0.5–2% sizing, ATR-offset stops, SVS + VMI gates, circuit breakers, daily decision card. |

---

**This document supersedes any conflicting rule elsewhere in the KB.** When a rule in files 01–59 conflicts with this document, this document wins. The component files remain authoritative on the *why*; this document is authoritative on the *what to do*.

*Operating principle*: read this once a month. Live by it daily. Update it quarterly with what reality teaches.
