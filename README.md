# Master Share Trading System

A complete trading operation for **Bursa Malaysia (KLSE)** — rulebook, Python screening pipeline, and TradingView Pine indicators — with a US-market mirror.

**The single operating document is [Knowledge Base/KLSE_MASTER_SYSTEM.md](Knowledge%20Base/KLSE_MASTER_SYSTEM.md).**
Every rule (buckets, regime, sizing, exits, circuit breakers) lives there. Everything else supports it.

---

## Daily / weekly operation (one click each)

| When | Run | What it does |
|---|---|---|
| **Every trading day, ~17:00** | `RUN_DAILY.bat` | KLSE screener (VCP stages + regime + action gate) → watchlist news scan |
| **Every Sunday** | `RUN_WEEKLY.bat` | Fresh fundamentals v2 → 7-light macro regime board → screener re-score |
| **Monthly** | `update_deps.bat` | Upgrades Python packages (daily runs deliberately never auto-upgrade) |

The screener warns when fundamentals are older than 7 days — rerun `Fundamentals\run_fundamentals.bat` when it does.

## The pipeline

```
Fundamentals v2 (weekly)        macro_lights.py (Sunday)
  quality grades A-D              7-light score -> regime -> bucket mix + risk%
        │                                  │
        ▼                                  ▼
KLSE Screener (daily EOD) ── regime-gated VCP stages: COILING / BREAKOUT / EXTENDED
        │                     + 100-pt composite score + signal journal (edge tracking)
        ▼
News Filter (daily) ── catalyst / risk scan on the watchlist
        │
        ▼
TradingView (live) ── confirm + execute with the Pine indicators below
```

## Folder map

| Folder | Purpose | Current version |
|---|---|---|
| `Knowledge Base/` | 59 reference files + operating docs (MASTER_SYSTEM, routines, checklists, journal) | — |
| `KLSE Screener/` | Daily Python screener, 7-light macro board, backtester, 100-stock universe | screener v2.3 |
| `Fundamentals/` | Fundamentals fetcher + quality models (KC Chong / Cold Eye / MONEY / Tong tier), annual-report AI analyzer | **v2** |
| `NEWS FILTER/` | News scans: watchlist / KLCI 30 / Mid 70 (AI classification with API key) | — |
| `KLSE Momentum Swing Screener/` | Swing entry indicator (TradingView) | **V12 Swing Sniper Pro** |
| `Intraday Sniper/` | 5-minute execution indicator + HUD + watchlist ranker | **V9 Phase 2** |
| `Minervini VCP + SmartMCDX Backtest/` | VCP pattern backtest + dashboard | **v9 Phase 2** (dashboard v8) |
| `Pro Quant Desk (KLSE)/` | RS/heat dashboard + market regime dashboard | **v9 Phase 2** |
| `Ex-Dividend Alert/` | Ex-date warning overlay | v2 |
| `TradingView/` | 8 small single-purpose utilities (trend template, RS rating, BB squeeze…) | — |
| `US Market System/` | SPX-benchmarked mirror of the KLSE stack | v1 |

> **V12 is the primary swing entry tool** (Master System §5, settings: Hard macro gate, 10% notional cap). V10 stays on the chart for parallel validation until **2026-07-03** — trust only its EXECUTE NOW signal. V11 is archived (signal-integrity bug, fixed in V12).

## TradingView usage

Open the Pine editor, paste the contents of the **highest-versioned** file in the relevant folder, **Add to chart**. Older versions stay only as history — never paste them.

## Setup notes

- Python 3 via the `py` launcher; packages install automatically on first run.
- AI features (news classification, annual reports) need an Anthropic API key:
  put it in `NEWS FILTER\api_key.txt` / `Fundamentals\api_key.txt` (both gitignored), or `setx ANTHROPIC_API_KEY "sk-ant-..."`.
  **Never paste keys into .bat files — they are tracked by git.**
- Generated reports land in each tool's `output/` folder (gitignored except `signal_journal.csv`, `macro_lights_history.csv` and `fundamentals_*.json`).
