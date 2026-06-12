@echo off
:: ============================================================
::  MASTER TRADING SYSTEM — SUNDAY WEEKLY RUN
::  Fresh fundamentals -> 7-light macro regime -> screener
::  (per WEEKLY_ROUTINE.md; ~15-20 minutes total)
:: ============================================================
title Master Trading System - WEEKLY RUN (Sunday)

echo Checking dependencies...
py -m pip install --quiet yfinance pandas numpy curl_cffi anthropic beautifulsoup4 certifi

echo.
echo ============================================================
echo  STEP 1/3 - Fundamentals v2 (quality grades, ~5-10 min)
echo ============================================================
py "%~dp0Fundamentals\fetch_fundamentals_v2.py"

echo.
echo ============================================================
echo  STEP 2/3 - 7-Light Macro Regime Board (sets the week's
echo             bucket mix and risk per trade)
echo ============================================================
py "%~dp0KLSE Screener\macro_lights.py"

echo.
echo ============================================================
echo  STEP 3/3 - KLSE Screener (re-scored with fresh fundamentals)
echo ============================================================
py "%~dp0KLSE Screener\klse_screener.py"

echo.
echo ============================================================
echo  WEEKLY RUN COMPLETE
echo  Next (WEEKLY_ROUTINE.md): copy the macro score into
echo  MACRO_DASHBOARD.md, update SECTOR_BREADTH_TRACKER.md,
echo  rebalance buckets, build the week's watchlist (max 5/bucket).
echo  Optional broad news sweeps: "NEWS FILTER\run_klci30.bat"
echo  and "NEWS FILTER\run_mid70.bat".
echo ============================================================
pause >nul
