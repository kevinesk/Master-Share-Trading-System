# David Ryan & Dan Zanger — The Schwager Wizards

This file combines two of the most actionable interviews from Jack Schwager's *Stock Market Wizards* (2001):

- **David Ryan** — Three-time U.S. Investing Champion (1985, 1986, 1987), protégé of William O'Neil at IBD
- **Dan Zanger** — Turned $11,000 into $42 million in under 2 years (1998-2000); holds the Guinness world record for the largest stock market percentage gain in a 12-month period (29,233%)

Both are momentum/breakout traders. Both are obsessive about chart patterns. Both have explicit, testable rules — making them ideal additions to your KLSE system.

---

## PART A — DAVID RYAN

### A1. Background and Approach

David Ryan trained directly under William O'Neil at *Investor's Business Daily*. He won the U.S. Investing Championship three years running using **CAN SLIM-derived methodology refined through extreme chart selectivity**.

His edge: **He looks at thousands of charts per week.** Pattern recognition through volume is his entire competitive advantage.

> "I look at 70 charts a night. Some nights more. Year after year. After a while you just SEE the right setups — the way a doctor sees a pattern in symptoms."

### A2. The Tight Weekly Closure Rule (Ryan's Signature)

Ryan's #1 setup criterion. On the **WEEKLY chart**:

A "tight closure" = the weekly closing prices over the most recent 3-7 weeks are within a very small range (typically 1-3% of each other).

```
Week 1 close: RM5.00
Week 2 close: RM5.05  
Week 3 close: RM4.98       ← Range: RM4.98 to RM5.05 (1.4%)
Week 4 close: RM5.02       ← VERY tight closures
Week 5 close: RM5.03
                           
THEN breakout above the range on volume → trade
```

### Why Tight Closures Matter

Tight weekly closes mean:
- **Almost no distribution** — sellers have stopped pushing price down
- **No froth** — buyers aren't paying up impulsively
- **Coiled spring** — all forces are balanced and energy is building
- **Institutional accumulation in progress** — big money buying without moving price

When the breakout finally comes, the move is explosive because there's no overhead supply.

### Ryan's Tight Closure Specifications

| Metric | Ryan's Rule |
|--------|------------|
| Number of weeks | 3-7 consecutive weeks |
| Range tightness | Within 3% (highest to lowest close) |
| Volume during tight period | Decreasing — under 50-day avg |
| Position in chart | Near 52-week high; Stage 2 |
| Breakout volume | ≥50% above 10-week average |

### A3. Ryan's Screening Routine

Every night, Ryan ran a multi-step screen:

```
Step 1: Look at ALL stocks above $10 (excludes penny noise)
Step 2: Filter to those near 52-week high
Step 3: Quick chart visual scan — eyeball pattern quality
Step 4: For interesting charts: check earnings (must be growing)
Step 5: Check RS Rating: must be top 20% of all stocks
Step 6: Note pivot point and stop level
Step 7: Final list: 10-15 names with alerts set
```

### KLSE Adaptation: Ryan's Nightly Routine

```
Each evening (30 minutes):

1. Pull KLSE Screener output (your existing tool)
2. Filter: Price > RM1.00, ADV > RM500K, within 15% of 52-week high
3. Visual scan top 30 weekly charts — look for tight closures
4. Mark candidates with 3+ tight weekly closes in upper range
5. Cross-check earnings: 3 consecutive quarters of growth
6. Check RS rating: must be RS+ vs KLCI
7. Set TradingView alert at the breakout pivot
8. Maintain rolling watchlist of 10-15 names
```

### A4. Ryan's 10-Day Moving Average Pullback

Beyond breakouts, Ryan's second-favorite entry: **pullback to the 10-day EMA** in a confirmed uptrend.

The setup:
1. Stock in clear uptrend (HH/HL on daily)
2. Above 10-day EMA for at least 10 trading days
3. Pulls back to TOUCH the 10-day EMA on light volume
4. First up-day after the touch → entry signal

