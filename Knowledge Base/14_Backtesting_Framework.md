# Backtesting Framework for KLSE

## Why Backtest?

Backtesting tells you whether your strategy has a statistical edge before you risk real money. Without it, you're trading on hope.

**Backtesting answers**:
- Does this system make money over many trades?
- What is the worst drawdown I'd have to survive?
- What is my realistic win rate and R:R ratio?
- Does the system work in different market conditions?

**The #1 rule**: A good backtest doesn't guarantee future profits. A bad backtest guarantees you understand nothing.

---

## Types of Backtesting

| Type | Method | Pros | Cons |
|------|--------|------|------|
| **Manual backtesting** | Scroll through charts, record each trade by hand | Deep learning; catches nuances | Slow; subject to hindsight bias |
| **Automated (Pine Script)** | Code the strategy; TradingView runs it | Fast; objective; reproducible | Misses execution reality; curve-fitting risk |
| **Paper trading** | Trade in real-time with virtual money | Forward-tests in real conditions | Takes months to get meaningful data |

**Best approach for KLSE**: Manual backtest first (to understand the strategy), then Pine Script to test on more data.

---

## The 5 Core Backtest Metrics

### 1. Win Rate
```
Win Rate = Winning Trades / Total Trades × 100
```
- Target: 40–60% for momentum strategies
- A 40% win rate CAN be very profitable if the average win is 2× the average loss

### 2. Average Win vs Average Loss (R:R Ratio)
```
Avg Win / Avg Loss = R:R Ratio
```
- If win rate = 40% and R:R = 2.5 → system is profitable
- Expected Value = (40% × 2.5) − (60% × 1) = 1.0 − 0.6 = **+0.4R per trade**

### 3. Profit Factor
```
Profit Factor = Gross Profit / Gross Loss
```
- <1.0: Losing system
- 1.0–1.5: Marginal
- 1.5–2.0: Good
- >2.0: Excellent

### 4. Maximum Drawdown
```
Max Drawdown = (Peak Portfolio Value − Trough) / Peak × 100
```
- This is the most important risk metric
- Ask yourself: "Can I live through this drawdown without quitting?"
- If max drawdown exceeds 20% → system is too risky or you need smaller position sizes

### 5. Sharpe Ratio
```
Sharpe Ratio = (Strategy Return − Risk-Free Rate) / Std Dev of Returns
```
- >1.0: Acceptable
- >2.0: Good
- >3.0: Excellent
- Risk-free rate for KLSE: use 3-month MGS rate (≈3.5%)

---

## Manual Backtesting: Step-by-Step

### Step 1: Define Your Rules Precisely

Before testing, write down EXACT rules. Vague rules = useless backtest.

**Example (VCP Breakout System)**:
```
ENTRY RULES:
- Stock must have EMA50 > EMA150 > EMA200 (Stage 2)
- EMA200 must be trending up (higher than 20 days ago)
- Stock must have formed a VCP pattern (2–4 contractions)
- Each contraction: depth < prior contraction, duration < prior
- Entry: Day price closes above pivot (VCP handle high) on volume ≥1.5× 20-day avg
- Entry price: Closing price of breakout day (market order next morning is also acceptable)
- Maximum entry: No more than 3% above pivot

STOP LOSS RULES:
- Initial stop: Below VCP base low
- Maximum stop: 8% from entry

EXIT RULES:
- Stop hit → exit immediately at market
- Gain ≥ +20% → exit 1/3 of position
- Gain ≥ +35% → exit another 1/3
- Daily close below EMA21 on above-average volume → exit final 1/3
```

### Step 2: Build a Universe

Use your existing `universe.txt` (100 KLSE stocks). Test on this universe.

### Step 3: Scroll Through 2–3 Years of Charts

On TradingView, for each stock in the universe:
1. Go to daily chart
2. Enable EMA 50, 150, 200
3. Scroll back to January 2022
4. Slowly scroll forward bar by bar (bar replay mode or manually)
5. When your entry criteria are met → record the trade

### Step 4: Record Every Trade in a Spreadsheet

| # | Date | Stock | Entry | Stop | Target | Exit Date | Exit Price | P&L % | Outcome |
|---|------|-------|-------|------|--------|-----------|-----------|-------|---------|
| 1 | 2022-03-15 | CIMB | 5.80 | 5.40 | 6.96 | 2022-04-10 | 6.85 | +18.1% | Win |
| 2 | 2022-03-22 | MAXIS | 3.90 | 3.62 | 4.68 | 2022-04-05 | 3.61 | -7.4% | Loss |

### Step 5: Calculate Your Metrics

After ≥30 trades (≥50 is better):
- Count wins vs losses → win rate
- Average all winning P&L → average win
- Average all losing P&L → average loss
- Calculate profit factor, expected value

### Step 6: Segment by Market Conditions

Run the numbers separately for:
- Trades when KLCI was above EMA50
- Trades when KLCI was below EMA50

You'll find: **almost all the profits come from trades taken when KLCI is above EMA50.**

---

## Automated Backtesting with TradingView Pine Script

### Full VCP Breakout Strategy (Simplified)

