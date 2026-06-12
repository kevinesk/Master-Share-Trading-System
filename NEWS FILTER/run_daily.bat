@echo off
:: ============================================================
:: KLSE News Filter — daily runner
:: Double-click this file to install dependencies and run.
:: ============================================================

title KLSE News Filter

:: ── Set your Claude API key here (optional — enables AI classification) ──────
:: If you have a key, replace the line below.
:: Leave blank to use keyword-based classification instead.
set ANTHROPIC_API_KEY=

:: ── Install / upgrade dependencies silently ───────────────────────────────────
echo Installing / updating dependencies...
py -m pip install --quiet --upgrade yfinance anthropic certifi beautifulsoup4 curl_cffi

:: ── Run the news filter ───────────────────────────────────────────────────────
echo.
echo Running KLSE News Filter...
echo.
py "%~dp0klse_news_filter.py"

echo.
echo Done. Press any key to close.
pause >nul
