from datetime import datetime

from app.person_service.models import Person, Connection, Location
from app.person_service import udaconnect_pb2
from app.person_service import udaconnect_pb2_grpc

from app.person_service.schemas import (
    PersonSchema, ConnectionSchema
)

from app.person_service.services import PersonService
from flask import request, jsonify
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List, Dict

import json
import grpc
import logging

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Persons.")  # noqa


# TODO: This needs better exception handling


# TODO: Review /persons
@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        payload = request.get_json()
        new_person: Person = PersonService.create(payload)
        return new_person

    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
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
        #start_date = datetime.strptime(request.args["start_date"], DATE_FORMAT)
        #end_date = datetime.strftime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)
        print("----- getConnection ----")
        print("Received Request id {person_id} - start: {end_date} - end: {end_date}".format(\
            person_id=person_id, start_date=request.args["end_date"], end_date=request.args["end_date"]))
        # TODO: Get Connection via gRPC Call
        # udaconnect-connection.default.svc.cluster.local

        person_map: Dict[str, Person] = {person.id: person for person in PersonService.retrieve_all()}
        result: List[Connection] = []
        print("querying grpc server")
        with grpc.insecure_channel("udaconnect-connection:50051") as channel:
        #with grpc.insecure_channel("localhost:50051") as channel:
            stub = udaconnect_pb2_grpc.udaConnectStub(channel=channel)
            connection = stub.getCloseConnections(udaconnect_pb2.ConnectionDataRequest(id=int(person_id), \
                        start_date=request.args["start_date"], end_date=request.args["end_date"], distance=int(request.args["distance"])))
            for response in connection.ConnectionDataResponse:
                print("response -> id:{id} - location:{location} - time:{time}".format(\
                    id=response.id, location=response.location_id, time=response.creation_time))
                location = Location(
                        id=response.location_id,
                        person_id=response.id,
                        creation_time=datetime.strptime(response.creation_time, DATE_FORMAT),
                    )
                location.set_wkt_with_coords(response.coord_x, response.coord_y)

                result.append(Connection(
                                person=person_map[response.id], location=location,
                            ))
                
        return result
