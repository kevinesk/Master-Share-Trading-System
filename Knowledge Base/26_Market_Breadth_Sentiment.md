# Market Breadth & Sentiment Indicators

## Why Breadth Matters

**Breadth tells you how healthy the rally really is.** A KLCI rising to new highs while 70% of stocks are falling = narrow, unhealthy rally (distribution). A KLCI rising with 80% of stocks participating = broad, healthy bull market.

> "If only generals are advancing but the soldiers are retreating, the battle is being lost."

---

## 1. Advance-Decline Line (A/D Line)

**What it is**: Running total of (Advancing stocks − Declining stocks) each day.

```
A/D Line = Yesterday's A/D Line + (Advances − Declines) today
```

**Interpretation**:
- A/D Line trending UP with KLCI trending up → Healthy; broad participation
- A/D Line trending DOWN while KLCI trending up → **Divergence — danger signal**
- A/D Line makes new high before KLCI → Leading indicator; bull market strong
- A/D Line fails to make new high when KLCI does → Distribution; reduce exposure

**Where to find KLSE A/D data**:
- Bursa Market Summary: Published daily (advances and declines)
- Calculate manually: track daily in Excel
- i3investor.com → Market → Breadth

### Trading Rule for A/D Line
| A/D Line Trend | KLCI Trend | Signal |
|---------------|-----------|--------|
| Rising | Rising | Strong bull — be fully invested |
| Rising | Flat/weak | A/D leads; KLCI should follow up |
| Falling | Rising | **Bearish divergence — reduce exposure** |
| Falling | Falling | Confirmed bear — go to cash |

---

## 2. McClellan Oscillator (KLSE Version)

The McClellan Oscillator is the most powerful breadth indicator for timing market turns.

**Formula**:
```
McClellan Oscillator = EMA19(Net Advances) − EMA39(Net Advances)
Where: Net Advances = Daily Advances − Daily Declines
```

**Simplified (approximate)**:
```
Raw = Advances − Declines (each day)
Fast EMA = EMA19 of Raw
Slow EMA = EMA39 of Raw
Oscillator = Fast EMA − Slow EMA
```

**Interpretation**:
| Oscillator Level | Market Condition | Action |
|-----------------|-----------------|--------|
| +150 or higher | Overbought — short-term top | Take partial profits |
| +50 to +150 | Bullish territory | Buy breakouts; hold positions |
| 0 to +50 | Neutral/mild bull | Selective; only best setups |
| −50 to 0 | Neutral/mild bear | Half exposure |
| −100 or lower | Oversold — potential bottom | Watch for bounce; buy carefully |
| −200 or lower | Panic selling climax | Look for reversal; major opportunity |

**The McClellan Summation Index** (cumulative McClellan):
- Sum of all daily McClellan values
- Above 0 and rising = bull market confirmed
- Below 0 and falling = bear market confirmed
- Crossing zero from below = new bull market signal
- Crossing zero from above = new bear market signal

**How to calculate for KLSE**:
Build a spreadsheet with daily Advances and Declines from Bursa. Calculate EMA19 and EMA39 of (A−D). Then subtract.

---

## 3. New 52-Week Highs vs Lows

**The most honest breadth indicator.**

```
New Highs-Lows Ratio = New 52W Highs / (New 52W Highs + New 52W Lows)
```

| Ratio | Interpretation |
|-------|---------------|
| >0.80 | Very bullish breadth |
| 0.60–0.80 | Healthy bull |
| 0.40–0.60 | Neutral/mixed |
| 0.20–0.40 | Bearish breadth |
| <0.20 | Very bearish; bear market confirmed |

**Key signal (O'Neil's rule)**:
- If KLCI makes a new high but fewer than 100 stocks are making new 52W highs → distribution — reduce exposure

**Where to find**: Bursa doesn't publish this directly, but your KLSE Screener (in this system) shows stocks within 25% of 52W highs (TT criterion C8).

---

## 4. VIX — The Fear Index

**What it is**: Chicago Board Options Exchange Volatility Index — measures expected S&P 500 volatility over the next 30 days. Published in real-time.

**TradingView**: `CBOE:VIX`

**Why KLSE traders need to watch it**: VIX spikes precede KLSE selloffs by 1–3 days (capital flight from emerging markets).

| VIX Level | Market Condition | KLSE Action |
|-----------|----------------|------------|
| < 12 | Extreme complacency | Markets may be vulnerable; don't add risk |
| 12–16 | Normal low fear | Good buying conditions |
| 16–20 | Mild concern | Selective; reduce new positions |
| 20–30 | Elevated fear | Reduce exposure 30–50% |
| 30–40 | High fear | Raise cash; only hold strongest stocks |
| > 40 | Panic (March 2020, COVID) | Potential generational buying opportunity — but confirm first |
| > 50 | Extreme panic (2008 GFC) | Wait for VIX to start declining before buying |

