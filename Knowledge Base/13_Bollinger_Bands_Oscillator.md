# Bollinger Bands & Bollinger Oscillator Mastery

## What Are Bollinger Bands?

Invented by John Bollinger in the 1980s. The bands are:
- **Middle Band**: 20-period Simple Moving Average (SMA20)
- **Upper Band**: SMA20 + (2 × Standard Deviation)
- **Lower Band**: SMA20 − (2 × Standard Deviation)

**Key property**: By definition, ~95% of price action falls INSIDE the bands. When price moves outside the bands, it's statistically unusual — a potential trading signal.

---

## The Bollinger Oscillator (%B)

The **%B indicator** measures WHERE price is relative to the bands, expressed as a 0–1 scale:

```
%B = (Close − Lower Band) / (Upper Band − Lower Band)
```

| %B Value | Interpretation |
|----------|---------------|
| 1.0 | Price is AT the upper band |
| >1.0 | Price is ABOVE the upper band (overbought territory) |
| 0.5 | Price is AT the middle band (SMA20) |
| 0.0 | Price is AT the lower band |
| <0.0 | Price is BELOW the lower band (oversold territory) |

**TradingView**: Add "Bollinger Bands %B" from the indicators library.

---

## Bandwidth — Measuring Squeeze and Expansion

```
Bandwidth = (Upper Band − Lower Band) / Middle Band × 100
```

- **Low bandwidth** (bands squeezing together): Volatility contracting — a big move is coming
- **High bandwidth** (bands expanding): Volatility expanding — a move is already underway
- **Squeeze**: Bandwidth at its lowest in 6 months → highest probability setup

---

## The 6 Core Bollinger Band Signals

### 1. The Squeeze (Most Important Setup)

**When bands are tight → a breakout is imminent (direction unknown).**

```
    ___________
   /           \
__/             \__  ← bands squeeze here
                   \_______  ← bands expand on the breakout
```

**Identification**:
- Bandwidth is at a 6-month low (or lower)
- Price is trading in a narrow range
- Volume is declining (confirming the squeeze)

**Trading the Squeeze for KLSE**:
1. Wait for the squeeze (Bandwidth < 6-month average)
2. Watch for a breakout in either direction
3. If breakout is UP on volume → BUY with stop below lower band
4. If breakout is DOWN on volume → Do NOT buy; wait for next setup
5. %B crossing above 0.8 on expanding bandwidth = buy signal

**Pine Script for BB Squeeze**:
```pine
//@version=5
indicator("BB Squeeze Alert")
[upper, mid, lower] = ta.bb(close, 20, 2.0)
bw = (upper - lower) / mid * 100
squeeze = bw == ta.lowest(bw, 126)  // 6-month low bandwidth
plot(bw, color=squeeze ? color.red : color.blue)
bgcolor(squeeze ? color.new(color.red, 85) : na)
```

---

### 2. Walking the Upper Band (Powerful Trend Signal)

When a stock is in a strong uptrend, price can "walk" along the upper band for days or weeks.

```
                       ____
                  ____/    \  ← upper band
         ____    /          \
    ____/    \  /
___/          \/
```

**What it means**: Strong demand is continuously pushing price into statistically overbought territory. In a real uptrend, this is NOT a sell signal — it's a HOLD signal.

**Misuse warning**: Beginners sell when price touches the upper band. In a Stage 2 uptrend, this is wrong. Walking the upper band means the trend is extremely strong.

**KLSE rule**: 
- Walking upper band + Volume staying elevated = continue to hold
- Walking upper band + Volume declining = prepare to exit; rally losing steam

---

### 3. The W-Bottom (Double Bottom with BB)

```
    Lower band: _______________________________________________
                    ↓              ↓
                   B1   (recover) B2
                  /  \_____   ___/ \
                 /         \_/      \___
```

**Pattern**:
1. Price closes below lower band (**B1**) on high volume — panic selling
2. Price bounces back above lower band
3. Price pulls back but does NOT close below lower band (**B2**) — volume lower
4. %B is higher at B2 than at B1 (positive divergence)
5. Price then surges above middle band (SMA20) → **buy signal**

**Entry**: When %B crosses above 0.5 (middle band) after the W-bottom
**Stop**: Below B2 low
**This is equivalent to the Wyckoff W-bottom / double bottom at support**

---

### 4. The M-Top (Double Top — Exit Signal)

Mirror of the W-bottom. Forms at tops:
1. Price closes above upper band (P1) — euphoria
2. Price pulls back, stays inside bands
3. Price rallies again but CANNOT close above upper band (P2) — weakness
4. %B is LOWER at P2 than at P1 (negative divergence)
5. Price crosses below middle band → **exit signal**

