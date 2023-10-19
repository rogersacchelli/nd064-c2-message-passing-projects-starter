import logging
from datetime import datetime, timedelta
from typing import Dict, List
from db_psql import get_close_connections
import udaconnect_pb2
import udaconnect_pb2_grpc
from udaconnect_pb2 import ConnectionDataReply
from datetime import datetime
import sys

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(filename)s:%(asctime)s %(message)s', datefmt='%d/%m/%Y, %H:%M:%S,')

stderr_handler = logging.StreamHandler(sys.stderr)

stderr_handler.setFormatter(formatter)
logger.addHandler(stderr_handler)


class ConnectionService(udaconnect_pb2_grpc.udaConnectServicer):
    def getCloseConnections(self, request, method):
        
        logger.info("got connection service request")
        connections = get_close_connections(person_id=request.id, start_date=request.start_date, end_date=request.end_date, \
                                             distance=request.distance)
        
        Connections = ConnectionDataReply()

        for connection in connections:
            logger.info("Connection found: " + str(connections))
            #resp = udaconnect_pb2.ConnectionData(id=connection[0], location_id = connection[1], \
            #                                            coord_x=connection[2], coord_y=connection[3], creation_time=connection[4].strftime('%Y-%m-%d'))
            Connections.ConnectionDataResponse.add(id=connection[0], location_id = connection[1], \
                                                        coord_x=connection[2], coord_y=connection[3], creation_time=connection[4].strftime('%Y-%m-%d'))
            
        return Connections
        
        