Entry: Above the day's high after the touch.
Stop: Below the day's low after the touch (typically 3-5% below entry).

This is the same setup Schwartz used (see [38_Pit_Bull_Schwartz_Method.md](38_Pit_Bull_Schwartz_Method.md)). Different traders, same edge.

### A5. Ryan's Position Sizing & Risk Rules

| Rule | Detail |
|------|--------|
| **Max risk per trade** | 1.5% of total capital (tighter than O'Neil's 2%) |
| **Stop loss** | 7% maximum from entry — typically 4-5% |
| **Position count** | 6-10 active positions (concentrated, not diversified) |
| **Cash level** | 100% cash during M-down markets — no exceptions |
| **Drawdown response** | Reduces size by 50% after -5% portfolio drawdown |

### A6. Ryan's Selling Discipline

Same as O'Neil with refinements:
1. 7% stop → exit immediately
2. Take 20-25% profit on most stocks
3. Hold 8 weeks minimum if up 20% in first 3 weeks (the "exceptional stock" rule)
4. Sell on first close below 50-day MA on heavy volume
5. Sell on largest weekly volume + range expansion (climax)

### A7. Ryan's Key Quotes (Print These)

1. *"The hardest thing in trading is doing nothing. Most setups aren't worth a trade. Wait."*
2. *"Tight closures are the market's whisper that something big is coming."*
3. *"I'd rather miss a 50% move than take a 15% loss."*
4. *"If you're not looking at charts every day, you're not in the game."*

---

## PART B — DAN ZANGER

### B1. Background and Approach

Dan Zanger was a swimming pool contractor in California who started trading after work hours. Between June 1998 and December 1999, he turned $10,775 into $18 million. By April 2000 he was at $42 million.

His method is **pure technical** — chart patterns, volume, momentum — with zero fundamental analysis. He runs the **Chart Pattern Trader** newsletter and famously says he doesn't even know what most of the companies he trades do.

> "I trade chart patterns, not stocks. I look at thousands of charts a day. The patterns are everything."

### B2. Zanger's Five Core Chart Patterns

#### Pattern 1: The Bull Flag

```
         ___ Pole top
        /
       /
      /   __  ← Flag (tight downward channel, 3-15 days)
     /   __\
    /   __\\
   /   ___\\\__   ← Breakout above upper trendline
  /                   
 / POLE — sharp, near-vertical advance (5-15 days)
/
```

Zanger's specs:
- Pole: ≥15% move in ≤10 trading days
- Flag: Tight downward-sloping channel, 3-15 days
- Flag retracement: Maximum 38% of the pole (Fibonacci)
- Volume: HIGH during pole, DRIES UP during flag, SURGES on breakout
- Entry: Above upper flag trendline + 0.10
- Stop: Below lower flag trendline (typically 5-8% from entry)
- Target: Pole length projected from breakout point

#### Pattern 2: The Pennant

Similar to bull flag but the consolidation is a SYMMETRICAL triangle, not a channel:

```
       ___
      /   \  
     /     \____
    /          ____  ← Converging trendlines
   /     pennant      
  /                       
 / pole                   
```

Specs:
- Pole: ≥15% in ≤10 days
- Pennant: 3-15 days, converging trendlines
- Volume: Dries up dramatically
- Entry: Above upper trendline of pennant
- Stop: Below lower trendline
- Target: Same as flag — pole length projected

#### Pattern 3: The Ascending Channel

```
       /          ← Upper trendline (resistance)
      /  /       
     /  /  /     
    /  /  /     ← Stock bouncing between trendlines
   /  /  /      ← BUY at lower trendline touches
  /  /  /      ← TAKE PARTIAL at upper trendline
                  
       /           ← Lower trendline (support)
      /          
     /            
    /             
```

Specs:
- Both trendlines have positive slope (rising)
- Stock has touched each line at least 3 times
- Volume rises with upper touches, dries on lower touches
- Trade: Buy at lower trendline test; sell partial at upper touch
- Stop: Below lower trendline

