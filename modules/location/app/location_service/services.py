import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app.location_service import db
from app.location_service.models import Location
from app.location_service.schemas import LocationSchema

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api-logging")

class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location