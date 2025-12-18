from flask import Blueprint, request, jsonify
from services.sentiment_model import analyze_sentiment
from services.dictionnary import load_sentiment_words

sentiment_bp = Blueprint("sentiment", __name__)

# Chargement des mots positifs / négatifs au démarrage
POS_WORDS, NEG_WORDS = load_sentiment_words()

@sentiment_bp.route("/sentiment", methods=["POST"])
def sentiment():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = analyze_sentiment(text, POS_WORDS, NEG_WORDS)

    return jsonify({
        "text": text,
        "sentiment": result
    })
