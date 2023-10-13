from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def register_routes(api, root="api"):
    from app.location_service.main import api as udaconnect_api_location

    api.add_namespace(udaconnect_api_location, path=f"/api")
