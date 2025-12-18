import json

def load_lexicon():
    with open("data/lexicon.json", "r", encoding="utf-8") as f:
        return set(json.load(f))
    
def load_sentiment_words():
    pos_words = {"fitiavana", "tsara", "mahafaly"}
    neg_words = {"ratsy", "malahelo", "fahoriana"}
    return pos_words, neg_words
