def analyze_sentiment(text, pos_words, neg_words):
    score = 0
    words = text.lower().split()

    for w in words:
        if w in pos_words:
            score += 1
        elif w in neg_words:
            score -= 1

    if score > 0:
        return "positif"
    elif score < 0:
        return "negatif"
    else:
        return "neutre"
