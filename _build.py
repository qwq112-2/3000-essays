#!/usr/bin/env python3
"""Build the single self-contained HTML by combining template + wordlist + stories + translations."""
import json
import sys

TEMPLATE_PATH = r'C:\Users\abala\Desktop\english-study\_template.html'
WORDLIST_PATH = r'C:\Users\abala\Desktop\english-study\wordlist.json'
STORIES_PATH = r'C:\Users\abala\Desktop\english-study\stories.json'
INTRO_PATH = r'C:\Users\abala\Desktop\english-study\_intro.json'
OUTPUT_PATH = r'C:\Users\abala\Desktop\english-study\index.html'

# Load translations
translations = {}
# Main file
with open(r'C:\Users\abala\Desktop\english-study\word_translations.py', 'r', encoding='utf-8') as f:
    src = f.read()
exec(src, {'__builtins__': {}}, translations)
# Chunks
for i in range(1, 11):
    fn = f'C:\\Users\\abala\\Desktop\\english-study\\translations_{i:02d}.py'
    with open(fn, 'r', encoding='utf-8') as f:
        src = f.read()
    chunk_dict = {}
    exec(src, {'__builtins__': {}}, chunk_dict)
    key = f'TRANSLATIONS_{i:02d}'
    if key in chunk_dict:
        translations.update(chunk_dict[key])

print(f'Total translations loaded: {len(translations)}')

# Load wordlist, merge translations
with open(WORDLIST_PATH, 'r', encoding='utf-8') as f:
    wordlist = json.load(f)

merged = 0
for word, info in wordlist.items():
    if word in translations:
        zh, en = translations[word]
        if zh:
            info['zh'] = zh
            merged += 1
        if en:
            info['e'] = en
print(f'Words with translations: {merged}/{len(wordlist)}')

# Load stories (with translations)
with open(STORIES_PATH, 'r', encoding='utf-8') as f:
    stories_text = f.read()

# Load intro
with open(INTRO_PATH, 'r', encoding='utf-8') as f:
    intro = json.load(f)

# Convert wordlist to JS-ready format
wordlist_json = json.dumps(wordlist, ensure_ascii=False, separators=(',', ':'))
intro_json = json.dumps(intro, ensure_ascii=False, separators=(',', ':'))

# Read template
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

# Substitute
final = template.replace('__WORDLIST__', wordlist_json)
final = final.replace('__STORIES__', stories_text)
final = final.replace('__INTRO__', intro_json)

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(final)

import os
print(f'Final size: {os.path.getsize(OUTPUT_PATH)} bytes ({os.path.getsize(OUTPUT_PATH)/1024:.1f} KB)')
