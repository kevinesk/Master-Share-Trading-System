# Perfect Buy Entry & Sell Exit Mastery

## The Core Truth

There is no "perfect" entry or exit — markets are probabilistic. What you can master is a **repeatable process** that puts the odds in your favour every time.

> "The best traders I know are not right more often. They are just right bigger and wrong smaller."
> — Mark Minervini

---

## Part 1: The Perfect Buy Entry

### The Pyramid of Buy Conditions

All 4 layers must be satisfied before you buy:

```
         Layer 4: EXECUTION
        Entry within 2–3% of pivot

       Layer 3: SETUP CONFIRMATION
      Volume ≥ 1.5× average on breakout

    Layer 2: STOCK CONDITION
   Stage 2 uptrend + Valid base pattern

 Layer 1: MACRO ENVIRONMENT
KLCI > EMA50 + Dow > EMA20 + Sector leading
```

**If any layer fails → do not buy.**

---

### The 3-Step Entry Process

#### Step 1: Pre-Market Preparation (Night Before)

1. Identify your top 3 setup candidates from the screener
2. For each stock, define:
   - **Pivot price**: Exact price where the breakout is confirmed
   - **Stop loss price**: Level where your thesis is wrong
   - **Position size**: Calculated from 2% portfolio risk rule
   - **Volume trigger**: What volume must you see to enter?
3. Set a price alert on TradingView at the pivot level

```
Example Setup Card:
Stock       : CIMB (1023.KL)
Pivot price : RM8.35 (above VCP handle high)
Stop loss   : RM7.80 (below VCP base low) = 6.6% risk
Position    : 1,800 shares (2% of RM50k portfolio = RM1,000 risk ÷ RM0.55/share)
Volume need : ≥ 3M shares on breakout (20-day avg = 1.8M)
```

#### Step 2: Market Open — Observe, Don't Rush

- Never buy in the first 15 minutes of trading
- Let the stock open and establish direction
- Check: Is pre-market volume already elevated? (Gap up with volume = confirm)
- Wait for the **first 15-minute candle to close** above the pivot

#### Step 3: Entry Execution

**Entry trigger (all 3 must be true simultaneously)**:

