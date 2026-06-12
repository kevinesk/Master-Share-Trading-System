# Market Regime Filter — Marks + Dalio Identification Template
**When**: Refresh every Sunday during `WEEKLY_ROUTINE.md` Phase 3.
**Purpose**: Identify the macro regime in 2 dimensions (cycle position + liquidity phase) to filter strategy.

> **Rule**: Strategy follows regime. Don't run momentum strategy in fear/recession; don't run defensive in early recovery.

---

## 🎯 The Two-Axis Regime Map

| | **Liquidity Expanding** | **Liquidity Neutral** | **Liquidity Tight** |
|---|---|---|---|
| **Marks Score 1-3 (Fear)** | 🟢 BEST BUYING | 🟢 Selective Buying | 🟡 Cautious accumulation |
| **Marks Score 4-6 (Neutral)** | 🟢 Active deploy | 🟢 Normal trading | 🟡 Trim trim trim |
| **Marks Score 7-8 (Elevated)** | 🟡 Trim, hold runners | 🟡 Trim aggressively | 🔴 Defensive only |
| **Marks Score 9-10 (Euphoria)** | 🔴 Sell into strength | 🔴 Cash-up | 🔴 RAISE CASH 50%+ |

---

## 📊 PART 1 — Marks Cycle Score (1-10)

> *"What the market believes today is more important than what is true. And what it will believe tomorrow is what matters for tomorrow's prices."* — Howard Marks

### Score Each Component 1-10, then Average

| # | Component | 1 (Max Fear) | 5 (Neutral) | 10 (Euphoria) | This Week |
|---|---|---|---|---|---|
| 1 | **KLCI distance from 52W high** | >25% below | 5-15% below | At/above high | __ |
| 2 | **Days since last >2% red day** | <5 days | 15-30 days | >60 days | __ |
| 3 | **IPO oversubscription** | No IPOs | 2-5x typical | >20x retail | __ |
| 4 | **Margin financing growth y/y** | Negative | 5-10% | >25% | __ |
| 5 | **Media tone** | Panic / cover stories on losses | Mixed reporting | "It's different this time" euphoria | __ |
| 6 | **Retail participation** | Account openings flat/down | Normal | Account openings record high | __ |
| 7 | **Valuation (KLCI fwd P/E)** | <12x | 14-16x | >18x | __ |

**Sum**: ____  **Average**: ____ / 10 = **MARKS SCORE: ___**

### Marks Score Interpretation

| Score | Label | Sentiment | Action |
|---|---|---|---|
| 1-2 | 🟢 **MAX FEAR** | Capitulation, blood in streets | Buy quality at any price. Lifetime opportunity. |
| 3-4 | 🟢 **FEAR** | "Stocks are terrible" sentiment | Aggressive accumulation. Step in 3-5 positions. |
| 5-6 | 🟢 **NEUTRAL** | Balanced views | Normal trading. Best risk/reward zone. |
| 7-8 | 🟡 **ELEVATED** | "Stocks are great" headlines | Trim, trail stops, no new aggressive positions. |
| 9-10 | 🔴 **EUPHORIA** | "It's different this time" / "FOMO" | Raise cash to 30-50%. Sell into strength. |

---

## 📈 PART 2 — Dalio Liquidity Phase

> *"Cycles are caused by the expansion and contraction of credit. Watch credit, watch liquidity, watch debt service."* — Ray Dalio

### Check These 6 Liquidity Indicators

| # | Indicator | This Week | Direction |
|---|---|---|---|
| 1 | **OPR (BNM)** | ____% | Cut / Hold / Hike |
| 2 | **System loan growth y/y** | ____% | Rising / Stable / Falling |
| 3 | **M3 money supply growth y/y** | ____% | Rising / Stable / Falling |
| 4 | **10Y MGS yield** | ____% | Rising / Stable / Falling |
| 5 | **USD/MYR** | ____ | MYR firming / Stable / Weakening |
| 6 | **Fed Funds rate trajectory** | ____% | Cut / Hold / Hike |

### Liquidity Phase Decision

| Phase | Conditions | Action Bias |
|---|---|---|
| 🟢 **EXPANDING** | OPR cutting + loan growth rising + MYR firming + Fed cutting | Pro-risk, favor growth, longer-duration assets, REITs benefit |
| 🟡 **NEUTRAL** | Mixed signals, no clear direction | Balanced — Bucket A 30%, B 30%, Cash 40% |
| 🔴 **TIGHT** | OPR hiking + loan growth falling + MYR weakening + Fed hiking | Defensive, favor short-duration, cash, dividend stalwarts |

**This week's phase: ____________**

---

## 🧭 PART 3 — Cross-Reference to Action

### Step 1: Plot Today's Position on the 2-Axis Map

```
                    ┌──────────────────────────────────────────┐
                    │   EXPAND      NEUTRAL       TIGHT        │
                    ├──────────────────────────────────────────┤
   FEAR (1-3)       │   🟢🟢       🟢            🟡            │
   NEUTRAL (4-6)    │   🟢         🟢            🟡            │
   ELEVATED (7-8)   │   🟡         🟡            🔴            │
   EUPHORIA (9-10)  │   🔴         🔴            🔴            │
                    └──────────────────────────────────────────┘
```

