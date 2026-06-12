============================================================
 TRADINGVIEW PINE SCRIPTS — KLSE TRADING SYSTEM
============================================================

Each .pine file in this folder is one ready-to-copy TradingView
indicator. Open a file, select ALL the text, copy it, and paste
it into the TradingView Pine Editor.

------------------------------------------------------------
 THE FILES
------------------------------------------------------------
1_KLSE_VCP_Stage_v2.pine    <-- MAIN SCRIPT. Use this one.
                                Stage background (COILING/BREAKOUT/
                                EXTENDED/BASING/WEAK), pivot line,
                                buy zone, IMMINENT/STARTER tags,
                                breakout alerts. Matches the Python
                                screener (klse_screener.py) exactly.

2_KLSE_Trend_Template.pine   Minervini 8-criteria Trend Template.
                             (Already included inside script 1 —
                             optional standalone.)

3_VCP_Volume_Contraction.pine  Volume + ATR contraction sub-pane.

4_RS_Rating_vs_KLCI.pine     Relative Strength vs the KLCI index.

5_VCP_Breakout_Backtest.pine A STRATEGY (not an indicator) — shows
                             backtest results in the Strategy Tester.

6_BB_Squeeze_Alert.pine      Bollinger Band squeeze detector.

7_Intraday_Execution_Helper.pine
                             For the 5-min / 15-min chart on
                             breakout day ONLY. VWAP, EMA 9/21,
                             opening range, and a buy-zone band you
                             set from the daily pivot price. Helps
                             you EXECUTE the entry — it does not find
                             setups.

You ONLY need script 1 for daily trading. Scripts 2-6 are extras.
Script 7 is for intraday entry execution.

------------------------------------------------------------
 HOW TO LOAD A SCRIPT INTO TRADINGVIEW
------------------------------------------------------------
1. Open the .pine file (Notepad or VS Code).
2. Select all text (Ctrl+A) and copy (Ctrl+C).
3. Go to tradingview.com and open a KLSE chart,
   e.g. search:  MYX:RHBBANK
4. At the bottom of the screen, click the "Pine Editor" tab.
5. Delete any default template code in the editor.
6. Paste your script (Ctrl+V).
7. Click "Save" (top-right of the editor) — give it the same
   name as the file.
8. Click "Add to chart".

Repeat for each script you want. Each saved script is reusable
across all your charts.

------------------------------------------------------------
 SETTING THE ALERTS (script 1 only)
------------------------------------------------------------
1. With "KLSE VCP Stage v2" on the chart, set timeframe = Daily.
2. Right-click the chart -> "Add alert".
3. Condition: select "KLSE VCP Stage v2".
4. Choose "VCP Breakout" (and optionally "Coil Imminent").
5. Enable email + mobile push notifications.
6. Click "Create".

Do this once per watchlist stock. The alert waits for the
breakout so your cash stays free — you never have to chase.

------------------------------------------------------------
 WHICH SCRIPT ON WHICH CHART INTERVAL
------------------------------------------------------------
Scripts 1-6 are calibrated for DAILY bars (e.g. 260 bars = 52
weeks). Do NOT put them on 1H/5min charts — the lookbacks become
meaningless. VCP / Minervini setups are a daily concept.

  Weekly  : script 2 for context (optional)
  Daily   : scripts 1, 3, 4 (1 is the main one) ; 5 = backtest
  1H / 4H : no script needed — use TradingView's built-in VWAP
  5 / 15m : script 7 (Intraday Execution Helper) on breakout day

WORKFLOW:
  1. FIND the trade on the DAILY chart with script 1.
  2. Note the pivot price it shows.
  3. On breakout day, open the 5-min chart, load script 7,
     type that pivot price into its settings.
  4. Execute when price crosses the pivot and holds above VWAP.

------------------------------------------------------------
 NOTE
------------------------------------------------------------
The script settings (pivot lookback 15, buy zone 3%, percentiles
35/20/10) are the SAME numbers as the CONFIG block in
klse_screener.py. If you change one, change the other so the
chart and the screener always agree.

Source reference: Knowledge Base/11_TradingView_Pine_Script.md
============================================================
