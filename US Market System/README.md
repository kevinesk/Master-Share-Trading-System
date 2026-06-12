# US Market System

US-equity (NYSE / NASDAQ) sibling of the KLSE ecosystem at the repo root. Same top-down framework (macro → sector → stock → entry → exit), re-tuned for US market mechanics.

## What's different from KLSE

| Layer | KLSE | US |
|---|---|---|
| Benchmark | KLCI | **SPX** |
| Macro stack | KLCI + Dow + McClellan | **SPX + NDX + VIX + NYSE McClellan** |
| Sectors | Banking / Property / Tech | **11 SPDR ETFs** (XLK XLF XLE XLV XLY XLP XLI XLB XLRE XLU XLC) |
| Relative Strength | vs KLCI | **stock vs sector ETF, sector ETF vs SPX** |
| Lot size | 100-share board lots | **single shares** (no rounding) |
| Sizing default | 7% / 10% / 1% | **5% target / 8% max / 1% risk** |
| Currency | RM | **USD** |

## Build status

| Phase | Tool | Status |
|---|---|---|
| 0 | Scaffold + US Engine + reference card | Done |
| 1 | **Pro Quant Desk (US)** | Done — `Pro Quant Desk (US)/Pro Quant Desk (US) v1.pine` |
| 2 | **Momentum Swing Screener (US)** | Done — `Momentum Swing Screener (US)/Momentum Swing Screener (US) v1.pine` |
| 3 | **Minervini VCP + SmartMCDX (US)** | Core done — `Minervini VCP + SmartMCDX (US)/Minervini VCP + SmartMCDX (US) v1.pine` (v9 pattern-layers + standalone dashboard optional follow-ons) |
| 4 | **US Swing Entry Planner** (pre-market order ticket) | Done — `Intraday Sniper (US)/US Swing Entry Planner v1.pine` (reframed from 5-min Sniper: daily pullback/breakout order planner, since US trades are set before open from Malaysia) |
| 5 | **Ex-Dividend / Fundamentals / News Filter (US)** | Done — Ex-Div Pine; Fundamentals + News are Python via `yfinance` (no API key) |
| 6 | Knowledge Base (US) | Pending |
| 7 | TradingView US alerts setup guide | Pending |

## Architecture

`US Engine/US_Engine_v1.pine` is the canonical block of reusable logic (macro gauge, two-layer RS, Weinstein stage, sizing, anti-FOMO). Every tool embeds the same logic so all tools compute identically. Reliability rules: all cross-symbol pulls use `request.security(..., lookahead=barmerge.lookahead_off)`; macro tickers are user-overridable inputs (symbol availability varies by TradingView plan).

## Usage

1. Open [TradingView](https://www.tradingview.com) → Pine Script editor.
2. Paste a tool's `.pine` file → **Add to chart**.
3. Run on a US equity, **Daily** timeframe for the swing tools.
4. Set the sector ETF input to match the stock's sector (see reference card in `Knowledge Base (US)/`).

> Defaults assume a swing-trading account. PDT (Pattern Day Trader) logic is intentionally omitted — revisit if day-trading under $25k.
