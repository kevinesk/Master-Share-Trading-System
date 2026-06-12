# KLSE Master Decision Tree

> One card. Every trade. Top to bottom.
> If any gate fails → **STOP** and skip the trade. No exceptions.

---

## GATE 0 — SVS TRIPLE-CHECK (Beyond Insights anchor)

Before any technical gate, the trade must be 🟢 on all three SVS pillars:

```
┌──────────────────────────────────────────────────────────────┐
│ S — SYSTEMATIC                                                │
│   Is this trade based on a documented rule in this KB,        │
│   not a tip, hunch, or "this time is different"?              │
│                                                               │
│ V — VERSATILE                                                 │
│   Is the chosen STYLE (LT growth / trend / swing / intraday)  │
│   appropriate for the current macro cycle phase?              │
│   (e.g. don't swing-long in late-cycle topping; don't         │
│   intraday-trade on FOMC day.)                                │
│                                                               │
│ S — SAFE                                                      │
│   Is cut-loss defined IN ADVANCE? Is capital at risk ≤ 1%     │
│   (weak macro: KLCI < EMA50) or ≤ 2% (strong macro)?          │
└──────────────────────────────────────────────────────────────┘
        │                                  │
   ALL 3 🟢 → continue to GATE 1        ANY 🔴 → STOP. Do not trade.
```

**Why this gate exists**: SVS is the Beyond Insights anchor (Kathlyn Toh). A perfect technical setup executed without one of these three pillars is gambling, not trading. [File: [58](58_Beyond_Insights_SVS_Framework.md)]

---

## GATE 1 — MARKET DIRECTION (M in CAN SLIM)

```
┌──────────────────────────────────────────────────┐
│ Is KLCI above its 10-day EMA?                    │
│ AND above 50-day EMA?                            │
│ AND McClellan Oscillator > -50?                  │
│ AND distribution days in last 25 sessions ≤ 4?  │
└──────────────────────────────────────────────────┘
        │                                  │
       YES → continue to GATE 2          NO → STOP. Cash is a position.
                                              Re-check tomorrow.
```

**Why this gate exists**: 3 of 4 stocks follow the market. Perfect setups fail in M-down environments. [Files: [10](10_CAN_SLIM_KLSE.md), [26](26_Market_Breadth_Sentiment.md), [20](20_Global_Macro_for_KLSE.md)]

---

## GATE 2 — STOCK QUALITY (CAN SLI + Stage 2)

```
┌──────────────────────────────────────────────────┐
│ Trend Template score ≥ 6/8? (8/8 ideal)          │
│ EMA50 > EMA150 > EMA200?                         │
│ Price within 25% of 52-week high?                │
│ RS Rating ≥ +5 vs KLCI?                          │
│ Last 3 quarters EPS growing?                     │
│ ADV ≥ RM500K (liquidity)?                        │
└──────────────────────────────────────────────────┘
        │                                  │
       YES → continue to GATE 3          NO → SKIP this stock.
                                              Move to next watchlist name.
```

**Why this gate exists**: Trade leaders, not laggards. Stage 2 stocks deliver the asymmetric reward. [Files: [02](02_Minervini_SEPA_KLSE.md), [10](10_CAN_SLIM_KLSE.md), [34](34_Advanced_Technical_Analysis.md)]

---

## GATE 3 — PATTERN IDENTIFICATION

```
┌──────────────────────────────────────────────────┐
│ Which pattern is present on the WEEKLY chart?    │
└──────────────────────────────────────────────────┘
        │
        ├── VCP (2-4 contractions, each tighter)        → continue
        ├── Cup-with-Handle (12-33% depth, 7-65 weeks)  → continue  
        ├── Flat Base (<15% range, 5+ weeks)            → continue
        ├── Double Bottom (W, with undercut ideal)      → continue
        ├── Bull Flag / Pennant (Zanger pattern)        → continue
        ├── Darvas Box (3-day confirmed top + bottom)   → continue
        ├── Tight Closures (3+ weeks within 3%) [Ryan]  → continue
        ├── High Tight Flag (rare, ≥100% pole)          → continue (full size)
        │
        └── No clean pattern visible                    → SKIP. Wait.
```

**Pattern specs**: [39](39_ONeil_Greatest_Winners_Templates.md), [37](37_Darvas_Box_Theory.md), [41](41_Ryan_Zanger_Methods.md), [04](04_VCP_Pattern_Playbook.md), [07](07_Technical_Chart_Patterns.md)

---

## GATE 4 — VOLUME CONFIRMATION

