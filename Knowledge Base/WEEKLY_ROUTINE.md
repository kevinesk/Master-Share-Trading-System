# Weekly Trading Routine — KLSE
**When**: Every Sunday, 10:00 AM – 12:00 PM (2 hours)
**Purpose**: Step out of the daily tick-noise and see the big picture. Set the week's playbook.

> *"In trading, the daily noise lies. The weekly signal tells the truth."*

---

## 🎯 The Weekly Mission

Answer 5 questions:

1. **Where are we in the market cycle?** (Marks)
2. **Which sectors are leading?** (Stovall + Weinstein + Morris)
3. **What's the macro liquidity tone?** (Dalio + Pauline Yong)
4. **What's on my watchlist for the coming week?** (Top-Down funnel)
5. **What did I do right/wrong last week?** (Journal review)

---

## 📊 PHASE 1 — Macro & Market Review (30 min)

### A. KLCI Weekly Chart Review
Open KLCI weekly chart. Answer:

- [ ] **Stage**: 1 (base) / 2 (uptrend) / 3 (topping) / 4 (downtrend)?
- [ ] Price vs 30-week MA: above or below?
- [ ] 30-week MA slope: rising / flat / falling?
- [ ] Last weekly close: up week or down week?
- [ ] How many up weeks vs down weeks in last 8?
- [ ] Any major support/resistance level just hit?

### B. Global Context
- [ ] Dow Jones weekly: stage? Trend intact?
- [ ] Nasdaq weekly: stage? (Tech proxy)
- [ ] USD/MYR weekly: direction? (Foreign flow proxy)
- [ ] 10-year MGS yield: rising / falling? (Discount rate proxy)
- [ ] Brent crude weekly: direction? (Oil & gas sector + macro inflation)

### C. Marks Cycle Score (1-10)
Where are we? (1 = max fear, 5-6 = neutral, 10 = max euphoria)

Inputs:
- KLCI distance from 52W high (closer = higher score)
- Days since last >2% red day (more days = higher score)
- IPO oversubscription multiples (high = higher score)
- Media tone (bullish headlines = higher score)
- Margin financing growth (faster = higher score)

**This week's Marks score: ___ / 10**

→ Rules:
- Score 1-3: Buy fear cautiously, focus on quality
- Score 4-6: Active engagement zone (best risk/reward)
- Score 7-8: Trim and trail, no new aggressive size
- Score 9-10: Defensive mode, raise cash to 30-50%

---

## 📈 PHASE 2 — Sector Rotation Review (30 min)

### A. Bursa Sector Index Scan
For each major sector, note:

| Sector | Weekly close | Stage (1-4) | RS vs KLCI | % above 50D | Decision |
|---|---|---|---|---|---|
| KLFIN (Financial) | | | | | Buy / Hold / Avoid |
| KLCON (Construction) | | | | | |
| KLPRP (Property) | | | | | |
| KLTEC (Tech) | | | | | |
| KLHC (Healthcare) | | | | | |
| KLPLT (Plantation) | | | | | |
| KLCG (Consumer) | | | | | |
| KLEW (Energy) | | | | | |
| KLIN (Industrial) | | | | | |
| KLUT (Utilities) | | | | | |
| KLTPS (Telco) | | | | | |
| KLREIT (REIT) | | | | | |

### B. Stovall Phase Alignment
Identify current economic phase:
- [ ] **Early Recovery** → Industrials, Cyclicals, Financials (late)
- [ ] **Full Recovery** → Tech, Consumer Discretionary, Industrials
- [ ] **Early Slowdown** → Energy, Staples, Healthcare
- [ ] **Recession** → Utilities, Staples, REITs, Healthcare

**This week's phase: ____________**
**Favored sectors: ____________**

### C. Top 3 Sector Leaders
Which sectors have BOTH (a) Stage 2 + (b) RS line at new high + (c) breadth >60%?

1. Sector: _____________ — leaders watch: __________
2. Sector: _____________ — leaders watch: __________
3. Sector: _____________ — leaders watch: __________

---

## 🌐 PHASE 3 — Macro Liquidity Check (20 min)

### A. Malaysian Liquidity (Pauline Yong)
- [ ] OPR current level: ____%, last change: ________, next OPR meeting: __________
- [ ] BNM SRR level: ____%
- [ ] System loan growth y/y: ____% (latest BNM stat)
- [ ] CPI y/y: ____% (latest DOSM)
- [ ] EPF dividend rate (last announced): ____%
- [ ] Major upcoming events: Budget date, election, OPR decision

