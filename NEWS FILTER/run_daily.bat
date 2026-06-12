@echo off
:: ============================================================
:: KLSE News Filter — daily runner
:: Double-click this file to install dependencies and run.
:: ============================================================

title KLSE News Filter

:: ── Claude API key (optional — enables AI classification) ────────────────────
:: NEVER paste your key into this file (it is tracked by git). Instead, put it
:: on one line in api_key.txt in this folder (gitignored), or set it once with:
::     setx ANTHROPIC_API_KEY "sk-ant-..."
:: Without a key the filter falls back to keyword-based classification.
if exist "%~dp0api_key.txt" set /p ANTHROPIC_API_KEY=<"%~dp0api_key.txt"

:: ── Install missing dependencies (no auto-upgrade — keeps runs reproducible) ──
echo Checking dependencies...
py -m pip install --quiet yfinance anthropic certifi beautifulsoup4 curl_cffi

:: ── Run the news filter ───────────────────────────────────────────────────────
echo.
echo Running KLSE News Filter...
echo.
py "%~dp0klse_news_filter.py"

echo.
echo Done. Press any key to close.
pause >nul
