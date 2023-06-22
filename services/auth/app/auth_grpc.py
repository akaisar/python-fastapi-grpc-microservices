import grpc
import threading
from concurrent import futures
from app.proto import auth_pb2, auth_pb2_grpc
from app.core.security import verify_access_token

class AuthService(auth_pb2_grpc.AuthServicer):
    def CheckToken(self, request, context):
        # Add your logic to check the authentication token against the test microservice
        token = request.token
        # Perform authentication token validation here
        is_valid = verify_access_token(token=token)

        return auth_pb2.TokenResponse(valid=is_valid)

grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
auth_pb2_grpc.add_AuthServicer_to_server(AuthService(), grpc_server)
grpc_server.add_insecure_port('0.0.0.0:50051')  # Replace with the desired port


def start_grpc_server():
    grpc_server.start()
    grpc_server.wait_for_termination()

def start_grpc_server_in_thread():
    grpc_thread = threading.Thread(target=start_grpc_server)
    grpc_thread.start()
