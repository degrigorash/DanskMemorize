"""Rebuild ../index.html from template.html + words.json.  Usage: python3 build.py"""
import json, pathlib
here = pathlib.Path(__file__).parent
words = json.load(open(here / 'words.json', encoding='utf-8'))
data = {k: [{'da': w['da'], 'en': w['en'], 'level': w['level'], 'f': w['f']} for w in words[k]] for k in ('verbs', 'adjs', 'hv')}
html = (here / 'template.html').read_text(encoding='utf-8').replace('__DATA__', json.dumps(data, ensure_ascii=False))
(here.parent / 'index.html').write_text(html, encoding='utf-8')
print('wrote index.html', len(html) // 1024, 'KB')
