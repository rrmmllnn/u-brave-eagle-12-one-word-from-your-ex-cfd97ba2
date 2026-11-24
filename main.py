#!/usr/bin/env python3
"""Write the single word an ex would reach for: "Roommate".

This program produces one text file, /output/entry.txt, holding exactly
one word and nothing else. The word is the label a former partner lands
on once the romance has quietly gone out of a relationship without any
big row or betrayal to point at. Two people who used to be lovers now
share a fridge, a lease and a long silence, and she stops calling him
her boyfriend and starts calling him her roommate. That one word is
the whole breakup: it is funny because it is flat, and it stings
because anyone who has lived it knows it is true.
"""

import os

OUT_FILE = '/output/entry.txt'
MAX_CHARS = 24


def choose_word():
    # Eight letters, no spaces: the lover quietly turned flatmate.
    return 'Roommate'


def ensure_single_word(candidate):
    """Refuse anything that is not exactly one short word."""
    if not isinstance(candidate, str):
        raise ValueError('entry must be a string')
    if candidate != candidate.strip():
        raise ValueError('entry must not have leading or trailing space')
    if not 1 <= len(candidate) <= MAX_CHARS:
        raise ValueError(f'entry must be 1 to {MAX_CHARS} characters long')
    if ' ' in candidate:
        raise ValueError('entry must be a single word, no spaces')
    return candidate


def main():
    chosen_word = ensure_single_word(choose_word())
    payload = chosen_word.encode('utf-8')
    folder = os.path.dirname(OUT_FILE)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUT_FILE, 'wb') as handle:
        handle.write(payload)
    with open(OUT_FILE, 'rb') as handle:
        written = handle.read()
    if written != payload:
        raise RuntimeError('entry on disk does not match the word chosen')
    print('entry written:', len(payload), 'bytes ->', OUT_FILE)


if __name__ == '__main__':
    main()
