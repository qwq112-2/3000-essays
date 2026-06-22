# 3000 essays

A quiet place to read English and remember words.

A single-page web app for learning the 3000 most frequent English words (Longman Communication 3000), in the context of short stories and interview notes.

## Features

- **3000 words pre-loaded** — every word from Longman Communication 3000 with part-of-speech and spoken/written frequency markers (S1–S3 / W1–W3)
- **5 short stories** — classic Aesop's fables in simple English, all public domain
- **Click any word** to see its definition, mark it as known, or save a personal Chinese note
- **Spaced repetition (SRS)** — 4-tier review (Again / Hard / Good / Easy) with 1/2/4/7-day intervals, simplified SM-2
- **Blog for interviews** — record the interviews you watch, paste transcripts, watch your 3000-word coverage update live
- **Light / Dark mode** with a warm cream paper aesthetic
- **No server, no tracking** — all data lives in your browser's `localStorage`

## Design

- Display + body: **Fraunces** (variable serif)
- UI + buttons: **Manrope**
- Color palette: warm cream paper, terracotta accent
- Drop caps, generous whitespace, hairline dividers, subtle paper texture

## Stack

- One file: `index.html` (~170 KB)
- Zero dependencies
- Web fonts via Google Fonts CDN
- No build step

## Run locally

Just open `index.html` in a browser. That's it.

```bash
# Or serve locally if you want a real URL:
python -m http.server 8000
# then open http://localhost:8000
```

## Data files

- `index.html` — the entire app
- `wordlist.json` — source data for the 3000 words (reference)
- `stories.json` — source data for the 5 stories (reference)

## License

Stories: public domain (Aesop).
Word list: Longman Communication 3000.
Code: MIT.
