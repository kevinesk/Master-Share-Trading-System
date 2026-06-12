# Gregory Morris — Sector Breadth & Internal Accumulation

> "By the time a sector index makes a new high, the leaders inside have already advanced 20-30%. Breadth indicators let you see the institutional money flowing into a sector BEFORE the index reflects it."
> — Adapted from Gregory L. Morris, *The Complete Guide to Market Breadth Indicators*

Most retail traders watch sector INDICES — and react when the index breaks out. By then, the institutional money is already in. The real edge lives in SECTOR-LEVEL BREADTH — measuring whether stocks INSIDE a sector are quietly being accumulated even when the headline index looks flat.

Gregory Morris's book covers 50+ breadth indicators. This file extracts the ones most useful for KLSE sector-level analysis and shows how to build a sector breadth dashboard.

---

## Part 1 — Why Sector Breadth Matters

### The Hidden Accumulation Problem

A sector index can stay flat while institutional money silently rotates IN. How?

- Heavy buying in 5-6 leaders (institutional accumulation)
- Heavy selling in 30+ laggards (institutions exiting weak stocks)
- Net effect on the sector index: flat
- But the COMPOSITION has changed — leaders are stronger, laggards are weaker

A trader watching only the index sees nothing. A trader watching breadth sees the rotation 4-8 weeks early.

### The Hidden Distribution Problem

The reverse: a sector index can keep rising while internals deteriorate:
- Index pushed up by 2-3 mega-caps (cap-weighted skew)
- Most stocks in the sector quietly declining
- Index appears strong; underneath, distribution is happening

Breadth reveals this divergence before the index rolls over.

### The Core Truth

> "Indexes can lie. Internals cannot."

Sector breadth is the lie-detector for sector indices.

---

## Part 2 — The 6 Core Sector Breadth Indicators

### Indicator 1: Sector Advance-Decline Line (Sector A-D)

**Definition**: For each trading day, count the number of stocks IN THE SECTOR that closed UP minus those that closed DOWN. Plot the running cumulative sum.

```
Sector A-D = Cumulative sum of (Daily Advancers - Daily Decliners) within sector
```

**What it tells you**:
- Rising A-D + Rising Sector Index = HEALTHY broad rally
- Rising A-D + Flat Index = STEALTH ACCUMULATION (high alert — bullish)
- Falling A-D + Rising Index = STEALTH DISTRIBUTION (warning — bearish)
- Falling A-D + Falling Index = Confirmed downtrend

**KLSE Implementation**:
Use the constituent list of each Bursa sector. For Banking (KLFIN):
- 8-10 constituents (MAYBANK, CIMB, PBBANK, HLBANK, RHBBANK, AMBANK, BIMB, AFFIN, MBSB, ALLIANZ)
- Count daily advancers vs decliners
- Plot the cumulative A-D over time

### Indicator 2: Sector New Highs vs New Lows (NH-NL)

**Definition**: Count how many stocks in the sector hit new 52-week highs vs new 52-week lows over a rolling 50-day window.

```
NH-NL = (Stocks at 52W highs in last 50 days) - (Stocks at 52W lows in last 50 days)
```

**What it tells you**:
- High NH-NL (5+) = sector showing leadership across multiple names
- Zero or slightly negative = transitional state
- Heavily negative (-5 or worse) = sector distribution

**KLSE Implementation**:
- For each sector's constituents, mark new highs/lows
- Manually tally weekly
- Or build a Pine Script scanner

### Indicator 3: % Above Moving Average (% > MA50)

**Definition**: What percentage of stocks IN THE SECTOR are trading above their 50-day moving average?

**What it tells you**:
- >70% = sector internally strong (broad advance)
- 50-70% = neutral to constructive
- 30-50% = weakening
- <30% = sector internally weak (broad decline)

**Why it matters**: This catches the divergence between cap-weighted index and equal-weighted internal health.

### Indicator 4: Sector McClellan Oscillator

**Definition**: Same construction as the broad-market McClellan, but applied to sector constituents only.

```
Sector McClellan = EMA(19, Net_Advances) - EMA(39, Net_Advances)
```

**What it tells you**:
- Cross above 0 = sector momentum turning positive
- Above +50 = strong sector momentum
- Below -50 = strong negative momentum
- Extreme levels (±150) = exhaustion signal

**Best for**: Timing sector entries — combines momentum and breadth.

