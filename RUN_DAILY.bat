@echo off
:: ============================================================
::  MASTER TRADING SYSTEM — DAILY RUN (17:00 post-market step)
::  One click = screener + watchlist news, per DAILY_ROUTINE.md
:: ============================================================
title Master Trading System - DAILY RUN

echo Checking dependencies...
py -m pip install --quiet yfinance pandas numpy curl_cffi anthropic beautifulsoup4 certifi

echo.
echo ============================================================
echo  STEP 1/2 - KLSE Daily Screener (VCP stages + action gate)
echo ============================================================
py "%~dp0KLSE Screener\klse_screener.py"

echo.
echo ============================================================
echo  STEP 2/2 - News Filter (active watchlist)
echo ============================================================
if exist "%~dp0NEWS FILTER\api_key.txt" set /p ANTHROPIC_API_KEY=<"%~dp0NEWS FILTER\api_key.txt"
py "%~dp0NEWS FILTER\klse_news_filter.py"

echo.
echo ============================================================
echo  DAILY RUN COMPLETE
echo  Next (DAILY_ROUTINE.md post-market): review TOP stocks,
echo  update TRADE_JOURNAL.md, set alerts, write tomorrow's plan.
echo ============================================================
pause >nul
