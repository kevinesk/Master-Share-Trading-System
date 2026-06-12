# Marty Schwartz — The Pit Bull Method

> "I always learned more from my losses than from my successes. Don't worry — there will be plenty of opportunities to learn."
> — Marty Schwartz, *Pit Bull* (1998)

Martin "Marty" Schwartz spent 10 years as a securities analyst on Wall Street, losing money the entire time. At age 33, with his back against the wall, he switched to short-term trading using his own system — and within 18 months won the U.S. Investing Championship with a **781% return** (futures division). For four consecutive years he averaged 25%+ per month.

His book *Pit Bull* is one of the most candid, profane, painful, and useful trading memoirs ever written. This file extracts his actual system: the checklist, the indicators, the drawdown rules, and the routine.

---

## Part 1 — The Schwartz Transformation (Why He Wins)

Schwartz didn't get smarter. He stopped doing three things:

1. **Stopped trying to be right** → started trying to make money
2. **Stopped using fundamentals** → switched 100% to technicals + market timing
3. **Stopped trading other people's ideas** → built his own system, traded only it

> "I now know that to be a winner, I have to be willing to give up being right."

This shift is the entire book. The methods below only work if this internal shift happens first.

---

## Part 2 — The Core Indicator: The 10-Day Moving Average

Schwartz's signature indicator is the **10-day exponential moving average** (some sources call it simple — both work; he used what was available). Everything he traded was filtered through this single tool.

### The 10-Day EMA Rules

**For long trades (KLSE):**
1. Stock must be **above the 10-day EMA** to qualify as a buy
2. **Pullbacks to the 10-day EMA** in an uptrend are buy entries
3. **Closing below the 10-day EMA** in an uptrend = warning; tighten stops
4. **Two consecutive closes below the 10-day EMA** = exit

**For market timing:**
1. KLCI above its 10-day EMA = bullish environment, take long trades
2. KLCI below its 10-day EMA = no new long trades; protect capital
3. The slope of the 10-day EMA tells you trend velocity

### Why 10 Days?

Long enough to filter intraday noise. Short enough to capture swing moves. It's the natural cadence of a 2-week trade cycle — the timeframe Schwartz worked in.

### KLSE Implementation

On TradingView, add:
- **EMA(10)** in bright colour on daily chart
- **EMA(10) on the KLCI index chart** as a market filter

Trade only when:
- Stock chart: price above the 10-day EMA
- KLCI chart: KLCI above its own 10-day EMA

This single filter eliminates 70% of bad trades.

---

## Part 3 — The Schwartz Pre-Trade Checklist

Every trade Schwartz took had to pass this checklist. He kept it written on a card on his desk.

### The 7 Questions Before Entry

```
1. Is the market trending in my direction?
   (KLCI above its 10-day EMA for longs)

2. Is the stock in a clear trend?
   (Above 10-day EMA, with higher highs/higher lows)

3. Is this an oversold pullback in an uptrend, OR a breakout?
   (Both are valid — but identify which one)

4. Where exactly will I get out if wrong?
   (Specific price level — NOT "if it goes down")

5. What is my risk in Ringgit?
   (Position size × stop distance = max loss)

6. Is the reward at least 2× the risk?
   (Realistic target, not hopeful)

7. Am I emotionally calm right now?
   (If euphoric or angry → no trade)
```

If ANY answer is no → no trade. He took the trade only on 7/7 yes.

---

## Part 4 — The Five Schwartz Trade Setups (KLSE-Adapted)

Schwartz traded futures and options, but his setups translate directly to KLSE stocks.

### Setup 1: The Pullback to the 10-Day EMA (Highest Probability)

**The setup**:
- Stock in clear uptrend (HH/HL)
- Above its 10-day EMA for at least 10 trading days
- Pullback for 2-4 days, touching or slightly piercing the 10-day EMA
- Volume drying up on the pullback

**The entry**:
- Day after the pullback ends — buy on the first up close
- Confirm: price closes back above the 10-day EMA

**The stop**:
- Below the lowest low of the pullback (typically 3-5% from entry)

**The target**:
- Previous swing high + measured move (typically 8-15%)

### Setup 2: The Breakout (Schwartz's Aggressive Play)

**The setup**:
- Stock consolidating tightly for 2-4 weeks
- Multiple touches of resistance
- Volume contracting during consolidation

**The entry**:
- Breakout above resistance on volume ≥ 1.5× average
- Schwartz often used buy-stop orders just above the resistance

**The stop**:
- Just below the breakout level (the level should hold as support)

**The target**:
- Height of the consolidation projected upward

### Setup 3: The Magic-T (Reversal with Confirmation)

**The setup**:
- Stock has fallen sharply (oversold)
- Forms a double-bottom or single bottom with capitulation volume
- The right shoulder/second bottom is HIGHER than the first

**The entry**:
- Close above the high between the two bottoms ("the neckline")
- Volume surge required

**The stop**:
- Below the second (higher) bottom

