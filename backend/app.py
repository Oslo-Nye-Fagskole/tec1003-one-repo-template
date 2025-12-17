import random
from flask import Flask, jsonify
from flask_cors import CORS

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(JSON_SORT_KEYS=False)

    CORS(app)

    @app.route("/api/mood", methods=["GET"])
    def get_mood():
        moods = ["Happy!", "Sad :(", "Whatever..."]
        return jsonify({
            "mood": random.choice(moods)
        })

    return app

app = create_app()