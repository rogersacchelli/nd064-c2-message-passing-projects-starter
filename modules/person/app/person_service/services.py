import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app.person_service import db
from app.person_service.models import Person
from app.person_service.schemas import PersonSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api-person")


class PersonService:
    @staticmethod
    def create(person: Dict) -> Person:
        new_person = Person()
        new_person.first_name = person["first_name"]
        new_person.last_name = person["last_name"]
        new_person.company_name = person["company_name"]

        db.session.add(new_person)
        db.session.commit()

        return new_person

    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        return db.session.query(Person).all()
    
    @staticmethod
    def delete(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        
        if person:
            # Delete the person from the database session
            db.session.delete(person)
            db.session.commit()
            return person
        else:
            return None