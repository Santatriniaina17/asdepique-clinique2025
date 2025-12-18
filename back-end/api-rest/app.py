from flask import Flask
from flask_cors import CORS
from api.autocomplete import autocomplete_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(autocomplete_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"status": "Flask NLP API running"}

if __name__ == "__main__":
    app.run(debug=True)
