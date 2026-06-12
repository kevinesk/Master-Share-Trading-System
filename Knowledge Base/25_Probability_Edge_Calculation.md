# Probability & Edge Calculation

## The Trader's Mindset: Think in Probabilities

A trader does not think "will this trade win?" A trader thinks "this setup wins 48% of the time with 2.5:1 payoff ratio, giving me +1.8% expectancy per trade. Over 100 trades, I expect +180% return."

Every trade is just ONE observation from a distribution. No single trade defines you.

---

## Expected Value (EV) — The Foundation

```
EV = (Probability of Win × Gain) + (Probability of Loss × Loss)
```

**Positive EV = long-term profitable** (if system is followed perfectly)
**Negative EV = long-term losing** (gambling)

**Example trade**:
- 45% chance of winning, average win = +18%
- 55% chance of losing, average loss = −7%

```
EV = (0.45 × 18%) + (0.55 × −7%)
   = 8.1% − 3.85%
   = +4.25% per trade
```

With RM50,000 portfolio and 15% position = RM7,500 per trade:
```
EV per trade in ringgit = RM7,500 × 4.25% = RM318.75
Over 100 trades = RM31,875 expected profit
```

**This is how professional traders think** — not about whether any specific trade wins, but about the long-run expected value of the entire system.

---

## R-Multiple System (Van Tharp's Framework)

Instead of thinking in percentages, think in "R" units:
- **1R** = the amount you risk on one trade (your stop loss distance × position size)

**Examples**:
- If you risk RM1,000 on a trade and win RM2,500 → +2.5R win
- If you risk RM1,000 and lose RM900 (stopped out) → −0.9R loss
- If you risk RM1,000 and lose RM1,100 (slippage past stop) → −1.1R loss

**Why R-multiples work**:
- Every trade is comparable regardless of position size
- Makes expectancy calculation simple
- Psychologically detaches you from the money amount

**Expectancy in R**:
```
E(R) = (Win Rate × Avg Win in R) − (Loss Rate × Avg Loss in R)
```

A well-run system should have E(R) > 0.3R per trade (you make at least 30% of your risk back on average).

---

## Monte Carlo Simulation — What Could Happen?

Monte Carlo simulation runs your system thousands of times with random ordering to show the range of possible outcomes.

**Why it matters**: Even a profitable system can hit a bad streak. Monte Carlo shows you the WORST realistic scenario you should prepare for.

### Manual Monte Carlo (Simple Version)

1. Take your last 50 trade results (in R-multiples)
2. Shuffle them randomly 1,000 times (or use Excel RAND function)
3. Calculate the maximum drawdown for each shuffle
4. The 95th percentile worst drawdown = your "one-in-twenty-year" worst case

**Simple Excel simulation**:
```excel
=RAND()  → generates random number for each trade result reordering
=CUMSUM(trade results in random order)  → equity curve
=MIN(equity curve) → maximum drawdown for this simulation
Run 1,000 times → distribution of max drawdowns
```

### Key Monte Carlo Insights for KLSE Swing Trading

Based on typical VCP system parameters (45% win rate, 2.5:1 R:R):
- 90th percentile worst drawdown: 15–20%
- 95th percentile worst drawdown: 22–28%
- 99th percentile worst drawdown: 30–38%

**Implication**: Size positions so that your 95th percentile drawdown is survivable. If your position sizes would cause 35% drawdown at worst, and you'd quit at 20%, you're sized too large.

---

## Kelly Criterion — Optimal Position Sizing

The Kelly Criterion tells you the mathematically optimal fraction of your capital to risk on each trade.

```
Kelly % = Win Rate − (Loss Rate / Win:Loss Ratio)
```

**Example** (45% win rate, 2.5:1 payoff):
```
Kelly % = 0.45 − (0.55 / 2.5)
        = 0.45 − 0.22
        = 0.23 = 23%
```

This means risking 23% of capital per trade is mathematically optimal for growth.

**But don't use full Kelly!** Full Kelly leads to psychologically devastating drawdowns (50%+).

### Half Kelly and Quarter Kelly

| Sizing | Risk Per Trade | Max Drawdown Risk | Recommended For |
|--------|---------------|------------------|----------------|
| Full Kelly | 23% | ~60–70% drawdown | Too aggressive; avoid |
| Half Kelly | 11.5% | ~30–40% drawdown | Professionals with high confidence |
| Quarter Kelly | 5.75% | ~15–25% drawdown | Most swing traders |
| 2% Rule | 2% | ~10–15% drawdown | Beginners; capital preservation |

