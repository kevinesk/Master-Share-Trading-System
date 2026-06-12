# Quantitative Stock Screening — Multi-Factor Ranking

## What is Factor Investing?

Factor investing = systematically selecting stocks based on proven, persistent drivers of outperformance. Instead of relying on gut feel, you rank ALL stocks by a quantitative score and invest in the top-ranked ones.

**Decades of academic research confirm 5 factors work consistently across markets**:
1. **Value** — cheap stocks outperform expensive ones over time
2. **Momentum** — stocks going up tend to keep going up
3. **Quality** — profitable, efficient companies outperform weak ones
4. **Low Volatility** — less volatile stocks outperform on risk-adjusted basis
5. **Size** — smaller companies outperform larger ones over long periods

---

## The KLSE Multi-Factor Scoring Model

Our KLSE Screener already calculates many of these. This file explains how to combine them into a **single composite score** that ranks all 100 stocks.

### Factor 1: Momentum Score (0–40 points)

| Metric | Points | Calculation |
|--------|--------|------------|
| RS Rating vs KLCI (12M) | 0–15 | RS +30% = 15pts; RS +10% = 10pts; RS 0% = 5pts; RS neg = 0 |
| Trend Template Score | 0–16 | TT score × 2 (max 8×2=16) |
| Price above EMA50 | 0–5 | Above = 5; Below = 0 |
| Price vs 52W High | 0–4 | Within 10% = 4; within 25% = 2; else 0 |

**Max momentum score: 40 points**

### Factor 2: Quality Score (0–30 points)

| Metric | Points | Threshold |
|--------|--------|-----------|
| ROE | 0–8 | ≥20%=8, ≥15%=6, ≥10%=4, ≥7%=2, <7%=0 |
| EPS growth (YoY) | 0–8 | ≥25%=8, ≥15%=6, ≥10%=4, ≥0%=2, neg=0 |
| Profit margin stability | 0–6 | Expanding=6, stable=4, slightly declining=2, negative=0 |
| Debt/Equity | 0–4 | <0.3=4, <0.5=3, <1.0=2, >1.0=0 |
| Free cash flow positive | 0–4 | Yes=4, No=0 |

**Max quality score: 30 points**

### Factor 3: Value Score (0–20 points)

| Metric | Points | Threshold |
|--------|--------|-----------|
| Dividend Yield | 0–8 | ≥6%=8, ≥4%=6, ≥2%=4, ≥1%=2, 0%=0 |
| PE Ratio | 0–6 | ≤12=6, ≤16=4, ≤22=2, ≤30=1, >30=0 |
| P/B Ratio | 0–4 | ≤1.0=4, ≤2.0=3, ≤3.0=2, ≤4.0=1, >4=0 |
| Price vs intrinsic value | 0–2 | Estimated (NTA comparison): below NTA=2, near NTA=1, above=0 |

**Max value score: 20 points**

### Factor 4: Liquidity Score (0–10 points)

| Metric | Points | Threshold |
|--------|--------|-----------|
| Daily turnover | 0–6 | >RM10M=6, >RM5M=4, >RM2M=2, <RM2M=0 |
| Market cap | 0–4 | >RM5B=4, >RM2B=3, >RM1B=2, >RM500M=1, <RM500M=0 |

**Max liquidity score: 10 points**

### Composite Score (Max 100 points)

```
Composite = Momentum (40) + Quality (30) + Value (20) + Liquidity (10)
```

**Rank all 100 stocks by Composite Score. Invest in the top 10–15.**

---

## Factor Score Interpretation

| Composite Score | Grade | Action |
|----------------|-------|--------|
| 75–100 | Elite (A+) | Maximum position size; highest conviction |
| 60–74 | Strong (A) | Full position size |
| 50–59 | Good (B) | Standard position size |
| 40–49 | Average (C) | Half position or watchlist only |
| < 40 | Weak (D) | Do not invest |

---

## Building the Multi-Factor Model in Excel

### Step 1: Pull Data from Our Screener

From `fundamentals_YYYY-MM-DD.json` and `klse_screener` output:
- PE, ROE, DY, EPS, Score → Value and Quality inputs
- RS Rating, TT Score, price vs EMA50 → Momentum inputs

