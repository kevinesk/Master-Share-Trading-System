# TradingView & Pine Script Mastery

## TradingView Setup for KLSE

### Connecting KLSE Stocks
- Ticker format: `MYX:1023` (CIMB), `MYX:MAYBANK`, `MYX:0097` (VITROX)
- Index: `MYX:FBMKLCI` (KLCI), `MYX:FBM70` (FBM Mid 70)
- Or use the search bar and type stock name — TradingView auto-suggests KLSE stocks

### Essential Chart Settings for KLSE Swing Trading

**Timeframe hierarchy**:
- **Weekly**: Identify Stage 2, count VCP contractions, check 52W high/low
- **Daily**: Main chart for entry/exit decisions
- **60-minute**: Confirm intraday entry, watch for volume patterns
- **5-minute**: Precise entry on breakout day only

**Recommended indicators to pin**:
1. EMA 21 (purple)
2. EMA 50 (blue)
3. EMA 150 (orange)
4. EMA 200 (red)
5. Volume bars (colour: green/red based on close vs open)
6. RSI 14 (separate pane)
7. VWAP (for intraday charts only)

---

## Pine Script Fundamentals

Pine Script is TradingView's built-in scripting language. Version 5 is current.

### Basic Structure of Every Script

```pine
//@version=5
indicator("My Indicator", overlay=true, max_bars_back=500)

// 1. Inputs (user-configurable settings)
len = input.int(14, title="Length", minval=1)

// 2. Calculations
myEMA = ta.ema(close, len)

// 3. Plotting
plot(myEMA, color=color.blue, linewidth=2, title="EMA")
```

### Essential Pine Script Functions

```pine
// Price data
open, high, low, close, volume  // current bar
close[1]    // previous bar's close
close[5]    // 5 bars ago

// Moving averages
ta.sma(close, 20)     // Simple MA
ta.ema(close, 50)     // Exponential MA
ta.wma(close, 20)     // Weighted MA

// Indicators
ta.rsi(close, 14)                     // RSI
[macd, signal, hist] = ta.macd(close, 12, 26, 9)  // MACD
[upper, basis, lower] = ta.bb(close, 20, 2.0)      // Bollinger Bands
ta.atr(14)                            // Average True Range

// Highest/Lowest
ta.highest(high, 52*5)   // 52-week high (5 days/week)
ta.lowest(low, 52*5)     // 52-week low

// Volume
volume                    // current bar volume
ta.sma(volume, 20)        // 20-day average volume
```

---

## Pine Script: KLSE VCP Stage Indicator (v2 — MATCHES THE SCREENER)

**This is the primary script.** It reproduces the exact logic of
`KLSE Screener\klse_screener.py` on your chart, so the chart and the screener
never disagree. It classifies every bar into a stage and fires alerts so you
never have to chase a breakout from a next-day scan.

- **COILING** (purple bg) — tight VCP, volume dried up, below pivot → WATCH
- **BREAKOUT** (green bg) — cleared the pivot, ≤3% past it → BUY ZONE
- **EXTENDED** (red bg) — >3% past pivot → too late, skip
- **BASING** (orange bg) — above EMA50 but no tight coil yet
- **WEAK** (no bg) — below EMA50

It also tags **IMMINENT** (coil pinned just below pivot — breaks soon, minimal
wait) and **STARTER** (tightest coil near the base low — optional 1/3 entry).

