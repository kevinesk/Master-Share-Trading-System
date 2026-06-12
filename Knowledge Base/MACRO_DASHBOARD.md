# Macro Dashboard — Weekly Fill-In
**When**: Refresh every Sunday during `WEEKLY_ROUTINE.md`
**Purpose**: One-glance read of the macro/breadth/sentiment regime to filter all trades.

> **Rule**: If 4+ metrics are 🔴, raise cash to 30-50%. If 5+ are 🟢, deploy aggressively. Default = balanced.

---

## 📊 The 7-Metric Dashboard

Fill in every Sunday. Keep a 12-week rolling history.

### Week of: 2026-MM-DD

| # | Metric | Value | Threshold | Status |
|---|---|---|---|---|
| 1 | **KLCI vs 200D MA** | ___ pts | Above = 🟢, Below = 🔴 | ___ |
| 2 | **KLCI 50D vs 200D** | ___ | 50D > 200D = 🟢, 50D < 200D = 🔴 | ___ |
| 3 | **OPR trajectory** | ___% | Cutting/Stable = 🟢, Hiking = 🔴 | ___ |
| 4 | **USD/MYR** | ___ | Firming (<4.40) = 🟢, Weakening (>4.60) = 🔴 | ___ |
| 5 | **KLCI vs Dow Jones (RS)** | ___ | KLCI outperforming = 🟢, Lagging badly = 🔴 | ___ |
| 6 | **Sector A-D line** (top 5 sectors avg) | ___ | Rising = 🟢, Falling = 🔴 | ___ |
| 7 | **Marks Cycle Score** | ___/10 | 3-7 = 🟢, <3 or >8 = 🔴 | ___ |

**Score**: ___ 🟢 / ___ 🔴

---

## 🚦 Score-to-Action Map

| 🟢 Count | Regime | Action |
|---|---|---|
| 6-7 🟢 | **Confirmed Bull** | Bucket A 40-50%, B 30-40%, Cash 10-20%. Full position sizes. |
| 4-5 🟢 | **Constructive** | Bucket A 30-40%, B 30-40%, Cash 20-30%. Normal sizes. |
| 3 🟢 / 4 🔴 | **Mixed** | Bucket A 20%, B 40%, Cash 40%. Half sizes only. |
| 0-2 🟢 | **Risk-Off** | Bucket A 0-10%, B 20-30%, Cash 60-80%. No new longs. |

---

## 📋 Metric Definitions & Data Sources

### Metric 1 — KLCI vs 200D MA
- **Data source**: TradingView KLSE:KLCI chart with 200-day MA
- **Why it matters**: Stage filter. Bull markets live above 200D; bears below.

### Metric 2 — KLCI 50D vs 200D MA
- **Data source**: Same chart
- **Why it matters**: Golden cross (50 > 200) = bull; death cross = bear

### Metric 3 — OPR Trajectory
- **Data source**: bnm.gov.my → Monetary Policy
- **Latest values to track**:
  - Current OPR: ___%
  - Last change: __________
  - Next MPC date: __________
  - Market expectation: cut/hold/hike

### Metric 4 — USD/MYR
- **Data source**: TradingView FX:USDMYR
- **Bull/bear thresholds**:
  - Below 4.30 = strong MYR (very 🟢)
  - 4.30-4.50 = neutral (🟢)
  - 4.50-4.70 = weakening (🟡)
  - Above 4.70 = stress (🔴)

### Metric 5 — KLCI vs Dow RS
- **Calculation**: KLCI weekly % change − Dow weekly % change (last 13 weeks rolling)
- **Why**: Foreign flow + relative attractiveness
- **🟢 if**: KLCI outperforming Dow over rolling 13 weeks

### Metric 6 — Sector A-D Line
- **Manual calc**: Count sectors making new 4-week highs minus making new 4-week lows
- **Source**: Bursa sector index chart review (12 sectors)
- **🟢 if**: A-D line rising over last 4 weeks

### Metric 7 — Marks Cycle Score
- **Self-assessment** based on:
  - Media headlines tone
  - Margin financing growth (BNM data)
  - IPO oversubscription multiples
  - KLCI distance from 52W high
  - Days since last >2% red day
- **Scale**: 1 = max fear, 10 = max euphoria

