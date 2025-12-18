from flask import Blueprint, jsonify
from services.ontology import suggest

ontology_bp = Blueprint("ontology_api", __name__)

@ontology_bp.route("/ontology/suggest/<term>", methods=["GET"])
def ontology_suggest(term):
    result = suggest(term)
    return jsonify({
        "query": term,
        **result
    })