1. Price has broken above the pivot level (not just touched it)
2. Volume at the time of entry is tracking ≥1.5× the full-day average (scale up: if it's 30 min into trading and you've already seen 60% of average daily volume → it's on pace for 3×)
3. The broad market (KLCI) is positive or at least flat on the day

**Entry technique (limit order, not market order)**:
- Place a limit order 0.5–1% above the pivot
- This ensures you get filled but only on genuine strength, not a gap-and-reversal
- If the stock gaps MORE than 3% above your pivot → skip it. Don't chase.

---

### Buy Entry Timing by Setup Type

| Setup | Best Entry Time | Volume Requirement |
|-------|----------------|-------------------|
| VCP Breakout | 9:30–11:30 AM | ≥2× average by mid-morning |
| Opening Range Breakout | 9:30–10:00 AM | ≥3× average in first 30 min |
| VWAP Reclaim | 9:30–11:30 AM | Above-average on reclaim candle |
| Cup & Handle Breakout | Any time | ≥1.5× average |
| LPS (Wyckoff) | Any time | Low volume = ideal (quiet test) |
| Afternoon Continuation | 14:00–15:30 | ≥1.2× average |

---

### The 5 Entry Mistakes to Never Make

| Mistake | Why It Kills You | The Fix |
|---------|-----------------|---------|
| Buying before the breakout ("anticipating") | You're buying into resistance, not through it | Wait for close above pivot |
| Chasing after missing the breakout | Extended entries have poor risk:reward | Let it go. Wait for pullback to pivot. |
| Ignoring volume on breakout | Low-volume breakouts fail 70%+ of the time | Volume is mandatory |
| Entering in a downtrending market | You're fighting the current | Check KLCI vs EMA50 first |
| Buying on the open without waiting | Opening prints are often misleading | Wait 15–30 minutes |

---

## Part 2: The Perfect Sell Exit

### The 3 Types of Exits — Know Which One You're Using

1. **Stop-loss exit** (losing trade): Defensive — limit damage
2. **Profit-target exit** (winning trade): Offensive — lock in gains at predetermined levels
3. **Trend-following exit** (big winner): Let it run — trail the stop as price rises

Most traders do these in the wrong order: they let losses run and cut winners short. **You must do the opposite.**

---

### Exit Framework: The 3-Tranche System

**Position = 3 tranches of equal size. Exit them at different levels.**

| Tranche | Exit Trigger | Amount | Reason |
|---------|-------------|--------|--------|
| 1st | +15–20% gain OR resistance level | 1/3 out | Lock in profit; protect against reversal |
| 2nd | +30–40% gain OR EMA21 break | 1/3 out | Realise large gain; reduce exposure |
| 3rd | EMA50 daily close below OR thesis broken | Final 1/3 | Let the last piece run with the trend |

**Result**: Even if the stock reverses after hitting +20%, you've locked in profit on 2/3 of the position.

---

### Stop Loss Exit — The Non-Negotiable Rules

**Rule 1: Set the stop at time of entry. Non-negotiable.**
- Before you buy: "If this stock hits RM7.80, I am wrong. I will sell."
- Write it down. Set a price alert.

**Rule 1b: Apply the ATR offset — never AT the obvious level.**
- The placed stop = (logical level) − 0.5 to 1.0 × ATR(14).
- Example: logical stop RM 7.80, ATR 0.15 → broker stop RM 7.69.
- Reason: institutional stop-hunting clears stops resting at the visible swing low/round number before reversing. The offset keeps you in the trade through the sweep.
- Re-size the position AFTER the offset (the wider stop distance feeds back into the 1% risk formula).
- [Full rule: [06_Risk_Management_and_Position_Sizing.md](06_Risk_Management_and_Position_Sizing.md) "ATR-Offset Rule" + source [59_Adam_Khoo_Piranha_Profits.md](59_Adam_Khoo_Piranha_Profits.md) PAM Modules 3 & 4]

**Rule 2: Never widen a stop.**
- Widening a stop is the beginning of the end. It means you're hoping, not trading.
- If the stop is in the wrong place → it was placed wrong. Fix it next trade.

**Rule 3: Move the stop UP as the stock rises. Never DOWN.**

**Stop progression table**:
| Gain | Stop Level | Reasoning |
|------|-----------|-----------|
| Entry | Initial stop (–7–8% or VCP low) | Thesis invalidation |
| +10% | Breakeven (entry price) | Ensure this is never a losing trade |
| +15% | +5% (small profit locked) | First tranche out; stop on 2/3 position |
| +20% | +10% OR EMA21 | Tranche 2 exit; trail remaining |
| +30%+ | EMA21 daily close | Trail aggressively |

---

### Profit Target Exit — When to Sell for Gains

**Automatic partial profit rule (Minervini)**:
- Take 1/3 to 1/2 off the table at +20–25% gain
- This is not optional — it's systematic

**When to sell the full position immediately** (regardless of stop):
- Stock gaps DOWN 10%+ on earnings or news
- Company announces fraud, investigation, or major financial restatement
- Stock closes below EMA50 on the highest volume in months
- The CEO or major shareholder sells a large block

**When NOT to sell (common mistake)**:
- "It's up 15%, let me lock in profits" — if thesis is intact and stop is still valid, hold
- "There's bad news in the sector" — unless YOUR stock breaks its stop, hold
- "I'm scared of a market pullback" — if your stop is properly placed, you're protected

---

### The Trend-Following Exit (For Your Big Winners)

Once a stock has gained >25%, switch from profit-target thinking to **trend-following thinking**:

**Trailing stop using EMAs**:
| Gain Level | Trail Stop Below |
|------------|-----------------|
| +15–25% | EMA21 (daily) |
| +25–40% | EMA10 (daily) |
| +40%+ | EMA10 or hand-trail 5% below recent high |

**Exit rule**: Sell if price CLOSES below the trailing EMA on ABOVE-AVERAGE volume.
- Do NOT sell intraday dips below EMA (noise)
- Require a daily CLOSE below EMA on significant volume (confirmation)

**The 8-Week Hold Rule (O'Neil)**:
- If a stock gains +20% in the first 3 weeks after breakout → this is an exceptional winner
- Hold it for at least 8 weeks from breakout before considering any exit
- These rare fast movers often end up going +50–200%

---

### Reading Climax Tops — When to Exit Before Reversal

Even if your trailing stop hasn't been hit, these signals say the move is ending:

| Signal | What It Looks Like | Action |
|--------|-------------------|--------|
| Exhaustion gap | Stock gaps up 5%+ after already rising 30%+ | Sell 1/2 immediately |
| Parabolic run | 3+ consecutive wide-range up days | Tight stop; ready to exit |
| Highest volume day ever | Record volume on an up day late in trend | Distribution; exit 1/3 |
| Multiple gap-ups in a row | 3+ gap-up opens | Climax behavior; reduce |
| Price too far from EMA50 | >30% above EMA50 | Extended; tight stop |

---

### The Re-Entry Rule

If you sell a stock and it keeps going up:

1. **Wait**: Do not chase. Let it pull back.
2. **Observe**: Does it pull back on low volume to a support level (EMA21, EMA50, or prior breakout level)?
3. **Enter**: If it holds support and volume dries up → re-enter at the new support level with a new stop
4. **This is an LPS (Last Point of Support) entry** — often lower-risk than the original breakout

---

## The Exit Decision Tree

```
Stock in portfolio — daily review:
│
├── Is it at or below my stop loss?
│   YES → SELL immediately. No exceptions.
│   NO  → Continue
│
├── Has it gained +20% or more?
│   YES → Take 1/3 off the table (Tranche 1 exit)
│   NO  → Continue
│
├── Has it shown a climax top signal?
│   YES → Tighten stop to 3% below recent high or exit 1/2
│   NO  → Continue
│
├── Is it below EMA21 on above-average volume (daily close)?
│   YES → Exit Tranche 2 (if not already done). Trail remaining.
│   NO  → Hold
│
└── Is the original thesis (Stage 2 + sector strength) still intact?
    NO  → Exit remaining position
    YES → Hold with stop at EMA21 or EMA50
```

---

## Quick Reference: Entry & Exit Checklist

### Entry Checklist (Every Trade)
- [ ] KLCI > EMA50 (macro is right)?
- [ ] Stock is in Stage 2 uptrend?
- [ ] Valid pattern identified (VCP / Cup / Flag)?
- [ ] Entry within 2–3% of pivot?
- [ ] Volume is ≥1.5× average on breakout?
- [ ] Stop loss level is defined?
- [ ] Position size calculated (max 2% portfolio risk)?
- [ ] Risk:reward ≥ 1:2?
- [ ] Am I buying because of setup, not FOMO?

### Exit Checklist (Every Day You Hold)
- [ ] Is price above my stop loss?
- [ ] Has gain hit +20% (Tranche 1 trigger)?
- [ ] Any climax top signals visible?
- [ ] Is price still above EMA21 on daily chart?
- [ ] Is the sector still leading?
- [ ] Is the original thesis still valid?
