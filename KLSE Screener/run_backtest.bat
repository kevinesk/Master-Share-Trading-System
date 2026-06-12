@echo off
title KLSE Screener Backtester

echo Installing / updating dependencies...
py -m pip install --quiet --upgrade yfinance pandas numpy curl_cffi

echo.
echo Running KLSE Screener Backtest...
echo This will take 3-6 minutes (5 years of history x 100 stocks x 2 runs).
echo.
py "%~dp0backtest_screener.py"

echo.
echo Done. Press any key to close.
pause >nul