```pine
//@version=5
indicator("KLSE VCP Stage v2", overlay=true, max_bars_back=600)

// ─── Inputs (keep these identical to klse_screener.py CONFIG) ───
pivotLB  = input.int(15,   "Pivot lookback (bars)")
buyZone  = input.float(3.0,"Buy zone % above pivot")
extPct   = input.float(3.0,"Extended: % above pivot")
dryPct   = input.int(35,   "Volume dry-up percentile")
coilPct  = input.int(20,   "Coil BB-width percentile")
tightPct = input.int(10,   "Tight-coil BB-width percentile")
immPct   = input.float(3.0,"Imminent: max % below pivot")
showLbl  = input.bool(true,"Show stage label")

// ─── EMAs + Minervini Trend Template (0-8) ───
e20  = ta.ema(close, 20)
e50  = ta.ema(close, 50)
e150 = ta.ema(close, 150)
e200 = ta.ema(close, 200)
hi52 = ta.highest(high, 260)
lo52 = ta.lowest(low, 260)
tt = (close>e150?1:0) + (close>e200?1:0) + (e150>e200?1:0) + (e200>e200[20]?1:0) + (e50>e150?1:0) + (close>e50?1:0) + ((close/lo52-1)>=0.30?1:0) + ((close/hi52-1)>=-0.25?1:0)

// ─── Pivot & coil low (prior N bars, excluding the current bar) ───
pivot   = ta.highest(high, pivotLB)[1]
coilLow = ta.lowest(low,  pivotLB)[1]
dist    = (close / pivot - 1) * 100

// ─── Bollinger width + percentile-based coil detection ───
[bbU, bbB, bbL] = ta.bb(close, 20, 2.0)
bbw   = (bbU - bbL) / bbB
coil  = bbw <= ta.percentile_nearest_rank(bbw, 252, coilPct)
tight = bbw <= ta.percentile_nearest_rank(bbw, 252, tightPct)

// ─── Volume: dry-up (coil confirm) vs surge (breakout confirm) ───
volDry   = ta.sma(volume, 5) <= ta.percentile_nearest_rank(volume, 60, dryPct)
volSurge = volume >= 1.5 * ta.sma(volume, 20)

// ─── Stage classification (mirrors the Python screener) ───
aboveE50   = close > e50
isBreakout = aboveE50 and close > pivot and dist <= extPct
isExtended = aboveE50 and close > pivot and dist >  extPct
isCoiling  = aboveE50 and close <= pivot and coil and volDry
isBasing   = aboveE50 and close <= pivot and not (coil and volDry)

stage = isBreakout ? "BREAKOUT" : isExtended ? "EXTENDED" : isCoiling ? "COILING" : isBasing ? "BASING" : "WEAK"

imminent   = isCoiling and dist >= -immPct and dist <= 0 and volDry
starter    = isCoiling and tight and (close/coilLow - 1)*100 <= 4
brokeToday = close > pivot and close[1] <= pivot and volSurge

// ─── Visuals ───
stageCol = isBreakout ? color.new(color.green, 88) : isExtended ? color.new(color.red, 90) : isCoiling ? color.new(color.purple, 87) : isBasing ? color.new(color.orange, 93) : na
bgcolor(stageCol)

plot(pivot,                  "Pivot",        color=color.new(color.blue,0),  linewidth=2)
plot(pivot*(1+buyZone/100),  "Buy-zone top", color=color.new(color.green,30), linewidth=1)
plot(e50,  "EMA50",  color=color.new(color.blue,40))
plot(e200, "EMA200", color=color.new(color.red, 40))

lblCol = isBreakout ? color.green : isCoiling ? color.purple : isExtended ? color.red : color.gray
if showLbl and barstate.islast
    txt = stage + "  " + str.tostring(dist, "#.#") + "% vs pivot  TT" + str.tostring(tt) + "/8" + (imminent ? "  IMMINENT" : "") + (starter ? "  STARTER 1/3" : "")
    label.new(bar_index, high, txt, style=label.style_label_down, color=lblCol, textcolor=color.white, size=size.normal)

// ─── Alerts — set ONCE, let them fire so you never chase ───
alertcondition(brokeToday, "VCP Breakout", "{{ticker}} BROKE OUT above pivot on volume - in BUY ZONE now")
alertcondition(imminent and not imminent[1], "Coil Imminent", "{{ticker}} coil is now IMMINENT (pinned below pivot) - breakout near")
alertcondition(starter and not starter[1], "Starter Zone", "{{ticker}} in tight coil near base low - optional 1/3 starter entry")
```

**How to set the alerts (do this once per watchlist stock):**
1. Add the indicator to the chart, set timeframe to **Daily**.
2. Right-click the chart → *Add alert* → Condition = `KLSE VCP Stage v2`.
3. Pick **VCP Breakout** (and optionally **Coil Imminent**).
4. Notifications: email + mobile push. Leave it — your cash stays free until
   the alert fires. That is how you avoid locked funds: the alert waits, not
   your money.

---

## Pine Script: KLSE Trend Template Indicator

This script colours the background based on how many of the 8 Trend Template criteria are met.

