# Risk Management & Position Sizing

## The Core Rule: Survive First, Profit Second

> "The first rule of trading is never lose more than you planned to lose."
> — Mark Minervini

A trader who loses 50% needs a **100% gain** just to break even.
A trader who never loses more than 2% per trade can survive 50 bad trades in a row.

---

## The 2% Risk Rule

**Never risk more than 2% of total portfolio on any single trade.**

### Position Size Formula
```
Shares to buy = (Portfolio × Risk%) / (Entry Price – Stop Loss Price)
```

### Example (RM50,000 portfolio)
| Entry  | Stop   | Risk/Share | 2% of Portfolio | Position Size | Lots   |
|--------|--------|------------|-----------------|---------------|--------|
| RM2.50 | RM2.30 | RM0.20     | RM1,000         | 5,000 shares  | 50 lots|
| RM5.00 | RM4.70 | RM0.30     | RM1,000         | 3,333 shares  | 33 lots|
| RM1.00 | RM0.92 | RM0.08     | RM1,000         | 12,500 shares | 125 lots|

**Cap position at 10–20% of portfolio** regardless of calculation result.

---

## Portfolio Allocation Rules

| Market Condition     | Max Open Positions | Max Single Position |
|----------------------|--------------------|---------------------|
| Strong uptrend (KLCI > EMA50, breadth good) | 5–8 | 20% |
| Mixed/choppy         | 2–4                | 12%                 |
| Downtrend or bearish | 0–1 (cash mode)    | 5%                  |

---

## Tranche Entry (Scaling In)

**Never put the full position on day 1.** Use tranches to reduce risk:

### 3-Tranche System
| Tranche | When               | Size         | Condition                 |
|---------|--------------------|--------------|---------------------------|
| 1st     | At breakout        | 50% of plan  | Volume confirms pivot break|
| 2nd     | +5% above entry    | 30% of plan  | Stock holds above pivot    |
| 3rd     | +10–15% above entry| 20% of plan  | Stock still trending up    |

**Stop loss** after all tranches = below 1st tranche entry (not below each individual entry).

---

## Tranche Exit (Scaling Out)

Minervini's approach: take partial profits at targets, let remainder run.

### 3-Stage Exit
| Exit    | When                          | Amount    | Action                    |
|---------|-------------------------------|-----------|---------------------------|
| 1st     | +15–20% gain                  | 1/3 out   | Lock in profit             |
| 2nd     | +30–40% gain                  | 1/3 out   | Trail stop on remainder    |
| 3rd     | When trend breaks (EMA50)     | Final 1/3 | Full exit                  |

**Result**: Average exit across 3 tranches ≈ +25–30% gain even if final 1/3 gives back 10%.

---

## Stop Loss Types

### 1. Initial Hard Stop (Most Important)
- Set at time of entry
- Level: below VCP base low (or 7–8% max from entry)
- **Non-negotiable** — honor this every time

#### ⚠️ ATR-Offset Rule (PAM anti-stop-hunt — MANDATORY)

Never place the stop AT the obvious swing low, round number, or visible base low. Institutional players sweep those levels before reversing the move.

**Rule:** the actual stop in the broker = (obvious level) − **(0.5 to 1.0 × ATR(14))**.

| Volatility | ATR multiplier | When to use |
|---|---|---|
| Low (ATR/Price < 2%) | 0.5 × ATR | Tight names, narrow ranges |
| Normal | 0.7 × ATR | Default |
| High (ATR/Price > 4%) | 1.0 × ATR | Volatile small/mid caps |

**Worked example** — entry RM 5.00, obvious swing low at RM 4.70, ATR(14) = RM 0.12:
- Naive stop: RM 4.70 (gets hunted)
- ATR-offset stop: RM 4.70 − (0.7 × 0.12) = **RM 4.616** → round down to RM 4.61
- Re-size: risk per share is now 0.39 (not 0.30), so position size shrinks ~23%. **This is the cost of the protection.**

**Why this works:** if RM 4.70 was a real support and institutionals sweep it to RM 4.65 before bouncing, you survive. If price genuinely breaks down through 4.70 with conviction, it almost always goes well below 4.65 — your stop fires either way, but you avoid the 4.70 → 4.65 → 4.85 sweep-and-reverse fakeout.

[Source: KB file [59_Adam_Khoo_Piranha_Profits.md](59_Adam_Khoo_Piranha_Profits.md) — PAM Modules 3 & 4]

### 2. Breakeven Stop
- Move stop to entry price after +10% gain
- Ensures you never lose on this trade again

### 3. Trailing Stop (EMA-Based)
- After +15% gain: trail below EMA21 (daily)
- After +25% gain: trail below EMA10 (daily)
- Exit if daily close below trailing EMA on heavy volume

### 4. Profit-Protection Stop
- After +30% gain: stop moved to +15% level
- You now lock in at least 15% profit on this trade

---

## Maximum Drawdown Rules

| Portfolio Drawdown | Action                                          |
|--------------------|-------------------------------------------------|
| –5%                | Review open positions. Are they still valid?    |
| –10%               | Reduce to half position sizes                  |
| –15%               | Close all positions. Go to 100% cash.          |
| –20%               | **Stop trading.** Review system. Wait 2 weeks. |

> If you're down 20%, something is wrong — either the market or your discipline. Fix it before losing more.

---

## Kelly Criterion (Optional Position Sizing)

If you track your trade history:
```
Kelly % = Win Rate – [(1 – Win Rate) / Win:Loss Ratio]
```

Example: 45% win rate, average win 2× average loss:
```
Kelly % = 0.45 – (0.55 / 2.0) = 0.45 – 0.275 = 17.5%
Use HALF Kelly = 8.75% per trade (more conservative)
```

---

## Trading Journal — What to Track

Every trade, record:
| Field              | Example                          |
|--------------------|----------------------------------|
| Stock              | CIMB (1023.KL)                   |
| Setup              | VCP breakout, 3 contractions     |
| Entry date/price   | 2026-05-15, RM8.20               |
| Stop loss          | RM7.65 (–6.7%)                   |
| Target             | RM9.84 (+20%)                    |
| Position size      | 2,000 shares (RM16,400)          |
| Risk amount        | RM1,100 (2.2% of portfolio)      |
| Exit date/price    | 2026-05-28, RM9.20               |
| Profit/Loss        | +RM2,000 (+12.2%)                |
| What went right    | Volume confirmed, held EMA20     |
| What went wrong    | Sold too early — stock went +25% |

Review journal **weekly** to spot patterns in your mistakes.

---

## The Mental Model: Expected Value

Each trade is not about "will I win this one" — it's about expected value over many trades:

```
Expected Value = (Win Rate × Avg Win) – (Loss Rate × Avg Loss)
```

If your system has:
- 40% win rate, average win +15%, average loss –7%:
```
EV = (0.40 × 15%) – (0.60 × 7%) = 6% – 4.2% = +1.8% per trade
```

Over 100 trades × RM10,000 average = **+RM18,000 expected profit**. Stick to the system.

---

## Capital Preservation Priority (Kevin's Rule)

Per the established trading framework:
1. **Macro must be favorable** (KLCI > EMA50, Dow > EMA20) before deploying capital
2. **Never fight the trend** — go to cash when KLCI breaks below EMA50
3. **Quality over quantity** — 5 great setups beat 20 mediocre ones
4. **Sectors matter** — buy the leading sector of the current cycle
5. **Cut losses fast, let winners run** — asymmetric payoff is the edge
