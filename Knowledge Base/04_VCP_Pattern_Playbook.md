# VCP Pattern Playbook — KLSE Edition

## What is VCP?

The **Volatility Contraction Pattern** (Mark Minervini) is a price consolidation that precedes a high-probability breakout. It shows:
- **Supply drying up** (sellers exhausted)
- **Demand quietly accumulating** (institutional buying)
- **Decreasing price volatility** (each swing smaller)

---

## The 3-Step VCP Setup

### Step 1 — Qualify the Stock (Trend Template)
Before looking for VCP, confirm the stock is in Stage 2:
- [ ] Price > EMA50 > EMA150 > EMA200
- [ ] EMA200 is sloping UP
- [ ] Price within 25% of 52-week high
- [ ] Price > 30% above 52-week low

### Step 2 — Find the Contractions
On a weekly chart, look for price pullbacks that are **getting smaller**:

```
VALID VCP (contractions shrinking):
Week chart view:
         ___
        /   \
  ___  /     \___
 /   \/           \___    ← Pivot buy point here
       C1     C2   C3     (3 contractions, volume drops each time)
```

**Contraction Rules:**
- Each pullback (C) must be **smaller in % than the previous**
- Typical: 3 contractions work best (2–4 acceptable)
- Each contraction should take **2–6 weeks** to form
- **Volume must decrease** into each contraction low

**Common contraction depth patterns:**
- Aggressive: 15% → 8% → 4%
- Moderate:   25% → 15% → 8%
- Tight:       10% → 5% → 2.5%

### Step 3 — Define the Pivot Buy Point
- Pivot = highest price of the LAST contraction
- Buy when price closes above pivot on **heavy volume** (≥1.5× 50-day avg)
- The **breakout day** should have the highest single-day volume in weeks

---

## Squeeze vs Surge — They Are SEQUENTIAL, Not Simultaneous

The single most common VCP mistake is treating "low volume squeeze" and "high
volume surge" as two signals that must both be true at the same time. **They
never are.** They are two consecutive stages of one trade:

```
STAGE 1 — THE COIL          STAGE 2 — THE BREAKOUT       STAGE 3 — EXTENDED
Volume DRIES UP             Volume SURGES (≥1.5×)        Volume fades
BB width squeezes tight     Price clears the pivot       Price >3% past pivot
Price sits BELOW pivot      Price AT the pivot           ─────────────────────
→ WATCH — set alert         → BUY (within 3% of pivot)   → TOO LATE — do not buy
   at the pivot
```

**Why waiting for both = becoming a latecomer:** volume only surges *on or after*
the breakout. If you wait for the squeeze AND the surge to both show green, the
breakout has already happened — you buy Stage 3 (extended) and take an instant
paper loss on the first pullback.

**The fix — act on the COIL, not the confirmation:**
1. When the squeeze appears (tight BB, volume dried up, still below pivot) →
   the stock goes on your **watchlist** and you set a TradingView price alert
   exactly at the pivot.
2. The alert fires intraday on the breakout → you buy *in the buy zone*
   (pivot to pivot +3%), not the next day after a daily scan.
3. **Optional starter tranche:** on the *tightest* final contraction, with price
   near the coil low, you may take a **1/3 position** with a stop just below the
   coil low — then add the rest on the breakout. This is the only legitimate
   "before the breakout" entry, and its risk is capped at the coil low.

> The `klse_screener.py` tool implements exactly this: it labels each stock
> **COILING** (watch / optional starter), **BREAKOUT** (buy zone), or
> **EXTENDED** (skip). Backtesting confirms entering on-pivot beats entering
> 3 days late by roughly +0.05R per trade — about a third of the whole edge.

---

## What Makes a VCP FAIL?

| Red Flag                              | What It Means                         |
|---------------------------------------|---------------------------------------|
| Volume increases during contraction   | Stock still under distribution        |
| Price making lower lows below VCP     | Stock in Stage 4, not Stage 2         |
| Contraction widens instead of narrows | Sellers not yet exhausted             |
| Breakout on below-average volume      | Fake breakout — exit quickly          |
| Breakout fails within 3–5 days        | Cut loss immediately (7–8% rule)      |

---

## Entry Timing

### Ideal Entry
1. Stock forms VCP (2–3 contractions visible on weekly chart)
2. Price approaches pivot from below on **drying up volume**
3. On breakout day: strong gap up OR steady climb through pivot with volume surge
4. Enter **at or within 2–3% of pivot** (not after it has already run 10%+)

### Intraday Entry (for better precision)
- Wait for first 30 minutes of trading (9:00–9:30) — let price discover
- If price opens above pivot with volume → enter market
- If price is still below pivot → set a buy-stop limit order at pivot+0.5%
- Cancel order if volume is weak by 11:00 AM

---

## Stop Loss & Exit Rules

### Initial Stop Loss
- Place stop 1–2 ticks below the **lowest point of the final VCP contraction**
- If this implies risk > 8% of entry price → skip the trade (too wide)
- Maximum risk: **2% of total portfolio per trade**

### Trailing the Trade
| After gain of... | Action                                    |
|-----------------|-------------------------------------------|
| +5%              | Nothing — hold through normal pullbacks   |
| +10%             | Move stop to breakeven (entry price)      |
| +15%             | Trail stop to EMA10 (daily)               |
| +20–25%          | Consider taking partial profit (1/3)      |
| +40%+            | Trail tightly — Minervini sells into strength|

### Selling Rules
- **Never let a +10% winner become a loser**
- Sell if: price closes below EMA50 on heavy volume
- Sell if: stock gaps down on heavy volume (distribution)
- Sell if: stock misses earnings badly and drops > 10% in one day

---

## Multi-Stage Pyramid (Advanced)

After a successful VCP breakout, stocks often build a second base before the next leg:

```
Phase 1: Initial VCP breakout → +30% gain
Phase 2: Stock forms a SECOND smaller VCP (3–5 weeks)
Phase 3: Second breakout → add ½ original position
Phase 4: Trail with EMA21 until the trend breaks
```

This pyramid approach lets you **ride big moves** while controlling risk.

---

## VCP Quick-Reference Card

```
SCREEN FOR:           LOOK FOR:              ENTRY:
─────────────         ─────────────          ──────────────
EMA50 > EMA200        2–4 contractions       Buy at pivot
Within 25% of 52W Hi  Volume dries up        Limit to +2–3%
Prior uptrend 30%+    Each pivot smaller      Stop = last low
RSI 50–75             Weekly chart best       Risk < 2% capital
```

---

## KLSE VCP Examples to Study

| Pattern          | What to Look For in KLSE              |
|------------------|---------------------------------------|
| 3-contraction VCP| CIMB, MAYBANK after quarterly results bounce |
| Tight VCP (< 5%) | Tech stocks: VITROX, FRONTKN before breakout |
| Wide VCP         | Plantation stocks after CPO cycle turns |
| Cup-with-Handle  | Common in strong REITs and banks         |

---

## Screening for VCP Daily Routine

1. **Macro check**: KLCI > EMA50? Dow > EMA20? (your current macro gate)
2. **Screener**: Pull T1/T2 stocks from KLSE screener
3. **VCP filter**: Among T1/T2, which show COIL flag? (BB width at 20th pct)
4. **Chart review**: Open TradingView, weekly chart — count contractions manually
5. **Add to watchlist**: Stocks with valid 2–3 contraction VCP approaching pivot
6. **Set alerts**: Price alert at pivot point in TradingView
7. **Execute**: Buy on breakout with volume confirmation
