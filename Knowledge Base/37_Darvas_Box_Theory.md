# Nicolas Darvas — The Box Theory

> "It was no longer a question of whether I would lose money — I knew I would. It was a question of how much I would lose before I knew I was wrong."
> — Nicolas Darvas, *How I Made $2,000,000 in the Stock Market* (1960)

Nicolas Darvas was a Hungarian-born ballroom dancer who, while touring the world, turned $36,000 into $2,250,000 between 1957 and 1959 (worth roughly $25 million today). He had no Wall Street connections, no real-time data, no charts — only weekly *Barron's* newspapers and cable telegrams sent to his hotel in Tokyo, Bombay, or Calcutta.

His system — the **Box Theory** — is the direct ancestor of modern swing trading, volatility contraction patterns, and breakout systems. This file extracts the full method and applies it to KLSE.

---

## Part 1 — The Story (Why It Matters)

Darvas began as a "tipster" — buying stocks based on Wall Street rumours, broker recommendations, hot tips at parties. He lost money continuously for years. His turning point came when he stopped listening to humans and started listening to the **stock itself** (its price and volume).

The result: a purely mechanical, emotionless system he could execute by cable from anywhere on earth. He never met any of the executives of the companies he traded. He never read annual reports. He didn't care what the company *did*. He only cared about price action.

**The lesson**: Edge comes from process, not from information.

---

## Part 2 — What Is a Darvas Box?

A Darvas Box is a **price range** that contains the recent trading action of a stock — a high and a low that price has not violated for at least 3 consecutive days.

```
$50  ──────────────────────  ← Box top (resistance)
$48        /\
$46   /\  /  \   /\
$44  /  \/    \_/  \
$42 /                   \
$40 ──────────────────────  ← Box bottom (support)
```

### The Box Construction Rules (Strict)

A valid Darvas Box requires both boundaries to be **confirmed**.

**Box top is confirmed when**:
- A stock makes a new high
- For **3 consecutive trading days afterward**, no higher high is made
- That high becomes the box top

**Box bottom is confirmed when**:
- After the box top is set, the stock makes a new low (a price below recent action)
- For **3 consecutive trading days afterward**, no lower low is made
- That low becomes the box bottom

**Until both top and bottom are confirmed, there is no valid box. No trade.**

### Why 3 Days?

Three days of failing to make a new high (or low) was Darvas's empirical evidence that buyers (or sellers) had stopped pushing. Less than 3 days = noise. More than 3 days = exhaustion confirmed.

In modern KLSE terms with our 5-day trading week, **3-5 trading days** is the standard confirmation window.

---

## Part 3 — The Entry: Breaking Out of the Box

The trade is triggered when **price closes above the confirmed box top** on the daily chart.

### Entry Rules

1. **Wait for the close** — not an intraday spike
2. **Volume must surge** — at least 1.5× the 20-day average (Darvas measured this manually; you have indicators)
3. **Place buy stop just above the box top** — Darvas used "on-stop buy orders" via cable
4. **Set protective stop just below the box top** — typically 1-2% below

### The Modern Translation

Modern KLSE order types let you replicate Darvas's cable-telegraph system exactly:

| Darvas (1957) | Modern Bursa Trader |
|--------------|---------------------|
| Cable: "Buy 200 shares XYZ at 51 stop" | Stop-buy order at RM5.10 |
| Cable: "Sell 200 shares XYZ at 49 stop" | Stop-loss order at RM4.90 |
| Wait for *Barron's* weekly | Wait for daily close confirmation |
| Read prices in hotel lobby | TradingView alert + mobile app |

You can be on holiday in Penang and still run a perfect Darvas system today.

---

## Part 4 — The Trail: Boxes Stacking on Boxes

The genius of Darvas's method is that he didn't try to predict the peak — he **let the trend tell him**.

### Stacking Boxes

After the initial breakout, a stock typically:
1. Advances to a new high
2. Pauses and forms a NEW box (higher than the previous box)
3. Either breaks UP from the new box → trend continues, trail stop higher
4. Or breaks DOWN from the new box → trend ending, exit

```
Box 4 ──────────────                  ← Current box
Box 3 ────────────       ← stop trails up here
Box 2 ──────────
Box 1 ────────                        ← original entry box
```

### Trailing the Stop

