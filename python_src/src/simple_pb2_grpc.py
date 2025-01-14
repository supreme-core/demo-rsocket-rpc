# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import simple_pb2 as simple__pb2


class SimpleServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RequestReply = channel.unary_unary(
        '/com.example.demorsocketrpc.SimpleService/RequestReply',
        request_serializer=simple__pb2.SimpleRequest.SerializeToString,
        response_deserializer=simple__pb2.SimpleResponse.FromString,
        )


class SimpleServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RequestReply(self, request, context):
    """Request / Response
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SimpleServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RequestReply': grpc.unary_unary_rpc_method_handler(
          servicer.RequestReply,
          request_deserializer=simple__pb2.SimpleRequest.FromString,
          response_serializer=simple__pb2.SimpleResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.example.demorsocketrpc.SimpleService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
