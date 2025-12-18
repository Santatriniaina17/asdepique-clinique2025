from rapidfuzz import process
from services.fallback_lexicon import local_fallback_lexicon
from services.mediawiki import fetch_words_by_prefix
from services.lang_filter import is_malagasy_like


def fuzzy_fallback(prefix, lexicon, limit=3):
    return [w for w, _, _ in process.extract(prefix, lexicon, limit=limit)]


def predict_on_demand(text, limit=5):
    if not text.strip():
        return []

    prefix = text.lower().split()[-1]

    # 1️⃣ MediaWiki ciblée
    suggestions = fetch_words_by_prefix(prefix)

    # 2️⃣ FILTRAGE MALAGASY (LA CLÉ 🔑)
    suggestions = [w for w in suggestions if is_malagasy_like(w)]

    # 3️⃣ Fallback local
    if not suggestions:
        local = local_fallback_lexicon()
        suggestions = [w for w in local if w.startswith(prefix)]

    # 4️⃣ Fuzzy (dernier recours)
    if not suggestions:
        suggestions = fuzzy_fallback(prefix, local_fallback_lexicon())

    return suggestions[:limit]