---

## 📈 12-Week Rolling History Table

| Week | 🟢 Count | Regime | KLCI Close | OPR | USD/MYR | Action Taken |
|---|---|---|---|---|---|---|
| Week 1 | | | | | | |
| Week 2 | | | | | | |
| Week 3 | | | | | | |
| Week 4 | | | | | | |
| Week 5 | | | | | | |
| Week 6 | | | | | | |
| Week 7 | | | | | | |
| Week 8 | | | | | | |
| Week 9 | | | | | | |
| Week 10 | | | | | | |
| Week 11 | | | | | | |
| Week 12 | | | | | | |

**Use this to detect regime changes early.** A trend from 6 🟢 → 4 🟢 → 2 🟢 over 3 weeks = warning. Tighten stops, raise cash, no new aggressive entries.

---

## 🌐 Extended Indicators (Optional Deeper Read)

If you have time, add these to refine the signal:

### Credit & Liquidity (Dalio layer)
- BNM M3 money supply growth y/y: ____%
- System loan growth y/y: ____%
- 10Y MGS yield: ____%
- Yield curve slope (10Y - 3M): ____ bps (positive = healthy)
- Corporate bond spreads: tight / widening?

### Sector Breadth (Morris layer)
For each major sector, calculate "% stocks above 50D MA":
- KLFIN: ___%
- KLCON: ___%
- KLPRP: ___%
- KLTEC: ___%
- KLHC: ___%
- KLPLT: ___%

Threshold: ≥60% = 🟢 / 40-60% = 🟡 / <40% = 🔴

### Capital Cycle (Chancellor layer)
For 3 sectors you trade, ask:
- "Is supply expanding (capex/IPOs) or contracting?"
- Expanding capex = late-cycle warning
- Contracting capex = early-cycle opportunity

---

## 🇲🇾 KLSE-Specific Macro Signals (Pauline Yong layer)

Add to your weekly check:

- [ ] **Foreign net buy/sell** (weekly Bursa data)
  - Net buying = 🟢
  - Heavy selling (>RM 1bn/week) = 🔴
- [ ] **EPF/PNB activity** (announced or rumored buy programs)
  - Active = 🟢 support
- [ ] **Brent crude trend** (oil & gas + plantation read)
- [ ] **CPO (palm oil) trend** (plantation read)
- [ ] **Glove ASP** (rubber gloves sector)
- [ ] **Property launches** weekly count
- [ ] **Major upcoming events**:
  - Budget date (typically Oct)
  - OPR MPC date (6x/yr)
  - GE timing (every 5 yrs)
  - Quarterly results window (Feb/May/Aug/Nov)

---

## 🎯 The Dashboard's Job

This dashboard answers ONE question:
**"Is the macro tape friendly or hostile to long-side KLSE trades this week?"**

If hostile → trim sizes, raise cash, skip B-grade setups, only take A+ in defensive sectors.
If friendly → deploy capital into the favored sectors at normal size.

**Macro doesn't tell you WHAT to buy. It tells you WHETHER to buy and HOW MUCH.**

---

## 🔄 Reset Each Sunday

1. Open this file
2. Update each metric (15 min)
3. Calculate 🟢 count
4. Write the regime label
5. Adjust bucket allocations accordingly
6. Save to history table
7. Use the verdict to filter the week's watchlist

---

## 📌 Quick Reference Card

```
┌────────────────────────────────────────────┐
│  MACRO DASHBOARD — Week of: ___________    │
├────────────────────────────────────────────┤
│  1. KLCI > 200D         ✅ / ❌            │
│  2. 50D > 200D          ✅ / ❌            │
│  3. OPR easing/stable   ✅ / ❌            │
│  4. MYR firming         ✅ / ❌            │
│  5. KLCI > Dow RS       ✅ / ❌            │
│  6. Sector A-D rising   ✅ / ❌            │
│  7. Marks score 3-7     ✅ / ❌            │
├────────────────────────────────────────────┤
│  GREEN COUNT: ___ / 7                      │
│  REGIME: _______________                   │
│  BUCKET A: __%  B: __%  CASH: __%          │
└────────────────────────────────────────────┘
```

**Print this card. Fill it every Sunday. Live by it Monday-Friday.**