### Indicator 5: Volume Breadth Indicators

**Definition**: Compare advancing VOLUME vs declining VOLUME within the sector. Even more powerful than price-only breadth.

**The 4 volume breadth metrics**:

```
1. Volume Advance-Decline (VA-VD): 
   Cumulative sum of (Up Volume - Down Volume) in sector
   
2. Up/Down Volume Ratio:
   Up Volume / Down Volume
   - Above 9:1 = climactic buying (one-day spike — bullish)
   - Below 1:9 = climactic selling (one-day spike — capitulation)
   
3. Volume Confirmation Index:
   Trend in (Advancing Volume / Total Volume) over 10 days
   
4. Climax Volume Days:
   Days where sector volume is >2× 20-day average
   - Cluster of up-volume climaxes = accumulation
   - Cluster of down-volume climaxes = distribution
```

### Indicator 6: New Highs/New Lows Ratio (NHL Ratio)

**Definition**: NH-NL EXPRESSED AS A RATIO of total sector stocks.

```
NHL Ratio = (NH - NL) / Total Sector Stocks
```

**Thresholds for sector strength**:
- > +0.20 (20%+ of stocks at new highs net of new lows) = strong leadership
- 0 to +0.20 = developing strength
- -0.20 to 0 = developing weakness
- < -0.20 = clear sector weakness

---

## Part 3 — The Killer Combo: Detecting Stealth Accumulation

The single most valuable Morris insight: a SPECIFIC pattern of breadth signals reveals stealth accumulation BEFORE the sector breaks out.

### The Stealth Accumulation Pattern

ALL of these conditions present for 4-8 weeks:

```
1. Sector INDEX: Flat to slightly down — appears to be doing nothing
2. Sector A-D LINE: Quietly rising
3. % above MA50: Increasing from <50% to >60%
4. New Highs - New Lows: Slowly increasing toward positive
5. Up/Down Volume Ratio: Tilting bullish (>1.5)
6. Volume on up days > volume on down days
```

**Interpretation**: Institutions are buying the LEADERS in the sector while the index drags on the WEAKER names. The internal composition is bullish.

**Action**: Identify the sector leaders (stocks driving the breadth) and position BEFORE the sector index breaks out.

### Reverse Pattern: Stealth Distribution

```
1. Sector INDEX: Flat to slightly up — appears strong
2. Sector A-D LINE: Quietly falling
3. % above MA50: Decreasing from >70% to <50%
4. New Highs - New Lows: Declining toward zero
5. Up/Down Volume Ratio: Falling toward 1:1
6. Volume on down days > volume on up days
```

**Interpretation**: Institutions are distributing leaders (taking profits) while weak names provide noise. The internal composition is bearish — the index is about to roll over.

**Action**: Exit positions in the sector even if individual charts still look fine. The macro internal signal trumps individual charts.

---

## Part 4 — KLSE Sector Breadth Dashboard

Build this for each of the 12 KLSE sectors. Update weekly.

### Sample Dashboard Entry (Banking — KLFIN)

```
==================================================================
KLFIN (BANKING) — As of [DATE]
==================================================================
Constituents: 10 stocks (MAYBANK, CIMB, PBBANK, HLBANK, RHBBANK, 
              AMBANK, BIMB, AFFIN, MBSB, ALLIANZ)

INDEX STATUS:
  KLFIN price: ___ (___ % change W-o-W)
  Above MA50:   YES/NO     |    Above MA200:    YES/NO
  vs KLCI RS:   Rising/Flat/Falling

BREADTH INTERNALS:
  Stocks above MA50:   ____ / 10  (__%)
  Stocks above MA200:  ____ / 10  (__%)
  Stocks at 52W high:  ____ / 10
  Stocks at 52W low:   ____ / 10
  NH - NL:             ____
  
A-D ACTION (LAST 5 SESSIONS):
  Total advancers:  ____
  Total decliners:  ____
  Avg Up Volume / Avg Down Volume:  __ : __
  
SECTOR McCLELLAN: _____ (Threshold: cross above 0 = bullish)
% ABOVE MA50: __% (Threshold: 70%+ = strong)

INTERPRETATION:
  □ Stealth Accumulation (bullish set-up — 6 conditions)
  □ Developing Strength
  □ Neutral
  □ Developing Weakness
  □ Stealth Distribution (bearish set-up — 6 conditions)
  □ Confirmed Trend (specify up/down)

ACTION:
  □ HUNT — full position sizing on stocks within
  □ WATCH — wait for confirmation
  □ NEUTRAL — no special action
  □ TRIM — reduce exposure
  □ EXIT — sector turning down
```

