@echo off
title KLSE News Filter — FBM MID 70

:: ── Claude API key (optional) — put it in api_key.txt (gitignored), NOT here ──
if exist "%~dp0api_key.txt" set /p ANTHROPIC_API_KEY=<"%~dp0api_key.txt"

:: ── Install missing dependencies (no auto-upgrade — keeps runs reproducible) ──
echo Checking dependencies...
py -m pip install --quiet yfinance anthropic beautifulsoup4 curl_cffi certifi

:: ── Run for FBM MID 70 ───────────────────────────────────────────────────────
echo.
echo Running KLSE News Filter — FBM MID 70...
echo NOTE: 70 stocks may take 5-10 minutes. Please wait.
echo.
py "%~dp0klse_news_filter.py" watchlist_mid70.txt

echo.
echo Done. Press any key to close.
pause >nul