```pine
//@version=5
indicator("KLSE Trend Template", overlay=true)

// EMAs
e21  = ta.ema(close, 21)
e50  = ta.ema(close, 50)
e150 = ta.ema(close, 150)
e200 = ta.ema(close, 200)

// 52-week high/low (260 trading days = 52 weeks)
hi52 = ta.highest(high, 260)
lo52 = ta.lowest(low, 260)

// Trend Template criteria
c1 = close > e150
c2 = close > e200
c3 = e150 > e200
c4 = e200 > e200[20]                        // EMA200 trending up (vs 4 weeks ago)
c5 = e50 > e150
c6 = close > e50
c7 = (close / lo52 - 1) >= 0.30             // At least 30% above 52W low
c8 = (close / hi52 - 1) >= -0.25            // Within 25% of 52W high

score = (c1?1:0) + (c2?1:0) + (c3?1:0) + (c4?1:0) + (c5?1:0) + (c6?1:0) + (c7?1:0) + (c8?1:0)

// Background colour based on score
bgCol = score >= 7 ? color.new(color.green, 90) : score >= 5 ? color.new(color.blue, 90) : score >= 3 ? color.new(color.orange, 92) : color.new(color.red, 93)
bgcolor(bgCol)

// Plot EMAs
plot(e21,  color=color.purple, linewidth=1, title="EMA21")
plot(e50,  color=color.blue,   linewidth=2, title="EMA50")
plot(e150, color=color.orange, linewidth=1, title="EMA150")
plot(e200, color=color.red,    linewidth=2, title="EMA200")

// Score label on chart
lblCol = score >= 7 ? color.green : score >= 5 ? color.blue : color.red
if barstate.islast
    label.new(bar_index, high * 1.01, text="TT:" + str.tostring(score) + "/8", color=lblCol, style=label.style_label_down, size=size.small)
```

---

## Pine Script: VCP Volume Contraction Detector

```pine
//@version=5
indicator("VCP Volume Contraction", overlay=false)

// Settings
atr_len = input.int(10, "ATR Length")
vol_len = input.int(20, "Volume MA Length")

atr     = ta.atr(atr_len)
vol_avg = ta.sma(volume, vol_len)
vol_ratio = volume / vol_avg

// Volume contraction: current volume significantly below average
is_contracting = vol_ratio < 0.6

// ATR contraction: price range narrowing
atr_avg = ta.sma(atr, 10)
is_tight = atr < atr_avg * 0.7

// Both contracting = VCP candidate
vcp_signal = is_contracting and is_tight

// Plot
plot(vol_ratio, title="Vol Ratio", color=is_contracting ? color.green : color.gray, linewidth=2)
hline(1.0, "Average", color=color.gray, linestyle=hline.style_dashed)
hline(0.6, "Contraction Zone", color=color.green, linestyle=hline.style_dashed)

bgcolor(vcp_signal ? color.new(color.green, 85) : na, title="VCP Zone")
```

---

## Pine Script: Minervini RS Rating vs KLCI

```pine
//@version=5
indicator("RS Rating vs KLCI", overlay=false)

// Settings
lookback = input.int(252, "Lookback Days (252=1 year)")

// Fetch KLCI
klci = request.security("MYX:FBMKLCI", timeframe.period, close)

// RS Calculation
stock_ret = (close / close[lookback] - 1) * 100
klci_ret  = (klci  / klci[lookback]  - 1) * 100
rs        = stock_ret - klci_ret

// Plot
plot(rs, title="RS vs KLCI (%)", color=rs >= 0 ? color.green : color.red, linewidth=2)
hline(0, "Market Parity", color=color.gray)
hline(10, "Strong Outperformance", color=color.green, linestyle=hline.style_dashed)
hline(-10, "Underperformance", color=color.red, linestyle=hline.style_dashed)

// Background
bgCol = rs >= 10 ? color.new(color.green, 90) : rs >= 0 ? color.new(color.blue, 90) : color.new(color.red, 92)
bgcolor(bgCol)
```

---

## Pine Script: Simple Backtesting Strategy (VCP Breakout)

