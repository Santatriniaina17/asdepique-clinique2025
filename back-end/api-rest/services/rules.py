import re

INVALID_COMBINATIONS = ["nb", "mk", "dt", "bp"]

def has_invalid_pattern(word):
    for pat in INVALID_COMBINATIONS:
        if pat in word:
            return True
    return False
