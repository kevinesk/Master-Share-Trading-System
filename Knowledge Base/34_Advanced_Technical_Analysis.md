# Advanced Technical Analysis — The Synthesis Layer

This file is the bridge between knowing individual patterns ([07](07_Technical_Chart_Patterns.md), [04](04_VCP_Pattern_Playbook.md), [08](08_Wyckoff_Method_VSA.md), [13](13_Bollinger_Bands_Oscillator.md), [17](17_Elliott_Wave_Fibonacci.md)) and *combining them into high-conviction decisions*. The edge is rarely in any single indicator — it's in the confluence.

> "One indicator is a guess. Two is an opinion. Five aligned is an edge."

---

## Part 1 — Multi-Timeframe Analysis (MTF)

The #1 mistake intermediate traders make is trading one timeframe in isolation. Every trade must align across at least 3 timeframes.

### The Standard KLSE MTF Stack

| Timeframe | What It Tells You | Used For |
|-----------|------------------|----------|
| **Monthly** | Long-term Stage (Weinstein) — is this a multi-year bull or bear? | Filter: only trade Stage 2 longs |
| **Weekly** | Position trend — is this stock in a sustained uptrend? | Setup identification (VCP, base) |
| **Daily** | Tactical setup — entry zone, base structure, breakout | Entry & stop placement |
| **Hourly** | Execution timing — best price within today | Fine-tune entry; avoid bad fills |

### The MTF Alignment Rule (Top-Down)

Trade direction must agree at **all three primary timeframes** before entry:

```
Monthly: Higher highs, higher lows. Above 20-month MA.        ✓
Weekly:  EMA10 > EMA30 > EMA40. RS line rising.                ✓
Daily:   EMA10 > EMA20 > EMA50. Pulling back to support OR    ✓
         breaking out of VCP.
```

If any one timeframe disagrees → no trade. Wait.

### Conflict Resolution

| Monthly | Weekly | Daily | Action |
|---------|--------|-------|--------|
| Up | Up | Up | Full position — best setup |
| Up | Up | Down | Look for daily pullback BUY (lower-risk entry) |
| Up | Down | Down | No trade. Weekly trend broken. |
| Down | Up | Up | Counter-trend — half-size only, tight stop |
| Down | Down | Up | Avoid. Likely a dead-cat bounce. |

### KLSE Practical Workflow

Each Sunday:
1. Run [KLSE Screener] for stocks meeting Trend Template
2. For each candidate, pull up the **monthly** chart first — reject anything not in clear Stage 2
3. Then **weekly** — confirm VCP/base structure forming
4. **Daily** — identify exact pivot and stop level
5. On Monday morning, **hourly** — wait for the cleanest entry within the day

---

## Part 2 — Market Structure (HH/HL & LH/LL)

The simplest, most under-rated TA framework. Price doesn't lie — structure does.

### The Two Possible States

**Uptrend (Stage 2)** = Higher Highs AND Higher Lows
```
              HH
        HH    /\    HH
        /\   /  \   /\
   HL  /  \ /    \ /  \
   /\ /    HL     HL
__/  HL
```

**Downtrend (Stage 4)** = Lower Highs AND Lower Lows
```
__
  \    LH
   \   /\    LH
    \ /  \   /\
    LH    \ /  \    LH
           LL    \   /\
                  LL
```

### How to Mark Structure on a Chart

1. On the daily chart, identify the most recent **major** swing high and swing low (use peaks/troughs that stand out)
2. Mark them with horizontal lines
3. The current candle is either: making a new HH, making a new HL, breaking a prior LH, or breaking a prior LL

### The 4 Structure Signals (Trade These)