### Maintain this for all 12 sectors

| Sector | Status | Hunt Priority |
|--------|--------|---------------|
| Banking (KLFIN) | ? | ? |
| Tech (KLTEC) | ? | ? |
| Plantation (KLPLN) | ? | ? |
| Property (KLPRP) | ? | ? |
| Construction (KLCNS) | ? | ? |
| Healthcare (KLHTH) | ? | ? |
| Consumer (KLCSU) | ? | ? |
| Telco (KLTEL) | ? | ? |
| REITs (KLREI) | ? | ? |
| Energy (KLEUT) | ? | ? |
| Industrial (KLIND) | ? | ? |
| Transport (KLTRN) | ? | ? |

Top 2-3 sectors with "Hunt" priority = your trading focus for the week.

---

## Part 5 — Identifying the Sector Leaders (From Breadth Data)

Once you've identified an accumulating sector via breadth, find the specific LEADER stocks driving it:

### The Leader Identification Process

```
Step 1: List all stocks in the strong sector
Step 2: For each, calculate 13-week price return AND volume change
Step 3: Rank by combined score:
        - 50% weight: 13-week price return vs sector average
        - 50% weight: 13-week volume change vs 50-day average

Step 4: Top 2-3 by combined score = the stocks driving the breadth
Step 5: These are your prime VCP / breakout candidates
```

### KLSE Banking Example (Hypothetical)

After detecting Banking stealth accumulation:

| Stock | 13W Price Return | 13W Vol vs 50d Avg | Combined Score |
|-------|------------------|-------------------|----------------|
| MAYBANK | +12% | +30% | 95 |
| CIMB | +18% | +45% | 100 |  ← Top leader
| PBBANK | +8% | +15% | 65 |
| HLBANK | +5% | +10% | 40 |
| RHBBANK | +14% | +25% | 80 |
| AMBANK | -2% | -5% | 10 |

**Action**: Focus on CIMB (top leader) and MAYBANK (second leader). Skip the laggards.

---

## Part 6 — Breadth Divergences (Predictive Signals)

The most powerful Morris signals come from BREADTH DIVERGING from INDEX. Look for these:

### Bullish Divergences (Buy Signal)

**Type 1 — Index makes new low, breadth doesn't**
```
Index:        Lower low
Sector A-D:   Higher low ← divergence
NHL Ratio:    Improving
```
Interpretation: Selling pressure exhausted in the leaders. Bottom forming.

**Type 2 — Index flat, internal % above MA50 rising**
```
Index:        Flat for 4 weeks
% > MA50:    Was 50%, now 65% ← strengthening
```
Interpretation: Stocks are quietly being accumulated even though headline isn't moving.

### Bearish Divergences (Sell Signal)

**Type 3 — Index makes new high, breadth doesn't**
```
Index:        Higher high
Sector A-D:   Lower high ← divergence
NHL Ratio:    Declining
```
Interpretation: New highs being driven by fewer stocks. Internal weakness — top forming.

**Type 4 — Index rising, % above MA50 declining**
```
Index:        Up 5% in last 4 weeks
% > MA50:    Was 75%, now 55% ← deteriorating
```
Interpretation: Rally is narrowing — only mega-caps lifting the index. Distribution underneath.

### How to Find Divergences

Visually overlay the sector index chart with the breadth indicator chart. Pay attention to:
- Direction of the most recent move in each
- Convergence vs divergence at swing highs/lows
- Multi-week divergence patterns (most predictive)

---

## Part 7 — Combining Morris with Cane and Weinstein

The full sector analysis stack:

```
CANE (leading indicators):    Sector should benefit from current macro
   → BNM cutting, loan growth up → Banking should benefit

WEINSTEIN (stage analysis):    Sector chart is in Stage 1→2 transition
   → KLFIN broke above 30-week MA, RS turning positive

MORRIS (breadth confirmation): Internals support the move
   → Sector A-D rising, % above MA50 at 70%, NH-NL strongly positive

= TRIPLE CONFIRMATION
Execute aggressively
```

### When Layers Disagree

