# Position Size Calculator — KLSE
**Status**: MANDATORY pre-trade calculation. Non-negotiable.
**Built after**: RHB sizing mistake 2026-05-20 (32.9% portfolio in one stock)

---

## 🚨 The One Rule That Saves Accounts

> **No single position exceeds 10% of total portfolio at entry. Target 5–7%. Calculate units BEFORE clicking buy.**

---

## 📐 The Three Formulas

### Formula 1 — Maximum Units (Hard Cap)
```
MAX UNITS = (Portfolio Value × 0.10) ÷ Entry Price
```

### Formula 2 — Target Units (Normal Trade)
```
TARGET UNITS = (Portfolio Value × 0.07) ÷ Entry Price
```

### Formula 3 — Conservative Units (Bucket B / Defensive)
```
CONSERVATIVE UNITS = (Portfolio Value × 0.05) ÷ Entry Price
```

**Then round DOWN to nearest 100 (Bursa lot size).**

---

## 💰 Worked Examples (Portfolio = RM 30,000)

| Stock | Entry | Max (10%) | Target (7%) | Conservative (5%) |
|---|---|---|---|---|
| Penny share | RM 0.50 | 6,000 units | 4,200 units | 3,000 units |
| Mid-cap | RM 2.50 | 1,200 units | 800 units | 600 units |
| RHB | RM 8.23 | 364 → **300** | 255 → **200** | 182 → **100** |
| KLBat | RM 28.00 | 107 → **100** | 75 → **0 (skip)** | 53 → **0 (skip)** |
| PChem | RM 6.50 | 461 → **400** | 322 → **300** | 230 → **200** |

**Lesson**: Expensive stocks (>RM 25) often can't be sized properly on a small portfolio. Skip them OR accept Max-cap only.

---

## 💰 Worked Examples (Portfolio = RM 50,000)

| Stock | Entry | Max (10%) | Target (7%) | Conservative (5%) |
|---|---|---|---|---|
| Penny | RM 0.50 | 10,000 | 7,000 | 5,000 |
| Mid-cap | RM 2.50 | 2,000 | 1,400 | 1,000 |
| RHB | RM 8.23 | 607 → **600** | 425 → **400** | 303 → **300** |
| KLBat | RM 28.00 | 178 → **100** | 125 → **100** | 89 → **0** |
| PChem | RM 6.50 | 769 → **700** | 538 → **500** | 384 → **300** |

---

## 💰 Worked Examples (Portfolio = RM 100,000)

| Stock | Entry | Max (10%) | Target (7%) | Conservative (5%) |
|---|---|---|---|---|
| Penny | RM 0.50 | 20,000 | 14,000 | 10,000 |
| Mid-cap | RM 2.50 | 4,000 | 2,800 | 2,000 |
| RHB | RM 8.23 | 1,215 → **1,200** | 850 → **800** | 607 → **600** |
| KLBat | RM 28.00 | 357 → **300** | 250 → **200** | 178 → **100** |
| PChem | RM 6.50 | 1,538 → **1,500** | 1,076 → **1,000** | 769 → **700** |

---

## 🎯 Which Size to Use? Decision Tree

```
Is the setup A+ quality?
  • TT 8/8 ✅
  • VCP contraction <0.5 ✅
  • Volume dryup confirmed ✅
  • Sector breadth healthy ✅
  • KLCI > 200D ✅
  All 5 yes? → Use TARGET (7%)
  4 of 5 yes? → Use CONSERVATIVE (5%)
  3 or fewer? → SKIP THE TRADE
```

**Use MAX (10%)** only when:
- You're forced to choose Max due to share price (e.g., bank stocks at RM 25+)
- Conviction is exceptional AND market regime is confirmed bull AND it's a Bucket B yield anchor

**Never above 10%.** Ever.

---

## 🧮 Risk-Based Sizing (Advanced — Position Sizing by Stop Distance)

When the stop loss is wider than usual (e.g., volatile small-cap), the position must be SMALLER so dollar-risk stays ≤1% of portfolio.

```
MAX RISK PER TRADE = Portfolio × 0.01     (1% rule — Schwartz/Minervini)

UNITS = (MAX RISK) ÷ (Entry Price − Stop Price)

THEN check: Units × Entry must still be ≤ 10% of portfolio
If it exceeds 10%, use 10% cap (the wider stop just made the trade too rich)
```

### Example: RM 30,000 portfolio, Stock @ RM 5.50, Stop @ RM 5.20

```
Max risk = 30,000 × 0.01 = RM 300
Stop distance = 5.50 − 5.20 = 0.30
Units by risk = 300 ÷ 0.30 = 1,000 units
Cost = 1,000 × 5.50 = RM 5,500 = 18.3% of portfolio ← OVER CAP

Fix: Reduce to 10% cap
Max units = (30,000 × 0.10) ÷ 5.50 = 545 → 500 units
Cost = RM 2,750 = 9.2% ✅
Actual risk = 500 × 0.30 = RM 150 = 0.5% ✅
```

→ **Both rules must pass. Use whichever is more restrictive.**

---

## ⚠️ Position Sizing Mistakes to Avoid

| Mistake | What happens | Fix |
|---|---|---|
| Buying "round number" of units (1,000, 2,000) without calculating | Likely oversized | Always calculate first |
| Going "all-in" on conviction | One bad gap = -30% portfolio | Cap at 10% |
| Pyramiding before profit | Average up on losing trade | Never add to losers; only add at next pivot above |
| Re-entering after stop | Same name multiple times = de facto oversized | Cooling-off period 5 days |
| Not adjusting for portfolio drawdown | Sized for old portfolio value | Recalc weekly from current value |

---

## 📋 Pre-Trade Sizing Checklist

Before EVERY buy order, fill this out (mental or written):

```
Stock: __________
Entry price: RM ______
My portfolio value: RM ______
Setup grade: A+ / A / B / Skip ______

Max units = (Portfolio × 0.10) ÷ Entry = ______ → rounded down to 100s: ______
Target units = (Portfolio × 0.07) ÷ Entry = ______ → rounded down: ______

Stop loss price: RM ______
Stop distance = Entry − Stop = ______
Risk per share = ______
Max risk = Portfolio × 0.01 = ______
Risk-based units = Max risk ÷ Stop distance = ______

Final size = MIN(Target units, Risk-based units, Max units) = ______
Final cost = Final size × Entry = RM ______
Final % of portfolio = ______%

Confirm: Is final % ≤ 10%? Y/N → If N, DO NOT BUY
```

**Place this calculation in your trading journal for every entry.**

---

## 🧠 Mental Model

Think of your portfolio as a fleet of 10–20 ships. Each ship represents one position. If one ship sinks (stock crashes), you still have 9–19 left.

- 32.9% in one stock = 3 ships fused into one mega-ship. If it sinks, you lose 1/3 of the fleet.
- 7% in one stock = healthy ship. If it sinks (stop hits −5%), you lose 0.35% of the fleet. Survivable.

**Diversification across 6–10 names is the only thing that survives a black swan.**

---

## ✅ The Habit That Will Save You Millions

Every time before clicking BUY:
1. Open this file (or recall the formula)
2. Calculate Max + Target + Risk-based
3. Write the final size in your journal
4. Place order

Takes 60 seconds. Saves you from the next RHB-size mistake.

**Discipline at the size box > genius at the chart.**