**VIX contrarian rule**: When VIX reaches extreme highs (>40) AND begins to fall back → that falling VIX is the buy signal. Don't buy on the spike; buy on the decline from the spike.

---

## 5. Put/Call Ratio (Options Sentiment)

**What it is**: Number of put options bought vs call options. High put/call = fear; low put/call = greed.

```
Put/Call Ratio = Volume of Put Options / Volume of Call Options
```

**TradingView**: `CBOE:PCC` (equity P/C ratio) or `CBOE:PCI` (index P/C ratio)

**Malaysia context**: KLSE has limited options market (mainly FBM KLCI Futures and structured warrants). Use the US put/call ratio as a global sentiment gauge.

| P/C Ratio | Sentiment | Contrarian Signal |
|-----------|----------|-------------------|
| < 0.5 | Extreme greed | Sell signal — too much optimism |
| 0.5–0.7 | Mild greed | Normal bull market |
| 0.7–0.9 | Neutral | Wait for direction |
| 0.9–1.1 | Mild fear | Start looking for buys |
| > 1.1 | Extreme fear | Strong buy signal (contrarian) |

---

## 6. KLSE Foreign Flow Breadth

**Unique to Malaysia**: Foreign investors are a significant force. Their collective buying/selling is published daily by Bursa.

**Key metrics**:
- Daily net foreign buy/sell (RM millions)
- Rolling 5-day net flow
- Rolling 20-day net flow

**Interpretation**:
| Foreign Flow (5-day rolling) | Signal |
|------------------------------|--------|
| Net buy >RM500M | Strong inflow; KLCI likely to continue rising |
| Net buy RM100–500M | Mild positive; supportive |
| Net sell RM100–500M | Mild outflow; caution |
| Net sell >RM500M | Significant outflow; reduce exposure |
| Net sell >RM1B in 5 days | Major exit; possible market top |

**The 20-day trend rule**: If 20-day cumulative foreign flow is negative but KLCI is holding up → local institutions (EPF/PNB) are buying. Stable floor but limited upside until foreigners return.

---

## 7. KLCI Breadth Scorecard (Daily Check — 5 Minutes)

Track these every day before market open:

| Indicator | Today | Trend (7-day) | Signal |
|-----------|-------|--------------|--------|
| Advance/Decline ratio | | | |
| New 52W Highs count | | | |
| New 52W Lows count | | | |
| VIX level | | | |
| Foreign net flow (RM) | | | |
| % KLSE stocks above EMA50 | | | |
| McClellan Oscillator | | | |

**Scoring**:
- 5+ indicators bullish → Full deployment
- 3–4 bullish → Selective; take only best setups
- <3 bullish → Reduce exposure; protect capital

---

## 8. Percentage of Stocks Above Key EMAs

**What it is**: Out of all KLSE stocks, what % are above their 50-day or 200-day EMA?

**Healthy bull market**:
- >70% of stocks above EMA50 = broad participation
- >60% of stocks above EMA200 = long-term uptrend intact

**Warning signs**:
- <50% above EMA50 while KLCI near highs = narrowing rally
- <40% above EMA200 = most stocks in downtrend (even if KLCI index holds up due to heavy weights)

**How to calculate**: Run your KLSE Screener and count what % of the 100 stocks have price > EMA50. Our screener already calculates this.

---

## 9. Sector Breadth Rotation

Watch how many SECTORS are participating in a rally:

| Sectors in Bull Mode | Market Assessment |
|---------------------|------------------|
| 7–8 of 8 sectors | Broad, healthy bull — full investment |
| 5–6 sectors | Good bull with some rotation |
| 3–4 sectors | Narrow rally — concentrated risk |
| 1–2 sectors | Very narrow — be in those sectors only; overall caution |
| 0 sectors | Bear market — cash |

**How to track**: Each week, check the RS Rating of the top 2 stocks in each sector. How many sectors have positive RS vs KLCI?

---

## Breadth Divergences — The Most Important Signals

**Bearish divergence** (most dangerous):
- KLCI makes new high
- BUT A/D Line fails to make new high
- AND New 52W Highs declining
- AND VIX rising
→ **REDUCE EXPOSURE IMMEDIATELY. Distribution phase is beginning.**

This pattern preceded every major KLSE top:
- 2008 pre-GFC: A/D diverged 3 months before KLCI peak
- 2018: Breadth weakened 2 months before KLCI decline
- 2021/2022: US breadth diverged, followed by EM including KLSE 

**Bullish confirmation** (best buying opportunity):
- KLCI has corrected 10%+
- A/D Line stabilises and begins rising before KLCI
- New 52W Highs start recovering
- VIX declining from high
- Foreign inflows resuming
→ **BUY AGGRESSIVELY. New bull phase beginning.**