### B. Global Liquidity (Dalio)
- [ ] Fed Funds rate: ____%
- [ ] Fed policy stance: hiking / pausing / cutting
- [ ] US 10Y yield direction: rising / falling
- [ ] USD index (DXY) direction
- [ ] Major upcoming Fed events

### C. Capital Cycle Check (Chancellor)
For 3 KLSE sectors, ask: "Is capital flooding in or pulling out?"
- Glove sector — phase?
- Property sector — phase?
- Tech sector — phase?

### D. Liquidity Verdict for the Week
- [ ] **Expanding liquidity** (rate cuts, MYR firming) → favor growth + duration assets
- [ ] **Tightening liquidity** (rate hikes, MYR weakening) → favor defensive + cash
- [ ] **Neutral** → status quo

---

## 🧰 PHASE 4 — Watchlist Construction (40 min)

### Step 1 — Run All Screeners
- [ ] `klse_screener.py` (Python EOD)
- [ ] KLSE Momentum Swing Screener (TradingView)
- [ ] Minervini VCP + SmartMCDX Dashboard
- [ ] Pro Quant Desk v8 (True RS + Heat)
- [ ] Export top 30-50 names

### Step 2 — Filter Down (Top-Down Funnel)

Apply in order:

```
50 names (raw screener output)
  ↓ Filter by favored sectors (Phase 2)
20 names (sector-aligned)
  ↓ Apply Minervini Trend Template 7-8/8
10 names (technical leaders)
  ↓ Apply KC Chong 8-criteria quality filter
6-8 names (fundamentally + technically strong)
  ↓ Apply Cold Eye / Tong Kooi Ong quality check
3-5 names (THE WATCHLIST for the week)
```

### Step 3 — For Each Watchlist Stock, Define
| Stock | Code | Pivot | Buy Zone | Stop | T1/T2/T3 | Max Size | Catalyst |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

### Step 4 — Bucket Allocation (Dual-Style Playbook)
Based on Marks score + Stovall phase:

| Bucket | Target % | Names in watchlist |
|---|---|---|
| A — Growth/Momentum | __% | |
| B — Defensive/Yield | __% | |
| Cash | __% | |

---

## 📓 PHASE 5 — Last Week Review (20 min)

### Open `TRADE_JOURNAL.md` → review last week's entries

For each trade made last week:
- [ ] Did I follow PRE_TRADE_CHECKLIST 12 gates?
- [ ] Was sizing within 10%?
- [ ] Did exit happen per plan?
- [ ] What's the lesson?

### Weekly Stats
- Trades taken: ___
- Trades I should have taken but skipped: ___
- Trades I shouldn't have taken (FOMO/chase): ___
- Win rate this week: ___ %
- Avg R this week: ___
- Mental state avg this week (1-10): ___

### Top 3 Lessons This Week
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

### Action Item for Next Week
What ONE habit will I improve next week? _____________________________________

---

## 🎲 PHASE 6 — The Week's Playbook (10 min)

Write this in journal as a single block:

```
WEEK OF: [Monday date]
KLCI stage: __  | Marks score: __/10  | Liquidity: Expanding/Tight/Neutral
Favored sectors: __________________________
Bucket allocation: A=__%  B=__%  Cash=__%

Watchlist (3-5 names with triggers):
  1. _______________________________
  2. _______________________________
  3. _______________________________
  4. _______________________________
  5. _______________________________

Open positions (action plan):
  - ____________: hold / trim at __ / stop at __
  - ____________: hold / add at break / stop at __

Risks to watch (events, news, levels):
  - _____________________________________
  - _____________________________________

ONE-line theme for the week: _____________________
```

---

## ⏰ Weekly Routine Time Budget

| Phase | Time | Cumulative |
|---|---|---|
| 1. Macro & Market Review | 30 min | 0:30 |
| 2. Sector Rotation | 30 min | 1:00 |
| 3. Macro Liquidity | 20 min | 1:20 |
| 4. Watchlist Construction | 40 min | 2:00 |
| 5. Last Week Review | 20 min | 2:20 |
| 6. Week Playbook | 10 min | 2:30 |

**Total: 2.5 hours every Sunday.**

This 2.5 hours is the highest-ROI time block in your week. Don't skip it. Don't rush it. Don't multitask it.

---

## 🔑 The Big Idea

> Most retail traders are reactive — they wake up Monday and ask "what's hot today?"
> Professionals are proactive — they entered Monday knowing exactly which 3-5 setups they're watching, at which prices, with which sizes, for which catalysts.
>
> This routine is what separates the two.

**Sunday is when you decide. Monday-Friday is when you execute.**