- Cane says bullish (macro favorable) but Morris says no breadth → **WAIT** for internals to confirm
- Weinstein shows Stage 2 but Morris shows weak breadth → **Suspect false breakout** — be selective
- All three agree → **TRIPLE CONVICTION** — position with conviction

**Morris is the final filter.** Even if macro and chart look right, weak breadth = wait.

---

## Part 8 — The Internal Strength Workflow (Weekly)

### Step 1: Macro & Cycle Position (5 min)
From TOP_DOWN_FRAMEWORK + 43_Marks_Market_Cycles. Establishes which sectors SHOULD lead.

### Step 2: Cane Indicator Check (10 min)
From 49_Cane_Sector_Rotation_Mechanics. Confirms macro signals at sector level.

### Step 3: Weinstein Stage Check (15 min)
From 44_Weinstein_Industry_Stage_Analysis. Confirms charts agree.

### Step 4: Morris Breadth Check (20 min)
THIS FILE. The definitive internal confirmation.

For each candidate sector:
- Build the breadth dashboard (Part 4)
- Identify stealth accumulation pattern (Part 3)
- Detect divergences (Part 6)
- Rank by internal strength

### Step 5: Identify Leaders Within Strong Sectors (10 min)
Use Part 5 to find specific stocks driving the breadth.

### Step 6: Execute via Master Decision Tree (variable)
Once leaders identified, the [MASTER_DECISION_TREE.md](MASTER_DECISION_TREE.md) handles entry execution.

### Total Time Investment
Weekly: 60-90 minutes of analysis → produces 3-5 high-conviction trade candidates with multi-layer confirmation.

---

## Part 9 — Common Morris Mistakes

### Mistake 1: Only Watching the Index
Without breadth, you're flying blind to the most important signal. ALWAYS check internals.

### Mistake 2: Ignoring Divergences
"The index is making new highs, so it's strong." Maybe — but check breadth. Divergences ARE warnings.

### Mistake 3: Trading on Breadth Alone
Breadth confirms; it shouldn't trigger alone. Combine with Stage analysis (Weinstein) and pattern (VCP).

### Mistake 4: Not Building the Dashboard
Eye-balling breadth fails. Build the actual dashboard, update it weekly. Discipline = data.

### Mistake 5: Using Daily Data for Weekly Decisions
Breadth signals stabilise over weeks. Don't make weekly position decisions on daily wiggles.

### Mistake 6: Confusing Breadth with Volume
Volume is one component of breadth, but breadth is fundamentally about WIDTH of participation, not just volume.

### Mistake 7: Watching Single-Day Spikes
A single climactic up-day means little. Look for SUSTAINED patterns over weeks.

---

## Part 10 — Building Your KLSE Sector Breadth Tools

You can build these in TradingView (Pine Script), Excel, or Python. Here are the building blocks:

### TradingView Pine Script Snippet (Sector A-D)

```pinescript
//@version=5
indicator("Banking Sector A-D Line", overlay=false)

// Define sector constituents (Banking example)
syms = array.from("BURSA:1155", "BURSA:1023", "BURSA:1295", 
                  "BURSA:5819", "BURSA:1066", "BURSA:1015",
                  "BURSA:2461", "BURSA:5258", "BURSA:1171", 
                  "BURSA:8583")

// Count daily advancers vs decliners
advs = 0
decs = 0
for sym in syms
    sclose = request.security(sym, timeframe.period, close)
    sopen = request.security(sym, timeframe.period, open)
    if sclose > sopen
        advs := advs + 1
    if sclose < sopen
        decs := decs + 1

// Cumulative A-D
var float ad = 0.0
ad := ad + (advs - decs)
plot(ad, "Banking A-D Line", color.blue, 2)
```

(This is a simplified template — extend to all sectors and add the other 5 indicators.)

### Excel Setup (Easier for Beginners)

For each sector:
- Column A: Date
- Columns B-K: Each constituent stock's daily close
- Column L: Count of (close[today] > close[yesterday])
- Column M: Count of (close[today] < close[yesterday])
- Column N: (L - M) cumulative running total = A-D line
- Chart Column N over time

Update daily. Within a few weeks, the patterns become visible.

### Python Alternative

