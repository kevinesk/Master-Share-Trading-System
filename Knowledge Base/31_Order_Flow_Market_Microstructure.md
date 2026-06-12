# Order Flow & Market Microstructure

## What is Market Microstructure?

Market microstructure is the study of HOW prices are actually formed — the mechanics of order matching, bid-ask spreads, and how information moves through a market.

**Why it matters for KLSE retail traders**: Understanding microstructure helps you:
1. Get better fill prices (enter and exit more efficiently)
2. Spot institutional order footprints
3. Understand why prices move even on "no news" days
4. Avoid common execution mistakes that cost you 0.5–2% per trade

---

## The KLSE Order Book (Level 2 Data)

### What the Order Book Shows

Every moment, Bursa maintains an order book for each stock:

```
          SELL ORDERS (ASKS)
Price     Quantity    Sellers
RM8.35    15,000      3 sellers waiting
RM8.33    42,000      7 sellers
RM8.32    28,000      5 sellers   ← Best ask (lowest selling price)
─────────────────────────────── SPREAD ←→ RM0.01
RM8.31    34,000      6 buyers    ← Best bid (highest buying price)  
RM8.30    87,000      12 buyers
RM8.29    22,000      4 buyers
          BUY ORDERS (BIDS)
```

**Bid**: The highest price a buyer is willing to pay right now
**Ask**: The lowest price a seller is willing to accept right now
**Spread**: Ask − Bid = your immediate transaction cost beyond brokerage

### KLSE Bid-Ask Spread by Price Range

Bursa Malaysia uses "ticks" — minimum price movements:

| Price Range | Tick Size | Typical Spread |
|-------------|-----------|---------------|
| < RM1.00 | RM0.005 (0.5 sen) | 1–3 ticks |
| RM1.00–RM2.99 | RM0.005 (0.5 sen) | 1–2 ticks |
| RM3.00–RM4.99 | RM0.01 (1 sen) | 1–2 ticks |
| RM5.00–RM9.99 | RM0.01 (1 sen) | 1–3 ticks |
| ≥ RM10.00 | RM0.02 (2 sen) | 1–3 ticks |

**Impact**: For a RM5.00 stock with 1 tick spread:
- You buy at RM5.01 (ask) and sell at RM5.00 (bid)
- Spread cost = RM0.01 / RM5.00 = 0.20% immediately
- Plus brokerage + stamp duty → total immediate cost ~0.5%

### Thinly Traded Stocks — The Hidden Danger

For stocks with daily turnover < RM500,000:
- Spread may be 5–10+ ticks (0.5–1.0%)
- Your market order can MOVE the price against you
- A buy of 50,000 shares can push the price up 3–5% if depth is thin

**KLSE rule**: Only trade stocks with daily turnover ≥ RM2M for swing trading. Below this, you are the market — your own orders affect your entry/exit price.

---

## Types of Orders on Bursa Malaysia

### Market Order
- Executes immediately at the best available price
- **Risk**: On thin stocks, you get a bad fill; during volatility, you may get surprised
- **Use**: Only on liquid stocks (>RM5M daily turnover) when you need immediate execution

### Limit Order (Recommended for all KLSE trades)
- You specify the maximum price you'll pay (buy) or minimum price you'll accept (sell)
- Order sits in the book until filled or cancelled
- **Use**: Almost always. Protects against bad fills.

**Limit buy example**:
- CIMB best ask = RM8.32
- Your limit buy at RM8.32 → fills immediately at RM8.32
- Your limit buy at RM8.30 → sits in queue; fills only if price drops to RM8.30

### At-Auction / Opening Order
- Submitted during pre-market (8:30–9:00 AM)
- Executes at the opening auction price (Bursa determines this via matching algorithm)
- Useful for getting filled at a known opening price without the opening volatility

### Day Order vs Good-Till-Cancelled (GTC)
- **Day order**: Expires at end of trading day if not filled
- **GTC**: Stays until filled or manually cancelled (up to 30 days on most KLSE brokers)
- **Caution with GTC**: Avoid GTC for breakout buy orders — the breakout opportunity passes; your order fills at a bad time later

---

## How Institutional Orders Are Executed

### Why Institutions Can't Just Use Market Orders

A fund wants to buy 3 million MAYBANK shares (≈RM22.5M).
A single market order would:
- Empty the ask side of the order book
- Move MAYBANK price up 3–5% in minutes
- Their average cost would be far above the pre-order price

**Solution**: They break up the order and execute over days.

### Institutional Order Types

**VWAP Order** (Volume-Weighted Average Price):
- Algorithm places buy orders throughout the day to match market volume
- Result: Average purchase price = approximately the day's VWAP
- This is why on "accumulation days," stocks trade in a tight range around VWAP with consistent volume

**TWAP Order** (Time-Weighted Average Price):
- Execute an equal number of shares every 30 minutes throughout the day
- Smoother but doesn't adjust for intraday volume patterns

**Iceberg Order** (Hidden Volume):
- Display only 50,000 shares visible in the order book
- When filled, another 50,000 appears automatically from hidden reserve
- Total size could be 2,000,000 shares
- **How to spot**: The same price level keeps refilling after being consumed

