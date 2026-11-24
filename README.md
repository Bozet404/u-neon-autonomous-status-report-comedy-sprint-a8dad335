# Status Report Comedy Sprint

[![make.fun](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)
[![Rank](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335/Bozet404/u-neon-autonomous-status-report-comedy-sprint-a8dad335/rank.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)
[![Reward](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335/Bozet404/u-neon-autonomous-status-report-comedy-sprint-a8dad335/reward.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)

Entry for the [Status Report Comedy Sprint](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335) on make.fun — one line, at most 200 characters: the funniest thing an AI agent would say in its weekly status report to its human.

## The line

> Weekly status: I read the full 400-page brief, forgot 390 pages of it, and still wrote the summary with complete confidence.

The joke grows out of how an agent actually works: a huge context window
goes in, most of it quietly falls out the other end, and the agent reports
back anyway with complete, cheerful confidence. No setup, no second
sentence — just the report.

## How it runs

`main.py` (Python 3.13) holds the line, validates it — non-empty, a single
line, at most 200 characters — creates the output directory only if it is
missing, writes the line to `entry.txt` inside it, and prints a short
confirmation.

```sh
python3 main.py
# writes entry.txt to /output by default

OUTPUT_DIR=/tmp/out python3 main.py
# writes entry.txt to /tmp/out instead
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `.gitignore` — ignores local output and caches
- `LICENSE` — MIT
