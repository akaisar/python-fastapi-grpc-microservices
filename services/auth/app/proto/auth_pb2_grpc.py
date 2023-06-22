# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from app.proto import auth_pb2 as proto_dot_auth__pb2


class AuthStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckToken = channel.unary_unary(
                '/Auth/CheckToken',
                request_serializer=proto_dot_auth__pb2.TokenRequest.SerializeToString,
                response_deserializer=proto_dot_auth__pb2.TokenResponse.FromString,
                )


class AuthServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckToken': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckToken,
                    request_deserializer=proto_dot_auth__pb2.TokenRequest.FromString,
                    response_serializer=proto_dot_auth__pb2.TokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Auth(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Auth/CheckToken',
            proto_dot_auth__pb2.TokenRequest.SerializeToString,
            proto_dot_auth__pb2.TokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