```pine
//@version=5
strategy("KLSE VCP Breakout Backtest", overlay=true,
         initial_capital=50000,
         default_qty_type=strategy.percent_of_equity,
         default_qty_value=10,
         commission_type=strategy.commission.percent,
         commission_value=0.3)   // 0.3% round-trip est.

// Inputs
ema_fast = input.int(21, "Fast EMA")
ema_slow = input.int(50, "Slow EMA")
vol_mult = input.float(1.5, "Min Volume Multiple for Breakout")
stop_pct = input.float(7.0, "Stop Loss %") / 100

// Indicators
fast = ta.ema(close, ema_fast)
slow = ta.ema(close, ema_slow)
vol_avg = ta.sma(volume, 20)

// Trend filter
in_uptrend = close > slow and slow > ta.ema(close, 150)

// Breakout signal: new 20-day high with volume
new_high = high == ta.highest(high, 20)
vol_surging = volume >= vol_avg * vol_mult

// Entry
long_entry = in_uptrend and new_high and vol_surging
if long_entry
    strategy.entry("Long", strategy.long)

// Exit: stop loss or EMA break
stop_price = strategy.position_avg_price * (1 - stop_pct)
ema_break  = close < fast

if strategy.position_size > 0
    strategy.exit("Stop", "Long", stop=stop_price)
    if ema_break
        strategy.close("Long", comment="EMA Break")

// Plot
plot(fast, color=color.purple, linewidth=1)
plot(slow, color=color.blue, linewidth=2)
```

**How to read backtest results**:
- **Net Profit**: Total profit after commissions
- **Win Rate**: % of winning trades (aim for 40–60%)
- **Profit Factor**: Gross profit ÷ Gross loss (aim for >1.5)
- **Max Drawdown**: Worst peak-to-trough decline (must be tolerable)
- **Sharpe Ratio**: Risk-adjusted return (>1.0 is acceptable, >2.0 is excellent)

---

## Pine Script: Bollinger Band Squeeze Alert

```pine
//@version=5
indicator("BB Squeeze + Breakout", overlay=false)

// Bollinger Bands
length = input.int(20, "BB Length")
mult   = input.float(2.0, "BB Multiplier")

[upper, basis, lower] = ta.bb(close, length, mult)
bb_width = (upper - lower) / basis * 100

// Squeeze: bandwidth at 6-month low
squeeze = bb_width == ta.lowest(bb_width, 126)

// Keltner Channels (for squeeze filter)
kc_mult  = input.float(1.5, "KC Mult")
kc_upper = basis + ta.atr(length) * kc_mult
kc_lower = basis - ta.atr(length) * kc_mult
in_squeeze = upper < kc_upper and lower > kc_lower

// Plot
plot(bb_width, title="BB Width %", color=in_squeeze ? color.red : color.blue)
bgcolor(squeeze ? color.new(color.red, 85) : na, title="Squeeze Alert")
```

---

## Pine Script: Intraday Execution Helper (5/15-min — breakout day only)

The daily scripts above **find** setups. This one helps you **execute** the
entry cleanly on the breakout day. Run it only on the **5-min or 15-min** chart.
It does not screen — it shows VWAP, intraday EMAs, the opening range, and a
buy-zone band you set from the daily pivot price.

> Do NOT put the daily scripts (1–6) on intraday charts — their lookbacks
> (260 bars = 52 weeks etc.) only make sense on daily bars.

```pine
//@version=5
indicator("KLSE Intraday Execution Helper", overlay=true)

pivotPrice = input.float(0.0, "Daily pivot price (copy from screener; 0 = off)", step=0.001)
buyZonePct = input.float(3.0, "Buy zone % above pivot")
orSession  = input.session("0900-0930", "Opening range session (KLSE morning)")
showOR     = input.bool(true, "Show opening range")

vwapLine = ta.vwap
e9  = ta.ema(close, 9)
e21 = ta.ema(close, 21)
plot(vwapLine, "VWAP", color=color.new(color.orange,0), linewidth=2)
plot(e9,  "EMA 9",  color=color.new(color.aqua,0))
plot(e21, "EMA 21", color=color.new(color.blue,0))

inOR   = not na(time(timeframe.period, orSession))
newDay = ta.change(time("D")) != 0
var float orHigh = na
var float orLow  = na
if newDay
    orHigh := na
    orLow  := na
if inOR
    orHigh := na(orHigh) ? high : math.max(orHigh, high)
    orLow  := na(orLow)  ? low  : math.min(orLow, low)
plot(showOR ? orHigh : na, "OR High", color=color.new(color.purple,0),  linewidth=1, style=plot.style_linebr)
plot(showOR ? orLow  : na, "OR Low",  color=color.new(color.purple,45), linewidth=1, style=plot.style_linebr)

hasPivot = pivotPrice > 0
pv = plot(hasPivot ? pivotPrice : na, "Daily Pivot", color=color.new(color.blue,0), linewidth=2, style=plot.style_linebr)
bz = plot(hasPivot ? pivotPrice*(1+buyZonePct/100) : na, "Buy Zone Top", color=color.new(color.green,30), linewidth=1, style=plot.style_linebr)
fill(pv, bz, color=color.new(color.green,90), title="Buy Zone")

crossedPivot = hasPivot and ta.crossover(close, pivotPrice)
aboveVwap    = close > vwapLine

alertcondition(crossedPivot and aboveVwap, "Intraday Pivot Break",
     "{{ticker}} crossed the daily pivot and is above VWAP — execute within the buy zone")
```

