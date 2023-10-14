
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def register_routes(api, person, root="api"):
    from app.person_service.main import api as udaconnect_api_person

    api.add_namespace(udaconnect_api_person, path=f"/api")
