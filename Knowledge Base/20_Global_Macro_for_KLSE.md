# Global Macro for KLSE — How the World Moves Bursa

## The Hierarchy of Global Forces

KLSE is a small, open, export-dependent market. Global forces dominate local forces. Know the global picture first, then look at Malaysia.

```
Level 1 (Strongest): US Federal Reserve → Interest rates worldwide
Level 2: US Economy / Dollar strength → Capital flows to emerging markets
Level 3: China economy → Commodity demand, regional trade
Level 4: Commodity prices (Oil, Palm Oil, LNG) → Malaysia's export earnings
Level 5: ASEAN regional trends → Investor regional allocation
Level 6: Malaysia-specific (BNM, Budget, Elections)
```

---

## Force 1: US Federal Reserve (The Most Powerful Global Driver)

**The Fed controls global liquidity.** When the Fed raises rates, money flows OUT of emerging markets (including KLSE) into US bonds. When the Fed cuts rates, money flows INTO emerging markets.

### Fed Rate Cycle Impact on KLSE

| Fed Policy | USD | EM Capital Flows | KLCI | Best KLSE Sectors |
|-----------|-----|-----------------|------|------------------|
| Hiking rates | Strengthens | Outflows from EM | Falls | Defensive (telcos, utilities) |
| Holding at high | Strong | Cautious flows | Sideways | Quality dividend stocks |
| Cutting rates | Weakens | Inflows to EM | Rallies | ALL sectors; banks, property, tech |
| Near-zero rates | Weak | Heavy EM inflows | Strong bull | Growth stocks, property |

**Key monitoring**:
- Fed Funds Rate: Current level and direction
- FOMC meetings: 8 per year (Jan, Mar, May, Jun, Jul, Sep, Nov, Dec)
- Fed Chair press conference: Every FOMC — watch for "pivot" signals
- US 10-year Treasury yield: Rising = USD strengthens = KLCI pressure

**TradingView references**:
- `TVC:US10Y` — US 10-year Treasury yield
- `FRED:FEDFUNDS` — Fed Funds Rate history
- `TVC:DXY` — US Dollar Index (DXY rising = bad for KLSE)

---

## Force 2: US Dollar Index (DXY)

**DXY rising = bad for KLSE (generally). DXY falling = good for KLSE.**

Why:
1. Malaysia's commodities (CPO, LNG) priced in USD — weaker USD hurts export earnings in USD terms but MYR-priced profits may vary
2. Capital flows: Strong USD attracts capital back to US → away from emerging markets
3. Foreign debt: Companies with USD debt suffer when MYR weakens

**Watch**: `TVC:DXY` on TradingView. Level above 105 = caution for KLSE. Level below 100 = bullish for KLSE.

### DXY vs USD/MYR Relationship
```
DXY rises → USD/MYR rises (MYR weakens) → Foreign outflow from KLSE → KLCI falls
DXY falls → USD/MYR falls (MYR strengthens) → Foreign inflow to KLSE → KLCI rises
```

---

## Force 3: China Economy

Malaysia's largest trading partner. China's economic health directly impacts KLSE.

### How China Moves KLSE

