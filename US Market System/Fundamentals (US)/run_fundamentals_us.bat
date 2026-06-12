@echo off
REM US Fundamentals fetcher — double-click to run.
REM One-time setup:  pip install yfinance
cd /d "%~dp0"
py fetch_fundamentals_us.py
if errorlevel 1 python fetch_fundamentals_us.py
echo.
pause