**Our system uses the 2% Rule** (file 06) — which is conservative but psychologically sustainable. This is correct for building consistent long-term returns.

---

## The Probability of Ruin

**Ruin** = losing so much capital you can no longer trade effectively (e.g., below RM10,000)

```
Probability of Ruin ≈ ((1-Edge) / Edge)^(Capital/Risk-per-trade)
```

Where Edge = Win Rate − (Loss Rate × (Risk/Reward))

**The practical lesson**: Small position sizes dramatically reduce ruin probability.

| Risk Per Trade | Probability of Ruin (with slight edge) |
|---------------|----------------------------------------|
| 10% | ~15% chance of ruin |
| 5% | ~3% chance of ruin |
| 2% | ~0.1% chance of ruin |
| 1% | ~0.001% chance of ruin |

**This is why the 2% rule is not optional — it's mathematically proven protection.**

---

## Probability Applied: When Should You Stop Trading?

**The Law of Large Numbers** guarantees your edge will manifest — but only if you can STAY IN THE GAME long enough.

### How many consecutive losses are normal?

For a system with 45% win rate:

```
Probability of N consecutive losses = (1 − 0.45)^N = 0.55^N
```

| Consecutive Losses | Probability | Action |
|-------------------|-------------|--------|
| 3 in a row | 16.6% | Normal — happens often |
| 5 in a row | 5.0% | Uncomfortable but normal |
| 7 in a row | 1.5% | Concerning — review rules |
| 10 in a row | 0.25% | Investigate — system may be broken |

**Rule**: Up to 7 consecutive losses = remain in the system (it's still statistically normal).
At 10+ consecutive losses → pause and investigate. Either the market regime has changed, or you've been breaking your rules.

---

## Conditional Probability — Market Context

Your win rate is NOT constant. It changes with market conditions.

**Estimated win rates by market regime**:
| Market Condition | VCP System Win Rate |
|----------------|-------------------|
| KLCI above EMA50, strong breadth | 52–60% |
| KLCI near EMA50, mixed signals | 38–45% |
| KLCI below EMA50, weak breadth | 22–30% |

**Implication**: When KLCI is above EMA50, your system's edge doubles. When below, it nearly disappears. This is why the macro filter (don't trade when KLCI < EMA50) is mathematically justified — it dramatically improves your win rate.

---

## Edge Decay — Why Systems Stop Working

**All edges decay over time** as more traders discover them. Monitor for edge decay:

| Sign | Meaning |
|------|---------|
| Win rate falling 5%+ below historical average over 6 months | Possible edge decay |
| Payoff ratio falling below 1.5 | Market structure changing |
| Expectancy turning negative for 3+ months | System no longer has edge in current market |

**Response to edge decay**: Don't abandon the system immediately (could be a market regime issue). Track for 3–6 months. If performance doesn't recover when the market improves, the edge has decayed and you need to adapt the system.

---

## Intermarket Probability — Using Correlation to Your Advantage

When two asset classes are highly correlated AND you have an edge in one, use the other as a LEADING INDICATOR.

**KLSE application**:
- SOX Index (US semiconductors) leads VITROX/INARI by ~2 weeks
- CPO futures lead plantation stocks by ~1–2 weeks
- US banks (XLF) lead KLSE banking stocks by ~1 week

**Probability enhancement**: If your VCP breakout system gives 45% win rate normally, but you only take the trade when:
1. The leading indicator (SOX for tech stocks) is also trending up
2. The sector RS Rating is positive

Your win rate may improve to 55–62%. This is edge stacking — combining multiple probability enhancers.

---

## The Trader's Probability Checklist

Before each trade, stack your probabilities:

| Factor | Met? | Probability Boost |
|--------|------|------------------|
| KLCI above EMA50 (macro) | ✓/✗ | +8% win rate |
| Stock in Stage 2 (TT 7+/8) | ✓/✗ | +5% win rate |
| VCP pattern (contractions confirmed) | ✓/✗ | +7% win rate |
| Volume surge on breakout (≥2× avg) | ✓/✗ | +5% win rate |
| RS Rating +10% vs KLCI | ✓/✗ | +4% win rate |
| Sector is leading this month | ✓/✗ | +3% win rate |
| Clean chart (no near resistance) | ✓/✗ | +3% win rate |

**All 7 factors met**: Win rate ≈ 60%+ → Maximum position size
**5–6 factors**: Win rate ≈ 50%+ → Standard position size
**3–4 factors**: Win rate ≈ 40%+ → Half position size
**<3 factors**: Win rate below break-even → SKIP THE TRADE

This is probability management in practice.
