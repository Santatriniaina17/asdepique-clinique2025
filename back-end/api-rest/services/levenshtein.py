from rapidfuzz import process

def suggest_words(word, lexicon, limit=3):
    return [w for w, score, _ in process.extract(word, lexicon, limit=limit)]