#### Pattern 4: The Symmetrical Triangle (Continuation)

```
       __
      |  ----___        ← Upper resistance falling
      |          ----   
      |_____________--  ← Apex; breakout point
      |              -- 
      |       ___---    ← Lower support rising
      |  ___--          
      |--               
```

Specs:
- Lower trendline rising (higher lows)
- Upper trendline falling (lower highs)
- Volume decreases during formation
- Breakout direction = direction of prior trend (continuation pattern)
- Entry: Breakout above upper trendline on volume

#### Pattern 5: The Cup-with-Handle (Zanger's Version)

Zanger uses O'Neil's cup-handle (see [39_ONeil_Greatest_Winners_Templates.md](39_ONeil_Greatest_Winners_Templates.md)) — but with FASTER cup formation (3-12 weeks vs O'Neil's 7-65 weeks). Zanger trades the **faster, smaller cup-handles** — momentum versions of O'Neil's classic.

### B3. Zanger's Volume Confirmation Rules

Volume is Zanger's most-emphasized concept. His rules:

| Phase | Required Volume |
|-------|----------------|
| Pole/run-up | At least 2× average daily volume on advance days |
| Consolidation | Volume drops to UNDER 50% of pole volume |
| Breakout day | Volume ≥ 2× the average of the consolidation period |
| Day 2-3 post-breakout | Volume holds elevated; if drops sharply → fake breakout |

### B4. Zanger's Entry Method

1. Identify the pattern (one of the 5 above)
2. Mark the breakout line precisely
3. Set buy-stop order at breakout line + 0.10
4. When triggered, also place hard stop-loss immediately
5. Take partial profits at projected target (pole length, channel width, etc.)
6. Trail remaining shares with 10-day EMA

### B5. Zanger's Stop Loss Rules

| Pattern | Stop Level |
|---------|-----------|
| Bull Flag | Below lower flag trendline |
| Pennant | Below lower pennant trendline |
| Ascending Channel | Below the lower trendline |
| Symmetrical Triangle | Below the rising trendline |
| Cup-with-Handle | Below the handle low |

**Max risk per trade**: 1-2% of capital. Often less (Zanger sometimes risks 0.5%).

### B6. Zanger's Position Management

> "Once a trade is working, I add. Once it's not working, I'm out. There's no middle."

**Pyramiding rules**:
- After +10% in trade, scale in another 25% on next consolidation breakout
- Never add to a loser
- Total position across pyramid: max 4× initial position

**Exit triggers**:
- Stop hit → out immediately
- Failed breakout (back inside the pattern) → out immediately
- Daily close below 10-day EMA on heavy volume → out
- Daily close below 21-day EMA → out (no exceptions for swing positions)
- Climactic gap up with reversal candle → take majority off

### B7. Zanger's Daily Routine

```
Pre-market: Scan 1,000+ charts (he literally does this)
            Identify 30-50 setups forming
            
Open: Watch for breakouts in first 30 min
      Take 3-5 best setups
      
Mid-day: Manage open positions
         Trail stops
         Take partial profits at targets
         
Close: Review every trade — what worked, what didn't
       Set alerts for next day setups
```

He scans MANY charts because the edge is in **only trading A+ setups**. Most days, he sees few or no A+ setups and stays flat.

### B8. Zanger's Key Quotes

1. *"I don't trade stocks. I trade chart patterns."*
2. *"If volume doesn't confirm, the pattern is a lie."*
3. *"I'd rather miss the trade than fight the trade."*
4. *"Scan thousands of charts. Trade three. That's the game."*

---

## PART C — APPLYING RYAN + ZANGER TO KLSE

### C1. Combined Setup Hierarchy

Use Ryan's tight closures + Zanger's patterns together. Stocks scoring on BOTH = highest priority:

| Setup | Ryan Element | Zanger Element | Action |
|-------|-------------|---------------|--------|
| **A+** | Tight 5+ week closures | Bull flag or cup-handle forming | Full position |
| **A** | Tight closures only | No clean pattern yet | Watch, wait |
| **B** | No tight closures | Clean Zanger pattern | Half position |
| **C** | Neither | Random setup | Skip |