**The target**:
- Distance from bottom to neckline, projected upward

### Setup 4: The Gap Fill Trade

**The setup**:
- Stock gaps down on bad news
- Within 1-3 days starts climbing back

**The entry**:
- Close above the previous day's high after the gap
- Confirms reversal has buyers

**The stop**:
- Below the gap low

**The target**:
- Close the gap (return to pre-gap price)

**KLSE note**: This works best on quality stocks gapping down on temporary issues (analyst downgrade, sector news) — NOT on fundamental breakdowns.

### Setup 5: The 3-Day Reversal

**The setup**:
- Stock has been falling for 5+ days
- A clear hammer or bullish engulfing candle appears at a support level

**The entry**:
- Above the high of the reversal candle, with volume

**The stop**:
- Below the low of the reversal candle

**The target**:
- Previous resistance (often 5-10% up)

This is a counter-trend trade — Schwartz allocated only HALF position size to these.

---

## Part 5 — The Risk Management Rules (The Survival Skills)

This is where Schwartz separates from amateurs. He had **specific, mechanical rules** for what to do when things went wrong.

### Rule 1: The 7% Loss Per Trade

Maximum loss per trade = 7% of position value, OR 1.5% of total capital (whichever is smaller).

| Trade Risk | Schwartz Action |
|-----------|----------------|
| Loss < 3% | Hold; this is normal noise |
| Loss 3-5% | Tighten stop; reassess |
| Loss 5-7% | Exit unless major support holds |
| Loss > 7% | EXIT IMMEDIATELY — no exceptions |

### Rule 2: The 5% Per Day Drawdown Stop

If your account drawdown for the day hits -5% of total capital → **STOP TRADING for the day.**

This is non-negotiable. Schwartz called it "the most important rule I ever made for myself."

### Rule 3: The 10% Weekly Drawdown Stop

If the week's loss hits -10% of total capital → **stop trading for the rest of the week.** Review what went wrong over the weekend.

### Rule 4: The 25% Account Drawdown Stop

If total account drawdown reaches -25% from peak → **stop trading entirely for at least 2 weeks.** Reduce position sizes by half when you return.

### Rule 5: The Doctor Rule

> "If I'm not feeling 100% — sick, tired, hungover, stressed — I don't trade."

Schwartz traded full-size only when physically and emotionally optimal. Otherwise: half-size or no trades.

---

## Part 6 — The Daily Routine (Tournament-Level)

This is Schwartz's actual daily routine during his championship years. Adapted to KLSE hours:

### Pre-Market (8:00 - 8:45 AM)

```
8:00   Coffee + 10 min of physical movement (his "wake-up")
8:10   Review overnight Dow, S&P, USD/MYR
8:15   Check KLCI futures (or proxy: SGX FTSE/KLCI)
8:25   Update 10-day EMA values on KLCI and top 20 watchlist stocks
8:35   Identify the 3 best setups for the day — write entry, stop, target on paper
8:43   Visualise executing each trade — entry + stop + exit
8:45   Walk away from screen until 9:00
```

### During Market (9:00 AM - 5:00 PM Bursa session)

```
9:00   Market opens — wait 15 min before any trade
9:15   First valid setup window opens
12:30  Lunch break (Bursa midday break) — STEP AWAY from screen
14:30  Afternoon session — only act on pre-planned setups
       Maximum 2-3 new trades per day
17:00  Close out any day-trades; reassess swing positions
```

### Post-Market (5:00 - 5:30 PM)

```
5:00   Print or save chart of every trade taken today
5:05   Journal: entry rationale, stop, exit (or current status)
5:15   Calculate today's P&L; note vs daily drawdown stop
5:20   Identify one thing done well, one thing to improve
5:30   Close laptop. Done.
```

### Weekend Review (Saturday Morning, 1 hour)

```
Sat 9am  Review every trade of the week
         Mark winners and losers on charts
         What is the pattern in my mistakes?
         What is the pattern in my wins?
         Update watchlist for Monday
         Rest the rest of the weekend
```

---

## Part 7 — The Position Sizing Method

Schwartz used a tiered sizing approach based on conviction AND market environment.

### The Tier System

| Conviction Level | Position Size | Setup Quality |
|-----------------|---------------|---------------|
| **A — Highest** | Full 100% allocation | All 7 checklist items pass + perfect 10-day EMA pullback in strong sector |
| **B — Good** | 50% allocation | All 7 checklist pass but setup is breakout (lower hit rate than pullback) |
| **C — Acceptable** | 25% allocation | 6/7 pass, counter-trend or speculative |
| **No trade** | 0% | Below 6/7 |

### The Market Environment Multiplier

After tier sizing, multiply by environment factor:

| KLCI vs 10-day EMA | Multiplier |
|-------------------|------------|
| Above and rising | 1.0× (full size) |
| Above but flat | 0.7× |
| Below | 0.5× |
| Below + falling | 0.0× (no trades) |