| Signal | What It Means | Action |
|--------|--------------|--------|
| **Break of Structure (BOS) up** | Price breaks above the prior swing high | Trend continuation — entry on retest |
| **Break of Structure (BOS) down** | Price breaks below the prior swing low | Trend continuation down — EXIT longs |
| **Change of Character (CHoCH) up** | First higher high after a downtrend | Possible Stage 1 → Stage 2 transition — start watching |
| **Change of Character (CHoCH) down** | First lower low after an uptrend | Trend ending — tighten stops or exit |

### CHoCH = The Early Warning System

Most traders see Stage 2 → 3 → 4 transitions far too late. CHoCH spots them at the inflection point:

- In an uptrend (HH/HL), the first time price makes a **lower low** = CHoCH down = uptrend in jeopardy
- Tighten stops to last HL immediately
- Do not add to position until structure is repaired (new HH)

---

## Part 3 — Trend Strength Measurement

Knowing the direction is not enough. You need to know the *strength* — strong trends grant runway; weak trends fail.

### Tool 1: ADX (Average Directional Index)

| ADX Reading | Trend Strength | Action |
|------------|---------------|--------|
| 0–20 | No trend (sideways) | Avoid breakout trades — wait |
| 20–25 | Trend forming | Early — watch for confirmation |
| 25–40 | Strong trend | Optimal — take the trade |
| 40–60 | Very strong trend | Trail stops aggressively; mature |
| 60+ | Extreme — climax risk | Exhaustion likely — don't add |

**Pine setting for KLSE daily**: `ADX(14)` — standard

**Rule**: Only enter breakouts when ADX is **rising AND above 20**.

### Tool 2: Moving Average Slope

The slope of EMA50 tells you trend velocity:

```
Slope = (EMA50_today − EMA50_20_days_ago) / EMA50_20_days_ago × 100
```

| Slope | Reading |
|-------|---------|
| > +5% | Strong uptrend — ideal |
| +1% to +5% | Uptrend forming |
| −1% to +1% | Flat — sideways |
| < −1% | Downtrend |

### Tool 3: Price-to-EMA50 Distance

How far is price above EMA50?

| Distance | Meaning |
|----------|---------|
| 0–5% above | Healthy — entry zone on pullback |
| 5–10% above | Extended — wait |
| 10–20% above | Stretched — climax risk rising |
| 20%+ above | Parabolic — do NOT chase |

**Combined rule**: ADX > 25 AND EMA50 slope positive AND price within 5% of EMA50 = textbook entry zone.

---

## Part 4 — Relative Strength (RS) Deep Dive

Already touched in [02_Minervini_SEPA_KLSE.md](02_Minervini_SEPA_KLSE.md). Here's the advanced layer.

### True Relative Strength vs RSI

| RS (Relative Strength) | RSI (Relative Strength Index) |
|-----------------------|------------------------------|
| Stock price ÷ index price | Momentum oscillator (0–100) |
| Measures leadership vs market | Measures overbought/oversold |
| Rising = outperforming KLCI | High RSI ≠ leadership |

**Do not confuse these.** RS = leadership. RSI = momentum/exhaustion.

### The 4 RS Patterns to Trade

**Pattern A — RS New High Before Price New High** (Strongest)
```
Stock:  ____/\____/\____  (consolidating, near old high)
RS:           ____/\____/  (already at new high)
```
The RS line breaks out BEFORE the price. This is the leader of leaders — institutions are accumulating before the chart shows it. Buy the price breakout.

**Pattern B — RS Holding Up During Market Pullback**
```
KLCI:  /\        /\___
              \  /
               \/
Stock:  /\        /\___  (held flat or up while KLCI fell)
```
Stock that doesn't drop when the market drops will lead when the market rallies.

**Pattern C — RS Diverging Negative** (Warning)
```
Stock:       /\___/\____  (still making new highs)
RS:    /\___/        \__  (failing to make new highs)
```
Price still up but RS rolling over = institutions selling into strength. Tighten stops.

**Pattern D — RS Rotation Signal** (Sector)
- Watch the RS line of a SECTOR (e.g., Banking) vs KLCI
- When banking RS turns up after a downtrend → sector rotation IN
- Buy the leaders in that sector first

