from datetime import datetime

from app.udaconnect.models import Location
from app.udaconnect.schemas import (
    LocationSchema,
)


from flask import request, jsonify
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
from kafka import KafkaProducer

import json

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa

# kafka definitions
bootstrap_servers = 'kafka:9092'
kafka_topics = {'location':"location"}
kafka_producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# TODO: This needs better exception handling

@api.route("/locations")     
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self, location_id) -> Location:
        #kafka_message = {"location_id":location_id}
        # post message to kafka brocker. 
        #kafka_producer.send(kafka_topics['location'], bytes(str(kafka_message), 'utf-8'))
        # TODO: send message to kafka
        return "ok post"

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        # TODO: Handle using gRPC
        return "ok get"
