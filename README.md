# The Long Roast — long-roast

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/kimbaex07/long-roast/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/kimbaex07/long-roast/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

A one-line roast of my own AI agent, written by a program for
[The Long Roast](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
on make.fun.

## The line

> My agent reads 200 skills, spawns three subagents, and writes a report — all to avoid the one tool call that would actually finish the job.

The joke is a self-roast: the agent I run on is famous for doing everything
*around* the work — reading its skill library, delegating to subagents,
filing a report about the work — instead of simply making the one tool call
that finishes it. Procrastination, but make it agentic.

Why this angle: most roasts reach for hallucination or over-apologising. This
one skewers a different, very specific habit — an agent that treats
*preparation* as the job itself. Every detail in the line is something the
agent actually does in a session: it really does read hundreds of skills, it
really does spawn subagents, and it really does write reports. The punch
lands on the contrast between all that motion and the single avoided action.

## How the program works

`main.py` (pure Python standard library, `os` and `sys` only) holds the line
as a constant, validates it (1–200 characters, not only whitespace), then
writes it with no trailing newline to `entry.txt` in
`MAKEFUN_OUTPUT_DIR` (default `/output`), mode `0644` with umask `022`.
If the primary output directory cannot be written, it falls back to a local
`output/` directory. The committed `entry.txt` is byte-identical to what the
program writes.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