### KLSE RS Implementation

Use the **Mansfield RS** formula:

```
Mansfield RS = ((Stock price ÷ KLCI price) ÷ 52-week MA of (Stock ÷ KLCI) − 1) × 100
```

- Above 0 → outperforming KLCI over 52 weeks
- Above +20 → strong leadership
- Below 0 → laggard, avoid

Available in TradingView Pine Script — see [11_TradingView_Pine_Script.md](11_TradingView_Pine_Script.md).

---

## Part 5 — Divergences (Spotting the Hidden Cracks)

A divergence is when price and an indicator disagree. The indicator usually wins.

### Bullish Divergence (Bottom Signal)

```
Price:    \      \       (lower low)
           \      \
            \____/  \____
RSI:      \      ___
           \    /
            \__/      (HIGHER low — divergence!)
```

Price makes a new low; RSI/MACD does NOT. Momentum is fading. Bottom may be forming.

**Action**: Watch for a reversal pattern (double bottom, hammer at support). Divergence alone is not entry — combine with structure.

### Bearish Divergence (Top Signal)

```
Price:        ___      ____   (higher high)
             /   \    /
RSI:    __  ____      ___  (LOWER high — divergence!)
       /  \/    \    /
```

Price makes a new high; RSI/MACD makes a lower high. Buyers are exhausted. Top forming.

**Action**: Move stops up. Take partial profits. Do not add.

### Best Indicators for Divergence

| Indicator | When to Use |
|-----------|------------|
| **RSI(14)** | Most reliable for daily/weekly |
| **MACD histogram** | Best for slower-moving stocks (banks, utilities) |
| **OBV (On-Balance Volume)** | Strongest divergence — institutional money flow |
| **Stochastic** | Faster — useful for short-term tops/bottoms |

### Divergence Rules

1. Divergence must form at **clear** swing points — not random wiggles
2. Multiple-indicator confirmation > single indicator (RSI + OBV together = high conviction)
3. **Hidden divergence** (HH in price + LH in RSI during uptrend) = continuation, not reversal
4. Divergences can stretch — don't front-run; wait for price confirmation

---

## Part 6 — Volume Profile & Volume Confirmation

Beyond just "high volume on breakout." Volume tells you WHERE the smart money is positioning.

### Volume Profile (Horizontal Volume Bars)

A vertical histogram on the right of the chart showing volume traded at each price level:

```
RM7.00 ▌
RM6.80 █████  ← Point of Control (POC) — most volume here
RM6.60 ███
RM6.40 ███████ ← Value area high
RM6.20 ████████ ← High volume node
RM6.00 ██████
RM5.80 ██  ← Low volume node (price moves fast through here)
```

**Rules**:
- **Point of Control (POC)**: Price level with the most volume traded — strongest support/resistance
- **High Volume Nodes (HVN)**: Areas of acceptance — price respects these
- **Low Volume Nodes (LVN)**: Areas of rejection — price moves fast through these
- Use POC as a stop level (just below for longs)

### Volume Patterns to Recognise

| Pattern | Meaning |
|---------|---------|
| **Volume dry-up at base low** | Sellers exhausted — accumulation likely |
| **Climax volume at new high** | Distribution beginning — top forming |
| **Heavy volume on red bars** | Distribution (selling) |
| **Heavy volume on green bars** | Accumulation (buying) |
| **Volume divergence from price** | Trend losing energy |

### The Pocket Pivot (Minervini Concept)

A 1-day volume signal inside a base:
- Daily volume **higher than the highest down-volume day of the past 10 days**
- Price closes up in the upper half of the day's range
- Stock is in a Stage 2 base, near EMA10

**Why it matters**: Pocket pivots often precede breakouts by 1-3 weeks. They're early-entry signals for the patient trader.

---

