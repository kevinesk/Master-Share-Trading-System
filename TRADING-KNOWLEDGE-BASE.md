# KLSE Trading Knowledge Base
### Kevin's Professional Trading Framework

This document captures the rules, criteria, and logic behind all trading decisions.
It is the specification that drives the screener, the Pine Scripts, and the AI filters.

---

## LAYER 1 — Macro Environment

### Daily Market Check (before opening bell)
1. Check **yesterday's KLCI performance** — bullish close = higher confidence to trade
2. Check **overnight Dow Jones performance** — sets the global sentiment tone
3. Check **McClellan Oscillator on KLCI 30** — confirms broad market participation
   - Oscillator positive + rising = healthy market, broad buying across stocks → risk-on
   - Oscillator negative or falling = narrowing participation, index held up by few stocks → reduce size or wait

### Risk-On vs Risk-Off
| Condition | Action |
|---|---|
| KLCI up + Dow up + McClellan positive | Full confidence — actively look for entries |
| KLCI flat/mixed + Dow up | Selective — only highest-conviction setups |
| KLCI down + Dow down | Reduce size — bargain hunt blue chips at 52-week lows only |
| Major global risk event (Fed, geopolitical shock) | Ask AI for impact on KLSE sectors before trading |

### Bargain Hunting Rule (bear conditions)
- Only buy **blue chip stocks** (KLCI 30 components or equivalent quality)
- Must be at or near **52-week low**
- Dip must be caused by **market-wide selloff**, not company-specific bad news
- If dip is company-specific (scandal, earnings collapse, debt crisis) → **do not buy**

### Interest Rate Sensitivity (BNM OPR)
- OPR cut → favour **Property and Technology** sectors
- OPR hold/rise → favour **Banking** sector (short-term margin benefit)
- Wire into sector weighting when screener flags opportunities

### News Filter (AI-assisted)
- AI scans daily Bursa announcements, financial news, and global headlines
- Reports to trader: which stocks are **positively impacted** and which are **negatively impacted**
- Trader does not need to read raw news — acts on filtered signal only

---

## LAYER 2 — Industry / Sector Level

### Primary Sectors (highest confidence)
1. **Banking** — understands fundamentals, follows rate cycle
2. **Technology / Semiconductor** — growth focus, follows global tech cycle
3. **Property** — rate-sensitive, watches volume and launch pipelines

### Sector Rotation Method
- Use **Moomoo sector heatmap** daily — look for sectors lighting up green together
- Use **KLScreener.com** for sector-level momentum confirmation
- A sector is "hot" when: multiple stocks in the sector move together (not just one)

### Sector Entry Signal
| Signal | Meaning |
|---|---|
| Whole sector heatmap green | Real rotation — high confidence to buy sector leaders |
| One stock moving, others flat | Stock-specific catalyst only — treat as individual trade |
| Sector reverting from oversold | Potential rotation start — watch for confirmation next 1-2 days |

### Hard Rules
- **No IPO purchases on listing day** — first-day euphoria frequently reverses by close
  - Exception: may revisit after 3–5 trading days once price discovery is complete
- All sectors are tradeable if evidence supports — no permanent sector avoids

---

## LAYER 3 — Company / Stock Selection

### Fundamental Quality Criteria (all must pass)
- [ ] **Consistent earnings growth** — profits rising year-on-year for minimum 2–3 years
- [ ] **Strong and growing revenue** — top-line growth confirms the business is expanding
- [ ] **Strong balance sheet** — low debt-to-equity, healthy cash flow
- [ ] **Good dividend track record** — regular payouts signal management confidence
- [ ] **Future growth visibility** — clear 1–5 year earnings growth story (expansion, new contracts, sector tailwind)

### Dividend Strategy
- Screen for upcoming **ex-dividend dates**
- Buy before ex-date to capture quarterly dividend
- Combine with technical setup — only buy if chart also supports entry
- Do not chase dividend alone if chart is deteriorating

