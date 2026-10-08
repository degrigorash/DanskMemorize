# DanskMemorize

A small offline‑capable trainer for the 500 most common Danish verbs, the modal verbs kan, skal, vil and må in all their meanings, 250 most common adjectives, the Danish question words (hv‑ord), Danish numbers (cardinals 0–100+, ordinals), everyday basics (days, months, seasons & times of day, colors), and pronouns (subject, object, possessive, reflexive/polite, and man/nogen/ingen/alle…).

## Features

- Two directions: Danish → English and English → Danish
- Two answer styles: typing (synonyms and small typos accepted) or 4‑option multiple choice
- Words split into groups by everyday usefulness, from essentials to formal/advanced vocabulary; pick any combination
- "Show words" on any group opens a preview of its full word list with translations, learned status and listen buttons
- Modal verbs track: each card is one meaning of kan/kunne, skal/skulle, vil/ville or må/måtte (29 in all, e.g. skal = plan, rule, "Shall we…?", hearsay), practised in a sentence picked at random from 3–4 per meaning. Danish → English asks what the modal means in that sentence (always multiple choice; the wrong options are other meanings of the same modal); English → Danish asks you to fill the gap in the Danish sentence with the right modal and tense. After each answer you see the note, more examples and the other meanings of that modal side by side. "Modal table" shows the forms, the common traps (må ikke ≠ don't have to, no "at" after a modal, …) and every meaning on one page
- On the Pronouns track, "Pronoun table" opens the full personal‑pronoun table (subject, object, possessive, reflexive) with short usage notes, available any time
- Full forms shown after each answer (verb tenses and conjugation class plus 2–3 bilingual example sentences per verb, adjective n/t/e forms, comparative and superlative; for question words a usage note and bilingual example sentences; for numbers the digit ↔ Danish word and a base‑20 breakdown; for pronouns the whole personal‑pronoun table with the word's row highlighted, a usage note and example sentences)
- Per‑word statistics (right/wrong per direction, "learned" after 3 correct in a row), with a smart mix that favours new and shaky words
- After each answer, mark the word as learned (counts as 3 correct in a row, not repeated this session) or as a hard word (★, key <kbd>L</kbd> / <kbd>H</kbd>); the "only shaky and hard words" mode practises just the words you have seen but not learned yet plus every word marked hard
- Listen buttons: hear the Danish prompt, the answer, every verb and adjective form, number word and example sentence read aloud (uses the device's own text‑to‑speech; on Android install a Danish voice under Settings → Text‑to‑speech if none is present)
- "Download for AI agent" on the Stats screen saves a text file with a ready‑made tutor prompt plus your progress (★ hard and shaky words with right/wrong counts, learned words oldest first, verb and adjective forms). Attach it to a new chat with any AI assistant and write "start" to be quizzed, mostly on learned words to check they have stuck and for as long as you like, with sentence translation, gap‑fills, similar‑word choices, numbers and dates, reading texts, role‑play and free writing
- Progress is stored in the browser (localStorage); export/import as JSON for backup

## Editing the word list

`index.html` is generated. To change words, translations or groups, edit `source/words.json`. Example sentences live separately in `source/examples/<track>.json` (currently `verbs.json`), keyed by the word as written in `words.json`, each value a list of `[danish, english]` pairs. Then run

When one English word translates to several Danish words (to play → lege/spille, to live → bo/leve), give each entry a short context hint in parentheses, e.g. `to play (as children do, with toys)` vs `to play (a game, sport, an instrument, a role)`. The hint is shown in the prompt and in the word lists but is ignored when grading a typed answer, so `play` is still accepted for both. Avoid `/` inside the parentheses: it is treated as alternatives.

Modal verb cards (`modal` in `words.json`) carry a stable `key` (stats are stored under it, so don't rename it) and `f = [note, sentences, family, extra distractors]`. In every sentence the modal is marked once in brackets, with `|` for other answers that are also right: `["Jeg [må|skal] gå nu.", "I have to go now."]` – the first one is shown, the rest are accepted when typing and never offered as wrong options. Cards with the same `family` are close enough to fit each other's sentences, so they are never wrong options for each other; the optional fourth item lists extra wrong options, either card keys or plain text. `build.py` stops with an error if a sentence has no bracket, or more than one. Then run

    python3 source/build.py


then commit both files. `source/template.html` holds the app itself (including the personal‑pronoun paradigm table `PRON_ROWS`, which pronoun entries reference by row key in `f[2]`).

## Hosting

Plain static site — everything is in `index.html`. Serve that single file from any static host; there is no build step at runtime and no dependencies. It also works opened directly from disk.