```
┌──────────────────────────────────────────────────┐
│ During base formation:                           │
│   Volume contracting (50%+ below 50-day avg)?    │
│   No major distribution days during base?        │
│                                                  │
│ At/near pivot:                                   │
│   Pocket pivot present (bonus signal)?           │
│   No "stalling days" (high vol + close in lower  │
│   half of range)?                                │
└──────────────────────────────────────────────────┘
        │                                  │
       YES → continue to GATE 5          NO → SKIP. Distribution risk.
```

**Why**: Volume contraction = institutional accumulation. Without it, it's just sideways noise. [Files: [04](04_VCP_Pattern_Playbook.md), [42](42_Momentum_Masters_Advanced_VCP.md), [08](08_Wyckoff_Method_VSA.md)]

---

## GATE 5 — ENTRY STYLE DECISION

```
┌──────────────────────────────────────────────────┐
│ Are ALL 5 cheat conditions met?                  │
│   1. Stage 2 ✓ (already verified Gate 2)         │
│   2. 2+ prior contractions complete              │
│   3. Final contraction range < 5%                │
│   4. Final contraction volume < 50% of avg       │
│   5. Price tested contraction lower boundary     │
└──────────────────────────────────────────────────┘
        │                                  │
       YES                                NO
        │                                  │
        ▼                                  ▼
┌─────────────────────────────┐    ┌─────────────────────────────┐
│ CHEAT ENTRY                 │    │ STANDARD ENTRY              │
│ Buy 1/3 to 1/2 position at  │    │ Wait for breakout above     │
│ contraction low (today's    │    │ pivot point + 0.10          │
│ close after testing low)    │    │                             │
│                             │    │ Buy zone: pivot to pivot+5% │
│ Stop: 1.5-2.5% below        │    │ Volume req: ≥1.5× 50-day    │
│ contraction low             │    │ avg (≥2× ideal)             │
│                             │    │                             │
│ Add tranche 2 on pivot      │    │ Stop: 7% below entry OR     │
│ breakout                    │    │ below base low (tighter)    │
└─────────────────────────────┘    └─────────────────────────────┘
```

[Files: [42](42_Momentum_Masters_Advanced_VCP.md), [12](12_Perfect_Entry_Exit.md)]

---

## GATE 6 — POSITION SIZING

```
┌──────────────────────────────────────────────────┐
│ Score the setup 1-10 against master checklist:   │
└──────────────────────────────────────────────────┘
        │
        ├── 9-10 ✓ + KLCI strong   → FULL POSITION (2% portfolio risk)
        ├── 7-8  ✓ + KLCI strong   → 70% POSITION (1.4% risk)
        ├── 5-6  ✓ + KLCI strong   → 50% POSITION or SKIP
        ├── Any   + KLCI flat       → × 0.7 multiplier
        ├── Any   + KLCI below MA  → × 0.5 OR no trade
        └── Drawdown >10%           → × 0.5
            Drawdown >15%           → × 0.25
            Drawdown >20%           → STOP trading entirely
```

**Sizing formula**: `Shares = (Capital × 2%) / (Entry − Stop)` then apply multipliers. [Files: [06](06_Risk_Management_and_Position_Sizing.md), [38](38_Pit_Bull_Schwartz_Method.md)]

---

## GATE 7 — FINAL MENTAL CHECK (Don't Skip)

```
Run through ALL FOUR before clicking buy:

  ☐ "If I had bought at yesterday's close, would I be 
     selling at today's price?" — If yes, SKIP.

  ☐ "Am I trading the chart, or trying to be right?"
     — If trying to be right, SKIP.

  ☐ "If this gaps down 5% overnight, am I okay?"
     — If no, SIZE IS TOO BIG.

  ☐ "Could I show this setup to David Ryan and have 
     him approve it?" — If hesitant, SKIP.

ALL 4 PASS → execute entry.
ANY FAIL → walk away. Re-check tomorrow.
```

[File: [33](33_Fear_FOMO_Confidence_Mastery.md)]

---

## ───────── AFTER ENTRY ─────────

## GATE 8 — STOP MANAGEMENT (Trailing Sequence)

```
Gain since entry         Stop position
──────────────────       ─────────────────────────────
0 to +5%                 Original stop (don't move)
+5% to +10%              Move to BREAKEVEN
+10% to +20%             Trail with 21-day EMA close
+20% to +35%             Take 1/3 off; trail rest 21-EMA
+35% to +50%             Trail with 10-day EMA close
+50%+                    Trail with 8-day EMA close
8-week rule              If up 20% in 3 weeks, HOLD min 8 weeks
```

**Heavy-volume rule**: Any EMA violation must be on volume ≥ 1.5× 50-day avg to act. Otherwise = noise. [File: [42](42_Momentum_Masters_Advanced_VCP.md) Part 4]