**KLSE action**: Exit remaining position when M-top + volume diminishing on second peak.

---

### 5. %B + Volume Oscillator Divergence

**Bullish divergence** (buy signal):
- %B making lower lows
- Volume on down bars is DECLINING (sellers weakening)
- Then %B turns up → strong buy signal

**Bearish divergence** (sell/avoid signal):
- %B making higher highs  
- Volume on up bars is DECLINING (buyers weakening)
- Then %B turns down → exit signal

---

### 6. Bollinger Band Bounce (Trend Continuation)

In an established uptrend, price pulling back to the lower band = a buying opportunity.

**Conditions for a valid bounce setup**:
- Stock is in clear Stage 2 (above EMA50 and EMA200)
- Price pulls back to lower Bollinger Band
- RSI is between 40–50 (not overbought, not oversold)
- Volume on the pullback is BELOW average (no heavy selling)
- %B drops to 0.0–0.2 range

**Entry**: When price closes back above SMA20 (middle band) with increasing volume
**Stop**: Below the lower band low
**Target**: Upper band or prior high

---

## %B + RSI Combined Strategy (High Accuracy)

Using both %B and RSI together filters out many false signals:

| %B | RSI | Signal |
|----|-----|--------|
| >0.9 and rising | >70 | Overbought — take partial profits |
| >0.9 and rising | 50–70 | Strong uptrend walking upper band — hold |
| 0.4–0.6 | 45–55 | Neutral — consolidation, no action |
| <0.2 and falling | <35 | Potential bottom — watch for reversal |
| <0.2 and rising | Crossing up from 30 | W-bottom setup — buy on confirmation |
| <0.0 (below lower band) | <25 | Oversold climax — possible Wyckoff SC |

---

## Bollinger Band Settings for KLSE

**Standard settings** (works for most stocks):
- Period: 20
- Standard Deviation: 2.0

**Alternative settings by timeframe**:
| Timeframe | Period | Std Dev | Best For |
|-----------|--------|---------|----------|
| Daily | 20 | 2.0 | Swing trading (standard) |
| Daily | 10 | 1.5 | Short-term trades |
| Weekly | 20 | 2.0 | Position trades, major trend |
| 60-min | 20 | 2.0 | Intraday swing within the day |
| 5-min | 20 | 2.0 | Intraday scalping |

**For VCP / Minervini setups**: Keep at 20/2.0 (daily). The squeeze on daily chart is the most meaningful.

---

## Bollinger Oscillator Dashboard (Pine Script)

```pine
//@version=5
indicator("BB Oscillator Dashboard", overlay=false)

// Calculations
[upper, mid, lower] = ta.bb(close, 20, 2.0)
pctB     = (close - lower) / (upper - lower)
bw       = (upper - lower) / mid * 100
bw_avg   = ta.sma(bw, 126)
squeeze  = bw < bw_avg * 0.7

// RSI
rsi = ta.rsi(close, 14)

// Plot %B
plot(pctB, title="%B", color=pctB > 0.8 ? color.green : pctB < 0.2 ? color.red : color.blue, linewidth=2)
hline(1.0, "Upper Band", color=color.green, linestyle=hline.style_dashed)
hline(0.8, "Near Upper", color=color.green, linestyle=hline.style_dotted)
hline(0.5, "Middle Band", color=color.gray, linestyle=hline.style_dashed)
hline(0.2, "Near Lower", color=color.red, linestyle=hline.style_dotted)
hline(0.0, "Lower Band", color=color.red, linestyle=hline.style_dashed)

// Background: squeeze alert
bgcolor(squeeze ? color.new(color.red, 88) : na, title="Squeeze")
```

---

## KLSE Bollinger Band Trading Rules

1. **Never sell just because price touches the upper band** — in a Stage 2 uptrend, this is strength, not a sell signal.

2. **The squeeze is your setup** — find stocks with bandwidth at 6-month lows. These will make big moves soon.

3. **%B below 0.2 in an uptrend = buy opportunity** — price is at the lower band of an uptrend, which is support.

4. **M-Top + declining volume = exit** — when price can no longer reach the upper band and volume drops, the trend is ending.

5. **Use %B with RSI for confirmation** — %B tells you WHERE price is; RSI tells you the MOMENTUM. Together they're much more reliable than either alone.

6. **Weekly Bollinger Squeeze → major move coming** — when the weekly chart squeezes, the resulting move can last months. This is the setup for position trades.
