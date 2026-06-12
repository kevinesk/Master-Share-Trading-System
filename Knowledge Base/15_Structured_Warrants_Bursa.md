# Structured Warrants on Bursa Malaysia

## What Are Structured Warrants?

Structured warrants are leveraged financial instruments issued by investment banks (not the listed company itself) that give the holder the right to buy (call warrant) or sell (put warrant) the underlying asset at a fixed price before an expiry date.

**Key point**: Structured warrants are NOT the same as company warrants (which are issued by the company itself). Structured warrants are issued by Maybank IB, CIMB, RHB, etc.

---

## Call Warrants vs Put Warrants

| Feature | Call Warrant | Put Warrant |
|---------|-------------|-------------|
| Profit when | Underlying stock RISES | Underlying stock FALLS |
| Use for | Leveraged long position | Hedging or bearish bet |
| KLSE retail use | 95% of warrant trading | 5% of warrant trading |
| Direction | Bullish | Bearish |

**KLSE focus**: Almost all retail structured warrant trading is in CALL warrants. Put warrants exist but are mainly used by institutions for hedging.

---

## How Warrant Codes Work on Bursa

Format: **STOCK-WA**, **STOCK-WB**, **STOCK-WC** etc.
Or for structured warrants: **STOCK-CX** (Call) or **STOCK-PX** (Put), where X is a number.

**Example**:
- `MAYBANK-C3Y` = Maybank Call Warrant, expiry some date, issued series Y
- `CIMB-C77` = CIMB Call Warrant #77
- The exact code details are in the warrant's term sheet

**Finding warrants on Bursa**:
- Bursa website → Derivatives → Structured Warrants
- Filter by underlying stock → compare terms

---

## Key Warrant Terminology

### Exercise Price (Strike Price)
The price at which you can buy the underlying stock using the warrant.

- **In the Money (ITM)**: Underlying price > Exercise price (has intrinsic value)
- **At the Money (ATM)**: Underlying price ≈ Exercise price
- **Out of the Money (OTM)**: Underlying price < Exercise price (no intrinsic value, only time value)

### Conversion Ratio
How many warrants you need to get 1 share.
- Conversion Ratio = 5 means you need 5 warrants to "convert" to 1 share
- Most KLSE warrants have conversion ratios of 2–10

### Gearing Ratio
How much leverage the warrant provides relative to the share.
```
Gearing = Share Price / (Warrant Price × Conversion Ratio)
```
- Gearing of 5× means if the stock rises 1%, the warrant (theoretically) rises 5%
- Higher gearing = higher potential return = higher risk of total loss

### Premium
How much extra you're paying over the intrinsic value.
```
Premium % = [(Warrant Price × Conversion Ratio + Exercise Price) / Share Price − 1] × 100
```
- Premium = time value you pay for the warrant
- Lower premium = better value (less time value wasted)
- Target: Premium < 15% for most trades

### Effective Gearing (Delta-Adjusted Gearing)
More accurate than simple gearing. Accounts for the fact that OTM warrants don't move 1:1 with the stock.
```
Effective Gearing = Gearing × Delta
```
- Delta: How much the warrant moves per RM1 move in the stock (0 to 1 for calls)
- ITM warrants have delta close to 1
- OTM warrants have delta close to 0

---

## Warrant Selection Guide

### Step 1: Choose the Right Strike Price
| Position | Strike vs Current Price | Best For |
|----------|------------------------|---------|
| ATM ±5% | At the money | Best balance of gearing and delta |
| ITM >5% | Below stock price | Lower gearing, more expensive, safer |
| OTM >5% | Above stock price | Higher gearing, cheap, riskier |

**KLSE recommendation**: For swing trades, choose ATM or slightly ITM warrants.
OTM warrants are lottery tickets — avoid unless for short-term speculation.

### Step 2: Choose Expiry — Enough Time
**Critical rule**: Buy warrants with at least 3 months to expiry.
- Time decay (theta) accelerates in the last month before expiry
- A warrant with <1 month to expiry can lose 50% of its value from time decay alone, even if the stock is flat

| Hold Period | Minimum Expiry |
|-------------|---------------|
| 1 week | 2+ months |
| 1 month | 3+ months |
| 3 months | 6+ months |

### Step 3: Choose Issuer — Liquidity Matters
- Maybank IB, CIMB, RHB, Macquarie are the main issuers
- Check the bid-ask spread: if spread > 3% of warrant price, liquidity is poor
- Market maker must be active: check that there are always both bid and ask quotes

### Step 4: Compare Warrants on the Same Stock
Multiple issuers may have warrants on the same stock (e.g., CIMB). Compare:
- Premium (lower = better)
- Effective gearing (higher = more leverage)
- Remaining life (more = better for swing trades)
- Issuer (major banks = better liquidity)