**Example**:
- A-grade setup × KLCI above & rising = full position (e.g., 2% portfolio risk)
- B-grade setup × KLCI flat = 50% × 0.7 = 35% sizing
- C-grade setup × KLCI below = 25% × 0.5 = 12.5% sizing

---

## Part 8 — Schwartz's Mental Game

The book *Pit Bull* spends as much time on psychology as it does on tactics. The recurring themes:

### The Champion's Mindset
> "I had a Marine Corps mentality. I figured if I could survive Parris Island, I could survive anything Wall Street threw at me."

Treat trading like elite athletics: physical fitness, mental preparation, post-game review, off-season learning.

### The Anti-Ego Rule
> "Being wrong is acceptable. Staying wrong is unacceptable."

When you realise you're wrong (price tells you), exit instantly. Ego — the desire to be proven right — is the most expensive emotion.

### The Recovery Protocol
After a big loss, Schwartz had a specific recovery routine:

1. **Take a day off the market** — no charts, no news
2. **Physical exercise** — to discharge stress hormones
3. **Review the loss with a partner or journal** — what was the rule I broke?
4. **Return with half-size** for the next 3-5 trades
5. **Only return to full size after 3 winners in a row**

### The Self-Image Anchor
He kept a photo of his championship trophy on his desk. Not for ego — as a **reminder that he had proven the system worked**. When doubt crept in, he looked at it and remembered: the process produces results. Trust the process.

---

## Part 9 — KLSE Application: The Full Schwartz Setup

### Watchlist Construction (Sunday)

1. Run KLSE screener for stocks in Stage 2 (Trend Template ≥ 6/8)
2. Filter to top 20 with ADV ≥ RM2M (Schwartz only traded liquid)
3. Open each chart, draw 10-day EMA, note price relative to EMA
4. Categorise:
   - **A-list (Pullback candidates)**: Above 10-day EMA, near it now, possible pullback entry this week
   - **B-list (Breakout candidates)**: Tight consolidation below resistance, possible breakout this week
   - **Watch (no trade yet)**: Stage 2 but extended, wait for setup

### Daily Execution

Each morning, check the A-list and B-list against the 7-question checklist:
- If a stock answers 7/7 → trade it that day
- Otherwise → wait

Maximum 2-3 new positions opened per day. No exceptions.

### Position Management (Daily)

For each open position:
1. Where is price vs the 10-day EMA?
2. Is the stop still appropriate, or should it move up?
3. Has any target tranche been hit?
4. Is the original thesis still intact?

### Drawdown Discipline

Check daily:
- Daily drawdown ≤ 5% of capital?
- Weekly drawdown ≤ 10%?
- Total drawdown from peak ≤ 25%?

Any breach → halt trading per Part 5 rules.

---

## Part 10 — The 12 Schwartz Commandments

Print and post:

1. **The market is always right. I am sometimes wrong.**
2. **Cut losses at -7% — always.**
3. **Daily loss ≥ 5% of account → stop trading for the day.**
4. **The 10-day EMA is the line in the sand.**
5. **No trade unless 7/7 on the checklist.**
6. **Maximum 2-3 new positions per day.**
7. **Take partial profits on the way up — never wait for the top.**
8. **After a big loss, halve position size for the next 3-5 trades.**
9. **If I'm tired, sick, or angry — no trades.**
10. **Trade my system; ignore tips, opinions, news.**
11. **Journal every trade — including the ones I didn't take.**
12. **Compete against my best trading, not against other traders.**

---

## Part 11 — Where Schwartz Differs from Other Masters

| Method | Schwartz | Others |
|--------|---------|--------|
| **Holding period** | Days to 2 weeks | Livermore: weeks-months; Buffett: years |
| **Primary tool** | 10-day EMA | Livermore: pivotal points; Darvas: boxes |
| **Best for** | Active swing traders, tournament-style | Position traders (Minervini), investors (Buffett) |
| **Daily attention** | High — must monitor positions | Lower for position traders |
| **Suits KLSE retail** | Yes — works on Bursa with 1-hour daily commitment | Yes, but requires more screen time than VCP |

**Use Schwartz's framework when**: you want to swing-trade actively, you have 1-2 hours daily, and you're willing to take 2-5 positions concurrently with active management.

**Use Minervini/Livermore framework when**: you want longer-term position trades with less daily attention, holding for weeks to months.

You can run BOTH simultaneously — different capital allocated to each style.

---

## Related Files
- [[36_Livermore_Rules_Reminiscences]] — pivotal points = Schwartz breakouts (same setup)
- [[37_Darvas_Box_Theory]] — alternative breakout system
- [[02_Minervini_SEPA_KLSE]] — longer-term position counterpart
- [[06_Risk_Management_and_Position_Sizing]] — extends Schwartz's tier system
- [[33_Fear_FOMO_Confidence_Mastery]] — the mental game Schwartz emphasised
- [[05_Intraday_Trading_KLSE]] — for the shortest-timeframe Schwartz setups
- [[09_Trading_Psychology]] — the discipline foundation
