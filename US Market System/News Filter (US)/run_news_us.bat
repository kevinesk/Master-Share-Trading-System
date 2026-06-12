@echo off
REM US News Filter — double-click to run.
REM One-time setup:  pip install yfinance
cd /d "%~dp0"
py us_news_filter.py
if errorlevel 1 python us_news_filter.py
echo.
pause
