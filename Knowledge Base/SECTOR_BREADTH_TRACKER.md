# Sector Breadth Tracker — Cane + Morris Weekly Fill-In
**When**: Refresh every Sunday during `WEEKLY_ROUTINE.md`
**Purpose**: Quantify which Bursa sectors are leading, lagging, or rotating — informs watchlist construction.

> **Rule**: Only buy from sectors with **breadth ≥ 60% above MA50 AND positive Cane indicators**. Don't fight sector breakdown.

---

## 📊 The 12 Bursa Sectors — Weekly Fill

### Week of: __________

| Sector | Index | Stage (1-4) | % above MA50 | Cane Leading Indicator | Morris Verdict | Action |
|---|---|---|---|---|---|---|
| Financial | KLFIN | __ | __% | OPR direction, loan growth | __ | __ |
| Construction | KLCON | __ | __% | Infra awards (MRT3, LRT) | __ | __ |
| Property | KLPRP | __ | __% | Launches, unbilled sales | __ | __ |
| Tech | KLTEC | __ | __% | Semicon book-bill, AI capex | __ | __ |
| Healthcare | KLHC | __ | __% | Bed occupancy, glove ASP | __ | __ |
| Plantation | KLPLT | __ | __% | CPO price, stockpiles | __ | __ |
| Consumer | KLCG | __ | __% | Retail sales, F&B SSSG | __ | __ |
| Energy | KLEW | __ | __% | Brent crude, rig count | __ | __ |
| Industrial | KLIN | __ | __% | PMI, capex orders | __ | __ |
| Utilities | KLUT | __ | __% | Electricity demand, rates | __ | __ |
| Telco | KLTPS | __ | __% | ARPU trend, 5G capex | __ | __ |
| REIT | KLREIT | __ | __% | Occupancy, rental reversion | __ | __ |

### Morris Verdict Codes
- 🟢 **STRONG** — Breadth ≥ 60% + A-D rising + new highs
- 🟡 **NEUTRAL** — Breadth 40-60% OR mixed signals
- 🔴 **WEAK** — Breadth < 40% OR A-D falling OR new lows

### Action Codes
- **BUY** — Add leaders from this sector to watchlist
- **HOLD** — Existing positions OK, no new entries
- **TRIM** — Reduce sector exposure
- **AVOID** — No new entries, exit existing on rallies

---

## 🎯 Cane Leading Indicators by Sector (file 49)

Refresh each Sunday. Mark ✅ green / ⚠️ mixed / ❌ red.

### Banking (KLFIN)
- [ ] System loan growth ≥ 5% y/y (BNM monthly stats)
- [ ] NPL ratio trend (falling = ✅)
- [ ] CASA ratio expansion
- [ ] 10Y MGS yield curve steepening
- [ ] Credit card receivables growth
- **Score**: ___ / 5 → ___

### Construction (KLCON)
- [ ] Government infra contract awards (RM bn last 90 days)
- [ ] Cement volume y/y
- [ ] Steel demand
- [ ] Tendered project values (Bursa announcements)
- [ ] Order book / replenishment ratio
- **Score**: ___ / 5 → ___

### Property (KLPRP)
- [ ] Property launches count y/y
- [ ] Unbilled sales backlog (top 5 developers)
- [ ] Mortgage approval rates
- [ ] Inventory months (NAPIC)
- [ ] Buy-to-let yield vs OPR
- **Score**: ___ / 5 → ___

### Tech (KLTEC)
- [ ] WSTS semicon book-to-bill ratio
- [ ] SOX index trend
- [ ] Major fab capex announcements (TSMC, Intel)
- [ ] PHLX Semi outperforming SPX
- [ ] AI / data centre orders
- **Score**: ___ / 5 → ___

### Healthcare (KLHC)
- [ ] Sunway/IHH bed occupancy %
- [ ] Glove ASP (Top Glove, Hartalega QR)
- [ ] Medical tourism arrivals
- [ ] Pharma inventory turnover
- [ ] R&D / capex announcements
- **Score**: ___ / 5 → ___

### Plantation (KLPLT)
- [ ] CPO price MYR/tonne (target ≥ 4000)
- [ ] Palm stockpile (MPOB monthly)
- [ ] Soybean oil spread
- [ ] Indo export policy
- [ ] India/China import volumes
- **Score**: ___ / 5 → ___

### Consumer (KLCG)
- [ ] Retail sales y/y (DOSM)
- [ ] F&B same-store sales growth
- [ ] Consumer confidence index
- [ ] Auto TIV (vehicle sales)
- [ ] Tourism arrivals
- **Score**: ___ / 5 → ___

### Energy (KLEW)
- [ ] Brent crude (target ≥ $75)
- [ ] Rig count (Baker Hughes)
- [ ] Petronas capex guidance
- [ ] Refining margins
- [ ] LNG spot prices
- **Score**: ___ / 5 → ___