**My current cell**: __________ (e.g. "Neutral × Expanding = 🟢")

### Step 2: Read the Strategy

| Cell | Bucket A (Momentum) | Bucket B (Yield) | Cash | New Position Size |
|---|---|---|---|---|
| 🟢🟢 (Fear × Expand) | 30-40% | 30-40% | 20-30% | Full 7% per name |
| 🟢 (Neutral × Expand) | 30-40% | 30-40% | 20-30% | Full 7% per name |
| 🟢 (Fear × Neutral) | 20% | 40% | 40% | 5-7% per name |
| 🟢 (Neutral × Neutral) | 30% | 30% | 40% | 5-7% per name |
| 🟡 (Elevated × Expand) | 20% | 30% | 50% | 3-5% per name |
| 🟡 (Fear × Tight) | 10% | 30% | 60% | 5% per name |
| 🟡 (Neutral × Tight) | 10% | 20% | 70% | 3-5% per name |
| 🟡 (Elevated × Neutral) | 10% | 20% | 70% | 3% per name |
| 🔴 (Elevated × Tight) | 0% | 20% | 80% | No new entries |
| 🔴 (Euphoria × any) | 0-10% | 10% | 80-90% | Defensive only |

### Step 3: Adjust Watchlist Construction

| Regime | Favored Sectors | Avoid Sectors |
|---|---|---|
| 🟢🟢 Fear+Expand | Banking, Construction, Property, Tech | Defensive overweight (already discounted) |
| 🟢 Neutral+Expand | Tech, Consumer, Industrial, Healthcare | Energy if oil falling |
| 🟡 Elevated | Healthcare, Consumer Staples, Telco, REIT | Property, Tech (late-cycle) |
| 🔴 Euphoria/Tight | Cash, T-bills, Gold | All cyclicals |

---

## 📊 12-Week Regime History

| Week | Marks | Liquidity | Cell | Cash % | Notes |
|---|---|---|---|---|---|
| W-11 | __ | __ | __ | __% | |
| W-10 | __ | __ | __ | __% | |
| W-9 | __ | __ | __ | __% | |
| W-8 | __ | __ | __ | __% | |
| W-7 | __ | __ | __ | __% | |
| W-6 | __ | __ | __ | __% | |
| W-5 | __ | __ | __ | __% | |
| W-4 | __ | __ | __ | __% | |
| W-3 | __ | __ | __ | __% | |
| W-2 | __ | __ | __ | __% | |
| W-1 | __ | __ | __ | __% | |
| **This Wk** | __ | __ | __ | __% | |

Watch for **regime transitions**: when you see 3 consecutive weeks of shifting Marks score or Liquidity phase, that's the *signal* to materially change allocation.

---

## ⚠️ Regime Transition Warning Signs

### Bull → Bear Warnings
- [ ] KLCI breaks 50D MA on volume
- [ ] Sector breadth drops from >60% to <50% in 4 weeks
- [ ] Marks score moves 5 → 8 within 8 weeks
- [ ] OPR starts hiking after 12+ month hold
- [ ] MYR weakens >5% in a month
- [ ] Foreign net selling >RM 2bn/week for 3 weeks

**Action**: If 4+ of these tick = move to 🟡 cell, cut new entries 50%, trim losers.

### Bear → Bull Warnings (Reverse — Buy Signals)
- [ ] KLCI reclaims 50D MA on volume
- [ ] Sector breadth recovers from <30% to >50%
- [ ] Marks score drops to 1-3 with capitulation candle
- [ ] OPR begins cutting cycle
- [ ] MYR stabilizes / starts firming
- [ ] Foreign net buying for 3+ consecutive weeks

**Action**: If 4+ of these tick = step in, accumulate quality, 6-month accumulation plan.

---

## 🇲🇾 KLSE-Specific Regime Anchors

### Bursa-specific signs you've moved into 🟢 fear zone:
- Glove sector at multi-year lows
- Property developer P/B < 0.5
- Bank P/B < 0.8
- Plantation P/E < 10x

### Bursa-specific signs you've moved into 🔴 euphoria zone:
- Penny stocks rallying 50%+ in a week
- IPO oversubscriptions >50x
- Margin financing growth >25% y/y
- Forwards "limit-up" daily on multiple counters
- TikTok/Twitter retail FOMO threads going viral
- Magazine covers proclaim "KLSE comeback"

---

## 🎯 The Big Idea

> **Strategy is what you do in a given regime. Regime is what the market is giving you.**
> 90% of trader losses come from running the wrong strategy in the wrong regime.
> Identify the cell. Adjust the buckets. Filter the watchlist. Compound.

**Update this file every Sunday. Cross-reference with `MACRO_DASHBOARD.md` and `SECTOR_BREADTH_TRACKER.md`. They form the macro trinity.**
