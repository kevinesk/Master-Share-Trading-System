# Trading Statistics Essentials

## Why Statistics Matter for Traders

You are running a business. Your edge is the statistical advantage your system has over random chance. Without understanding the numbers, you cannot:
- Know if your system actually has an edge (or if you've been lucky)
- Size positions correctly
- Know when to stop trading (drawdown rules)
- Improve your system methodically

---

## Core Statistical Concepts for Traders

### 1. Mean (Average) and Expectancy

**Trade expectancy** = your average profit/loss per trade, accounting for win rate.

```
Expectancy = (Win Rate × Average Win) − (Loss Rate × Average Loss)
```

**Example**:
- Win rate: 45%
- Average win: +15%
- Average loss: −7%

```
Expectancy = (0.45 × 15%) − (0.55 × 7%)
           = 6.75% − 3.85%
           = +2.9% per trade
```

This means: Over 100 trades with 10% position size, you expect to make +2.9% per trade on average.

**What a good system looks like**:
| System Type | Win Rate | Avg Win | Avg Loss | Expectancy |
|-------------|----------|---------|---------|-----------|
| Trend following | 35–45% | +20% | −8% | +2.9% |
| Mean reversion | 55–65% | +8% | −12% | +0.05% |
| VCP/Minervini | 45–55% | +18% | −7% | +4.2% |
| Random | 50% | +10% | −10% | 0% |

**Key insight**: You do NOT need to be right most of the time to make money. A 40% win rate with a 2.5:1 win:loss ratio is very profitable.

---

### 2. Standard Deviation — Measuring Consistency

Standard deviation measures how spread out your trade results are.

**Low standard deviation**: Consistent results (good — predictable performance)
**High standard deviation**: Erratic results (concerning — outcomes are random-feeling)

**For your trading journal**, calculate:
```
Std Dev of trade returns = √( Σ(each return - average return)² / number of trades )
```

In Excel: `=STDEV(B2:B101)` where column B has each trade's % return.

**Why it matters**: Two systems can have the same average return but very different risk:
- System A: Average +5%, Std Dev 3% → Sharpe Ratio 1.67 (consistent)
- System B: Average +5%, Std Dev 15% → Sharpe Ratio 0.33 (erratic)

System A is far superior even though the average return is the same.

---

### 3. Sharpe Ratio — Risk-Adjusted Return

```
Sharpe Ratio = (Average Return − Risk-Free Rate) / Standard Deviation
```

- Risk-free rate for Malaysia: Use 3-month MGS yield (≈3.5%)
- Calculate on MONTHLY returns for your trading account

| Sharpe Ratio | Assessment |
|-------------|------------|
| < 0 | Losing money (below risk-free) |
| 0–0.5 | Poor; too much risk for return |
| 0.5–1.0 | Acceptable but improvable |
| 1.0–2.0 | Good |
| 2.0–3.0 | Excellent |
| > 3.0 | Exceptional (Buffett runs ~0.8; top hedge funds 1.5–2.0) |

**Monthly Sharpe in Excel** (after 12+ months of trading):
```excel
=AVERAGE(monthly_returns - 0.29%) / STDEV(monthly_returns)
```
(0.29% = 3.5% annual risk-free rate ÷ 12 months)

---

### 4. Maximum Drawdown — The Gut-Check Number

```
Max Drawdown = (Peak Portfolio Value − Lowest Value After Peak) / Peak × 100
```

**This is the most important risk metric for a trader.**

Why: A system with 30% annual returns but 50% max drawdown is psychologically impossible to trade. You would quit at the bottom and miss the recovery.

**Target drawdowns by strategy**:
| Strategy | Target Max Drawdown |
|----------|-------------------|
| Conservative position trading | < 10% |
| Standard swing trading (our system) | < 20% |
| Aggressive growth | < 30% |
| Venture/speculative | < 50% (institutional grade) |

**Our rule** (from file 06): Stop all trading at −20% portfolio drawdown. Something is wrong with the system or the market.

---

### 5. Win Rate vs Payoff Ratio — The Trade-Off

The most important relationship in trading statistics:

```
Minimum Win Rate to Break Even = 1 / (1 + Payoff Ratio)
```

| Payoff Ratio (Win:Loss) | Minimum Win Rate Needed |
|------------------------|------------------------|
| 1:1 | 50.1% |
| 1.5:1 | 40.0% |
| 2:1 | 33.3% |
| 2.5:1 | 28.6% |
| 3:1 | 25.0% |

**Our VCP system target**: 2–2.5:1 payoff ratio → need only 29–33% win rate to break even. At 45% win rate with 2.5:1 payoff → excellent edge.

---

### 6. Z-Score — Is Your System Performing Normally?

Z-Score tells you if your recent performance is within the normal range of your system, or if something is wrong.

```
Z-Score = (Current Performance − Historical Mean) / Standard Deviation
```

| Z-Score | Interpretation |
|---------|---------------|
| −2 to +2 | Normal variation — stay the course |
| < −2 | Performance significantly below average — review system |
| > +2 | Performance significantly above average — possible luck; don't oversize |
| < −3 | Stop trading — something has fundamentally changed |

**Example**: Your system averages 5% per month (std dev 8%). This month you made −15%.
```
Z-Score = (−15% − 5%) / 8% = −2.5 → Unusual; review system and market conditions
```

---

### 7. Correlation — Are Your Positions Actually Diversified?

**Correlation** measures how two assets move together (−1 to +1):
- +1.0: Move in perfect lockstep (not diversified at all)
- 0: No relationship (fully diversified)
- −1.0: Move in opposite directions (perfect hedge)

**In KLSE context**:
- MAYBANK and CIMB: Correlation ~0.85 (very high — holding both = concentrated banking bet)
- MAYBANK and VITROX: Correlation ~0.3 (acceptable diversification)
- KLCI and REITs: Correlation ~0.5 (some diversification benefit)
- CPO and plantation stocks: Correlation ~0.75 (they move together)

**Rule**: Keep correlation between positions < 0.6. If higher, you're not diversified — you're just running the same bet multiple times.

**In Excel**: `=CORREL(stock1_returns, stock2_returns)` using monthly return data.

---

### 8. Sample Size — How Many Trades Before Your System Is Proven?

This is the most underappreciated concept in trading.

**Minimum sample sizes**:
| Purpose | Minimum Trades |
|---------|---------------|
| Rough indication | 30 |
| Statistical significance | 50 |
| Confident system validation | 100 |
| Robust system validation | 200+ |

**Why 30 trades isn't enough**: With only 30 trades, you could get 15 consecutive winners and still be running a losing system (just got lucky). At 200 trades, luck averages out.

**The gambler's fallacy trap**: After 5 losing trades in a row, many traders abandon a good system. Statistically, 5 consecutive losses in a 45% win-rate system happens ~4% of the time — completely normal. Don't quit.

```
Probability of N consecutive losses = (1 − Win Rate)^N

For 45% win rate, 5 consecutive losses:
= 0.55^5 = 5.0% probability per trade sequence
Over 100 trades → Expected to happen ~3–4 times
```

---

## Building Your Trading Statistics Dashboard

Track these monthly in a spreadsheet:

| Metric | Formula | Target |
|--------|---------|--------|
| Total trades | Count | 8–15/month |
| Win rate | Winners / Total | 40–55% |
| Avg win | Mean of winning trades | +15–20% |
| Avg loss | Mean of losing trades | −6–8% |
| Payoff ratio | Avg Win / Avg Loss | ≥2.0 |
| Expectancy | (WR × Avg Win) − (LR × Avg Loss) | >+2% |
| Profit factor | Gross profit / Gross loss | >1.5 |
| Max drawdown | (Peak − Trough) / Peak | <20% |
| Sharpe ratio | (Return − 3.5%) / Std Dev | >1.0 |

---

## The Law of Large Numbers — Trust Your System

The mathematical guarantee: Over enough trades, your edge WILL manifest.

A system with +2% expectancy per trade will:
- Lose on 55% of individual trades (painful)
- But over 100 trades: produce approximately +2% × 100 = +200% cumulative return

**But only if you follow the rules on EVERY trade.**

Breaking your rules on even 1 in 10 trades can eliminate your edge entirely. This is why statistics and psychology are inseparable — you know your edge mathematically, but fear/greed will tempt you to break the rules on trade #47. Don't.

---

## Quick Calculator: Is Your System Good Enough?

Fill in from your trading journal:

```
Win Rate (W): _____%
Average Win (A): _____%
Average Loss (L): _____%

Payoff Ratio = A / L = _____
Break-even Win Rate = 1 / (1 + Payoff Ratio) = _____%

If W > Break-even Win Rate → Your system has an EDGE ✓
If W < Break-even Win Rate → Your system is losing money ✗

Expectancy per trade = (W × A) − ((1−W) × L) = _____%

Annualised expectancy (assuming 10 trades/month) =
Expectancy × 10 × 12 × Position size = _____
```
