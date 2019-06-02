import concurrent.futures
import time
import logging
import grpc

import src.simple_pb2
import src.simple_pb2_grpc


class RequestReplyServicer(src.simple_pb2_grpc.SimpleServiceServicer):
    def RequestReply(self, request, context):
        print('recv ' + str(request))
        return src.simple_pb2.SimpleResponse(responseMessage='Echo ' + request.requestMessage)


class RequestReplyServe():
    def __init__(self, port):
        print(request_reply_serve.__name__ + ' started on port ' + str(port))
        self.port = port
        self.server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
        src.simple_pb2_grpc.add_SimpleServiceServicer_to_server(RequestReplyServicer(), self.server)
        self.server.add_insecure_port('[::]:' + str(port))

    def __del__(self):
        self.server.stop(0)
        del self.port
        del self.server

    def start(self):
        self.server.start()


def request_reply_serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    src.simple_pb2_grpc.add_SimpleServiceServicer_to_server(RequestReplyServicer(), server)
    server.add_insecure_port('[::]:8801')
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


def request_reply_serve1():
    try:
        RequestReplyServe(8801).start()
        while True:
            time.sleep(1)
    except:
        pass




if __name__ == "__main__":
    logging.basicConfig()
    request_reply_serve()
    # request_reply_serve1()