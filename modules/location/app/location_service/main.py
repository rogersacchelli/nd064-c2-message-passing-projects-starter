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
import logging
import sys

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(filename)s:%(asctime)s %(message)s', datefmt='%d/%m/%Y, %H:%M:%S,')

stdout_handler = logging.StreamHandler(sys.stdout)

stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)

api = Namespace("Location Entry", description="Connections via geolocation.")  # noqa

# kafka definitions
bootstrap_servers = 'kafka:9094'
kafka_topics = {'location':"location"}

try:
    kafka_producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    logging.info("kafka connected")
except:
    logging.error("Failed to connect to kafka")

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
            
            message = {"method":"POST", "location_id":location_id, "id":request_data['id'],\
                       "longitude":request_data["longitude"], "latitude":request_data["latitude"],"creation_time":request_data["creation_time"]}
                        
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

        

