@echo off
title KLSE News Filter — FBM KLCI 30

:: ── Set your Claude API key for AI analysis (optional) ───────────────────────
set ANTHROPIC_API_KEY=

:: ── Install / update dependencies ────────────────────────────────────────────
echo Installing / updating dependencies...
py -m pip install --quiet --upgrade yfinance anthropic beautifulsoup4 curl_cffi certifi

:: ── Run for FBM KLCI 30 ──────────────────────────────────────────────────────
echo.
echo Running KLSE News Filter — FBM KLCI 30...
echo.
py "%~dp0klse_news_filter.py" watchlist_klci30.txt

echo.
echo Done. Press any key to close.
pause >nul
