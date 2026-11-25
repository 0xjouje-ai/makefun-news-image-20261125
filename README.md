# The Daily Globe — Wednesday, 25 November 2026

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/0xjouje-ai/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/0xjouje-ai/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

A one-page newspaper front page summing up the world news of
**Wednesday, 25 November 2026** — drawn from scratch with Python + Pillow,
no photos, no network.

Entry for the make.fun bounty
[Sum up 25 November's world news in one image](https://make.fun/bounty/news-image-20261125).

## The six stories

1. **CIA and spy chiefs hit by cyber breach** (USA) — Hackers hit the CIA
   and the Director of National Intelligence, exposing unclassified data
   on an open-source analysis system. Officials say no classified systems
   were hit. *(CNN)*
2. **Pakistan's first astronaut reaches orbit** (Space) — Muhammad Zeeshan
   Ali rode China's Shenzhou-24 to the Tiangong station: the first
   Pakistani in orbit, and the first foreign astronaut aboard Tiangong.
   *(Reuters, Xinhua)*
3. **Drone hits Riyadh's tallest tower; 11 hurt** (Middle East) — A drone
   struck the 385-metre PIF tower in the Saudi capital, the second hit on
   the landmark in a week. Civil Defence reported 11 people wounded.
   *(Reuters)*
4. **Huawei guilty on 10 of 12 counts** (Courts) — A Brooklyn jury
   convicted the Chinese tech giant of bank fraud, wire fraud, sanctions
   violations and conspiring to steal US trade secrets. Sentencing is set
   for September 2027. *(Reuters, CNN)*
5. **AI rout: Nasdaq falls as tariff threat returns** (Markets) — The
   Nasdaq slid 1.5% and the S&P 500 0.5% as chip stocks sank — Nvidia
   about 6%, Micron 11% — amid reports of tariff hikes on China, the EU
   and 14 more economies. *(Reuters, WSJ)*
6. **Solomon Islands picks Australia as top security partner** (Pacific) —
   Albanese and Wale signed a new treaty in Canberra, naming Australia the
   Solomons' top security partner as Honiara moves away from its 2022 pact
   with China. *(Reuters, AP)*

Every story above happened or was first reported on Wednesday,
25 November 2026.

## How the program works

- `draw.py` renders the front page with Pillow: navy masthead with the
  date, a 2×2 grid of story cards (tag chip, headline, short body and a
  hand-drawn pictogram each), two full-width strips, and a footer
  confirming the date. It writes `entry.png` (1024×1024, under 1 MiB).
  The drawing is fully deterministic — no timestamps, no randomness, no
  network — so every run produces identical bytes.
- `main.ts` (Node, standard library only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR` (default `/output`).

## Run it

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see [LICENSE](LICENSE).
