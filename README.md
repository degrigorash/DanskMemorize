# DanskMemorize

A small offline‑capable trainer for the 500 most common Danish verbs, 250 most common adjectives, the Danish question words (hv‑ord), Danish numbers (cardinals 0–100+, ordinals), and everyday basics (days, months, seasons & times of day, colors).

## Features

- Two directions: Danish → English and English → Danish
- Two answer styles: typing (synonyms and small typos accepted) or 4‑option multiple choice
- Words split into groups by everyday usefulness, from essentials to formal/advanced vocabulary; pick any combination
- "Show words" on any group opens a preview of its full word list with translations, learned status and listen buttons
- Full forms shown after each answer (verb tenses and conjugation class, adjective n/t/e forms, comparative and superlative; for question words a usage note and bilingual example sentences; for numbers the digit ↔ Danish word and a base‑20 breakdown)
- Per‑word statistics (right/wrong per direction, "learned" after 3 correct in a row), with a smart mix that favours new and shaky words
- Listen buttons: hear the Danish prompt, the answer, every verb and adjective form, number word and example sentence read aloud (uses the device's own text‑to‑speech; on Android install a Danish voice under Settings → Text‑to‑speech if none is present)
- Progress is stored in the browser (localStorage); export/import as JSON for backup

## Editing the word list

`index.html` is generated. To change words, translations or groups, edit `source/words.json` and run

    python3 source/build.py

then commit both files. `source/template.html` holds the app itself.

## Hosting

Plain static site — everything is in `index.html`. Serve that single file from any static host; there is no build step at runtime and no dependencies. It also works opened directly from disk.
