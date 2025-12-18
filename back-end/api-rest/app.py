from flask import Flask
from api.spellcheck import spellcheck_bp
from api.autocomplete import autocomplete_bp
from api.sentiment import sentiment_bp

app = Flask(__name__)

app.register_blueprint(spellcheck_bp, url_prefix="/api")
app.register_blueprint(autocomplete_bp, url_prefix="/api")
app.register_blueprint(sentiment_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"status": "Flask NLP API running"}

if __name__ == "__main__":
    app.run(debug=True)
