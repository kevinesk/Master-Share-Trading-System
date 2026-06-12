# Intermarket Analysis — How Asset Classes Signal Each Other

## What is Intermarket Analysis?

Intermarket analysis (pioneered by John Murphy) studies how different asset classes — stocks, bonds, currencies, and commodities — interact and lead each other. Understanding these relationships gives you early warning signals before they show up in KLSE stock prices.

> "No market exists in isolation."

---

## The 4 Asset Classes and Their Relationships

```
BONDS ←→ STOCKS ←→ COMMODITIES ←→ CURRENCIES
         ↑                              ↓
    (inverse mostly)              (US Dollar)
```

### Bond-Stock Relationship (Most Important)
- **Rising bond prices** (falling yields) → Good for stocks (cheaper borrowing, more valuation support)
- **Falling bond prices** (rising yields) → Bad for growth stocks, REITs, high-PE stocks

**For KLSE**:
- US 10Y yield rising → Pressure on KLSE REITs and high-PE tech stocks
- MGS (Malaysian Government Securities) yield rising → BNM may be hiking OPR → banks benefit, property suffers

**TradingView**: Monitor `TVC:US10Y` (US 10-year yield)

---

## Currency Relationships Critical for KLSE

### USD/MYR (The Master Variable)

Everything in KLSE ultimately traces back to USD/MYR:

```
US Fed Rate ↑ → DXY ↑ → USD/MYR ↑ (MYR weakens)
                → Foreign capital leaves EM → KLCI falls
                → KLSE exporters benefit (USD revenues in MYR terms rise)

US Fed Rate ↓ → DXY ↓ → USD/MYR ↓ (MYR strengthens)
                → Foreign capital returns to EM → KLCI rises
                → KLSE importers benefit (cheaper USD costs)
```

### MYR vs Other ASEAN Currencies

| Currency Pair | KLSE Signal |
|--------------|------------|
| MYR/SGD rising (MYR strengthening vs SGD) | Foreign inflows; KLCI bullish |
| MYR/CNY | China demand for Malaysian exports (CPO, electronics) |
| MYR/JPY | Carry trade flows — yen carry unwind = ASEAN selloff |
| MYR/IDR | When IDR collapses, often MYR weakens too (EM contagion) |

**The Yen Carry Trade Warning**: When Japanese Yen strengthens rapidly (USD/JPY falling), it signals unwinding of carry trades — investors borrowed cheap yen, bought high-yield EM assets. When yen strengthens, they sell EM assets to repay yen loans. This can cause sudden KLSE selloffs even with no Malaysian-specific news. (This happened in August 2024.)

---

## Commodity-Currency Relationships for Malaysia

### CPO → MYR (Direct)

Malaysia is the world's second-largest palm oil exporter. CPO export revenues directly impact the MYR.

```
CPO price rises → Malaysia export earnings rise → MYR strengthens (demand for MYR to pay exporters)
                → Plantation stocks rally
                → Some of this flows into KLCI (positive wealth effect)
```

**Monitor**: `BURSA:FCPO1!` (CPO front month futures on Bursa)

### Oil → Malaysia (Complex Relationship)

Malaysia is a net oil exporter (Petronas). Higher oil = more government revenue.

| Oil Price Direction | Malaysia Impact |
|--------------------|----------------|
| Oil rising | Government revenue up; PETRONAS pays higher dividends → KLSE blue chips benefit |
| | DIALOG, MISC, YINSON benefit directly |
| | BUT airlines (AIRASIA, MAB) suffer (fuel costs) |
| Oil falling | Government budget pressure; KLSE may face fiscal headwinds |
| | Airlines benefit |

**Monitor**: `NYMEX:CL1!` (WTI Crude) or `ICEEUR:B!` (Brent Crude)

---

## Gold as a Global Signal

Gold is not a KLSE sector, but it signals global risk appetite.

| Gold Price | Interpretation | KLSE Impact |
|-----------|---------------|------------|
| Gold rising sharply | Risk-off globally; investors fleeing to safety | KLSE likely under pressure |
| Gold falling | Risk-on; investors buying equities and EM | KLSE likely rising |
| Gold stable or rising slowly | Normal; consistent with mild uncertainty | Neutral for KLSE |

**Exception**: Gold mines and gold-linked stocks (if any) benefit directly from gold price rises.

**TradingView**: `COMEX:GC1!`

---

## The Bond Market as a Leading Indicator

**Bonds are called "smart money"** — institutional fixed income investors are often more sophisticated than equity investors.

### Yield Curve for KLSE Traders

The US yield curve (10Y minus 2Y spread) is the best single recession predictor:

