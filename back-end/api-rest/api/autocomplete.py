from flask import Blueprint, request, jsonify
from services.ngrams import predict_on_demand

autocomplete_bp = Blueprint("autocomplete", __name__)

@autocomplete_bp.route("/autocomplete", methods=["POST"])
def autocomplete():
    text = request.json.get("text", "")

    suggestions = predict_on_demand(text)

    return jsonify({
        "input": text,
        "strategy": "on-demand prefixsearch + fallback + fuzzy",
        "suggestions": suggestions
    })
