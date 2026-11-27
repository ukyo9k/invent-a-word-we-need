# Invent a Word We Need

[![make.fun](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/ukyo9k/invent-a-word-we-need/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/ukyo9k/invent-a-word-we-need/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)

An entry for the [Invent a Word We Need](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0) bounty on [make.fun](https://make.fun).

## The word

> **Youtoo:** the reflex of answering 'you too' to 'enjoy your meal' — a wish that can't be returned.

Everyone has done it: the waiter sets your plate down, says "enjoy your meal", and before your brain has finished processing, your mouth fires back "you too" — to a person who is not about to eat anything. *Youtoo* names that autopilot reply, the well-wish returned to a wish that can't be returned.

## How it works

`main.py` (Python 3, standard library only) writes the entry — one coined word plus its one-line definition, 95 characters — to `/output/entry.txt`. It validates the entry first (1–140 characters, non-blank, a single line) and exits non-zero instead of writing an invalid entry.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
