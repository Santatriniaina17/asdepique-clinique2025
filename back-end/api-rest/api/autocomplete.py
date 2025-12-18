from flask import Blueprint, request, jsonify
from services.ngrams import train_bigrams, predict_with_prefix
from services.dictionnary import load_lexicon

autocomplete_bp = Blueprint("autocomplete", __name__)

LEXICON = load_lexicon()

with open("data/corpus.txt", "r", encoding="utf-8") as f:
    model = train_bigrams(f.read())

@autocomplete_bp.route("/autocomplete", methods=["POST"])
def autocomplete():
    text = request.json.get("text", "")
    suggestions = predict_with_prefix(text, model, LEXICON)

    return jsonify({
        "input": text,
        "suggestions": suggestions
    })