```
Normal: 10Y > 2Y (positive spread) → Economy healthy
Flat: 10Y ≈ 2Y → Warning; economic slowdown approaching
Inverted: 10Y < 2Y → Recession likely in 12–18 months
```

**TradingView**: `FRED:T10Y2Y` — When this crosses below 0 → start reducing equity exposure.

### MGS (Malaysian Government Securities) Yield

For KLSE specifically:
- Rising MGS yields → BNM tightening or MYR weakening → pressure on KLSE
- Falling MGS yields → BNM easing or MYR strengthening → KLSE supportive

**KLSE sectors most sensitive to MGS yields**:
| Sector | High MGS Yield | Low MGS Yield |
|--------|---------------|--------------|
| REITs | Underperform (bonds compete for yield-seekers) | Outperform |
| Banking | Outperform (NIM expands) | Underperform |
| Property | Underperform (mortgage rates high) | Outperform |
| Utilities | Underperform (bond proxy; yield rises) | Outperform |

---

## Global Equity Intermarket Signals

### US Market Leads KLSE (With Lag)

```
US S&P 500 closes -2% → KLSE opens next morning -0.5 to -1.0%
US S&P 500 in 3-month downtrend → KLSE follows within 4–8 weeks
US S&P 500 makes new ATH → KLSE may follow in 2–4 weeks (not always)
```

**The lag occurs because**:
- US market closes; KLSE opens 15 hours later (next morning)
- Foreign funds watching US before allocating to KLSE
- US earnings season data flows into KLSE sector stocks (semi, tech)

### SOX Index → KLSE Semiconductor (Critical Relationship)

**Philadelphia Semiconductor Index (SOX)** leads KLSE semiconductor stocks by 1–4 weeks.

```
SOX rallies 10% → 2–4 weeks later → VITROX, INARI, FRONTKN rally
SOX sells off 15% → 1–2 weeks later → KLSE semi stocks fall
```

**TradingView**: `NASDAQ:SOX`

**How to use**: When SOX breaks out to new highs, prepare VCP/Cup setups on VITROX, INARI, FRONTKN. The KLSE move comes after.

### FTSE Bursa Malaysia KLCI vs STI (Singapore), IHSG (Indonesia)

Regional equity market correlation:

| Market | Correlation with KLCI | Lead/Lag |
|--------|---------------------|---------|
| Singapore STI | 0.65 | Simultaneous |
| Indonesia IHSG | 0.60 | Simultaneous (but often more volatile) |
| Thailand SET | 0.55 | Simultaneous |
| Hong Kong HSI | 0.55 | HSI may lead slightly (China proxy) |
| US S&P 500 | 0.50 | US leads by 1 day |

**ASEAN risk-off signal**: When Singapore STI AND Indonesia IHSG fall on the same day → almost certain KLCI falls same day or next. This represents coordinated regional outflow.

---

## The Intermarket Dashboard (Weekly Review — 15 Minutes)

Check every Sunday night before KLSE opens Monday:

| Asset | Level | 4-Week Trend | Signal for KLSE |
|-------|-------|-------------|----------------|
| S&P 500 | | | |
| NASDAQ | | | |
| SOX (semiconductors) | | | |
| US 10Y yield | | | |
| DXY (US Dollar) | | | |
| USD/MYR | | | |
| Brent crude | | | |
| CPO (FCPO1!) | | | |
| Gold | | | |
| VIX | | | |
| Singapore STI | | | |

**Count bullish vs bearish signals**:
- 8+ bullish → Full deployment; buy setups aggressively
- 5–7 bullish → Normal trading; standard risk
- 3–4 bullish → Selective only; reduce new positions
- <3 bullish → Defensive; raise cash

---

## Practical Intermarket Trading Rules for KLSE

### Rule 1: Never fight the DXY trend
- If DXY has been rising for 3+ months, KLSE will face headwinds regardless of domestic fundamentals
- Reduce exposure, not increase, when DXY is in a strong uptrend

### Rule 2: Follow the SOX for semiconductor stocks
- Before buying VITROX, INARI, or any semi stock, check if SOX is above EMA50 and trending up
- If SOX is below EMA50 → avoid Malaysian semi stocks even if chart looks good locally

### Rule 3: CPO confirms or denies plantation trades
- Never buy a plantation stock breakout if CPO is in a downtrend
- CPO above EMA50 and trending up = tailwind for planters; buy breakouts confidently

### Rule 4: Use gold as a risk filter
- Gold rallying strongly (+5% in 2 weeks) = risk-off environment globally
- Avoid buying new positions when gold is rallying strongly

### Rule 5: Monitor the yen for surprise crashes
- USD/JPY below 140 or falling rapidly = unwinding of yen carry trade
- This can cause sudden KLSE selloff (no Malaysian news required)
- When USD/JPY falls fast → tighten all stops immediately
