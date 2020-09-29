#!/usr/bin/env python3
from concurrent import futures
from PIL import Image
import io
import grpc
import hello_pb2
import hello_pb2_grpc

class Server(hello_pb2_grpc.GreeterServicer):
    count = 0
    def __init__(self):
        Server.count = 0
        print("Initializing Server instance")
    
    def SayHello(self, request, context):
        print("Receive SayHello({})".format(request.name))
        return hello_pb2.HelloReply(
            message = "Hello, {}!".format(request.name) )
    
    
    def SayHelloAgain(self, request, context):
        Server.count = Server.count + 1
        print("Receive SayHelloAgain({})".format(request.name))
        return hello_pb2.HelloReply(
            message = "Hello #{}, {}".format(
                Server.count, request.name))


def serve():    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:9999')
    server.start()
    server.wait_for_termination()

serve()