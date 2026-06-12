# Livermore Market Key — The Mathematical System

> "I have always believed that anyone who is willing to study the market with the proper attitude, in the same way that he would study any other profession, can soon master the rudimentary principles."
> — Jesse Livermore, *How to Trade in Stocks* (1940)

In 1940, near the end of his life, Jesse Livermore finally published HIS OWN book — separate from Edwin Lefèvre's biographical *Reminiscences* (1923, see [36_Livermore_Rules_Reminiscences.md](36_Livermore_Rules_Reminiscences.md)).

While *Reminiscences* covers Livermore's philosophy and psychology, his own book reveals his actual **mechanical system** — the **Livermore Market Key**. This was a hand-drawn, six-column price-tracking method designed to identify the *exact moment* a stock or market changed direction.

This file translates that 86-year-old system into modern terms and applies it to KLSE.

---

## Part 1 — Why the Market Key Exists

By 1940, Livermore had identified a problem: even traders who knew his rules (pivotal points, cut losses, sit tight) struggled to **identify a turning point in real time**. Hindsight is always clear; the moment-of-truth is murky.

The Market Key was his solution: a structured way to **record price action** in six columns that mechanically flagged when:
- A trend was firmly in place (line of least resistance)
- A natural reaction was occurring (normal correction within trend)
- A natural rally was occurring (normal bounce within downtrend)
- A trend was potentially REVERSING (the most valuable signal)

It is essentially a **manual swing-point classifier** — the ancestor of today's market-structure analysis (HH/HL, BOS, CHoCH — see [34_Advanced_Technical_Analysis.md](34_Advanced_Technical_Analysis.md)).

---

## Part 2 — The Six Columns Explained

Livermore drew six columns on a paper ledger. Each price update went into ONE column based on what was happening.

```
| Column 1     | Column 2     | Column 3     | Column 4     | Column 5     | Column 6     |
| SECONDARY    | NATURAL      | UPWARD       | DOWNWARD     | NATURAL      | SECONDARY    |
| RALLY        | RALLY        | TREND        | TREND        | REACTION     | REACTION     |
|              |              |              |              |              |              |
| Black ink    | Black ink    | Red ink      | Black ink    | Red ink      | Red ink      |
```

(Original colour convention — red for trend confirmations, black for counter-moves.)

### The Six Categories Defined

**Column 3 — Upward Trend** (red): A new high above the prior pivot. The trend is up; trade longs.

**Column 4 — Downward Trend** (black): A new low below the prior pivot. The trend is down; do not buy.

