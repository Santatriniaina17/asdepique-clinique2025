from flask import Blueprint, request, jsonify
from services.dictionnary import load_lexicon
from services.levenshtein import suggest_words

spellcheck_bp = Blueprint("spellcheck", __name__)
LEXICON = load_lexicon()

@spellcheck_bp.route("/spellcheck", methods=["POST"])
def spellcheck():
    data = request.json
    text = data["text"]

    corrections = {}
    for word in text.split():
        if word.lower() not in LEXICON:
            corrections[word] = suggest_words(word, LEXICON)

    return jsonify(corrections)
