# KLSE Top-Down Execution Framework

> "A mediocre stock in a booming industry will often outperform a great stock in a dying industry. A great stock in a dying industry will lose money even when the chart looks perfect."

This is the **integration card** for your knowledge base. It synthesises macro analysis (Marks, Murphy), industry analysis (Weinstein, Stovall), and company analysis (Lynch, Minervini, O'Neil) into one execution funnel.

Read this card with the [Master Decision Tree](MASTER_DECISION_TREE.md). The Decision Tree is the *tactical* checklist (per-trade). This Framework is the *strategic* funnel (per-week / per-month).

---

## The 3-Level Top-Down Funnel

```
┌────────────────────────────────────────────────────────────────────┐
│  LEVEL 1 — MACRO (The Ocean)                                       │
│  Question: Is the global environment safe for capital deployment?  │
│  Decision: GO / CAUTION / DEFEND                                   │
└────────────────────────────────────────────────────────────────────┘
                              ↓ if GO
┌────────────────────────────────────────────────────────────────────┐
│  LEVEL 2 — INDUSTRY (The Current)                                  │
│  Question: Which sectors have institutional money flowing in?      │
│  Decision: Which 2-3 sectors to hunt within                        │
└────────────────────────────────────────────────────────────────────┘
                              ↓ Stage 2 industries only
┌────────────────────────────────────────────────────────────────────┐
│  LEVEL 3 — COMPANY (The Ship)                                      │
│  Question: Which specific stocks have the technical + fundamental  │
│            edge to buy now?                                        │
│  Decision: Execute the trade using Master Decision Tree            │
└────────────────────────────────────────────────────────────────────┘
```

---

## LEVEL 1 — MACRO ASSESSMENT (The Ocean)

### The 7-Metric Macro Dashboard

Check these every Sunday and update your "Macro Score":

| # | Metric | Source | Reading |
|---|--------|--------|---------|
| 1 | **KLCI vs 50-day MA** | TradingView | Above = +1 / Below = -1 |
| 2 | **KLCI vs 200-day MA** | TradingView | Above = +1 / Below = -1 |
| 3 | **Dow Jones vs 20-day MA** | US futures | Above = +1 / Below = -1 |
| 4 | **USD/MYR trend** | Investing.com | Stable/Weakening = +1; Strengthening = -1 |
| 5 | **McClellan Oscillator** | KLSE breadth | Above 0 = +1 / Below -50 = -1 |
| 6 | **VIX level** | CBOE | Below 20 = +1 / Above 30 = -1 |
| 7 | **Marks Cycle Position** | Subjective assessment | 1-3 (early/mid bull) = +1; 7-10 (late bull/bear) = -1 |

### Macro Score Decisions

```
Score +5 to +7 → AGGRESSIVE MODE
  • Full position sizing
  • Take A and A+ setups
  • Up to 6 open positions
  • Use cheat entries on textbook VCPs

Score +2 to +4  → STANDARD MODE
  • Normal sizing
  • Only A+ setups
  • Max 4 open positions
  • Standard entries only (no cheats)

Score -1 to +1  → DEFENSIVE MODE
  • 50% sizing
  • A+ setups only
  • Max 2 open positions
  • Tighter stops
  • Take partial profits earlier

Score -7 to -2  → CAPITAL PRESERVATION MODE
  • NO new long positions
  • Trail stops on existing positions tighter
  • Take partial profits more aggressively
  • Watch for next macro turn
```

### The Marks Cycle Position (Subjective 1-10)

Howard Marks's pendulum — where are we right now?

| Score | Description | Behavior |
|-------|-------------|----------|
| 1-2 | **Capitulation low** | Everyone's terrified. Best buying opportunity. Rare. |
| 3-4 | **Early recovery** | Doubt remains. Best risk-reward. Aggressive long. |
| 5-6 | **Mid-bull** | Confidence rising. Normal. Standard execution. |
| 7-8 | **Late-bull / Euphoria** | "This time is different." Reduce size, raise stops. |
| 9-10 | **Mania / Top** | Taxi drivers giving tips. Stop new buys. Heavy cash. |

Updated detail in [43_Marks_Market_Cycles.md](43_Marks_Market_Cycles.md).

### Murphy Intermarket Quick-Check

Before deploying capital, run the intermarket dashboard from [32_Intermarket_Analysis.md](32_Intermarket_Analysis.md):

```
USD/MYR weakening   → Foreign flows favourable → bullish KLSE
SOX Index rising    → bullish KLSE tech (VITROX, FRONTKN, INARI)
CPO above MA200     → bullish KLSE plantation (SIME, KLK, IOI)
Gold rising sharply → defensive signal — risk-off
US 10Y dropping     → bullish equities (lower discount rate)
US 10Y rising fast  → bearish equities (compresses valuations)
```

---

## LEVEL 2 — INDUSTRY ANALYSIS (The Current)

### The Weinstein Industry Stage Map

For EACH major KLSE sector index, identify its current stage:

| Stage | Definition | Action |
|-------|-----------|--------|
| **Stage 1 — Basing** | Sector index sideways below MA200, after long decline; volume drying up | WATCH — accumulation phase |
| **Stage 2 — Advancing** | Sector index above rising MA200; making higher highs; RS positive | HUNT — find stocks here |
| **Stage 3 — Topping** | Sector index sideways above MA200, but RS turning flat or down | TIGHTEN — exits on rallies |
| **Stage 4 — Declining** | Sector index below MA200; lower lows; RS negative | AVOID — no new positions |

### KLSE Sector Tracking List

Track these sectors' weekly charts:

| Sector | Bursa Index | Key Stocks |
|--------|------------|-----------|
| Banking | KLFIN | MAYBANK, CIMB, PBBANK, HLBANK, RHBBANK |
| Tech / Semi | KLTEC | VITROX, INARI, FRONTKN, MPI, GTRONIC |
| Plantation | KLPLN | SIME, KLK, IOI, GENP, TSH |
| Property | KLPRP | SIMEPROP, MAHSING, ECOWLD, S P SETIA |
| Construction | KLCNS | GAMUDA, IJM, SUNCON, MUHIBAH |
| Healthcare | KLHTH | IHH, KPJ, TOPGLOV, HARTA, SUPERMX |
| Consumer | KLCSU | NESTLE, F&N, AEON, MR DIY |
| Telco | KLTEL | MAXIS, CDB (CelcomDigi), AXIATA, TM |
| REITs | KLPRP* | KLCC, IGB, SUNWAY REIT, AXIS, PAVILION |
| Energy | KLEUT | TENAGA, YTL POWER, PETDAG, PCHEM |
| Utilities | KLEUT | TENAGA, YTL POWER, GAS MALAYSIA |

### The Stovall Cycle Map

Different sectors thrive in different economic phases (see [45_Stovall_Sector_Rotation_Model.md](45_Stovall_Sector_Rotation_Model.md)):

```
ECONOMIC PHASE            SECTORS THAT LEAD              KLSE EXAMPLES
─────────────────────     ───────────────────────────    ──────────────────────
1. Early Recovery         Tech, Consumer Discretionary,   VITROX, AEON, GAMUDA
   (just exited recession) Construction
2. Full Expansion         Industrials, Energy,            PETDAG, KLK, PCHEM
   (peak of growth)       Materials
3. Early Recession         Consumer Staples, Healthcare,   NESTLE, IHH, MAXIS
   (slowdown beginning)   Utilities
4. Full Recession         Defensive, Cash, Bonds,         REITs, TNB, gold
   (deepest contraction)  Counter-cyclical
```

### Industry Selection Workflow

```
Step 1: Identify the current economic phase (Stovall framework)
Step 2: List the 3-4 sectors that should lead in that phase
Step 3: For each, check the Weinstein stage — confirm Stage 2
Step 4: Calculate the sector RS line vs KLCI (3-month, 6-month)
Step 5: Top 2-3 sectors by Stage 2 + positive RS = HUNT here
Step 6: All other sectors are reference only — no positions
```

### Industry Relative Strength Quick Math

```
Sector RS = (Sector Index ÷ KLCI) over time

If Sector RS line is rising → sector outperforming KLCI → HUNT
If Sector RS line is falling → sector underperforming KLCI → AVOID
```

In TradingView: plot `KLFIN/KLCI` as a custom symbol. If the line rises, banking leads. If it falls, banking lags.

---

## LEVEL 3 — COMPANY SELECTION (The Ship)

Once macro is GO and you've narrowed to 2-3 leading sectors, hunt within them.

### The 3-Filter Funnel

```
Filter A (Quality):     Lynch's 6 categories — pick the right type of stock
                         for your trading horizon
Filter B (Quantitative): CAN SLIM + Minervini Trend Template — does it score?
Filter C (Technical):    VCP or other valid base pattern in place?
```

### Lynch Category Decision (Filter A)

Match your trade type to the right Lynch category:

| Lynch Category | Best Trade Style | KLSE Example |
|---------------|------------------|--------------|
| **Fast Grower** (20-25%+ EPS) | VCP breakout swing trade | VITROX, INARI in tech expansion |
| **Stalwart** (10-12% EPS) | Pullback to EMA50 buy-and-hold | NESTLE, MAXIS, PBBANK |
| **Slow Grower** (2-4% EPS) | Dividend hold, not trade | TNB, REITs |
| **Cyclical** | Bottom-of-cycle accumulation | KLK, IOI in CPO recovery |
| **Turnaround** | Confirmed recovery breakout only | Sime Darby restructuring story |
| **Asset Play** | Discount-to-NTA value position | Land bank developers, holding companies |

Detail: [46_Lynch_Six_Categories.md](46_Lynch_Six_Categories.md).

### CAN SLIM + Trend Template Score (Filter B)

The full 14-point CAN SLIM scoring is in [10_CAN_SLIM_KLSE.md](10_CAN_SLIM_KLSE.md). Quick gate:

```
Required (all must pass):
  □ EPS growing ≥15% latest quarter
  □ Revenue growing ≥10% latest quarter
  □ 3-year EPS CAGR ≥15%
  □ ROE ≥15%
  □ RS Rating ≥ +5 vs KLCI
  □ Trend Template ≥ 6/8
  
Bonus (more = stronger):
  □ Making new 52-week highs
  □ Institutional buying visible
  □ EPS growth accelerating Q-over-Q
```

### Technical Setup (Filter C)

From your master Decision Tree Gate 3. The setup must be ONE of:

```
□ VCP (2-4 contractions, tighter each time)         → [04]
□ Cup-with-Handle (O'Neil specs)                    → [39]
□ Flat Base                                          → [39]
□ Double Bottom (with undercut ideal)               → [39]
□ Darvas Box                                         → [37]
□ Tight Closures + Zanger pattern                    → [41]
□ High Tight Flag (rare, full size)                  → [39]
```

---

## THE UNIFIED WEEKLY ROUTINE

### Sunday Evening (90 minutes — strategic)

```
0:00-0:15  Update Macro Dashboard (7 metrics, score)
           → Decide AGGRESSIVE / STANDARD / DEFENSIVE / PRESERVATION

0:15-0:30  Update Marks Cycle Position (1-10)
           → Adjust posture accordingly

0:30-0:45  Update Murphy Intermarket Quick-Check
           → Identify regional/sector signals

0:45-1:00  Run Weinstein Stage Analysis on all KLSE sectors
           → Mark each sector Stage 1/2/3/4

1:00-1:15  Apply Stovall framework
           → Confirm which phase we're in; pick 2-3 best sectors

1:15-1:30  Within those 2-3 sectors, screen for individual stocks
           → CAN SLIM scoring on each candidate
           → Identify the 5-10 strongest candidates

1:30-1:45  Open each candidate's WEEKLY chart
           → Confirm Stage 2 (Trend Template)
           → Identify any valid pattern (VCP, cup-handle, etc.)
           → Mark pivot, stop, target

1:45-1:50  Final A+/A/B list:
           A+ (3-4 names): All filters perfect — full position when triggered
           A  (3-5 names): One minor flaw — reduced size when triggered
           B  (3-5 names): Watch only, don't trade yet

1:50-2:00  Set TradingView alerts on all candidates
           Write trade plan: entry / stop / target / size for each
```

### Daily During the Week (15 minutes)

```
Morning : Check macro hasn't degraded (KLCI vs 50-MA, USD/MYR)
        : Check alerts — any pivots triggered?
        : Execute alerted trades per Decision Tree
        
Evening : Update journal
        : Adjust stops on open positions
        : Note any sector RS changes
```

### Daily Routine Wrapper

The [Master Decision Tree](MASTER_DECISION_TREE.md) handles every individual trade decision. This Framework determines:
- WHEN you should be trading at all (Level 1)
- WHERE in the market you should be looking (Level 2)
- WHICH category and pattern fit (Level 3)

---

## THE TOP-DOWN EXECUTION MATRIX (Master Card)

| Level | Question | Leading Indicators | Primary Files |
|-------|----------|-------------------|--------------|
| **1. Macro** | Is the environment safe? | KLCI vs MAs, USD/MYR, VIX, Marks position, McClellan | [43](43_Marks_Market_Cycles.md), [32](32_Intermarket_Analysis.md), [20](20_Global_Macro_for_KLSE.md), [26](26_Market_Breadth_Sentiment.md) |
| **2. Industry** | Where is institutional money? | Sector Stage Analysis, sector RS lines, sector 52W highs | [44](44_Weinstein_Industry_Stage_Analysis.md), [45](45_Stovall_Sector_Rotation_Model.md), [03](03_KLSE_Sectors_and_Macro.md), [16](16_Sector_Playbooks.md) |
| **3. Company** | Which stocks have the edge? | EPS growth, RS Rating, Stage 2, VCP base | [46](46_Lynch_Six_Categories.md), [02](02_Minervini_SEPA_KLSE.md), [10](10_CAN_SLIM_KLSE.md), [04](04_VCP_Pattern_Playbook.md), [42](42_Momentum_Masters_Advanced_VCP.md) |
| **Execution** | How do I trade this NOW? | Pivot, stop, sizing, mental check | [MASTER_DECISION_TREE](MASTER_DECISION_TREE.md), [12](12_Perfect_Entry_Exit.md), [06](06_Risk_Management_and_Position_Sizing.md) |
| **Psychology** | Am I in the right state? | Mental routine, FOMO interrupt, drawdown protocol | [33](33_Fear_FOMO_Confidence_Mastery.md), [STICKY_NOTE](STICKY_NOTE_Anti_FOMO.md) |

---

## THE 10 TOP-DOWN COMMANDMENTS

1. **Never trade against the macro tide.** If KLCI is below its 50-day MA, you are swimming against the current. Sit in cash.

2. **Never trade in a Stage 4 industry.** Even the best individual stock will be dragged down by the sector. Mark Stage 4 sectors as "do not touch."

3. **Match your trade style to the Lynch category.** Don't try to swing-trade a Slow Grower or buy-and-hold a Cyclical at the peak. The category dictates the strategy.

4. **Trade only the leaders, never the laggards.** Within a Stage 2 sector, the #1 RS stock outperforms #3 by a factor of 3-5×. Pay up for leadership.

5. **The funnel narrows; never widen it.** If macro is bad, stop. If sectors are weak, stop. If no setup, stop. Discipline = saying no to 95% of opportunities.

6. **Confirm BEFORE entering, doubt AFTER entering.** Before a trade: stack confluence. After entry: trust the system and sit.

7. **Marks pendulum > daily news.** The cycle position matters far more than any single headline. Macro mood beats macro data.

8. **Sector RS is the smart-money tracker.** When institutions rotate INTO a sector, the RS line rises before the news. Follow the RS, not the analysts.

9. **The same setup means different things in different macro regimes.** A perfect VCP breakout in Stage 1 macro (recovery) vs Stage 9 macro (mania) have wildly different probabilities.

10. **The funnel feeds the Decision Tree.** Use this Framework strategically (weekly). Use the [Decision Tree](MASTER_DECISION_TREE.md) tactically (per trade).

---

## EXAMPLE: A FULL TOP-DOWN WALKTHROUGH (KLSE 2026)

Let's say it's a Sunday in May 2026. Here's the funnel in action:

### Level 1 — Macro Check
- KLCI above 50-MA and 200-MA → +2
- Dow above 20-MA → +1
- USD/MYR stable around 4.35 → +1
- McClellan +75 → +1
- VIX at 17 → +1
- Marks position: 5 (mid-bull) → +1
- **Macro Score = +7 → AGGRESSIVE MODE**

### Level 2 — Industry Check
Economic phase: Full Expansion (Stovall) — leading sectors should be Industrials, Energy, Materials.

Apply Weinstein Stage Analysis to KLSE sectors:
- KLFIN (Banking): Stage 2 ✓, RS rising ✓
- KLTEC (Tech): Stage 2 ✓, RS strongest ✓
- KLPLN (Plantation): Stage 1, RS flat → skip
- KLPRP (Property): Stage 3 — TIGHTEN existing only
- KLCNS (Construction): Stage 2 ✓, RS positive ✓

**Hunting in**: KLFIN, KLTEC, KLCNS

### Level 3 — Company Selection
Within KLTEC, VITROX shows:
- EPS growing 28% latest quarter ✓
- 3Y CAGR 22% ✓
- ROE 19% ✓
- RS Rating +18 vs KLCI ✓
- Trend Template 8/8 ✓
- Lynch Category: Fast Grower ✓
- WEEKLY chart: 3-contraction VCP with final contraction 4%, volume dried up ✓
- All 5 cheat conditions met ✓

**Execution**: Take cheat entry at contraction low, 1/3 position; add 1/3 on pivot breakout; add final 1/3 on first new pivot up. Full Decision Tree Gate 5-7 applies.

---

## Related Files

### Daily Use
- [MASTER_DECISION_TREE.md](MASTER_DECISION_TREE.md) — per-trade tactical checklist
- [STICKY_NOTE_Anti_FOMO.md](STICKY_NOTE_Anti_FOMO.md) — pre-buy mental check

### Macro Layer
- [[43_Marks_Market_Cycles]] — Howard Marks pendulum & cycle position
- [[32_Intermarket_Analysis]] — Murphy's intermarket framework
- [[20_Global_Macro_for_KLSE]] — Global macro signals
- [[26_Market_Breadth_Sentiment]] — McClellan, breadth, sentiment

### Industry Layer
- [[44_Weinstein_Industry_Stage_Analysis]] — Industry-level stage analysis
- [[45_Stovall_Sector_Rotation_Model]] — Economic phase → sector rotation
- [[03_KLSE_Sectors_and_Macro]] — Sector reference
- [[16_Sector_Playbooks]] — Sector-specific playbooks

### Company Layer
- [[46_Lynch_Six_Categories]] — 6 stock categories
- [[02_Minervini_SEPA_KLSE]] — Trend Template + SEPA
- [[10_CAN_SLIM_KLSE]] — O'Neil's full screening logic
- [[04_VCP_Pattern_Playbook]] — VCP entry execution
- [[42_Momentum_Masters_Advanced_VCP]] — Cheat entries, advanced VCP

---

*Strategy is the funnel. Tactics are the Decision Tree. Psychology is the foundation. Without all three, the system fails.*