---

## Warrant Pricing — What Moves the Price

### Intrinsic Value
```
Intrinsic Value = MAX(0, (Stock Price − Exercise Price) / Conversion Ratio)
```
- If stock is at RM10, exercise price is RM9, conversion ratio is 5:
- Intrinsic value = (10 − 9) / 5 = RM0.20

### Time Value
- The extra amount the market pays for the possibility the warrant goes deeper ITM
- Decreases as expiry approaches (time decay / theta)
- This is the "cost" of using warrants vs buying shares directly

### Volatility Effect (Vega)
- Higher volatility → higher warrant price (both calls and puts)
- If implied volatility increases (e.g., pre-earnings), warrants become more expensive
- After an earnings event, implied volatility collapses → "vol crush" → warrants lose value even if stock moves correctly

---

## KLSE Warrant Trading Strategy

### Strategy 1: Trend Confirmation Play (Swing Trade)
**Setup**: VCP breakout confirmed on the underlying stock
**Trade**: Buy an ATM call warrant with ≥3 months to expiry
**Risk**: 50% of premium paid (pre-determined)
**Target**: 80–150% gain on the warrant (requires 15–25% move in the stock with gearing of ~5×)
**Stop**: If underlying stock breaks below VCP low, exit warrant immediately

**Position sizing rule**: Never put more than 2–3% of portfolio into a single warrant position.

### Strategy 2: Earnings Momentum Play (Short-term)
**Setup**: Company about to report strong quarterly earnings
**Trade**: Buy ATM call warrant 1–2 weeks before results
**Risk**: Vol crush after results can hurt even if earnings are good
**Exit**: Within 1–2 days after results announcement

**Warning**: This is high-risk. Earnings surprises on KLSE are unpredictable.

### Strategy 3: Leverage on a Confirmed Leader
**Setup**: KLCI is in Stage 2 (above EMA50, trending up), sector is leading
**Trade**: Buy ATM call warrant on the sector leader (e.g., CIMB-C77 when banking sector is leading)
**Hold**: For the duration of the sector rally (2–6 weeks typically)
**Exit**: When underlying breaks EMA21 or warrant gains 80%+

---

## Risk Management for Warrants

### Maximum Loss = 100% of Premium Paid
Unlike shares, warrants can go to zero if:
- The stock price is below the exercise price at expiry
- You hold to expiry (don't do this)

### Rules
1. **Never invest more than 5% of portfolio in warrants total**
2. **Never put more than 2% in any single warrant**
3. **Always exit if the underlying breaks your stop loss** — do not hold hoping for recovery
4. **Never hold past the last 4 weeks before expiry**
5. **Monitor bid-ask spreads** — if the market maker stops quoting, you may be unable to exit

---

## Warrant vs Share — When to Use Each

| Factor | Buy Shares | Buy Warrants |
|--------|-----------|--------------|
| Capital required | Full (RM10,000 for 2,000 CIMB shares) | Fraction (RM2,000 for equivalent exposure) |
| Downside risk | Limited to share price reaching 0 | 100% of premium |
| Dividends | Yes (if declared) | No |
| Holding period | Unlimited | Limited (expiry date) |
| Leverage | None | 3–10× |
| Best for | Core positions, position trading | Short-term tactical swing trades |

**Rule of thumb**: If you're confident in a setup and want to hold for months → buy shares.
If you want short-term leverage on a high-conviction swing trade → consider warrants (up to 5% of portfolio).

---

## Where to Find Warrant Data on KLSE

| Source | What You Get |
|--------|-------------|
| Bursa Malaysia website | Full list of all structured warrants, term sheets, issuer details |
| Maybank IB Warrant page | Live bid/ask, gearing, premium, delta for all Maybank warrants |
| CIMB Warrant page | Same for CIMB-issued warrants |
| Rakuten Trade / Mplus app | Real-time warrant prices integrated with order placement |
| i3investor.com | Warrant comparison tool — compare all warrants on same stock |

---

## Common Warrant Mistakes on KLSE

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Buying near expiry | Time decay destroys value | Always ≥3 months to expiry |
| Buying deep OTM for "cheap" | Near-zero delta; stock must move a lot | Buy ATM ±5% |
| Ignoring the premium | Overpaying for time value | Premium < 15% |
| Not checking liquidity | Cannot exit; large bid-ask spread losses | Only trade active warrants |
| Holding after stop on underlying | Warrant to near-zero | Exit warrant when stock hits stop |
| Over-allocating | Emotional decisions; large losses | Max 5% of portfolio in warrants total |
