import grpc
import udaconnect_pb2
import udaconnect_pb2_grpc

def run_grpc_client():

    start_date = '2018-01-01'
    end_date = '2022-12-30'
    distance = 500

    #with grpc.insecure_channel("udaconnect-connection:50051") as channel:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = udaconnect_pb2_grpc.udaConnectStub(channel=channel)
        response = stub.getCloseConnections(udaconnect_pb2.ConnectionDataRequest(id=5, start_date = start_date, end_date=end_date, distance=distance))
        for a in response.ConnectionDataResponse:
            print(a.id)

run_grpc_client()
