# Elliott Wave Theory & Fibonacci for KLSE

## What is Elliott Wave?

Ralph Nelson Elliott (1871–1948) discovered that stock markets move in repetitive wave patterns driven by crowd psychology. The same pattern repeats at every degree of trend — from a 5-minute chart to a century-long chart.

**The core pattern**: Markets move in a **5-wave impulse** (in the direction of the trend) followed by a **3-wave correction** (against the trend).

---

## The 5-3 Wave Structure

### Impulse Waves (Direction of Trend)

```
        5
       / \
      /   \
     3     \
    / \     \
   /   4     \
  1    |      \
 / \   |       \
/   2  |        A
       |         \
       |          B
       |           \
       |            C
       ← 5 waves → ←3 waves→
         (trend)   (correction)
```

**Wave characteristics**:
| Wave | Character | Volume | Investor Mood |
|------|-----------|--------|---------------|
| 1 | Weak start; few believers | Low | Scepticism |
| 2 | Retraces 50–61.8% of Wave 1 | Low | "It was a dead cat bounce" |
| 3 | LONGEST and strongest wave | HIGH | Excitement; public buying |
| 4 | Correction; stays above Wave 1 top | Lower | Profit-taking |
| 5 | Final push; momentum diverges | Often lower than Wave 3 | Euphoria |

**The critical rule**: **Wave 3 is NEVER the shortest impulse wave.** If it is, you've miscounted.

---

## Elliott Wave Rules (Non-Negotiable)

1. **Wave 2 never retraces more than 100% of Wave 1**
   - If it does, the count is wrong. Start over.

2. **Wave 3 is never the shortest impulse wave**
   - Wave 3 must be longer than at least one of Wave 1 or Wave 5

3. **Wave 4 never overlaps into Wave 1's price territory**
   - Exception: diagonal triangles (rare, not for beginners)

If any rule is violated → your wave count is wrong. The market is always right.

---

## Corrective Waves (A-B-C)

After the 5-wave impulse, markets correct in 3 waves (A-B-C):

```
         B
        / \
       /   \
      A     \
     /       C  ← End of correction = new buying opportunity
```

**Wave A**: First leg down; most people think it's just a pullback
**Wave B**: Counter-rally; "the uptrend is resuming!" — trap for bulls
**Wave C**: Final leg down, equals or exceeds Wave A in length; destroys late buyers

**Key insight**: Wave C is where the real damage happens. Don't buy in Wave A or B — wait for Wave C to complete.

---

## Fibonacci — The Mathematical Foundation

Elliott found that wave relationships follow **Fibonacci ratios**:

### Key Fibonacci Ratios
| Ratio | Source | Trading Use |
|-------|--------|-------------|
| 0.382 (38.2%) | Golden ratio derived | Shallow correction target |
| 0.500 (50%) | Not Fibonacci, but respected | Mid-point correction |
| 0.618 (61.8%) | The "golden ratio" | Deep correction target |
| 0.786 (78.6%) | Square root of 0.618 | Very deep correction |
| 1.000 (100%) | Equal move | A=C projections |
| 1.272 (127.2%) | Extension | Wave 3/5 target |
| 1.618 (161.8%) | Golden extension | Wave 3 target (most common) |
| 2.618 (261.8%) | Double extension | Explosive Wave 3 target |

---

## Wave Retracement Relationships

**Wave 2 (retracement of Wave 1)**:
- Typically retraces 50–61.8% of Wave 1
- If shallow (38.2%): expect a strong Wave 3
- If deep (61.8–78.6%): more common; still valid

**Wave 4 (retracement of Wave 3)**:
- Typically retraces 38.2% of Wave 3
- Often shallow because Wave 3 momentum carries into Wave 4

**A-B-C correction (retracement of entire 5-wave impulse)**:
- Typically retraces 38.2–61.8% of the 5-wave impulse
- Wave C often equals Wave A in length

---

## Wave Extension Projections

**Wave 3 (strongest wave)**:
- Typically 161.8% of Wave 1 length (measured from Wave 2 low)
- Can extend to 261.8% in very strong trends

**Wave 5 (final wave)**:
- Typically equals Wave 1 in length
- Or projects to 61.8% of Wave 1+3 combined

**Wave C (corrective)**:
- Typically equals Wave A in length (100%)
- Can extend to 127.2% or 161.8% of Wave A

---

## How to Draw Fibonacci on TradingView

### Fibonacci Retracement (Finding correction targets)
1. Click "Fib Retracement" tool
2. For an uptrend: Click from the Wave 1 start (low) → drag to Wave 1 end (high)
3. Lines appear at 23.6%, 38.2%, 50%, 61.8%, 78.6%
4. These are your expected Wave 2 support levels

