from datetime import datetime
import grpc
import udaconnect_pb2
import udaconnect_pb2_grpc
from concurrent import futures

from services import ConnectionService

# from typing import Optional, List

import logging, sys

GRPC_SERVER_PORT = 50051


def run_grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    udaconnect_pb2_grpc.add_udaConnectServicer_to_server(ConnectionService(), server)
    server.add_insecure_port('[::]:' + str(GRPC_SERVER_PORT))  # Listen on port 50051
    
    logging.debug("Starting gRPC server on port:" + str(GRPC_SERVER_PORT))
    server.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run_grpc_server()