Each time a new higher box forms and is confirmed:
- Raise the stop to **just below the new box bottom**
- Never lower a stop — only raise it
- The last box's bottom is your final exit trigger

This is the original "trailing stop" methodology — mechanically defined, emotion-free.

---

## Part 5 — The Exit (Three Scenarios)

### Exit 1: Stop Hit
Price closes below the most recent box bottom → exit immediately. The trend has changed.

### Exit 2: Failed Breakout
You enter at box-top breakout, but within 1-3 days price falls back below the box top → exit. Failed breakouts often reverse hard. Don't hope.

### Exit 3: Climax Reversal
A wide-range bar with explosive volume on the day's high → no new high the next session → exhaustion. Take majority off; trail the rest.

### Darvas's Critical Insight: No Profit Targets

Darvas **never** set profit targets. He let the boxes trail upward indefinitely. His biggest winner (Lorillard, then E.L. Bruce, Universal Controls in 1958-1959) ran from $35 to $171 — a 388% gain — because he didn't second-guess.

> **Lesson**: A profit target caps your winners. The trail-the-box method lets winners run.

---

## Part 6 — The Filter: What Stocks Qualify

Darvas didn't trade just any stock that formed a box. He had a strict selection filter — and this filter is what modern momentum traders still use.

### The Darvas Stock Selection Criteria (1959)

1. **Price near or making new 52-week highs** — must be in a clear uptrend
2. **Volume increasing** over the prior 3-6 months
3. **Earnings momentum** — sector or industry leader with rising earnings
4. **Price range > $20** in 1950s dollars — meaning enough liquidity, no penny stocks
5. **In a new "leading industry"** — semiconductors, aerospace, defence were his 1950s plays

### KLSE Translation (2026)

| Darvas Criterion | KLSE Filter |
|-----------------|-------------|
| 52-week high | Within 15% of 52-week high |
| Volume increasing | 50-day avg volume > 100-day avg volume |
| Earnings momentum | 3 consecutive quarters of EPS growth |
| Adequate price | Stock price ≥ RM1.00 AND ADV ≥ RM2M/day |
| Leading industry | Sector RS rising vs KLCI |

This filter, combined with the box breakout, gives you the modern momentum trade.

---

## Part 7 — Darvas Box vs VCP (How They Differ and Overlap)

Both are consolidation breakouts. But they look at different things.

| Feature | Darvas Box | Minervini VCP |
|---------|-----------|---------------|
| **Duration** | Minimum 6 days (3+3); typically 2-8 weeks | Typically 5-26 weeks |
| **Shape** | Rectangle (flat top, flat bottom) | Series of tighter contractions (sawtooth) |
| **Number of contractions** | One box at a time, then next | 2-6 contractions before breakout |
| **Volume** | Surge on breakout day | Drying up THROUGHOUT base, surge on breakout |
| **Best for** | Pure trend-following any stock | Stage 2 leaders with fundamentals |
| **Speed of signal** | Faster (6+ days) | Slower (multiple weeks) |
| **Hit rate** | ~45-55% wins | ~50-60% wins (with filters) |

### When to Use Which

- **Darvas Box**: Fast-moving momentum stocks, news-driven sectors, breakout swing trades
- **VCP**: Multi-week position trades on highest-quality Stage 2 leaders
- **Combined**: When a stock forms a VCP AND its final contraction is a clean Darvas Box → strongest possible setup

You can run both systems simultaneously. They're complementary, not competing.

---

## Part 8 — The Cable Telegraph Method (Why It Still Works)