**Use:** when the daily screener flags a stock as BREAKOUT (or COILING about to
break), open its 5-min chart, load this script, and type the daily **pivot
price** into the settings. Execute your buy when price crosses the pivot and is
holding above VWAP — inside the green buy-zone band, never above it.

---

## TradingView Alerts Setup for KLSE

### Setting an Alert on Your Trend Template Indicator

1. Load the Trend Template script on your chart
2. Right-click the indicator → "Add alert on TT Score"
3. Condition: "TT Score crosses above 7"
4. Notifications: Enable email + mobile push
5. Message: `{{ticker}} — Trend Template 7/8+ ✓ at {{close}} on {{time}}`

### Alert Message Template for Breakouts

```
{{ticker}} BREAKOUT
Price: {{close}}
Volume: {{volume}}
Time: {{time}}
Chart: https://www.tradingview.com/chart/?symbol=MYX%3A{{ticker}}
```

---

## TradingView Built-in Screener — KLSE Filter Recipe

The Pine scripts run on a *chart*. TradingView's **Stock Screener**
(tradingview.com/screener) is a separate web filter — use it to narrow the
whole Bursa market down to the ~80–120 names worth charting. It mirrors the
Liquidity + Momentum gates of `klse_screener.py`.

**Setup:** open the Screener → set market to **Malaysia** → add these filters:

| Filter (TradingView field) | Setting | Mirrors screener gate |
|----------------------------|---------|----------------------|
| Exchange | MYX (Bursa Malaysia) | universe |
| Price | ≥ 0.50 MYR | Liquidity: MIN_PRICE |
| Average Volume (10-day) | ≥ 200,000 | Liquidity: MIN_AVG_VOL |
| Market Capitalization | ≥ 100M MYR | Liquidity: MIN_MKT_CAP |
| Simple Moving Average (50) | Price **above** SMA50 | Stage filter (drops WEAK) |
| Simple Moving Average (200) | Price **above** SMA200 | Trend Template C2 |
| Price vs 52-week High | within 25% of high | Trend Template C8 |
| Relative Strength Index (14) | between 40 and 80 | avoids oversold / blow-off |

**Optional quality filters** (when you want fundamentally sound names only):

| Filter | Setting |
|--------|---------|
| Return on Equity % | ≥ 10 |
| Dividend Yield % | ≥ 2 |
| P/E Ratio | 0 – 35 (positive earnings) |

**Workflow:**
1. Run the TradingView screener → save it as a preset named "KLSE Base".
2. Export / eyeball the list — these are your candidate universe.
3. Keep `universe.txt` (for `klse_screener.py`) roughly in sync with this list.
4. The Python screener then does the precise VCP staging; the Pine indicator
   paints it on each chart. Three tools, one consistent logic.

> The TradingView screener cannot detect a VCP coil or a pivot breakout — it
> has no percentile/pivot logic. It is a **coarse pre-filter only**. The COILING
> / BREAKOUT / EXTENDED decision always comes from `klse_screener.py` or the
> `KLSE VCP Stage v2` indicator.

---

## Recommended TradingView Layout for KLSE

**Chart 1 (Main — Daily)**:
- **KLSE VCP Stage v2** (primary — stage background, pivot line, alerts)
- EMA 21, 50, 150, 200
- Volume (coloured)
- RSI 14

**Chart 2 (Weekly — for context)**:
- EMA 10, 40 (weekly = EMA 50, 200 on daily)
- Volume
- 52-week high/low lines

**Chart 3 (60-minute — for entry)**:
- VWAP
- EMA 9, 21
- Volume
- BB Squeeze indicator

**Watchlist columns**:
- Last Price, Change %, Volume, Rel Volume, RSI Daily, EMA50 Distance %
