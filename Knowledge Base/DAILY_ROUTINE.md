# Daily Trading Routine — KLSE
**Bursa Hours**: 9:00–12:30 (morning session), 14:30–17:00 (afternoon session) MYT
**Purpose**: A repeatable workflow that turns trading into a process, not an emotion.

---

## 🌅 PRE-MARKET (08:00 – 08:55)

### Step 1 — Macro Sweep (5 min)
- [ ] **Dow Jones overnight**: Close direction? Volume? (gauge tone)
- [ ] **S&P 500 / Nasdaq**: Stage 2/3/4?
- [ ] **USD/MYR**: Direction (firming = foreign inflow positive)
- [ ] **Crude oil + Brent**: Direction (KLSE oil & gas + plantation read)
- [ ] **Asian futures** (Nikkei, Hang Seng): Open direction
- [ ] **Major overnight news**: Any black swans? (war, central bank surprise, regulatory shock)

### Step 2 — KLSE Pre-Open Check (5 min)
- [ ] Read `MACRO_DASHBOARD.md` — is the 7-metric score still valid from yesterday?
- [ ] Check overnight Bursa announcements (i3investor, Bursa.com.my)
- [ ] Read any company-specific news for your open positions
- [ ] Check ex-dividend dates within next 3 days (Ex-Dividend Alert tool)

### Step 2b — EVENT BLACKOUT CHECK (Beyond Insights rule — 2 min)

Scan the next 24 hours for any of these scheduled events:

- [ ] **US FOMC** decision or Powell press conference
- [ ] **BNM MPC** (OPR decision)
- [ ] **US CPI / NFP / GDP** release
- [ ] **China PMI / GDP** release
- [ ] **Major Bursa results** for any held position or active watchlist name
- [ ] **MY Budget**, election, or major fiscal announcement
- [ ] **Geopolitical escalation** (sanctions, war event, tariff announcement)

**If ANY box ticks YES within the next 24h:**

| Action | Rule |
|---|---|
| New entries | ❌ BLOCKED — no new positions until event passes + 1 session of confirmation |
| Existing positions | ⚠️ Tighten stops by 50% (move closer to market) |
| Pyramid / add-on | ❌ BLOCKED |
| Intraday trades | ❌ BLOCKED (overnight risk re-emerges around the event) |
| Defensive hedge | ✅ Allowed (e.g. SPY put for US side, raise cash on KLSE side) |

**Why**: Beyond Insights / Kathlyn Toh — even an A+ technical setup gets steamrolled by a central-bank surprise. You can't out-system a macro event. Sitting out IS the trade. [File: [58](58_Beyond_Insights_SVS_Framework.md)]

### Step 3 — Position Review (10 min)
- [ ] Open `TRADE_JOURNAL.md` → review "Open Positions" table
- [ ] For each position:
  - Current price vs entry (% gain/loss)
  - Stop still appropriate? (raise if trade moved +5%+)
  - Approaching T1/T2/T3? (prepare sell tranche)
  - Thesis still valid? (no breaking news?)
- [ ] If approaching pivot/breakout for any: note it

### Step 4 — Watchlist Refresh (10 min)
- [ ] Open `TRADE_JOURNAL.md` → "Watchlist (Active Triggers)" table
- [ ] For each watchlist stock:
  - Where is it vs trigger price?
  - Setup still valid? (base intact?)
  - Volume signature in last 3 days?
- [ ] Remove any that broke down (stop tracking failed setups)
- [ ] Confirm triggers and buy zones still accurate

### Step 5 — Daily Plan Written (5 min)
Write in journal (or notepad):

```
DATE: 2026-MM-DD
KLCI overnight tone: BULL / NEUTRAL / BEAR
My open positions: [list with current status]
My triggers today:
  - STOCK1: Buy if price > RM X.XX on volume; size = NNN units
  - STOCK2: Sell tranche if price > RM Y.YY
  - STOCK3: Stop if breaks RM Z.ZZ
My mental state: 1-10 (under 6 = no new trades today)
ONE word for today: PATIENT / DISCIPLINED / OBSERVE
```

---

## 🔔 MARKET OPEN (09:00 – 09:30) — DO NOT TRADE

**The first 30 minutes are auction-driven chaos.** Most retail loss happens here.

### Rules during opening 30 min:
- ❌ NO new BUY orders
- ❌ NO sell unless stop hit
- ❌ NO chart-watching tick-by-tick
- ✅ OBSERVE the open: which sectors strong/weak, breadth direction, KLCI vs Dow

### What to look for:
- KLCI opens higher or lower vs yesterday's close?
- Which sectors lead the opening 30 min? (Use Pro Quant Desk heat map)
- Volume in first 30 min — strong or weak?
- Your watchlist stocks: any gapping?

**Note observations. Do NOT act.**

---

## 📊 EARLY SESSION (09:30 – 12:30)

### Action Window 1 — Triggered Entries (09:30 – 11:00)
If a watchlist stock hits its trigger:
- [ ] Confirm trigger conditions (price + volume + close above pivot)
- [ ] Run `PRE_TRADE_CHECKLIST.md` — all 12 gates
- [ ] Run `POSITION_SIZE_CALCULATOR.md` — calculate units
- [ ] If all green → place limit order at trigger price
- [ ] After fill → place stop in broker immediately
- [ ] Log in `TRADE_JOURNAL.md`

