# Git Quick Reference — Master Share Trading System

## What this repo is for
Every Pine Script change you make can be saved here with a description of why you made it.
GitHub keeps the full history forever. If anything breaks, you can roll back.

---

## Daily workflow (30 seconds)

After changing a script, tell Claude Code what you changed and it will run these for you:

```
git add "path/to/script"
git commit -m "describe what you changed and why"
git push
```

### Example commit messages
- `"Raise EMA9 pullback depth gate from 1% to 1.5%"`
- `"Tighten volume surge threshold to 1.8x — too many false signals at 1.5x"`
- `"Add PDC as third entry gate for Intraday Sniper"`

---

## Useful commands

| What you want | Command |
|---|---|
| See what changed | `git status` |
| See full history | `git log --oneline` |
| See exact changes in a file | `git diff "filename"` |
| Experiment safely | `git checkout -b experiment/idea-name` |
| Go back to a previous version | `git checkout <commit-hash> -- "filename"` |

---

## Your scripts and their latest versions

| Tool | Latest file |
|---|---|
| Intraday Sniper | `Intraday Sniper/V7 Intraday Sniper (Long) + PD Levels` |
| KLSE Momentum Swing Screener | `.claude/KLSE MSS/KLSE Momentum Swing Screener-v5` |
| Minervini VCP Backtest | `Minervini VCP + SmartMCDX Backtest/Minervini VCP + SmartMCDX Backtest-v8-KLSE.txt` |
| Pro Quant Desk | `Pro Quant Desk (KLSE)/Pro Quant Desk (KLSE) + True RS + Heat- v7` |

---

## GitHub repo
https://github.com/kevinesk/Master-Share-Trading-System

---

## If you get stuck
Just tell Claude Code:
- *"I updated [script name] — [what you changed]"* → it will commit and push
- *"Show me what changed in [script name]"* → it will diff the file
- *"Roll back [script name] to yesterday"* → it will find and restore the version
