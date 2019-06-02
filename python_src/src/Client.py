import src.simple_pb2
import src.simple_pb2_grpc
import grpc
import logging


if __name__ == "__main__":

    def request_reply_test():
        port = 8801
        with grpc.insecure_channel('localhost:' + str(port)) as channel:
            client =  src.simple_pb2_grpc.SimpleServiceStub(channel)
            print(client.RequestReply.future)
            response = client.RequestReply(src.simple_pb2.SimpleRequest(requestMessage='hello there'))
            print(response)


    class Client(object):
        def __init__(self, host, port):
            self.channel = grpc.insecure_channel(host + ':' + str(port))
            self.stub = src.simple_pb2_grpc.SimpleServiceStub(self.channel)

        def __del__(self):
            del self.channel

        def RequestReply(self, **kwargs):
            return self.stub.RequestReply(src.simple_pb2.SimpleRequest(**kwargs))


    logging.basicConfig()
    # client = Client('localhost', 8801)
    # print(client.RequestReply(requestMessage='hello there'))

    request_reply_test()