| China Indicator | Impact on KLSE |
|----------------|---------------|
| China GDP growth >5% | CPO demand strong (China imports ≈20% of world's palm oil) |
| China PMI (Caixin) >50 | Manufacturing recovery → Electronics demand → INARI, VITROX |
| China stimulus packages | Construction boom → Steel, cement demand → commodity stocks |
| China property sector crisis | Reduces commodity demand; weakens MYR as trade partner |
| China-US trade tensions | Redirect orders to Malaysia manufacturers (opportunity for INARI, UNISEM) |

**Where to watch**: 
- Caixin Manufacturing PMI (published 1st of each month)
- China retail sales, industrial production (published ~15th each month)
- NBS PMI (official Chinese government PMI)
- TradingView: `ECONOMICS:CNPMI`

**Trading rule**: When China's PMI crosses above 50 and is rising → Commodities and electronics stocks on KLSE outperform. Buy planters and semi stocks.

---

## Force 4: Commodity Super-Cycles

Malaysia's economy is deeply tied to commodities. Understanding commodity super-cycles is essential.

### Commodity Impact Matrix

| Commodity | KLSE Impact | Key Stocks | Where to Watch |
|-----------|------------|-----------|---------------|
| **Crude Palm Oil (CPO)** | Direct — plantation earnings | KLK, GENP, SOP, SDGUTHRIE | `BURSA:FCPO1!` |
| **Crude Oil (Brent)** | Positive for MISC, DIALOG; negative for airlines | DIALOG, MISC, YINSON | `NYMEX:CL1!` |
| **LNG prices** | Direct → PETRONAS revenue → KLSE dividend | KLSE blue chips broadly | JKM LNG spot price |
| **Copper** | Leading indicator of global industrial demand | Construction, utilities | `COMEX:HG1!` |
| **Gold** | Safe haven — when gold rallies, KLSE usually under pressure | — | `COMEX:GC1!` |
| **Steel/Iron Ore** | Construction cost → contractor margins | MCEMENT (inverse), IJM, GAMUDA | `SGX:FEF1!` |
| **Semiconductor spot prices** | NAND/DRAM pricing → OSAT demand | INARI, UNISEM, MPI | WSTS data |

### The CPO-Soybean Spread (Crucial for Planters)

```
When CPO is cheap relative to Soybean Oil → Buyers substitute CPO → CPO demand rises → CPO price rises
When CPO is expensive relative to Soybean Oil → Buyers switch away → CPO demand falls
```

Monitor: CPO/Soybean oil price ratio (both on TradingView). When ratio is near the bottom of its historical range → CPO is cheap → planters are near a bottom → potential buy.

---

## Force 5: US Stock Market (S&P 500 / Dow / NASDAQ)

KLSE correlates with US markets, but with a lag and lower magnitude.

**Correlation rules**:
- US market down >1% overnight → KLSE opens down 0.3–0.7%
- US market down >2% (selloff) → KLSE could fall 0.5–1.5%
- US market up strongly for weeks → KLSE eventually follows
- US market selloff >10% → Almost certain KLSE bear market follows

**But KLSE is less volatile**: It falls less but also rallies less than US markets in most cycles.

**TradingView**: Monitor `SP:SPX`, `DJ:DJI`, `NASDAQ:NDX`

**The VIX rule (Fear Index)**:
- VIX < 15: Low fear; stocks safe to buy
- VIX 15–25: Moderate concern; be selective
- VIX 25–35: High fear; reduce exposure
- VIX > 35: Panic; potential buying opportunity with confirmation
- TradingView: `CBOE:VIX`

---

## Force 6: ASEAN Regional Flows

Foreign funds allocate to "ASEAN" as a block. When funds rotate INTO ASEAN, Malaysia gets capital inflows even if Malaysia's own fundamentals haven't changed.

**Monitor**:
- FTSE ASEAN index performance
- Indonesia (IHSG), Thailand (SET), Philippines (PSEi) — if all rising, KLSE will follow
- iShares MSCI Malaysia ETF (`EWM` on NYSE) — US-listed; tracks foreign fund interest in Malaysia

**KLSE vs regional peers**:
| Country | Index | 2024 Performance | KLSE comparison |
|---------|-------|-----------------|-----------------|
| Malaysia | FBMKLCI | ~+9% | Moderate |
| Indonesia | IHSG | −2% | Better than Indonesia |
| Thailand | SET | −10% | Much better |
| Philippines | PSEi | +2% | Similar |
| Singapore | STI | +15% | Underperformed SGX |

**Trading implication**: KLSE tends to attract rotation when Indonesia or Thailand underperforms — funds need to be in ASEAN but move to the best-performing market.

---

## Force 7: Geopolitical Risk

| Event | KLSE Impact |
|-------|------------|
| US-China trade war escalation | Short-term negative; but long-term Malaysia benefits from supply chain diversion |
| Middle East conflict | Oil price rises → MISC, DIALOG benefit; airlines hurt |
| South China Sea tensions | Shipping cost spike → MISC benefits; general uncertainty hurts |
| Russia-Ukraine conflict | LNG prices rise → PETRONAS benefits → KLSE broadly positive |
| Global pandemic signal | Healthcare (IHH, KOSSAN) outperform; cyclicals fall |

**Rule**: Geopolitical events are noise unless they affect Malaysia's top 4 exports (electronics, palm oil, petroleum, rubber). Focus there.

---

## Global Macro Monitoring Checklist (Weekly, Every Sunday)

| Indicator | Current Level | Direction | KLSE Signal |
|-----------|--------------|-----------|------------|
| S&P 500 (vs EMA50) | | | |
| DXY (US Dollar Index) | | | |
| VIX (Fear Index) | | | |
| US 10Y Treasury Yield | | | |
| Brent Crude Oil | | | |
| CPO (FCPO front month) | | | |
| China Caixin PMI (latest) | | | |
| USD/MYR | | | |
| KLCI (vs EMA50) | | | |
| Foreign net flow (last 5 days) | | | |

**Scoring**:
- 7–10 green → Full deployment; buy setups aggressively
- 5–6 green → Selective; only highest-conviction setups
- <5 green → Reduce exposure; raise cash; protect capital

---

## The Global Macro Trading Clock for KLSE

```
US Fed CUTS → DXY weakens → MYR strengthens → Foreign inflows to KLSE
→ Banking (NIM falls but foreign buying) and Property lead
→ Then Technology and Consumer discretionary
→ Then Industrials
→ Finally: Commodity stocks as inflation picks up again

US Fed HIKES → DXY strengthens → MYR weakens → Foreign outflows
→ Defensives (utilities, telcos, REITs) first
→ Then avoid all growth stocks
→ Only plantation (if CPO strong) and exporters
```
