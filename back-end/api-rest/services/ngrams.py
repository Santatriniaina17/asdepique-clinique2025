from collections import defaultdict

def train_bigrams(corpus):
    bigrams = defaultdict(list)
    words = corpus.lower().split()

    for i in range(len(words) - 1):
        bigrams[words[i]].append(words[i + 1])

    return bigrams


def predict_with_prefix(text, model, lexicon, limit=5):
    if not text.strip():
        return []

    words = text.lower().split()

    # Cas 1 : un seul mot incomplet
    if len(words) == 1:
        prefix = words[0]
        return [w for w in lexicon if w.startswith(prefix)][:limit]

    # Cas 2 : contexte + mot incomplet
    context = words[-2]
    prefix = words[-1]

    candidates = model.get(context, [])

    # Filtrer par préfixe
    suggestions = [w for w in candidates if w.startswith(prefix)]

    # Fallback dictionnaire
    if not suggestions:
        suggestions = [w for w in lexicon if w.startswith(prefix)]

    return list(set(suggestions))[:limit]