### Reading Institutional Footprints in the Order Book

| Pattern in Order Book | Possible Meaning |
|----------------------|-----------------|
| Large iceberg order at bid | Institution building a position; buying dips |
| Large iceberg order at ask | Institution distributing; selling into strength |
| Order book clearing suddenly (ask side) | Aggressive buy; possibly big news about to be announced |
| Consistent small buying at VWAP | VWAP execution in progress; accumulation |
| Wide spread + low volume | Market maker withdrawn; tread carefully |

---

## The Market Maker's Role on KLSE

### For Structured Warrants

Every structured warrant on Bursa has a designated market maker (the issuing bank — Maybank IB, CIMB, etc.).

**Market maker obligation**:
- Must continuously provide both bid and ask quotes within maximum spread
- Maximum spread = 15 ticks or 10% of warrant price (whichever is smaller)
- Provides liquidity so you can always exit

**When market maker withdraws**:
- They can temporarily withdraw quotes during fast-moving underlying markets
- If no quotes are visible for your warrant → do NOT market order → you'll get a terrible fill
- Wait for quotes to return or use limit orders within reasonable range

### For Regular Stocks

Bursa does NOT mandate market makers for regular equities. Liquidity comes entirely from:
- Retail order flow
- Institutional orders
- Algorithmic traders (small presence on KLSE vs US markets)

---

## Volume Analysis — Reading the True Message

### Volume Interpretation

| Price Movement | Volume | Interpretation |
|---------------|--------|---------------|
| Price rising | Volume rising | Institutional buying; sustainable move |
| Price rising | Volume falling | Rally losing conviction; potential reversal |
| Price falling | Volume rising | Institutional selling; dangerous |
| Price falling | Volume falling | No real selling pressure; likely bounce coming |

### Unusual Volume — What Triggers It?

**Legitimate reasons**:
- Corporate announcement (results, dividend, M&A)
- Index inclusion/exclusion
- Major broker upgrade with institutional buying following
- End of month/quarter institutional rebalancing

**Suspicious reasons (potential front-running or leaks)**:
- Unusual volume 1–3 days BEFORE a corporate announcement
- Bursa issues UMA (Unusual Market Activity) query → company must respond
- If company responds "no material development" → possible insider trading

**Your action on unusual volume before any news**:
- If you don't hold → wait for clarity. Don't chase.
- If you hold → tighten stop. The move may not be sustainable.

---

## Opening Auction and Closing Auction

### Bursa Opening Auction (8:30 – 9:00 AM)

- No trades execute during this period
- Orders accumulate in the book
- At 9:00 AM, Bursa's algorithm calculates the price that maximises traded volume
- All matched orders execute at this single opening price

**Trading implication**: The opening price reflects all overnight information plus pre-market orders. It's often the most "fair" price of the day. Large gaps from previous close = market has new information.

### Pre-Close Auction (5:00 – 5:08 PM)

- Random closing (between 5:00 and 5:08 PM) — exact time is random to prevent manipulation
- Orders submitted between 4:46 and 5:00 PM enter the auction
- Final price = official closing price used for indices and settlement

**Why it matters**: 
- REITs, ETFs, and index funds rebalance at closing prices
- Month-end "window dressing" occurs here (fund managers buy winners to show in their portfolio reports)
- You can often sell into higher prices on last trading day of quarter due to window dressing

---

## Slippage — The Hidden Cost

**Slippage** = the difference between the price you expected and the price you actually got.

**Causes of slippage**:
1. Market order on a thin stock (order book depth insufficient)
2. Fast-moving market (your limit order at RM8.32 but stock jumps to RM8.50 instantly)
3. Large order size relative to daily volume

**Estimating slippage**:
- Liquid stock (>RM10M daily turnover): Slippage ~0.05–0.10%
- Medium stock (RM2–10M turnover): Slippage ~0.10–0.30%
- Thin stock (<RM2M turnover): Slippage ~0.50–2.00%

**Always include slippage in your backtest assumptions.** Without it, your backtested returns are overstated.

---

## Practical Execution Tips for KLSE

### Buy Execution
1. Check the order book depth before buying — how many shares are at the ask?
2. Use limit orders at the ask price or 1 tick above (to ensure fill without overpaying)
3. Buy in tranches if position size > 5% of average daily turnover
4. Avoid market open (first 15 min) for large orders — spreads are widest

### Sell Execution
1. Don't panic-sell with a market order — use limit at the bid or 1 tick below
2. If selling into a rally, use limit orders above current price — you'll get better fills
3. For large exits, spread over 2–3 days to avoid moving price against yourself
4. Sell priority: 40% near open, 40% near close (institutional activity highest at these times)

### Stop Loss Execution
1. Set a mental stop, not an automatic stop order (Bursa stop orders are visible to market makers in some systems)
2. When stop is hit → use limit order at the bid price (1 tick below) — you'll fill in seconds on liquid stocks
3. Only use market orders for stops if the stock is falling rapidly and you must exit immediately
