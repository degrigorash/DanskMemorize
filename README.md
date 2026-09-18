# DanskMemorize

A small offline‑capable trainer for the 500 most common Danish verbs, 250 most common adjectives, and the Danish question words (hv‑ord).

**Live:** https://degrigorash.github.io/DanskMemorize/

## Features

- Two directions: Danish → English and English → Danish
- Two answer styles: typing (synonyms and small typos accepted) or 4‑option multiple choice
- Words split into groups by everyday usefulness, from essentials to formal/advanced vocabulary; pick any combination
- Full forms shown after each answer (verb tenses and conjugation class, adjective n/t/e forms, comparative and superlative; for question words a usage note and a bilingual example sentence)
- Per‑word statistics (right/wrong per direction, "learned" after 3 correct in a row), with a smart mix that favours new and shaky words
- Progress is stored in the browser (localStorage); export/import as JSON for backup

## Editing the word list

`index.html` is generated. To change words, translations or groups, edit `source/words.json` and run

    python3 source/build.py

then commit both files. `source/template.html` holds the app itself.

## Hosting

Plain static site — GitHub Pages serves `index.html` from the repository root. No build step, no dependencies.