### Fibonacci Extension (Finding Wave 3/5 targets)
1. Click "Fib Extension" (or "Trend-Based Fib Extension")
2. Three clicks: Wave 1 start → Wave 1 end → Wave 2 end
3. Lines project forward at 100%, 127.2%, 161.8%, 261.8%
4. These are your Wave 3 and Wave 5 targets

---

## KLSE Practical Elliott Wave Application

### Step 1: Identify the Larger Degree Wave

**Weekly chart**: Are we in an overall Bull (Waves 1–5 up) or Bear (A-B-C down)?
- KLCI above EMA200 and trending up = Bull market impulse → look for Wave 2 dips to buy
- KLCI below EMA200 = Correction or Bear market → do not look for longs

### Step 2: Find Where We Are in the Pattern

**Daily chart**: Count the waves from the most recent low.

Example reading for CIMB:
```
"CIMB completed a 5-wave impulse from RM5.00 to RM8.50.
It is now in an A-B-C correction.
Wave A low is RM7.20, Wave B high is RM8.00.
Currently in Wave C — target RM6.80 (61.8% of full 5-wave impulse).
WAIT for Wave C to complete before buying."
```

### Step 3: Use Fibonacci to Find Entry Zones

- Wave 2 and Wave 4 retracements are the **ideal buy zones** in an uptrend
- Wave C completion is the **best buying opportunity** after a full 5-wave impulse

**Best entry setup**:
1. 5-wave impulse completes
2. A-B-C correction begins
3. Wave C reaches 61.8% Fibonacci retracement of the impulse
4. Wave C low on low volume (Wyckoff spring / no supply)
5. Price turns up — **buy here with stop below Wave C low**

---

## Fibonacci + KLSE Screener Integration

When a stock breaks out (VCP or Cup & Handle):

**Project the target using Fibonacci**:
1. Measure the length of the base (from lowest point to breakout)
2. Project 61.8%, 100%, 161.8% of the base length above the breakout

**Example**:
- MRDIY base: Low RM1.50, breakout at RM2.00. Base height = RM0.50
- 61.8% extension: RM2.00 + (RM0.50 × 0.618) = RM2.31 (1st target)
- 100% extension: RM2.00 + RM0.50 = RM2.50 (2nd target)
- 161.8% extension: RM2.00 + (RM0.50 × 1.618) = RM2.81 (3rd target)

**Use 61.8% target for Tranche 1 exit, 100% for Tranche 2, 161.8% for final tranche.**

---

## Elliott Wave Red Flags — When Your Count Is Wrong

| Signal | What It Means |
|--------|--------------|
| Wave 2 retraces >100% of Wave 1 | Entire count is wrong — restart |
| Wave 4 enters Wave 1's price range | Not a standard impulse — different pattern |
| Wave 3 is the shortest | Misidentified waves — recount |
| Correction deeper than 78.6% | May be a deeper pattern (flat, triangle) |
| Can't label waves without forcing | The count is likely wrong |

**The honest rule**: Elliott Wave is interpretive. Two experienced analysts often disagree on the count. Use it as a **guideline for targets and entry zones**, not as a precise prediction tool.

---

## Fibonacci Confluence — The Highest-Probability Zones

The most powerful support/resistance levels are where multiple Fibonacci relationships converge.

**Example of confluence**:
- Wave A = Wave C at RM6.80
- 61.8% retracement of the full 5-wave impulse = RM6.80
- Previous breakout level (now support) = RM6.75
- Lower Bollinger Band at same time = RM6.82

**→ RM6.78–6.82 is a high-confluence buy zone with very tight stop below RM6.60**

**Confluence tools in TradingView**:
- Fib Retracement + Fib Extension simultaneously
- Add horizontal lines at prior support levels
- Where 3+ Fibonacci levels cluster within 1% = high-confidence entry zone

---

## Quick Reference — Fibonacci Cheat Sheet

### Retracement Levels (for pullback entries)
- 23.6% — Shallow; momentum very strong
- **38.2% — Wave 4 / shallow correction → buy**
- **50.0% — Mid-point → buy cautiously**
- **61.8% — Golden ratio → Wave 2 buy zone (highest confidence)**
- 78.6% — Deep correction; still valid but weakening trend

### Extension Levels (for profit targets)
- 100.0% — Equal move; conservative target
- 127.2% — Modest extension
- **161.8% — Golden extension → Wave 3 primary target**
- 200.0% — Strong extension
- **261.8% — Extreme extension → Wave 3 in parabolic markets**
