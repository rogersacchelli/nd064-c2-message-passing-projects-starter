import logging
from datetime import datetime, timedelta
from typing import Dict, List
from db_psql import get_close_connections
import udaconnect_pb2
import udaconnect_pb2_grpc
from datetime import datetime


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api-connectivity")

from concurrent import futures


class ConnectionService(udaconnect_pb2_grpc.udaConnectServicer):
    def getCloseConnections(self, request, method):
        
        print("got connection service request")
        connections = get_close_connections(person_id=request.id, start_date=request.start_date, end_date=request.end_date, \
                                             distance=request.distance)
        
        for connection in connections:
            print("Connection found: " + str(connection))
            response = udaconnect_pb2.ConnectionDataReply(id=connection[0], location_id = connection[1], \
                                                          coord_x=connection[2], coord_y=connection[3], creation_time=connection[4].strftime('%Y-%m-%d'))
            return response
        
        