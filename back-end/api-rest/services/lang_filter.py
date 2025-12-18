import re

FRENCH_SUFFIXES = (
    "tion", "ment", "aux", "eur", "euse", "ique"
)

INVALID_MG_PATTERNS = (
    "nb", "mk", "dt", "bp", "sz","th", "sn", "nl","dn","nf","tt","fv", "ss"
)

def is_malagasy_like(word):
    word = word.lower()

    if re.search(r"[éèêàùçôîcqxu]", word):
        return False

    for suf in FRENCH_SUFFIXES:
        if word.endswith(suf):
            return False

    for pat in INVALID_MG_PATTERNS:
        if pat in word:
            return False

    if not re.search(r"[aeiouy]", word):
        return False

    return True