```pine
//@version=5
strategy("KLSE VCP Backtest",
         overlay=true,
         initial_capital=100000,
         default_qty_type=strategy.fixed,
         default_qty_value=10000,          // RM10k per trade (10% of capital)
         commission_type=strategy.commission.percent,
         commission_value=0.3,             // 0.3% round-trip fees
         slippage=2)                       // 2 ticks slippage estimate

// ── Settings ──────────────────────────────────────────────────
date_start = input.time(timestamp("2022-01-01"), "Backtest Start")
date_end   = input.time(timestamp("2025-12-31"), "Backtest End")
in_range   = time >= date_start and time <= date_end

// ── Indicators ────────────────────────────────────────────────
e21  = ta.ema(close, 21)
e50  = ta.ema(close, 50)
e150 = ta.ema(close, 150)
e200 = ta.ema(close, 200)
vol_avg = ta.sma(volume, 20)

// ── Stage 2 Filter ─────────────────────────────────────────────
stage2 = close > e50 and e50 > e150 and e150 > e200 and e200 > e200[20]

// ── Breakout Signal ────────────────────────────────────────────
new_20d_high = high == ta.highest(high, 20)
vol_confirm  = volume >= vol_avg * 1.5

long_signal  = stage2 and new_20d_high and vol_confirm and in_range

// ── Entry ──────────────────────────────────────────────────────
if long_signal and strategy.position_size == 0
    strategy.entry("Long", strategy.long)

// ── Exits ──────────────────────────────────────────────────────
stop_loss = strategy.position_avg_price * 0.93   // 7% stop
tp1       = strategy.position_avg_price * 1.20   // 20% target
ema_break = close < e21 and volume > vol_avg

if strategy.position_size > 0
    strategy.exit("SL", "Long", stop=stop_loss)
    if close >= tp1
        strategy.close("Long", qty_percent=33, comment="+20% partial")
    if ema_break
        strategy.close("Long", comment="EMA21 break")

// ── Visuals ────────────────────────────────────────────────────
bgcolor(stage2 ? color.new(color.green, 95) : na)
plotshape(long_signal, style=shape.triangleup, location=location.belowbar,
          color=color.green, size=size.small, title="Entry")
```

**How to run**:
1. Open any KLSE stock on TradingView (daily chart)
2. Open Pine Script Editor → paste code → Add to chart
3. Click "Strategy Tester" tab at bottom
4. View: Net Profit, Max Drawdown, Win Rate, Profit Factor, Sharpe Ratio

---

## Walk-Forward Testing (Preventing Overfitting)

**Overfitting**: Your strategy is tuned to past data and won't work in the future.

**Walk-forward method**:
1. Divide your data into 3 periods (e.g., 2019–2021, 2022–2023, 2024)
2. Optimise strategy parameters on Period 1 (in-sample)
3. Test on Period 2 WITHOUT changing parameters (out-of-sample)
4. Test on Period 3 (final validation)

If the strategy works in all 3 periods → it's likely robust.
If it only works in Period 1 → it's curve-fitted, don't trade it.

---

## Common Backtesting Mistakes

| Mistake | How It Distorts Results |
|---------|------------------------|
| **Look-ahead bias** | Using future data to make decisions (e.g., knowing next day's volume) |
| **Survivorship bias** | Only testing stocks that survived — ignoring ones that went bankrupt |
| **Ignoring commissions** | KLSE fees are 0.3–0.5% round-trip — significant impact on high-frequency systems |
| **Ignoring slippage** | Market orders on KLSE can slip 0.5–1% on smaller stocks |
| **Overfitting** | Too many rules = strategy works on history only |
| **Not testing enough trades** | <30 trades gives no statistical significance |

---

## KLSE Backtest Reality Check

**Practical adjustments for KLSE**:
- Apply a 0.3% commission per trade (buy + sell)
- Apply 0.5% slippage on stocks with daily turnover < RM2M
- Use starting capital of RM50,000–RM100,000 (realistic for retail)
- Test across 2019–2025 (includes COVID crash, recovery, rate cycle)

**Key market regimes in KLSE backtest period**:
| Period | Market Regime | Expected Strategy Performance |
|--------|--------------|------------------------------|
| Jan 2019 – Dec 2019 | Sideways/mild uptrend | Moderate |
| Jan 2020 – Mar 2020 | Crash (COVID) | Poor (stop losses triggering) |
| Apr 2020 – Dec 2021 | Strong rally | Excellent |
| Jan 2022 – Dec 2022 | Mixed/bearish | Poor |
| Jan 2023 – Dec 2024 | Recovery/uptrend | Good |

**A good system**: Works in 2019, 2021, 2023–2024. Loses minimally in 2020, 2022.

---

## Building Your Personal Performance Database

Track these statistics quarterly:

```
Period: Q1 2026
Total trades  : 8
Winners       : 4 (50%)
Losers        : 4 (50%)
Avg win       : +15.2%
Avg loss      : -6.8%
Profit factor : 2.24
Expected value: +0.60R per trade
Max drawdown  : -8.3%
Portfolio gain: +6.1%
KLCI return   : +2.8%
Alpha generated: +3.3%

Best trade: CIMB +22.5%
Worst trade: TENAGA -7.1%
Rule violations: 1 (averaged down on AXIATA — lesson: never again)
```

Maintain this quarterly. Over 1–2 years, you will have a precise picture of your edge.