Darvas had no phone, no real-time data, no friends on Wall Street, no Bloomberg terminal. He traded with information that was **6-7 days old** (weekly *Barron's*) and orders sent by cable.

### How He Did It

1. Read weekly *Barron's* every Friday (received Monday in his current city)
2. Mark stocks that fit his criteria — make a watchlist
3. Calculate the boxes manually from the *Barron's* weekly highs/lows
4. Cable his broker:
   - "Buy 200 shares Lorillard at 28 1/2 stop"
   - "Sell 200 shares Lorillard at 26 stop"
5. Sleep in Karachi, dance in Singapore, wake up to confirmations or stop-outs

### Why This Matters Today

You have 1000× the information Darvas had. **You don't need more information — you need a better process.**

If a man on a steamship in 1958 with 6-day-old data could compound 60×, then your TradingView setup, mobile alerts, and real-time order book are massively over-engineered. Don't drown in data. Use rules.

### The Modern Darvas Setup (Mobile-Friendly KLSE Workflow)

```
Sunday    : Run KLSE screener for new-high candidates
          : Add 5-10 to TradingView watchlist
          : Mark box top and box bottom on each chart

Monday-Fri: Check watchlist 2x per day (lunch + close)
          : Set buy-stop alerts at box top + 1 tick
          : Set sell-stop orders at box bottom on positions

          : DO NOT watch tick-by-tick
          : DO NOT modify orders during the day
          : Let the system execute
```

You can run this from a beach in Langkawi. Just like Darvas.

---

## Part 9 — Common Mistakes (How Darvas Lost When He Did)

Even Darvas had losing periods. Each one taught a rule.

### Mistake 1: "Confirming" Premature Boxes
Before he refined the 3-day rule, Darvas would draw boxes after 1-2 days of no new high. He got faked out repeatedly. **Fix**: Strict 3-day rule. No exceptions.

### Mistake 2: Listening to Tips Mid-Trade
He'd enter a clean box breakout, then hear at a cocktail party that "the company is rumoured to be in trouble" and exit early. **Fix**: Ignore all non-price information after entry. The price is the only opinion that matters.

### Mistake 3: Moving Stops Down
He once moved a stop *lower* to "give the stock room to breathe." The stock fell straight through both stop levels. **Fix**: Stops only move UP, never down. Period.

### Mistake 4: Trading Too Many Stocks
At one point he had 15 open positions and couldn't track them while travelling. **Fix**: Maximum 4-6 open positions. Capital allocation is also attention allocation.

### Mistake 5: Adding to Losers
Early in his career, he averaged down and lost everything. **Fix**: Pyramid winners only. Never add to a position below your average price.

---

## Part 10 — KLSE Application: The Full Darvas Trade

### Setup Phase (Sunday Evening)
1. Screen for KLSE stocks within 15% of 52-week high, RS > 80, sector leading
2. Open each chart, identify the most recent box (top + bottom)
3. Confirm box: 3+ days at top, 3+ days at bottom, both verified
4. Note the box top RM value

### Entry Phase (During the Week)
1. Set TradingView alert at box top + 1 tick
2. When alert fires, check:
   - Is it a daily CLOSE above box top? (not just an intraday wick)
   - Is volume ≥ 1.5× 20-day average?
   - Is KLCI still above EMA50?
3. If all yes → buy at the close or next morning open
4. Place stop-loss at box top - 2% (just below the resistance-turned-support)

### Management Phase
1. Do not check the position more than once per session
2. Watch for a new box forming higher (typically 5-15 trading days)
3. When new box confirms, raise stop to new box bottom
4. Repeat: stack boxes, trail stops, sit tight

### Exit Phase
1. Stop hit → exit, no questions
2. Failed re-entry into the box → exit
3. Climax day with no follow-through → take 1/2 profit, trail remainder

---

## Part 11 — The Top 10 Darvas Lessons (Print and Keep)

1. **Trade the price, not the company.** You're not investing in a business — you're trading market action.
2. **Tips kill traders.** All information from outside is noise.
3. **The box defines the trade.** Top, bottom, breakout — no improvisation.
4. **3-day confirmation = no premature boxes.** Patience is structural.
5. **Stops only move up.** Lowering a stop is a confession of being wrong.
6. **Pyramid winners, never losers.** Add only when the stock has earned it.
7. **No profit target.** Trail boxes upward until the trend ends itself.
8. **Few positions.** 4-6 maximum. Attention is finite.
9. **Be elsewhere.** You don't need to watch the market to trade it.
10. **Cut losses at the box bottom.** Always. Without exception. Without hope.

---

## Related Files
- [[04_VCP_Pattern_Playbook]] — VCP is the deeper cousin of the Darvas Box
- [[07_Technical_Chart_Patterns]] — flat base = stationary Darvas Box
- [[36_Livermore_Rules_Reminiscences]] — pivotal points = Darvas Box breakouts
- [[02_Minervini_SEPA_KLSE]] — modern leadership stock selection
- [[12_Perfect_Entry_Exit]] — tranche entries align with stacked boxes
- [[33_Fear_FOMO_Confidence_Mastery]] — the discipline to not over-trade
