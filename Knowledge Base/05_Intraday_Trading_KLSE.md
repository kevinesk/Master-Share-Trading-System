# Intraday Trading on KLSE

## Core Principle
Intraday trading on KLSE = **buy and sell the same stock within the same trading day**.
No overnight risk. Uses the same CDS account as swing trading.

---

## KLSE Intraday vs Swing vs Contra

| Type        | Hold Period    | Settlement       | Risk Level |
|-------------|----------------|------------------|------------|
| Intraday    | Hours (same day)| Close by 5 PM   | High       |
| Contra      | 1–3 days       | T+2 (net)        | Medium-High|
| Swing       | Days to weeks  | Full T+2 payment | Medium     |
| Position    | Weeks to months| Full T+2 payment | Medium-Low |

---

## Intraday Session Structure

### Pre-Market (8:30–9:00)
- Orders queue but no trades execute
- Watch: overnight US market, pre-market news, Bursa announcements
- Identify: which stocks have catalyst today?

### Opening Burst (9:00–9:30)
- Most volatile 30 minutes — large gaps, price discovery
- **Strategy**: Watch, don't rush. Let price settle.
- Identify early movers with genuine volume (not just gap)

### Morning Session (9:30–11:30)
- Best setup window: momentum trades with volume confirmation
- VWAP strategies work well here
- Volume is highest in morning session

### Lunchtime Fade (11:30–14:00)
- Volume drops sharply
- Gaps tend to close (fade trades)
- Avoid new entries — low liquidity = wide spreads

### Afternoon Session (14:00–16:30)
- Second active period
- End-of-day momentum / closing strategies
- Window dressing effect near month/quarter end

### Closing (16:30–17:08)
- Pre-close call auction determines official closing price
- Avoid intraday positions past 16:30 unless intentional

---

## Key Intraday Indicators

### 1. VWAP (Volume Weighted Average Price)
```
VWAP = Σ(Price × Volume) / Σ(Volume)  [resets each day at 9:00]
```
- Price **above VWAP** = buyers in control → look for LONG setups
- Price **below VWAP** = sellers in control → avoid longs
- Price **returns to VWAP** after morning gap = potential entry

### 2. Intraday EMA (5-min or 15-min chart)
- EMA9 and EMA20 on 5-minute chart
- EMA crossover (EMA9 > EMA20) on 5-min = intraday uptrend
- Price bouncing off EMA20 on 5-min = pullback entry

### 3. Volume Profile
- High volume at a price = strong support/resistance
- Breakout through high-volume node = real move
- Breakout on thin volume = likely to reverse

### 4. Opening Range Breakout (ORB)
- Define range from 9:00–9:30 (first 30 min)
- Buy if price breaks ABOVE morning range high with volume
- Short (if allowed) if price breaks BELOW morning range low with volume
- Stop = other side of the range

---

## KLSE Intraday Setup Types

### Setup 1 — Gap-and-Go
**Condition**: Stock gaps up on news/results → continues higher
- Entry: Buy when price holds above gap level for 15 min
- Target: Previous high or next resistance
- Stop: Below gap opening price
- **KLSE caution**: Many gaps fill by lunchtime — ensure it's news-driven

### Setup 2 — VWAP Reclaim
**Condition**: Stock opens below VWAP, then climbs back above it
- Entry: First candle that closes above VWAP with above-avg volume
- Target: Previous day's high or daily R1
- Stop: Below VWAP

### Setup 3 — Opening Range Breakout (ORB)
**Condition**: Stock is in Stage 2 uptrend, quiet open, then breaks out
- Define range: 9:00–9:30 high and low
- Buy: When price breaks above range high after 9:30, with volume surge
- Stop: Below range low
- Target: Range width × 2 projected above breakout

### Setup 4 — Intraday Momentum Continuation
**Condition**: Stock already trending on daily chart, pulls back to EMA20 (5-min) intraday
- Entry: Bounce off EMA20 on 5-min with bullish candle
- Target: Day's high or swing high
- Stop: Below EMA20 close

---

## Intraday Risk Rules

1. **Maximum 2 intraday trades per day** — quality over quantity
2. **Never risk more than 0.5% of capital** on a single intraday trade
3. **Close ALL positions by 16:30** — no exceptions (T+2 surprise risk)
4. **Do not trade first 30 minutes** unless it's a strong catalyst
5. **Volume must confirm** — no trades on thin volume
6. **Avoid stocks < RM500,000 daily turnover** — spreads are too wide

---

## KLSE Intraday Stock Selection Criteria

Daily (before market opens), filter for:
- Average daily turnover > RM2 million (sufficient liquidity for intraday)
- Stock in Stage 2 uptrend (daily chart)
- Has a catalyst: earnings, news, sector theme, index inclusion
- Volume already above 3-day average by 9:30 (early strength)
- Within 5% of a breakout level (near resistance)

---

## Intraday Profit Targets

Use **1:2 minimum risk:reward** for intraday:
- If stop = 3% below entry → target = 6% above entry
- If stop = 1.5% below entry → target = 3% above entry

Take **partial profits at 1:1** (50% out), trail the rest.

---

## Psychological Traps in Intraday Trading

| Trap                    | Solution                                       |
|-------------------------|------------------------------------------------|
| FOMO after big gap up   | Wait for pullback to VWAP before entering      |
| Holding a losing trade  | Pre-define stop BEFORE entry. Honor it.        |
| Averaging down intraday | Never. Close and reassess.                     |
| Over-trading            | Max 2 trades/day. Rest is watching.            |
| Getting attached to a view | The price is always right. Respect it.    |
| Revenge trading after loss | Take a break. Next trade tomorrow.         |
