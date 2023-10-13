from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api

def create_app(env=None):
    from app.routes import register_routes

    app = Flask(__name__)
    api = Api(app, title="Location Entry", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api, app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