Using yfinance or your existing KLSE screener tool:
```python
import yfinance as yf
import pandas as pd

# Define sector constituents
banking_tickers = ['1155.KL', '1023.KL', '1295.KL', '5819.KL', '1066.KL',
                   '1015.KL', '2461.KL', '5258.KL', '1171.KL', '8583.KL']

# Download data
data = yf.download(banking_tickers, period="1y", interval="1d")

# Calculate daily advancers vs decliners
prices = data['Close']
changes = prices.diff()
advancers = (changes > 0).sum(axis=1)
decliners = (changes < 0).sum(axis=1)

# Cumulative A-D
ad_line = (advancers - decliners).cumsum()

# Plot
ad_line.plot(title="Banking Sector A-D Line")
```

---

## Part 11 — The 10 Morris Commandments

1. **Internals lead indices.** Breadth turns before sector indices break out OR break down.

2. **A-D is the king indicator.** If you only track one, track the cumulative A-D line.

3. **Stealth accumulation is the highest-value signal.** Recognize the 6-condition pattern (Part 3).

4. **Volume breadth > price breadth.** Volume reveals conviction; price reveals attention.

5. **Divergences ARE warnings — heed them.** Don't trade against persistent breadth divergence.

6. **Update weekly, religiously.** Stale breadth data is useless data.

7. **Combine with Cane signals.** Macro indicators tell you WHERE; breadth tells you WHEN within where.

8. **Don't trade on single-day breadth spikes.** Wait for sustained patterns.

9. **Watch sector McClellan crossings.** The cross above 0 is a high-quality timing signal.

10. **The institutions move first; breadth reveals their fingerprints.** You can't beat them, but you can follow them.

---

## Part 12 — Worked Example: Detecting KLSE Tech Accumulation (Hypothetical)

### Setting (March 2026)
- Macro: Dalio Phase 1 confirmed
- Cane: SOX rising, USD/MYR weakening, ISM PMI > 52
- Weinstein: KLTEC just broke above 30-week MA
- All three signal "Tech should be bought"

### Morris Confirmation Check
For KLTEC (10 constituents — VITROX, INARI, FRONTKN, MPI, etc.):

```
KLTEC Index (4 weeks): +3% (modest)
Sector A-D Line: Strongly rising
% Above MA50: 80% (up from 40% six weeks ago)
NH-NL: +6 (six stocks at new highs, 0 at new lows)
Sector McClellan: +85 (crossed 0 three weeks ago)
Up/Down Volume Ratio: 2.8 (well above 1.5)
```

### Interpretation
6 of 6 stealth accumulation conditions met. INTERNAL STRENGTH MUCH STRONGER THAN INDEX SUGGESTS.

### Leader Identification

| Stock | 13W Return | 13W Vol Change | Score |
|-------|-----------|---------------|-------|
| VITROX | +18% | +50% | 95 |
| INARI | +22% | +40% | 100 ← Top |
| FRONTKN | +15% | +35% | 85 |
| MPI | +8% | +20% | 55 |
| UNISEM | +3% | +5% | 25 |

### Action
- Aggressive buy INARI on next VCP / breakout
- Strong buy VITROX on pullback
- Watch FRONTKN for entry
- Skip MPI and UNISEM (laggards)

### Result Validation
A few weeks later, KLTEC index breaks out decisively (+8% in 3 weeks). The traders watching only the index entered then. The Morris-aware trader entered 4-6 weeks earlier and is up +15% on positions already.

---

## Related Files

### Macro & Sector Framework
- [[TOP_DOWN_FRAMEWORK]] — Strategic funnel
- [[DUAL_STYLE_PLAYBOOK]] — Phase-based allocation
- [[44_Weinstein_Industry_Stage_Analysis]] — Stage analysis
- [[45_Stovall_Sector_Rotation_Model]] — Phase → sector mapping
- [[49_Cane_Sector_Rotation_Mechanics]] — Leading indicators (consumed by Morris)
- [[47_Dalio_Debt_Crises_Liquidity]] — Macro layer
- [[48_Chancellor_Capital_Cycle]] — Supply-side cycle

### Breadth & Market Internals
- [[26_Market_Breadth_Sentiment]] — Broad market breadth (KLCI-level)
- [[34_Advanced_Technical_Analysis]] — RS analysis
- [[31_Order_Flow_Market_Microstructure]] — Order flow as micro-breadth

### Execution
- [[MASTER_DECISION_TREE]] — Per-trade execution after breadth signal
- [[04_VCP_Pattern_Playbook]] — VCP entries on identified leaders
- [[11_TradingView_Pine_Script]] — Implementing breadth tools in code
- [[14_Backtesting_Framework]] — Validating breadth strategies historically
