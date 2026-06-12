# Stock Valuation Methods — Pricing What You Buy

> "Price is what you pay. Value is what you get." — Warren Buffett

This file complements [29_Reading_Financial_Statements.md](29_Reading_Financial_Statements.md). That file shows you how to read the books. This file shows you how to **translate numbers into a fair price** and decide if the market is overpaying or underpaying.

For a KLSE momentum trader, valuation is not the primary signal (technical setup is). But it answers a critical question: **"Am I buying a great stock or a falling knife?"**

---

## Part 1 — Why Valuation Matters Even for Technical Traders

A perfect VCP breakout on a stock priced at 60× P/E with declining earnings is a trap. Valuation tells you:

1. **Margin of safety** — how much downside protection if the trade goes wrong
2. **Holding capacity** — can you hold through a -15% pullback because you know it's worth more?
3. **Filter quality** — separates leaders from speculation

**Rule**: Run technical screen first. Run valuation second. Reject any stock failing BOTH checks.

---

## Part 2 — The Five Core Valuation Multiples

### Multiple 1: Price-to-Earnings (P/E)

```
P/E = Price per share / Earnings per share (EPS)
```

**What it tells you**: How many years of current earnings you're paying for.

| P/E Range | Interpretation | KLSE Context |
|-----------|---------------|--------------|
| < 8 | Deep value or distressed | Plantations in down cycle, troubled banks |
| 8–15 | Reasonable | Most mature KLSE blue chips (CIMB, MAYBANK, PBBANK) |
| 15–25 | Growth premium | Tech, consumer (NESTLE, F&N) |
| 25–40 | High growth pricing | Glove makers in 2020-style boom |
| 40+ | Speculative / story stock | Watch carefully |

**Forward P/E vs Trailing P/E**:
- Trailing = uses last 12 months earnings (real, reported)
- Forward = uses next 12 months estimated earnings (projection, often optimistic)
- Use TRAILING as your anchor. Forward is for sanity-check only.

**KLSE-specific traps**:
- Banks: low P/E (8-12) is normal — they're capital-heavy
- REITs: don't use P/E — use Distribution Yield instead
- Cyclicals (plantation, oil & gas): low P/E at the TOP of cycle, high P/E at BOTTOM (counter-intuitive)

### Multiple 2: PEG Ratio (P/E to Growth)

```
PEG = P/E ÷ Earnings Growth Rate (%)
```

**Why it matters**: A P/E of 25 sounds expensive — unless the company is growing earnings 35% per year. PEG normalises this.

| PEG | Interpretation |
|-----|---------------|
| < 1.0 | Undervalued relative to growth |
| 1.0–1.5 | Fairly valued |
| 1.5–2.0 | Slightly expensive |
| > 2.0 | Expensive — price ahead of growth |

**Example**:
- Stock A: P/E 12, growth 8% → PEG = 1.5 (slightly expensive)
- Stock B: P/E 22, growth 25% → PEG = 0.88 (cheaper for the growth!)

**Caveat**: Growth rate must be sustainable. Don't use one-off pandemic growth.

### Multiple 3: Price-to-Book (P/B)

```
P/B = Price per share / Book value per share (NTA)
```

**What it tells you**: What you pay vs the company's net asset value.

| P/B | Interpretation |
|-----|---------------|
| < 1.0 | Trading below book — possible value (or trouble) |
| 1.0–2.0 | Reasonable for asset-heavy businesses (banks, property) |
| 2.0–5.0 | Premium for ROE quality |
| > 5.0 | Asset-light businesses (tech, brands) — judge with ROE |

**Critical rule**: P/B is meaningful only when paired with ROE.

```
A stock with P/B 1.5 and ROE 18% → great (earning 18% on capital)
A stock with P/B 3.0 and ROE 6%  → expensive (earning only 6% on premium-priced capital)
```

**Rule of thumb (Buffett-style)**: P/B ≤ (ROE / Cost of equity). If cost of equity is 10%, ROE 20% → P/B up to 2.0 is justified.

### Multiple 4: EV/EBITDA (Enterprise Value to EBITDA)

```
EV = Market Cap + Total Debt − Cash
EBITDA = Earnings Before Interest, Tax, Depreciation, Amortisation
```

