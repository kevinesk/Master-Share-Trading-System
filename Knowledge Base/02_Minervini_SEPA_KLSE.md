# Minervini's SEPA Methodology — Adapted for KLSE

Mark Minervini (2× US Investing Champion) developed SEPA:
**S**pecific Entry Point Analysis — buy only when ALL criteria align.

---

## The Trend Template (Stage 2 Uptrend — Mandatory Entry Condition)

A stock must satisfy ALL 8 criteria to be in a Stage 2 uptrend:

| # | Criterion                                  | KLSE Adaptation                          |
|---|--------------------------------------------|------------------------------------------|
| 1 | Price > 150-day (30-week) MA               | Close > EMA150                           |
| 2 | Price > 200-day (40-week) MA               | Close > EMA200                           |
| 3 | 150-day MA > 200-day MA                    | EMA150 > EMA200                          |
| 4 | 200-day MA trending up ≥ 1 month           | EMA200 slope positive (last 20 bars)     |
| 5 | 50-day MA > both 150-day and 200-day MA    | EMA50 > EMA150 > EMA200                  |
| 6 | Price > 50-day MA                          | Close > EMA50                            |
| 7 | Price ≥ 30% above 52-week low              | (Price / 52W_Low – 1) ≥ 30%             |
| 8 | Price within 25% of 52-week high           | (Price / 52W_High – 1) ≥ –25%           |

> **KLSE note:** Stocks passing all 8 = rare, high-conviction buys. Stocks passing 6–7 = watchlist.

---

## The VCP (Volatility Contraction Pattern)

VCP is the ideal **entry setup** within a Stage 2 stock.

### How to Identify a VCP

1. **Base formation**: Stock consolidates for 3–8 weeks after a prior uptrend
2. **Contractions**: Price swings narrow sequentially (each swing is smaller than the last)
   - Typical pattern: 3 contractions, e.g., –25% → –15% → –8% → pivot
   - Volume must DECREASE with each contraction (supply drying up)
3. **Pivot buy point**: Buy on a breakout above the last contraction's high
   - Ideal: breakout on **1.5–2× average volume** (demand overwhelming supply)
4. **Stop loss**: Below the lowest point of the final contraction

### VCP Contraction Count
```
    High        
     |  \     
     |   \  High
     |    \ /  \
     |     X    \  High
     |    / \    \/  \
     |   /   \   /\   \  ← Pivot buy
Pivot+   /     \ /  \  /\
         C1     C2    C3  ← 3 contractions, each smaller
```

### Valid VCP Checklist
- [ ] Prior uptrend of ≥ 30% (Stage 2)
- [ ] 2–4 contractions visible
- [ ] Each contraction is smaller than the previous (% range narrows)
- [ ] Volume dries up into each contraction low
- [ ] Breakout volume ≥ 1.5× 50-day average volume

---

## SEPA Entry Rules

### Buy Trigger
- Stock must be in Stage 2 (Trend Template ✓)
- VCP or flat base setup present
- **Buy on breakout**: Price crosses ABOVE the pivot point (last contraction high)
- Enter within 1–3% of the pivot (do not chase if > 5% above)

### Position Sizing (Risk-Based)
- Risk no more than **1–2% of total capital** per trade
- Position size = (Capital × Risk%) / (Entry price – Stop loss price)
- Example: RM50,000 capital, 1% risk = RM500 max loss
  - Entry RM2.50, Stop RM2.30 → Risk = RM0.20/share → Buy 2,500 shares (25 lots)

### Stop Loss
- Initial stop: Below pivot base (last VCP low) OR 7–8% below entry, whichever is tighter
- Never move stop FURTHER away (adds risk)
- Move stop to breakeven after +10% gain

---

## Stage Analysis (Stan Weinstein / Minervini)

| Stage | Description          | Action          |
|-------|----------------------|-----------------|
| 1     | Basing / accumulation| Watch, don't buy |
| 2     | Uptrend (markup)     | **BUY here only**|
| 3     | Topping / distribution| Begin selling   |
| 4     | Downtrend (markdown) | Never buy        |

> **Rule**: Only buy Stage 2 stocks. Never try to "catch a bottom" in Stage 4.

---

## Minervini's 7 Risk Rules (Adapted for KLSE)

1. **Never average down** — a stock going against you is telling you something; listen.
2. **Cut losses at 7–8% maximum** — ego has no place in trading.
3. **Let winners run** — trail stop only after +20–25% gain.
4. **Buy only in uptrending markets** — KLCI > EMA50 preferred.
5. **Position size down** in choppy markets — uncertainty = smaller bets.
6. **Never hold through earnings without a plan** — gap risk is real on KLSE.
7. **Pyramiding**: Add to winning positions only (never losers). Add ½ initial position on first pullback to EMA10 after breakout.

---

## RS Rating (Relative Strength vs KLCI)

Minervini focuses on stocks **outperforming the index**.

```
RS Rating = (Stock % change over 12 months) – (KLCI % change over 12 months)
```

A positive RS = stock is stronger than the market.
Aim for RS ≥ +10% (stock outperforming KLCI by 10%+ over the year).

---

## KLSE-Specific Adjustments

- **Thinner liquidity**: KLSE stocks trade far less volume than US. Minimum avg daily volume RM500,000 value (not just share count).
- **Sector rotation**: CPO price drives plantation stocks (SIMEPLT, IOICORP, KLK). BNM rate drives banks. Construction driven by government project announcements.
- **Foreign flow**: Watch for "net foreign buy/sell" data on Bursa — institutional accumulation precedes big moves.
- **Results season**: Avoid holding through earnings unless fundamentals are extremely strong.
- **Penny stocks**: Avoid stocks below RM0.50 — manipulation risk, wide spreads, and poor liquidity.
