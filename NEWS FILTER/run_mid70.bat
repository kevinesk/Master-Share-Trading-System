@echo off
title KLSE News Filter — FBM MID 70

:: ── Set your Claude API key for AI analysis (optional) ───────────────────────
set ANTHROPIC_API_KEY=

:: ── Install / update dependencies ────────────────────────────────────────────
echo Installing / updating dependencies...
py -m pip install --quiet --upgrade yfinance anthropic beautifulsoup4 curl_cffi certifi

:: ── Run for FBM MID 70 ───────────────────────────────────────────────────────
echo.
echo Running KLSE News Filter — FBM MID 70...
echo NOTE: 70 stocks may take 5-10 minutes. Please wait.
echo.
py "%~dp0klse_news_filter.py" watchlist_mid70.txt

echo.
echo Done. Press any key to close.
pause >nul
