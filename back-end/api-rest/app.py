from flask import Flask
from flask_cors import CORS

from api.autocomplete import autocomplete_bp
from api.ontology import ontology_bp


def create_app():
    app = Flask(__name__)

    # CORS (frontend React / Quill)
    CORS(app)

    # Blueprints API
    app.register_blueprint(autocomplete_bp, url_prefix="/api")
    app.register_blueprint(ontology_bp, url_prefix="/api")

    @app.route("/")
    def home():
        return {"status": "Flask NLP API running"}

    return app


# 🔑 IMPORTANT POUR RENDER / GUNICORN
app = create_app()