### Monitoring Open Positions (continuous)
- Stops are already in broker. Don't watch ticks.
- Set price alerts for T1/T2/T3 and stop level
- Only check stocks at :30 and :00 of each hour (4 checks max)

### Action Window 2 — Manage Profits (11:00 – 12:30)
- [ ] If T1 hit: sell tranche, raise stop on remainder
- [ ] If T2 hit: sell tranche, raise stop to T1 level
- [ ] If T3 hit: trail under 20 EMA, do NOT exit fully if trend intact

---

## 🍴 LUNCH BREAK (12:30 – 14:30) — STEP AWAY

Bursa is closed. **Step away from the screen completely.**

### Things to do:
- Eat lunch (real food, not at the desk)
- Walk outside 15-20 min
- NO chart-watching
- NO news-reading
- NO researching new stocks

This 2-hour break is built into the Malaysian market for a reason. Use it.

### Optional (if compelled):
- Review one Knowledge Base file you haven't read in a while
- Update yesterday's journal entries

---

## 📈 AFTERNOON SESSION (14:30 – 17:00)

### 14:30 – 15:30 — Re-engage Carefully
- KLCI direction vs morning?
- Any reversal patterns on KLCI 30-min chart?
- Your positions: did momentum continue or fade?

### 15:30 – 16:30 — The Real Action Window
Most KLSE breakouts confirm or fail in this window.
- [ ] Recheck watchlist triggers
- [ ] If any new A+ setup appears with all 12 gates: execute
- [ ] If positions hit T1/T2/T3: scale out
- [ ] If positions break down: let stop work, don't pre-empt

### 16:30 – 17:00 — Closing Hour
**WARNING**: Closing-hour buying = chasing. Almost never a good idea unless you're scaling INTO an existing winner that's just broken its pivot.
- ✅ OK: Adding to confirmed breakout in last 30 min
- ❌ NOT OK: Starting a new position in last 30 min

---

## 🌙 POST-MARKET (17:00 – 18:00)

### Step 1 — Position Updates (10 min)
- [ ] Update `TRADE_JOURNAL.md` for any trades made today
- [ ] For each open position: note today's close + % from entry
- [ ] For each closed trade: complete the exit log + 5 questions

### Step 2 — KLSE Screener Run (15 min)
- [ ] Run `klse_screener.py` (end-of-day scan)
- [ ] Run KLSE Momentum Swing Screener on TradingView
- [ ] Run Minervini VCP + SmartMCDX scan
- [ ] Review TOP 10-20 output stocks
- [ ] Add new candidates to watchlist (max 5 new per day)

### Step 3 — Tomorrow's Plan (10 min)
- [ ] Review watchlist — which 3 stocks could trigger tomorrow?
- [ ] Note their triggers, buy zones, planned sizes
- [ ] Set price alerts in TradingView/MooMoo
- [ ] Write tomorrow's plan in journal

### Step 4 — Daily Reflection (5 min)
- [ ] Did I follow my plan today? (Y/N + why)
- [ ] Any trades I shouldn't have taken? (FOMO / size / chase)
- [ ] Any trades I should have taken but didn't? (Hesitation / fear)
- [ ] Mental state at close: 1-10
- [ ] Lesson of the day (one sentence): __________

---

## 🌐 EVENING (after dinner — optional)

### News & Macro Catch-Up (30 min max)
- Read 1-2 KLSE news pieces (i3investor, The Edge, KLSE Screener news)
- Read 1 macro piece (Fed, BNM, global)
- Scan US market open (KLSE evening = US morning Sep-Mar; US after-close Apr-Aug due to DST)
- DO NOT make trade decisions at night — too tired, too emotional

### Skill Building (15-30 min)
- Read ONE Knowledge Base file slowly
- Re-read your worst trade from past month, extract lesson
- Watch ONE chart from past month — what did you miss?

---

## 📆 WEEKLY RHYTHM

| Day | Focus |
|---|---|
| Monday | Fresh start — review weekly plan from Sunday's `WEEKLY_ROUTINE.md` |
| Tuesday | Mid-week setups developing |
| Wednesday | Mid-week review — adjust watchlist |
| Thursday | Look for Friday's setups |
| Friday | Avoid new entries (weekend gap risk); manage existing positions |
| Saturday | OFF — no charts, no thinking about trades |
| Sunday | `WEEKLY_ROUTINE.md` — full top-down review |

---

## 🚦 Mental State Gating

At three checkpoints per day, rate your mental state 1-10:

- 08:00 (pre-market): If <6, no new trades today — only manage existing
- 12:30 (lunch): If <5, take afternoon off, no trades
- 17:00 (close): If trading caused stress, journal it before forgetting

**Rule**: Two consecutive <5 days = take 48 hours off completely.

---

## 🎯 The Whole Routine in One Sentence

> Pre-market plan → Open watch (no trade) → Triggered entries (mid-morning) → Manage profits (mid-day) → Step away (lunch) → Late triggers (afternoon) → Close reflection → Journal → Plan tomorrow.

**Process beats prediction. Routine beats intuition. Discipline beats genius.**