### Results Season Strategy
| Scenario | Action |
|---|---|
| Expecting earnings beat (based on industry checks) | May buy before results announcement |
| Results beat confirmed (positive surprise) | Buy the reaction if chart holds up |
| Results miss | Do not buy — wait for stabilisation |
| Results in line, no surprise | Neutral — rely on technical setup only |

### Company Red Flags (auto-reject even if chart looks good)
- Thinly traded / low liquidity stock
- Promoter-driven or operator-controlled price action
- High debt load relative to earnings
- Recent corporate scandal or regulatory action
- Weak or questionable management track record
- Sudden unexplained volume spike without news (manipulation risk)

---

## LAYER 4 — Entry Rules

### Ideal Entry Setup (all three preferred)
1. **Pullback to EMA / VWAP** — price has retraced to a key dynamic support level
2. **Hammer candlestick** at support — rejection of lower prices, buyers stepping in
3. **VCP (Volatility Contraction Pattern)** — tightening price range showing distribution is done

### Entry Checklist
- [ ] Macro environment is risk-on (Layer 1 passes)
- [ ] Sector is showing strength or rotation (Layer 2 passes)
- [ ] Stock passes all fundamental criteria (Layer 3 passes)
- [ ] Chart shows pullback to EMA/VWAP with hammer or VCP
- [ ] Volume confirms — surge on the entry candle or prior breakout bar
- [ ] Not an IPO listing day

---

## LAYER 5 — Position Sizing

| Confidence Level | Position Size |
|---|---|
| Standard setup | RM 5,000 |
| High conviction (all layers align perfectly) | RM 10,000 |
| Speculative / early-stage idea | Do not trade — wait for confirmation |

- Never exceed RM 10,000 in a single stock entry
- Diversify across sectors — avoid having two positions in the same sector at the same time

---

## LAYER 6 — Stop Loss Rules

### Scenario A — Fundamental / Long-Term Hold
- Stock selected because of **very strong fundamentals** (passes all Layer 3 criteria)
- Hold through normal dips and volatility
- **Hard stop: price closes below EMA 200**
- After EMA 200 breach → exit, wait for recovery
- Re-enter when price reclaims EMA 200 with volume confirmation

### Scenario B — Momentum / Trend Trade
- Stock selected for **short-to-medium term trend play**
- **Hard stop: price closes below EMA 20**
- No exceptions — cut immediately when EMA 20 is breached on close
- Do not average down on momentum trades

---

## LAYER 7 — Profit Taking Rules

### Method: Sell in Tranches + Trailing Stop
- **Do not sell entire position at once** — sell in portions as price rises
- Example structure:
  - Sell 1/3 at first resistance or +15% gain
  - Sell 1/3 at second target or +30% gain
  - Trail remaining 1/3 with a stop below EMA 20 (momentum) or EMA 50 (fundamental)

### Core Principle
> **"Earn less is better than loss money."**
> Protecting capital is the first priority. A smaller gain that is locked in beats a bigger gain that turns into a loss.

### Profit Taking Triggers
- Price hits a known resistance level (PDH, 52-week high, round number)
- Volume starts declining as price rises (momentum fading)
- Sector heatmap turns cold
- Fundamental thesis changes (bad results, management change, sector headwind)

---

## FUTURE EXPANSION — US Market

- To be developed after KLSE system is stable and consistently profitable
- Same framework applies (Macro → Sector → Company → Entry/Exit)
- Key differences to learn: US earnings season timing, Fed sensitivity, sector ETF flows
- AI assistance planned for news filtering and sector rotation signals

---

## System Components

| Component | Tool | Status |
|---|---|---|
| Daily macro check | Manual + McClellan Oscillator | Active |
| Sector rotation | Moomoo heatmap + KLScreener | Active |
| News filtering | AI-assisted (planned automation) | Manual for now |
| Stock fundamentals | Manual research + AI | Manual for now |
| Technical entry timing | TradingView Pine Scripts | Active (V7) |
| Screener automation | Python screener (planned) | Not built yet |
