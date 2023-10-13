from app.location_service.schemas import (
    LocationSchema,
)
from app.location_service.models import Location
from app.location_service.services import LocationService

from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
from kafka import KafkaProducer

import json


api = Namespace("Location Entry", description="Connections via geolocation.")  # noqa

# kafka definitions
bootstrap_servers = 'localhost:9092'
kafka_topics = {'location':"location"}
kafka_producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# TODO: This needs better exception handling

@api.route("/locations")     
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self, location_id):
        request_data = request.get_json()
        if request_data:
            
            message = {"method":"POST","location_id":location_id, "data":request_data}            
            print("got request data: " + str(message))
            message = json.dumps(message).encode('utf-8')
            try:
                kafka_producer.send(kafka_topics['location'], message)
                return json.dumps({'success':True}), 200, {'ContentType':'*/*'}
            except:
                return json.dumps({'success':False}), 500, {'ContentType':'*/*'}

    @responds(schema=LocationSchema)
    def get(self, location_id):
        location: Location = LocationService.retrieve(location_id)
        return location

        