**Column 2 — Natural Rally** (black): In a downtrend, a counter-move UP that does NOT exceed 6 points (Livermore's stock-price units, roughly equivalent to a 6% move on KLSE). Normal correction; don't trust it.

**Column 5 — Natural Reaction** (red): In an uptrend, a counter-move DOWN that does NOT exceed 6%. Normal pullback; uptrend still intact.

**Column 1 — Secondary Rally** (black): In a downtrend, a rally that EXCEEDS 6%. Now we have to watch — possible reversal.

**Column 6 — Secondary Reaction** (red): In an uptrend, a pullback that EXCEEDS 6%. Now we have to watch — possible reversal.

### The Critical Rule: When to Switch Columns

A new entry is only made when one of these triggers fires:

| Action | Trigger |
|--------|---------|
| Make new entry in current column | Price moves further in that direction by ≥1 point (1%) |
| Switch to a counter-move column | Price reverses ≥3 points (3%) from the most recent extreme |
| Confirm trend continuation | Price exceeds the prior pivot in the trend direction |
| Confirm trend reversal | Price exceeds the prior pivot AGAINST the trend |

The 3% reversal filter prevents you from getting whipsawed by noise. Only moves of meaningful size warrant attention.

---

## Part 3 — Pivotal Points & Continuation Points

These are the two action triggers in Livermore's system.

### Pivotal Point (Major Turning Signal)

A pivotal point is established when:
1. A stock makes a NEW high above the most recent peak (in any column)
2. OR a stock makes a NEW low below the most recent trough

**Action**: Trade in the direction of the pivot. A pivot up = buy. A pivot down = sell longs / short.

### Continuation Point (Trend Re-Engagement)

A continuation point occurs when:
1. Price is in a confirmed trend (Column 3 or 4)
2. A natural reaction (Column 5) or natural rally (Column 2) is completing
3. Price moves back through the most recent SHORT-TERM pivot in the trend direction

**Action**: Re-enter or pyramid in the trend direction.

### Modern Translation

| Livermore 1940 | Modern Equivalent (KLSE 2026) |
|----------------|-------------------------------|
| Pivotal Point UP | Break of Structure (BOS) up = new HH after consolidation |
| Pivotal Point DOWN | BOS down = new LL after consolidation |
| Continuation Point | Higher Low (HL) confirmation in uptrend |
| Natural Reaction | Pullback to 10-day or 20-day EMA |
| Secondary Reaction | Pullback that breaks short-term structure (CHoCH warning) |

---

## Part 4 — The 6% Rule (Modern Adaptation)

Livermore used $6 moves for high-priced stocks of his era ($30-$100 range, equivalent to 6-20%). The modern adaptation is **6% on the underlying** — applicable across all KLSE price ranges.

### The 6% Rule in Practice

For any KLSE stock or KLCI:

| Move Size | Classification | Action |
|-----------|---------------|--------|
| 0–3% | Noise | Ignore; no entry change |
| 3–6% | Natural counter-move | Trend intact; expect resumption |
| > 6% | Secondary move | Warning — trend may be ending |

### Worked Example: CIMB

Assume CIMB is in a confirmed uptrend (Column 3). Last pivot at RM7.20.

- CIMB rises to RM7.80 → **new high** → next entry in Column 3 (trend confirmed)
- CIMB pulls back to RM7.55 (pullback of 3.2%) → **natural reaction** → Column 5 entry
- CIMB rises to RM7.95 → **new high** → Column 3 again, trend continues
- CIMB falls to RM7.35 (-7.5% from RM7.95) → **secondary reaction** → Column 6 entry, WARNING
- CIMB rallies to RM7.60 but does NOT exceed RM7.95 → **natural rally within a possibly-changing trend** → caution
- CIMB falls below RM7.35 → **trend reversal confirmed** → exit longs

---

## Part 5 — The Line of Least Resistance

Livermore's most quoted concept. The Market Key was designed to **identify it mechanically**.

### Definition

The "line of least resistance" is the direction the market WILL move because all friction has been removed:
- All eager sellers have sold (downtrend exhausted)
- All eager buyers have bought (uptrend exhausted)
- Now whoever pushes wins

### How the Market Key Identifies It

The line of least resistance is established when:
1. **In an uptrend**: Price makes a new pivot up, with the prior reaction having been a "natural reaction" only (not a "secondary reaction"). The trend is healthy; line up.
2. **In a downtrend**: Mirror image. Line down.
3. **In a sideways range**: Price oscillates between Column 1/6 and Column 2/5 without reaching new pivots. No line of least resistance. **Stay out.**

### KLSE Application

This is the SAME concept as today's "trend strength" — see [34_Advanced_Technical_Analysis.md](34_Advanced_Technical_Analysis.md) Part 3. Modern indicators (ADX, MA slope, market structure) measure exactly what Livermore tracked with paper and ink.

**Practical rule**: Only enter trades when the line of least resistance is clearly UP (longs) or clearly DOWN (avoid). When the line is sideways → wait.

---

## Part 6 — Constructing Your Own Market Key (Modern KLSE Version)

You don't need paper and ink — but the discipline of tracking key levels manually has value.

### Method A: The Paper Journal (Pure Livermore)

For your 5-10 watchlist stocks, maintain a simple ledger:

```
STOCK: CIMB
─────────────────────────────────────────────────────────
DATE        | PRICE  | MOVE %  | CATEGORY        | NOTE
─────────────────────────────────────────────────────────
2026-05-01  | 7.20   |   --    | Trend (up)      | Start
2026-05-08  | 7.50   | +4.2%   | Trend (up)      | New pivot
2026-05-15  | 7.30   | -2.7%   | Natural react.  | Normal
2026-05-22  | 7.80   | +6.8%   | Trend (up)      | New pivot
2026-05-29  | 7.30   | -6.4%   | Secondary react.| WARNING
2026-06-05  | 7.15   | -2.1%   | Trend (down)    | Reversed
```

### Method B: TradingView Manual Marks

On TradingView weekly chart:
1. Mark every swing high and swing low with a horizontal line
2. Label as PP (pivotal point) or CP (continuation point)
3. Use coloured lines: red for up-trend pivots, blue for down-trend pivots
4. When price makes new PP → action triggered

### Method C: Pine Script Implementation

The Market Key logic can be coded in Pine Script:

```
Inputs:
- Reversal threshold: 3%
- Reaction threshold: 6%

For each new daily bar:
- Compare to last extreme (high or low)
- If move > 6% counter to trend → flag "Secondary"
- If move > 3% counter to trend → flag "Natural"
- If new extreme exceeds last pivot → flag "Pivotal" (action signal)
```

A simple TradingView indicator with these flags would replicate Livermore's table digitally. See [11_TradingView_Pine_Script.md](11_TradingView_Pine_Script.md) for the framework.

---

## Part 7 — The 7 Critical Livermore Trade Rules (From His Own Book)

These come directly from *How to Trade in Stocks* (1940). They complement the Reminiscences rules in [36_Livermore_Rules_Reminiscences.md](36_Livermore_Rules_Reminiscences.md).

1. **Trade only at pivotal points.** Anything else is gambling. The Market Key tells you when.

2. **Trade in the line of least resistance.** If the line is sideways, do not trade. Cash is a position.

3. **Pyramid only when adding tranches in the SAME direction as the line.** Never add against the line.

4. **Use the 3% rule for noise filtering.** Any move under 3% is not actionable. Ignore it.

5. **Use the 6% rule for warning thresholds.** A 6%+ counter-move is the line warning that direction may change.

6. **Cut losses at 10%.** (Modern: 7-8% per O'Neil, who refined Livermore.)

7. **Wait for confirmation.** A pivot is not actionable until price has TRADED through it — not just touched it.

---

## Part 8 — When the Market Key Fails (Modern Caveats)

Livermore's system was designed for the markets of 1900-1940. Some adjustments for 2026 KLSE:

### Caveat 1: Algorithmic & HFT Noise
Modern markets have algorithmic trading that creates faster, sharper moves than 1940. The 3% reversal threshold may need to be widened (4-5%) for very volatile stocks. Use ATR-based thresholds for precision.

### Caveat 2: Gap Risk
The 1940 market didn't have overnight ETF rebalancing or major futures-driven gaps. A 6% overnight gap in KLSE today may not represent a trend change — it may be a one-day macro reaction.

### Caveat 3: Smaller Position Sizes
Livermore traded enormous positions and moved markets himself. As retail on KLSE, your size doesn't move price — you must wait for institutions to do it (the cup, the base, the contraction).

### Caveat 4: News-Driven Reversals
KLSE is heavily news-sensitive (Budget Day, BNM rate decisions, Bursa earnings days). A 6% move on news day may not be a "secondary reaction" — it may just be the news. Filter accordingly.

---

## Part 9 — The Modern KLSE Market Key Workflow

### Weekly Setup (Sunday, 20 minutes)

1. List your top 10 watchlist stocks
2. For each, identify the most recent **pivot up** and **pivot down** (last 6-12 months)
3. Note the % distance from current price to each pivot
4. Classify the stock's CURRENT state:
   - **Above last up-pivot, no >6% reaction** = Line of least resistance UP, trade longs
   - **Below last down-pivot, no >6% rally** = Line of least resistance DOWN, no longs
   - **Sideways between pivots** = No trade

### Daily Routine (5 minutes)

For each open position:
1. Calculate % move from last pivot
2. If move continues trend → no action
3. If move counter to trend but < 3% → noise, hold
4. If counter-move 3-6% → natural reaction, hold but watch
5. If counter-move > 6% → warning, tighten stop or take partial profit
6. If breaks counter-pivot → exit, line of least resistance has changed

### Real-Time Alert Levels

For each position, set TradingView alerts at:
- **+3% from entry pivot** (natural reaction watch)
- **+6% from entry pivot** (secondary warning)
- **At last counter-pivot** (trend reversal trigger)

This is essentially Livermore's ledger, automated.

---

## Part 10 — Market Key vs Modern Tools (Side-by-Side)

| Livermore 1940 | Modern Equivalent |
|----------------|-------------------|
| Six-column ledger | Market structure on chart (HH/HL/LH/LL) |
| Pivotal point | Break of Structure (BOS) |
| Natural reaction | Pullback to 20-day MA |
| Secondary reaction | Pullback that violates short-term structure |
| Line of least resistance | ADX > 25 + MA slope positive |
| 3% noise filter | ATR-based filter (~ 1× daily ATR) |
| 6% reaction threshold | ATR-based filter (~ 2.5× daily ATR) |
| Hand-drawn ledger | Pine Script + TradingView alerts |

**Key insight**: The TOOLS have evolved, but Livermore's framework — **identify the line of least resistance, trade only at pivotal points, cut losses fast** — IS the modern momentum-trading system. You're not learning something obsolete; you're learning the original blueprint.

---

## Part 11 — Putting It All Together (The Livermore Stack)

You now have three Livermore-derived layers in your knowledge base:

| Layer | File | What It Provides |
|-------|------|-----------------|
| **Philosophy** | [36_Livermore_Rules_Reminiscences.md](36_Livermore_Rules_Reminiscences.md) | The mindset, discipline, lessons |
| **Mechanics** | This file (40) | The mathematical system, pivots, line of least resistance |
| **Modern execution** | [04_VCP_Pattern_Playbook.md](04_VCP_Pattern_Playbook.md) + [12_Perfect_Entry_Exit.md](12_Perfect_Entry_Exit.md) | How to execute in 2026 |

Use them together:
- Philosophy keeps you disciplined during stress
- The Market Key tells you WHEN to act (pivot identification)
- Modern execution gives you specific entry/stop levels

---

## Related Files
- [[36_Livermore_Rules_Reminiscences]] — the philosophical companion
- [[34_Advanced_Technical_Analysis]] — modern equivalents (BOS, CHoCH, ADX)
- [[04_VCP_Pattern_Playbook]] — pivotal points as VCP breakouts
- [[11_TradingView_Pine_Script]] — implementing Market Key in code
- [[12_Perfect_Entry_Exit]] — pyramiding aligned with line of least resistance
- [[14_Backtesting_Framework]] — backtesting Market Key triggers historically
