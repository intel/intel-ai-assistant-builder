import grpc
import superbuilder_middleware_pb2 as sb
import superbuilder_middleware_pb2_grpc as sbg

def check_pybackend(stub):
    try:
        print("Calling superbuilder service APIs: SayHelloPyllm()")
        helloPyllmResponse = stub.SayHelloPyllm(sb.SayHelloRequest(
            name='SuperBuilder Python Clients!'))
        if not helloPyllmResponse.message:
            return False
        print("Server replied: " + helloPyllmResponse.message)
        return True
    except grpc.RpcError as e:
        print(f"gRPC error: {e.details()}")
        return False

def connect(channel):
    success = False
    stub = None

    try:
        grpc.channel_ready_future(channel).result(timeout=15)  # Wait until the channel is ready
        stub = sbg.SuperBuilderStub(channel)
    except grpc.RpcError as e:
        print(f"gRPC error: {e.details()}")
    except grpc.FutureTimeoutError:
        print("gRPC channel connection busy or missing")
    else:
        success = True
    
    return success, stub


def disconnect(stub, channel):
    if stub is not None:
        stub.ClientDisconnected(sb.ClientDisconnectedRequest())
    if channel is not None:
        channel.close()