**Why it's better than P/E** for capital-heavy companies:
- Strips out the effect of debt structure
- Strips out non-cash depreciation
- Compares businesses with different capital structures fairly

| EV/EBITDA | Interpretation |
|-----------|---------------|
| < 6 | Cheap |
| 6–10 | Fair |
| 10–15 | Premium |
| > 15 | Expensive |

**Best for**: Property, telco, utilities, capital-intensive businesses
**Not great for**: Banks (EBITDA doesn't apply to financial businesses), REITs

### Multiple 5: Dividend Yield

```
Dividend Yield = Annual DPS / Price per share × 100
```

| Yield | Interpretation |
|-------|---------------|
| 0–2% | Growth stock — reinvesting earnings |
| 2–4% | Standard |
| 4–6% | Income-oriented (banks, telcos, REITs) |
| 6–10% | High income — verify sustainability |
| > 10% | Warning: either trap or distressed |

**Sustainability check**: Payout ratio = Dividends / Net profit. If > 80%, dividend may be cut.

**KLSE context**:
- MAYBANK historical yield: ~6%
- PBBANK: ~4-5%
- KLCC: ~5%
- AXIATA: variable, lower yield
- Sunway REIT, IGB REIT: 5-7% typical

---

## Part 3 — Discounted Cash Flow (DCF) Basics

The most rigorous valuation method. Calculates the present value of all future free cash flows.

### The Formula (Simplified)

```
DCF Value = Σ (FCF_t / (1+r)^t) for t=1 to N + Terminal Value / (1+r)^N
```

Where:
- FCF_t = Free Cash Flow in year t
- r = Discount rate (cost of capital, usually 8–12%)
- N = Forecast period (usually 5–10 years)
- Terminal Value = FCF_N+1 / (r − g), where g = perpetual growth rate

### The Quick DCF (For Mental Estimation)

For a KLSE retail trader, full DCF is overkill. Use this simplified version:

**Step 1**: Estimate next year's FCF (use last year as proxy, adjust for trend)
**Step 2**: Apply a growth multiple based on growth rate:

| Sustainable Growth | Fair Multiple of FCF |
|-------------------|---------------------|
| 0–3% | 10–12× |
| 3–6% | 12–16× |
| 6–10% | 16–22× |
| 10–15% | 22–30× |
| 15%+ | 30×+ (high uncertainty) |

**Step 3**: Multiply FCF × Multiple = Fair Equity Value
**Step 4**: Divide by shares outstanding = Fair Value per share

**Example**: Stock with FCF RM500M, growth ~6%, shares 1 billion:
```
Fair Value = RM500M × 16 = RM8 billion
Per share = RM8 billion / 1 billion = RM8.00
```
If trading at RM6.00 → 25% margin of safety.

### Discount Rate Cheat Sheet (KLSE)

| Company Type | Discount Rate |
|-------------|---------------|
| Stable utility/REIT | 7–9% |
| Blue-chip bank/consumer | 9–11% |
| Mid-cap industrial | 11–13% |
| Small-cap growth | 13–16% |
| High-risk / speculative | 16%+ |

---

## Part 4 — Dividend Discount Model (DDM)

Best for: Stable, dividend-paying stocks (banks, REITs, utilities, telcos).

### The Gordon Growth Model

```
Fair Value = Next Year's Dividend / (Discount Rate − Growth Rate)
```

**Example**: MAYBANK paying RM0.60 DPS, growing 4%, discount rate 10%:
```
Fair Value = RM0.60 / (0.10 − 0.04) = RM10.00
```

If MAYBANK trades at RM8.50 → 15% undervalued by DDM.

**Limits**:
- Only works when growth < discount rate
- Useless for non-dividend stocks
- Sensitive to growth assumption (small change = big swing)

### When DDM Works Best on KLSE

- MAYBANK, CIMB, PBBANK, HLBANK (stable dividend payers)
- MAXIS, AXIATA, TM (telco)
- Sunway REIT, IGB REIT, KLCC (REITs)
- TNB (utility)

### When NOT to Use DDM

- Tech / growth stocks (low or no dividends)
- Cyclical (plantation in down year — dividend may be zero)
- Distressed (dividend cut imminent)

---

## Part 5 — Economic Moat Analysis (Buffett's Framework)

A "moat" is a structural competitive advantage that protects long-term returns. Five sources:

### Moat 1: Intangible Assets (Brand, Patents, Licenses)
**Examples**: NESTLE, F&N (brand). Banks (BNM licence).
**Sign**: Pricing power — can raise prices without losing customers.

### Moat 2: Switching Costs
**Examples**: Banks (changing bank is painful). Software companies. Healthcare incumbent providers.
**Sign**: High customer retention rate, even with higher prices.

### Moat 3: Network Effects
**Examples**: Bursa Malaysia itself (only exchange). Public Bank's branch density.
**Sign**: Each new user makes the service more valuable.

### Moat 4: Cost Advantages
**Examples**: SD Plantation (large-scale CPO production). Large refineries.
**Sign**: Lowest-cost producer; competitors can't match price profitably.

### Moat 5: Efficient Scale
**Examples**: TENAGA (power transmission monopoly). PLUS (highway concessions).
**Sign**: Market large enough for only one or few players; deterring entry.

### Moat Quality Scorecard

| Moat Width | Sustainability | KLSE Examples |
|-----------|---------------|---------------|
| Wide | 20+ years | NESTLE, PETRONAS Chemicals, MAYBANK |
| Narrow | 5-20 years | TOPGLOVE, SUPERMX (cyclical) |
| None | <5 years | Most small-cap industrials |

**Why this matters**: Wide-moat companies sustain pricing power → grow earnings → justify higher multiples. Narrow/no-moat companies are competing on price → margin pressure → multiples compress.

---

## Part 6 — Porter's Five Forces (Industry Analysis)

Before buying any stock, evaluate the industry it operates in. Five forces determine industry profitability:

### Force 1: Threat of New Entrants
**High threat** = low barriers, easy to start → margins eroded
**Low threat** = high capital/regulatory barriers → protected margins

**KLSE example**: Banking has low entry threat (BNM licence required, capital requirements high) → protected margins.

### Force 2: Bargaining Power of Suppliers
**High supplier power** = few suppliers, switching costly → squeezed margins
**Low supplier power** = many suppliers, commoditised → flexibility

**KLSE example**: Glove makers depend on natural rubber suppliers — supplier power moderate.

### Force 3: Bargaining Power of Buyers
**High buyer power** = concentrated buyers, price-sensitive → margins squeezed
**Low buyer power** = fragmented buyers → pricing flexibility

**KLSE example**: Banks have low buyer power (millions of retail customers, can't negotiate).

### Force 4: Threat of Substitutes
**High substitute threat** = alternatives easy → demand caps
**Low substitute threat** = essential, no alternative → durable demand

**KLSE example**: TENAGA — electricity has no substitute → demand stable.

### Force 5: Competitive Rivalry
**High rivalry** = many similar competitors → price wars
**Low rivalry** = few competitors, differentiated → stable margins

**KLSE example**: Telco (3 major: Maxis, CelcomDigi, U Mobile) — moderate rivalry but rational.

### The Industry Score

For each force, rate: Favourable (+1), Neutral (0), Unfavourable (-1). Sum:

| Score | Industry Attractiveness |
|-------|------------------------|
| +4 to +5 | Highly attractive — high sustained ROE |
| +1 to +3 | Average |
| 0 to -2 | Difficult — cyclical/competitive |
| -3 to -5 | Avoid — structurally unprofitable |

---

## Part 7 — Management Quality Assessment

Companies don't make money — people do. A great business with bad management destroys value.

### The 8 Management Quality Checks

| # | Question | Where to Find |
|---|----------|---------------|
| 1 | Insider ownership ≥ 10%? | Annual report — directors' shareholding |
| 2 | Insider buying in last 6 months? | Bursa announcements (Form 29A/29B) |
| 3 | CEO tenure ≥ 5 years? | Annual report |
| 4 | Capital allocation: are profits reinvested at ≥ 12% ROE? | 5-year ROE trend |
| 5 | Dividend policy consistent (not erratic)? | 5-year DPS history |
| 6 | No history of issuing shares at low prices? | Share count history |
| 7 | Clear strategy communicated annually? | Chairman's statement, MD&A |
| 8 | No major related-party transactions? | Notes to accounts |

**Score**: 7-8 ✓ = strong management. <5 ✓ = caution.

### Red Flags (Drop the Stock)

- CEO changes every 1-2 years
- Multiple rights issues during shareholder dilution
- Large director sales just before disappointing results
- Auditor qualifications or resignations
- Frequent profit guidance revisions downward

---

## Part 8 — Earnings Forecast & Surprise

### Why Earnings Forecasts Matter

Stock prices move on the gap between **expectation** and **reality**. A stock can drop 15% on "good" earnings if analysts expected better. And vice versa.

### Where to Find KLSE Estimates

- Bursa Marketplace (free, basic consensus)
- iSaham (free + paid tiers)
- Bloomberg Terminal (institutional)
- CGS-CIMB, Maybank IB, RHB research reports
- ShareInvestor (broker estimates)

### The 4 Earnings Surprise Outcomes

| Result vs Estimate | Likely Price Reaction |
|-------------------|----------------------|
| Beat + raised guidance | +5% to +15% over 1-2 weeks |
| Beat + flat guidance | +0% to +5% |
| In-line | Neutral; depends on guidance |
| Miss + lowered guidance | -10% to -25% — exit immediately |

### The "Whisper Number" Effect

For high-profile KLSE stocks, the "official consensus" may be lower than the actual market expectation. If a stock has rallied 15% into earnings, the bar is higher than the printed estimate. Be cautious.

### Earnings Trading Rules

1. **Never hold full position into earnings** unless you have a long-term thesis
2. Take 50% off the day before earnings — keep your runners only on conviction names
3. If earnings miss: exit at market open, don't hope
4. If earnings beat AND breakout: add on the breakout retest, not the first spike

---

## Part 9 — The Combined Valuation Score (KLSE Practical)

For any stock, score 0-10 across these 10 metrics:

| # | Metric | Score 1 | Score 0 |
|---|--------|---------|---------|
| 1 | P/E < industry average | 1 | 0 |
| 2 | PEG < 1.5 | 1 | 0 |
| 3 | P/B reasonable for ROE | 1 | 0 |
| 4 | EV/EBITDA < 10 | 1 | 0 |
| 5 | Dividend yield ≥ 3% AND sustainable | 1 | 0 |
| 6 | DCF fair value ≥ 20% above price | 1 | 0 |
| 7 | Wide or narrow moat present | 1 | 0 |
| 8 | Industry Porter score ≥ +2 | 1 | 0 |
| 9 | Management quality 6+ / 8 | 1 | 0 |
| 10 | Earnings momentum positive (3 consecutive growth quarters) | 1 | 0 |

**Combined with technical confluence** (from [34_Advanced_Technical_Analysis.md](34_Advanced_Technical_Analysis.md)):

| Technical Score | Valuation Score | Action |
|----------------|-----------------|--------|
| 9-10 | 7-10 | A-grade — full position |
| 9-10 | 4-6 | Trade but tight stops — pure momentum |
| 5-8 | 7-10 | Investment, not trade — long horizon |
| 5-8 | 4-6 | Pass |
| <5 | Any | No trade |

---

## Part 10 — The KLSE Valuation Workflow (30 minutes)

For each candidate stock from your screen:

```
1.  Pull the latest quarterly report (5 min)
    — Income, balance, cash flow snapshots

2.  Calculate the 5 multiples (10 min)
    — P/E (trailing), PEG, P/B, EV/EBITDA, Yield

3.  Apply Quick DCF (5 min)
    — Estimate FCF × multiple = fair value
    — Compare to current price

4.  Moat check (3 min)
    — Identify which moat(s) exist; rate width

5.  Management check (3 min)
    — Run the 8-point checklist

6.  Score 0-10 on the combined card (2 min)

7.  Decision (2 min)
    — Combine with technical score from Part 9
    — Position size accordingly
```

---

## Related Files
- [[29_Reading_Financial_Statements]] — read the books first
- [[28_Corporate_Actions_Bursa]] — dividends, rights, splits affect valuation
- [[16_Sector_Playbooks]] — sector-specific valuation norms
- [[27_Quantitative_Stock_Screening]] — quant filters using these metrics
- [[34_Advanced_Technical_Analysis]] — combine TA + FA = strongest edge
- [[22_Trading_Masters_Biographies]] — Buffett, Lynch, Greenblatt approaches
