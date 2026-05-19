# TradingView Alert Setup Guide

How to activate push notifications and email alerts for all signals in your scripts.

---

## Step 1 — Load the script on a chart

1. Open TradingView and go to any KLSE stock chart
2. Click **Indicators** (top toolbar) → **My Scripts** or **Pine Editor**
3. Paste the script and click **Add to chart**

---

## Step 2 — Create an alert for a signal

1. Right-click on the chart → **Add alert**  
   OR click the **clock icon** (⏰) in the top toolbar
2. In the **Condition** dropdown — select the script name (e.g. `V8 Intraday Sniper`)
3. In the second dropdown — choose the signal you want:

### V8 Intraday Sniper (5-min chart) — available alerts
| Alert name | When it fires |
|---|---|
| **COIL — Prepare Entry** | Volume drying up on EMA pullback. Earliest warning — place limit order |
| **WATCH Setup** | Setup forming, waiting for surge |
| **SNIPE Entry** | EMA pullback + volume surge confirmed — buy now |
| **SNIPE+ Entry** | Hammer at support + volume surge — highest conviction |
| **TP1 Hit — Sell 1/3** | Price reached TP1 — sell first tranche |
| **TP2 Hit — Sell 1/3** | Price reached TP2 — sell second tranche |
| **EXIT Signal** | Close remaining position |

### KLSE MSS V6 (daily swing) — available alerts
| Alert name | When it fires |
|---|---|
| **VCP COIL — Prepare Entry** | BB tightest + volume at N-day low — spring wound, breakout 1-5 days away |
| **T1 HIGH CONVICTION BUY** | Score ≥ 11, all gates pass |
| **T2 MOMENTUM BUY** | Score ≥ 9 |
| **WATCHLIST PRE-BREAKOUT** | Score ≥ 7, coiling |
| **TP1 Hit — Sell 1/3** | Sell first tranche |
| **TP2 Hit — Sell 1/3** | Sell second tranche |
| **EXIT SIGNAL** | Close position |

---

## Step 3 — Configure the notification

In the alert settings window:

| Setting | Recommended value |
|---|---|
| **Expiration** | Open-ended (set far future date) |
| **Alert actions** | Tick: **Notify on app** + **Send email** |
| **Message** | Leave as-is (pre-filled by script) |

Click **Create** — alert is now live.

---

## Step 4 — Enable push notifications on your phone

1. Install the **TradingView app** on your phone (iOS or Android)
2. Log in with the same account
3. Go to **Profile → Settings → Notifications**
4. Enable **Price alerts** and **Script alerts**

Alerts will now appear as phone notifications in real time.

---

## Step 5 — Setting up for multiple stocks

TradingView requires one alert per stock per signal. Recommended workflow:

1. Build a watchlist of stocks that pass your fundamental filters (Layer 3)
2. For each stock, open its 5-min chart, load V8 Intraday Sniper, create COIL + SNIPE alerts
3. For each stock, open its daily chart, load KLSE MSS V6, create VCP COIL + T1 alerts

**TradingView plan note:**  
- Free plan: 1 alert at a time  
- Pro plan: 20 alerts  
- Pro+ plan: 100 alerts (recommended for a watchlist of 10-20 stocks)

---

## Signal sequence — what order to expect

```
Daily chart (KLSE MSS V6):
    VCP COIL  →  T3 WATCH  →  T2 BUY  →  T1 BUY
    (1-5 days early)        (breakout confirmed)

5-min chart (V8 Intraday Sniper):
    COIL  →  WATCH  →  SNIPE / SNIPE+
    (limit order)   (market order)
```

**Best practice:** When VCP COIL fires on the daily chart, open the 5-min chart and watch for the COIL → SNIPE sequence to time your exact entry.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Alert fired but chart shows nothing | Alert may have fired on a bar that has since closed. Check the 5-min history for a purple circle (COIL) or green label (SNIPE) |
| Too many false alerts | Increase `Volume Dry-Up Lookback` in the COIL settings |
| Missing alerts | Check TradingView notification settings and phone app permissions |
| Alert expired | TradingView alerts expire — re-create with an open-ended expiration date |