---

## GATE 9 — EXIT TRIGGERS

```
EXIT IMMEDIATELY if ANY of the following occur:

  ✗ Hard stop hit                    (price ≤ stop level)
  ✗ Failed breakout                  (close back below pivot within 3 days)
  ✗ -7% loss from entry              (master rule, no exceptions)
  ✗ Daily close below relevant EMA   (per Gate 8) on heavy volume
  ✗ Climax day                       (parabolic move + reversal candle)
  ✗ Earnings miss > 5%               (next morning gap exit)
  ✗ RS Rating drops below 70         (no longer a leader)
  ✗ KLCI breaks below 10-day EMA     (raise to break-even on all positions)
  ✗ KLCI breaks below 50-day EMA     (exit all marginal positions)
```

[Files: [12](12_Perfect_Entry_Exit.md), [39](39_ONeil_Greatest_Winners_Templates.md) Part 6]

---

## GATE 10 — DRAWDOWN PROTOCOL

```
Account drawdown from peak     Required action
─────────────────────────      ─────────────────────────────────────
0-5%                            Normal variance. Continue system.
5-10%                            New sizes × 0.75. A+ setups only.
10-15%                           Sizes × 0.50. Pause 2-3 days, review.
15-20%                           Sizes × 0.25. Paper trade 1 week.
20%+ ← circuit breaker          STOP for 2 weeks minimum. Post-mortem.
                                Return at 25% size. Full sizing only 
                                after 3 consecutive winning weeks.
```

[File: [42](42_Momentum_Masters_Advanced_VCP.md) Part 5]

---

## ───────── DAILY ROUTINE WRAPPER ─────────

### Pre-Market (8:30 AM)

```
□ Box-breathing 4 min                          [33]
□ Read 5 Truths + 7 Commandments out loud      [33]
□ Macro check (Gate 1)                          [20, 26]
□ Update watchlist alerts                       [02, 04]
□ Define today's 2-3 best setups               
```

### During Market

```
□ Only watch the watchlist (no random tickers)
□ Max 2-3 NEW positions per day
□ STOP protocol on any panic [33 Part 5]
□ 10-min walk before lunch break
```

### Post-Market (5:00 PM)

```
□ Journal every trade (entry, stop, exit, why)
□ Rate emotional control 1-10
□ One thing done right, one to improve
□ Set alerts for tomorrow
□ Close laptop. Done.
```

---

## ───────── ONE-LINE SUMMARY ─────────

> **Macro green → Stage 2 leader → tight base → volume confirms → cheat OR standard entry → hard stop → trail with EMA → exit on rule → respect drawdown gates.**
> Everything else is noise.

---

## File Reference Index

| Gate | Primary File(s) |
|------|----------------|
| 1 — Market | [10](10_CAN_SLIM_KLSE.md), [20](20_Global_Macro_for_KLSE.md), [26](26_Market_Breadth_Sentiment.md) |
| 2 — Stock | [02](02_Minervini_SEPA_KLSE.md), [10](10_CAN_SLIM_KLSE.md), [34](34_Advanced_Technical_Analysis.md) |
| 3 — Pattern | [04](04_VCP_Pattern_Playbook.md), [07](07_Technical_Chart_Patterns.md), [37](37_Darvas_Box_Theory.md), [39](39_ONeil_Greatest_Winners_Templates.md), [41](41_Ryan_Zanger_Methods.md) |
| 4 — Volume | [04](04_VCP_Pattern_Playbook.md), [08](08_Wyckoff_Method_VSA.md), [42](42_Momentum_Masters_Advanced_VCP.md) |
| 5 — Entry | [12](12_Perfect_Entry_Exit.md), [42](42_Momentum_Masters_Advanced_VCP.md) |
| 6 — Sizing | [06](06_Risk_Management_and_Position_Sizing.md), [38](38_Pit_Bull_Schwartz_Method.md) |
| 7 — Mental | [33](33_Fear_FOMO_Confidence_Mastery.md), [09](09_Trading_Psychology.md) |
| 8 — Stops | [12](12_Perfect_Entry_Exit.md), [42](42_Momentum_Masters_Advanced_VCP.md) |
| 9 — Exit | [12](12_Perfect_Entry_Exit.md), [39](39_ONeil_Greatest_Winners_Templates.md) |
| 10 — Drawdown | [38](38_Pit_Bull_Schwartz_Method.md), [42](42_Momentum_Masters_Advanced_VCP.md) |

---

*Print this. Tape it next to your monitor. Read it every morning.
The 42 files are your library. This card is your daily checklist.*