### Industrial (KLIN)
- [ ] PMI ≥ 50 (S&P / Markit)
- [ ] Capex orders backlog
- [ ] Export figures
- [ ] Container traffic
- [ ] Industrial production y/y
- **Score**: ___ / 5 → ___

### Utilities (KLUT)
- [ ] Electricity demand y/y (TNB)
- [ ] Gas tariff stability
- [ ] Solar / RE capacity additions
- [ ] FX impact on USD-denominated debt
- [ ] Capex outlook
- **Score**: ___ / 5 → ___

### Telco (KLTPS)
- [ ] ARPU trend
- [ ] 5G subscriber additions
- [ ] Capex / opex ratio
- [ ] Net adds vs churn
- [ ] Spectrum auction outcomes
- **Score**: ___ / 5 → ___

### REIT (KLREIT)
- [ ] Office / retail occupancy rates
- [ ] Rental reversion direction
- [ ] OPR vs distribution yield spread
- [ ] New asset injections
- [ ] Refinancing rates
- **Score**: ___ / 5 → ___

---

## 📈 Morris Breadth Components (file 50)

For each sector, calculate weekly:

### 1. % Stocks Above 50-Day MA
- **Source**: Manual count from sector index components OR i3investor heat map
- **Threshold**: ≥60% = healthy / 40-60% = neutral / <40% = weakening

### 2. Sector A-D Line (Advance-Decline)
- **Calc**: Count stocks UP minus DOWN over past 5 days
- **Trend**: Make-new-highs = ✅ / make-new-lows = ❌

### 3. Sector New 52-Week Highs
- **Threshold**: ≥ 3 names = strong / 0-2 = weak

### 4. Sector RS Line vs KLCI
- **Calc**: Sector index / KLCI, watch for new high or new low
- **Bullish**: RS line at new high = leadership

---

## 🚦 Top 3 Sectors of the Week

After filling all 12, identify the **top 3 sectors** where BOTH conditions hold:
1. Morris Verdict = 🟢 STRONG
2. Cane Leading Indicators ≥ 3 / 5

### This week's Top 3:
1. _____________ — leader stocks to watch: ____________________
2. _____________ — leader stocks to watch: ____________________
3. _____________ — leader stocks to watch: ____________________

---

## ⛔ Bottom 3 Sectors of the Week (Avoid These)

| Rank | Sector | Why | Existing positions action |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## 📅 4-Week Sector Trend Tracker

| Sector | Wk-3 | Wk-2 | Wk-1 | **This Wk** | Direction |
|---|---|---|---|---|---|
| KLFIN | __ | __ | __ | __ | __ |
| KLCON | __ | __ | __ | __ | __ |
| KLPRP | __ | __ | __ | __ | __ |
| KLTEC | __ | __ | __ | __ | __ |
| KLHC | __ | __ | __ | __ | __ |
| KLPLT | __ | __ | __ | __ | __ |
| KLCG | __ | __ | __ | __ | __ |
| KLEW | __ | __ | __ | __ | __ |
| KLIN | __ | __ | __ | __ | __ |
| KLUT | __ | __ | __ | __ | __ |
| KLTPS | __ | __ | __ | __ | __ |
| KLREIT | __ | __ | __ | __ | __ |

Use scores (e.g. 3 ✅ + 2 ❌ = "3-2"). Look for sectors **improving across 3+ weeks** = early-stage rotation winner.

---

## 🧠 The Big Pattern Recognition

After 8+ weeks of tracking, you'll start to see:

1. **Lead-Lag pairs** — e.g. KLCON leading KLPRP by 4-6 weeks
2. **Macro driver reactivity** — KLFIN lags OPR cuts by 2-3 weeks; KLTEC tracks SOX same week
3. **Mean-reversion zones** — sectors at <30% breadth for 6+ weeks often bounce
4. **Persistence patterns** — sectors with 4+ weeks of strong breadth tend to extend another 4-8

This is your edge over 90% of retail traders who just watch KLCI.

---

## 🎯 Integration with the System

- **Use top 3 sectors** to filter `klse_screener_v3_quality_overlay.py` output
- **Add to `WEEKLY_ROUTINE.md`** Phase 2 (Sector Rotation Review)
- **Cross-check** with V9 Pro Quant Desk's Stovall Phase input
- **Avoid stocks** in bottom 3 sectors regardless of how good their TT score looks

---

## 📝 This Week's Final Verdict

```
WEEK OF: __________

TOP 3 SECTORS:        BUY FROM
1. _______________    Watchlist: _____________
2. _______________    Watchlist: _____________
3. _______________    Watchlist: _____________

BOTTOM 3:             AVOID
1. _______________    Action: _____________
2. _______________    Action: _____________
3. _______________    Action: _____________

ROTATION SIGNAL:      [no change / sector shift in progress]
                      _______________________________________

ONE-LINE SUMMARY: ____________________________________________
```

**Macro doesn't tell you what to buy. Sector breadth tells you WHERE to fish.**
