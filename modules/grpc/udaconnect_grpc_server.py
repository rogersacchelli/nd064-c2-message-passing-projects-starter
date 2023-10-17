import grpc

import udaconnect_pb2
import udaconnect_pb2_grpc

from concurrent import futures


class getConnection(udaconnect_pb2_grpc.udaConnectServicer):
    def getConnections(self, request, method):
        response = udaconnect_pb2.ConnectionDataReply(id=10)
        return response

def run_grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    udaconnect_pb2_grpc.add_udaConnectServicer_to_server(getConnection(), server)
    server.add_insecure_port('[::]:50051')  # Listen on port 50051

    print("Starting gRPC server on port 50051...")
    server.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run_grpc_server()