from datetime import datetime

from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.schemas import (
    ConnectionSchema,
    LocationSchema,
    PersonSchema,
)
from app.udaconnect.services import ConnectionService, LocationService, PersonService
from flask import request, jsonify
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
from kafka import KafkaProducer

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa

# kafka definitions
bootstrap_servers = 'kafka:9092'
kafka_topics = {'person':"person", 'location':"location"}
kafka_producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# TODO: This needs better exception handling

@api.route("/locations")     
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        data = request.get_json()
        # post message to kafka brocker. 
        #kafka_producer.send(kafka_topics['location'], value=data.encode("UTF-8"))
        location: Location = LocationService.create(request.get_json())
        return jsonify(success=True)

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        # TODO: Handle using gRPC
        location: Location = LocationService.retrieve(location_id)
        return location


@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        payload = request.get_json()
        #kafka_producer.send(kafka_topics['person'], value=payload.encode("UTF-8"))
        new_person: Person = PersonService.create(payload)
        return jsonify(success=True)

    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        #kafka_producer.send(kafka_topics['person'], value=persons.encode("UTF-8"))
        persons: List[Person] = PersonService.retrieve_all()
        return persons


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return person


@api.route("/persons/<person_id>/connection")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        start_date: datetime = datetime.strptime(
            request.args["start_date"], DATE_FORMAT
        )
        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)

        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )
        return results
