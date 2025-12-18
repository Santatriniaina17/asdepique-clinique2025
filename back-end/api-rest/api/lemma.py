PREFIXES = ["man", "mi", "ma"]

def lemmatize(word):
    for p in PREFIXES:
        if word.startswith(p):
            return word[len(p):]
    return word