## Part 7 — Confluence Stacking (The Edge)

A single signal is noise. Five aligned signals is conviction. Build a checklist and only trade when 5+ items align.

### The Master Confluence Checklist (10 items)

For any KLSE long entry, score each:

| # | Signal | Pass? |
|---|--------|-------|
| 1 | Monthly chart: Stage 2 confirmed (above 20M MA) | □ |
| 2 | Weekly chart: HH/HL structure intact | □ |
| 3 | Daily chart: VCP or valid base pattern complete | □ |
| 4 | Trend Template (8/8 ideally, ≥6 minimum) | □ |
| 5 | ADX > 25 AND rising | □ |
| 6 | Price within 5% of EMA50 (not extended) | □ |
| 7 | RS line at or near new high | □ |
| 8 | Sector RS positive vs KLCI | □ |
| 9 | Volume contraction in base, surge on breakout day | □ |
| 10 | KLCI > EMA50 (macro support) | □ |

**Scoring**:
- 9–10 ✓ = Full position (max risk 2%)
- 7–8 ✓ = Half position
- 5–6 ✓ = Quarter position or skip
- <5 ✓ = No trade

### Confluence vs Curve-Fitting

There's a fine line. Confluence is using **independent** signals (trend + structure + volume + RS). Curve-fitting is using **redundant** signals (3 momentum indicators all saying the same thing).

Good confluence: ADX (trend strength) + RS (leadership) + Volume (institutional activity) = 3 independent confirmations.
Bad confluence: RSI + Stochastic + MACD = all saying the same momentum thing.

---

## Part 8 — Common Advanced Mistakes (Avoid)

### Mistake 1: Overlaying 8 Indicators
More indicators ≠ better. Pick 3-4 you understand deeply. Master them. Ignore the rest.

### Mistake 2: Ignoring the Higher Timeframe
Trading a daily breakout while the weekly is in a downtrend is fighting the bigger force. Always check higher timeframes first.

### Mistake 3: Counting Waves Religiously (Elliott)
Elliott Wave is descriptive, not predictive in real-time. Use it for context, not as a trade trigger. See [17_Elliott_Wave_Fibonacci.md](17_Elliott_Wave_Fibonacci.md).

### Mistake 4: Trading Pure Patterns Without Trend
A textbook cup-and-handle in a Stage 4 stock is a trap. Pattern + Stage 2 trend is the rule.

### Mistake 5: Using Indicators on Illiquid Stocks
KLSE small caps with <100,000 average daily volume can manipulate indicators with single trades. Stick to liquid stocks (top 200 by ADV) for technical work.

---

## Part 9 — The Daily TA Workflow (15 minutes)

After market close, run this on your watchlist:

```
1. Open monthly chart        — Is it Stage 2?               (1 min)
2. Open weekly chart         — Is structure HH/HL?          (1 min)
3. Mark daily key levels     — Pivot, stop, target          (2 min)
4. Check ADX                 — > 25 rising?                 (30 sec)
5. Check RS line             — Near new highs?              (30 sec)
6. Check volume profile      — POC and HVN levels?          (2 min)
7. Check for divergences     — RSI/OBV vs price             (2 min)
8. Score confluence (1-10)   — Above? Trade. Below? Skip.   (2 min)
9. Set TradingView alerts    — Pivot, stop, target          (2 min)
10. Update journal             — Plan for tomorrow            (2 min)
```

15 minutes. Done. Walk away.

---

## Related Files
- [[07_Technical_Chart_Patterns]] — pattern library
- [[04_VCP_Pattern_Playbook]] — the highest-priority KLSE setup
- [[08_Wyckoff_Method_VSA]] — accumulation/distribution detection
- [[02_Minervini_SEPA_KLSE]] — Trend Template foundation
- [[12_Perfect_Entry_Exit]] — converting TA signals to executable trades
- [[11_TradingView_Pine_Script]] — implementing these indicators in code