### C2. KLSE Daily Workflow (Ryan + Zanger Combined)

**Sunday Evening (45 minutes)**:
1. Pull KLSE screener for stocks meeting Trend Template
2. Open WEEKLY charts of top 30 candidates
3. Apply Ryan's tight closure scan (3+ weeks within 3% range)
4. For each tight-closure stock, check DAILY chart for Zanger patterns
5. Build A+ list (5-10 names with both elements)
6. Build A list (5-10 names with just one)
7. Set TradingView alerts at all pivot points

**During Week (15 min/day)**:
1. Check alerts each morning
2. When triggered, verify:
   - Volume ≥ 1.5× average (≥2× ideal)
   - Closing in upper third of day's range
   - KLCI above 10-day EMA
3. Buy on confirmation
4. Place hard stop per pattern rules
5. Set partial-profit alerts at pattern targets

**Weekend Review (30 min)**:
- Review every trade taken
- Mark winning patterns and losing patterns
- Build a personal "what works on KLSE" pattern library

### C3. KLSE-Specific Pattern Frequency

| Pattern | KLSE Frequency | Best Sectors |
|---------|---------------|--------------|
| Tight closures (Ryan) | Very common | Banking, REITs, Consumer staples |
| Bull Flag | Common | Tech (after sector momentum), Gloves (during cycles) |
| Pennant | Moderate | Mid-caps post-news |
| Ascending Channel | Common | Banks, plantation stocks |
| Cup-with-Handle (fast) | Moderate | Tech leaders, healthcare |
| Cup-with-Handle (slow) | Very common | Large-caps, REITs |

### C4. The "Cheat" Entry (Combined with [42](42_Momentum_Masters_Advanced_VCP.md))

Both Ryan and Zanger sometimes enter EARLY — before the official breakout — when:
- The tight closure is extremely tight (last 2 weeks within 1%)
- The pattern is textbook
- The market is in a confirmed uptrend

The "cheat" entry: buy at the LAST tight close, before the breakout, with a stop just below the tight range. This gives an extra 2-3% of upside but requires the discipline to exit immediately on a failed breakout.

This is more detailed in [42_Momentum_Masters_Advanced_VCP.md](42_Momentum_Masters_Advanced_VCP.md).

---

## Part D — Combined 10-Point Master Checklist

Use this before every entry from a Ryan-Zanger setup:

| # | Check | Pass? |
|---|-------|-------|
| 1 | Stock in Stage 2 uptrend (TT ≥ 6/8) | □ |
| 2 | RS Rating ≥ +5 vs KLCI | □ |
| 3 | Weekly closures tight (3+ weeks within 3%) [Ryan] | □ |
| 4 | Daily chart shows clean Zanger pattern | □ |
| 5 | Volume contracted during base/flag | □ |
| 6 | Pivot point clearly defined | □ |
| 7 | Stop loss < 7% from entry | □ |
| 8 | Breakout volume ≥ 1.5× 50-day average | □ |
| 9 | Close in upper 1/3 of day's range | □ |
| 10 | KLCI above 10-day EMA | □ |

**Scoring**:
- 9-10 ✓ = A+ trade, full position
- 7-8 ✓ = A trade, 70% position
- 5-6 ✓ = B trade, 50% position or skip
- <5 ✓ = No trade

---

## Related Files
- [[39_ONeil_Greatest_Winners_Templates]] — chart pattern specs
- [[37_Darvas_Box_Theory]] — earlier ancestor of breakout systems
- [[36_Livermore_Rules_Reminiscences]] — the philosophical foundation
- [[38_Pit_Bull_Schwartz_Method]] — similar 10-day MA pullback method
- [[42_Momentum_Masters_Advanced_VCP]] — the cheat entry and advanced execution
- [[07_Technical_Chart_Patterns]] — pattern library reference
- [[34_Advanced_Technical_Analysis]] — confluence and MTF analysis
