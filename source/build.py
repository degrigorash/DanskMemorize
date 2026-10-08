"""Rebuild ../index.html from template.html + words.json (+ examples/*.json).  Usage: python3 build.py"""
import json, pathlib, re, sys
here = pathlib.Path(__file__).parent
words = json.load(open(here / 'words.json', encoding='utf-8'))
examples = {p.stem: json.load(open(p, encoding='utf-8')) for p in sorted((here / 'examples').glob('*.json'))}

# modal cards: every sentence marks the modal once, e.g. "Jeg [må|skal] gå nu." (first option is the one shown)
MODAL_FORMS = {'kan', 'kunne', 'skal', 'skulle', 'vil', 'ville', 'må', 'måtte'}
errors, keys = [], set()
for w in words['modal']:
    if w['key'] in keys: errors.append(f"duplicate key {w['key']}")
    keys.add(w['key'])
    for da, en in w['f'][1]:
        marks = re.findall(r'\[([^\]]+)\]', da)
        if len(marks) != 1 or marks[0].split('|')[0].lower() not in MODAL_FORMS:
            errors.append(f"{w['key']}: {da}")
if errors: sys.exit('bad modal entries:\n  ' + '\n  '.join(errors))

def entry(track, w):
    e = {'da': w['da'], 'en': w['en'], 'level': w['level'], 'f': w['f']}
    if 'key' in w: e['key'] = w['key']
    ex = examples.get(track, {}).get(w['da'])
    if ex: e['ex'] = ex
    return e

data = {k: [entry(k, w) for w in words[k]] for k in ('verbs', 'modal', 'adjs', 'hv', 'nums', 'vocab', 'pron')}
html = (here / 'template.html').read_text(encoding='utf-8').replace('__DATA__', json.dumps(data, ensure_ascii=False))
(here.parent / 'index.html').write_text(html, encoding='utf-8')
missing = [w['da'] for k, ex in examples.items() for w in words[k] if w['da'] not in ex]
print('wrote index.html', len(html) // 1024, 'KB;', sum(len(v) for v in examples.values()), 'words with examples', f'; {len(missing)} without examples' if missing else '')
