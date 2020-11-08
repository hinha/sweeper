# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import instagram_pb2 as proto_dot_instagram__pb2


class instagramStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamRequest = channel.unary_unary(
                '/instagram.instagram/StreamRequest',
                request_serializer=proto_dot_instagram__pb2.instagramRequest.SerializeToString,
                response_deserializer=proto_dot_instagram__pb2.instagramResponse.FromString,
                )


class instagramServicer(object):
    """Missing associated documentation comment in .proto file"""

    def StreamRequest(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_instagramServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.StreamRequest,
                    request_deserializer=proto_dot_instagram__pb2.instagramRequest.FromString,
                    response_serializer=proto_dot_instagram__pb2.instagramResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'instagram.instagram', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class instagram(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def StreamRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/instagram.instagram/StreamRequest',
            proto_dot_instagram__pb2.instagramRequest.SerializeToString,
            proto_dot_instagram__pb2.instagramResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
