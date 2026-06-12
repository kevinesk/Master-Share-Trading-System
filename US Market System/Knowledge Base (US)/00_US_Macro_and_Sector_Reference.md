# US Macro & Sector Reference Card

Quick reference for every US tool in this system. Set your tool inputs from here.

## ⚠️ Data plan: equity ETFs only (free delayed data)

Kevin's TradingView has **no paid US real-time data**. In `request.security`, **US equity ETFs with their standard exchange prefix work** (delayed data — fine for swing). **Index & breadth symbols do NOT work** (need paid entitlement). Confirmed via the indicator's symbol picker. (`BATS:` prefix does NOT work — ignore it.)

## Macro tickers

| Signal | Use (works, delayed) | Paid-only alt | Read |
|---|---|---|---|
| S&P 500 | `AMEX:SPY` | `TVC:SPX` ✗ | Trend (vs 200-day SMA) |
| Nasdaq 100 | `NASDAQ:QQQ` | `TVC:NDX` ✗ | Growth/tech trend |
| VIX (proxy) | `CBOE:VIXY` | `CBOE:VIX` ✗ | fear; rising = risk-off |
| NYSE McClellan | `USI:NYMO` ✗ | — | >0 breadth (paid; keep off) |

> ✗ = needs paid US data entitlement Kevin doesn't have. RS and 200-MA math are identical on the ETF vs the index (ratios scale-invariant). The VIX and McClellan gates are **optional toggles, OFF by default**. With both off, macro scores out of 2 (SPX+NDX trend); each enabled gate adds to the max.

**Risk-on:** SPX>200MA, NDX>200MA (+ VIX calm/falling, + McClellan>0 if enabled). At most one signal red.

## The 11 SPDR sectors (GICS)

All SPDR sectors use the `AMEX:` prefix (works with free delayed data).

| Sector | Symbol |
|---|---|
| Technology | `AMEX:XLK` |
| Financials | `AMEX:XLF` |
| Energy | `AMEX:XLE` |
| Healthcare | `AMEX:XLV` |
| Consumer Discretionary | `AMEX:XLY` |
| Consumer Staples | `AMEX:XLP` |
| Industrials | `AMEX:XLI` |
| Materials | `AMEX:XLB` |
| Real Estate | `AMEX:XLRE` |
| Utilities | `AMEX:XLU` |
| Communication Services | `AMEX:XLC` |

## Stovall / Fidelity sector rotation by economic phase

| Phase | Favored sectors |
|---|---|
| **Early Recovery** (early cycle) | Discretionary, Financials, Industrials, Real Estate, Technology |
| **Full Recovery** (mid cycle) | Technology, Communications, Industrials, Energy, Materials |
| **Early Slowdown** (late cycle) | Energy, Materials, Staples, Healthcare |
| **Recession** (defensive) | Staples, Utilities, Healthcare |

## Two-layer Relative Strength

1. **Stock vs sector ETF** — is this a leader within its group?
2. **Sector ETF vs SPX** — is the group leading the market?

Best setups = leader in a leading group (both rising).

## US market mechanics (vs KLSE)

- **Single shares** — no 100-share board lots; size in whole shares.
- **T+1 settlement** (since May 2024).
- **Earnings blackout** — avoid initiating swing positions within ~5 trading days of earnings unless intentional.
- **Sessions** — RTH 09:30–16:00 ET; pre 04:00–09:30, post 16:00–20:00.
- **PDT rule** — accounts under $25k limited to 3 day trades / 5 business days. (Not enforced in current swing-only tools.)
- **Sizing defaults** — 5% target / 8% max per position / 1% risk per trade.