### Step 2: Score Each Factor

```excel
Column A: Ticker
Column B: RS Rating → =IF(B2>=30,15, IF(B2>=10,10, IF(B2>=0,5, 0)))
Column C: TT Score  → =C2*2
Column D: Above EMA50 → =IF(D2="Y",5,0)
... etc.

Column N: Composite Score = SUM(B2:M2)
Column O: Rank = RANK(N2, $N$2:$N$101, 0)
```

### Step 3: Sort by Composite Score Descending

Top 10–15 stocks = your universe for the week.

### Step 4: Apply Technical Filter

From the composite ranking, only trade stocks that ALSO have:
- A valid chart pattern (VCP, Cup, Flag)
- Breakout pending or just confirmed
- Broad market (KLCI) above EMA50

---

## Factor Timing — When Each Factor Works Best

| Market Phase | Best Performing Factor | KLSE Implication |
|-------------|----------------------|-----------------|
| Early recovery | Momentum | Buy recent breakouts, RS leaders |
| Mid-cycle bull | Quality + Momentum | Buy profitable growers at breakouts |
| Late cycle | Quality + Low Volatility | Shift to stable, dividend-paying quality |
| Bear market | Value + Low Volatility | If investing at all: utilities, staples |
| Crash recovery | Momentum (early) | Buy the stocks leading the bounce |

**KLSE-specific factor ranking (based on historical outperformance)**:
1. Momentum (RS Rating) — most powerful factor on KLSE
2. Quality (ROE + earnings growth) — separates lasting winners from pumps
3. Value (PE + DY) — useful in late cycles and sector rotations
4. Low Volatility — defensive; useful in bearish markets

---

## The KLSE "Sweet Spot" Combination

**Stocks in the intersection of Momentum + Quality consistently outperform:**

```
Momentum + Quality stocks = 
  RS Rating > +10% (outperforming KLCI)
  AND TT Score ≥ 7/8
  AND ROE ≥ 15%
  AND EPS growing ≥ 15% YoY
  AND PE ≤ 25 (not absurdly expensive)
```

**Historical observation on global markets**: Stocks meeting all 5 criteria have returned 3–5× the broad market index over 5-year periods.

**In our screener**: Filter for RS > 10%, TT ≥ 7, fundamentals Grade B or above. This intersection is your highest-priority watchlist.

---

## Sector Momentum Factor

**Beyond individual stock factors, rank SECTORS by momentum:**

```
Sector RS Score = Average RS Rating of top 2 stocks in each sector
```

| Sector | RS Score | Rank |
|--------|---------|------|
| Technology | +18% | #1 |
| Banking | +12% | #2 |
| Property | +5% | #3 |
| Plantation | −2% | #4 |
| Utilities | −8% | #5 |

**Rule**: Only invest in stocks from the top 3 ranked sectors. Avoid bottom 2 sectors entirely.

This is pure quantitative sector rotation — no opinion, just numbers.

---

## Rebalancing the Factor Portfolio

**Weekly**: Re-rank all 100 stocks. If a stock falls below composite score 50 → exit.
**Monthly**: Full portfolio review. Update factor scores with latest earnings.

**Entry**: When a stock enters the top 15 AND has a valid technical pattern.
**Exit**: When composite score falls below 40 OR technical stop is hit.

---

## Factor Investing vs Discretionary Trading — Comparison

| Approach | KLSE Multi-Factor | VCP/Minervini |
|----------|-----------------|--------------|
| Entry trigger | Score threshold + technical | VCP breakout + volume |
| Universe | All 100 stocks quantitatively ranked | Only stocks with patterns |
| Number of positions | 8–15 | 4–8 |
| Holding period | Weeks to months | Days to months |
| Required skill | Excel + basic analysis | Pattern recognition |
| Best in | Trending markets with breadth | Strong trend + low volatility |

**Best approach for KLSE retail traders**: Use multi-factor ranking to BUILD your watchlist, then use VCP/Minervini to TIME your entries. Quantitative to filter 100 → 15 stocks. Technical to pick the exact entry from those 15.
