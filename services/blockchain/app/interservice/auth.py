import grpc
from app.interservice.proto import auth_pb2, auth_pb2_grpc


def check_auth_token(
    *,
    auth_token: str
):
    channel = grpc.insecure_channel('auth-service:50051')
    stub = auth_pb2_grpc.AuthStub(channel)

    request = auth_pb2.TokenRequest(token=auth_token)
    response = stub.CheckToken(request)

    return response.valid
