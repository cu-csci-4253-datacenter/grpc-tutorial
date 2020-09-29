from concurrent import futures
from PIL import Image
import io
import grpc
import hello_pb2
import hello_pb2_grpc

class Server(hello_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.count = 0
        
    def SayHello(self, request, context):
                print("Receive SayHello({})".format(request.name))

        return hello_pb2.HelloReply(
            message = "Hello, {}!".format(request.name) )
    
    
    def SayHelloAgain(self, request, context):
        self.count = self.count + 1
        return hello_pb2.HelloReply(
            message = "Hello #{}, {}".format(
                self.count, request.name))

def serve():    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:9999')
    server.start()
    server.wait_for_termination()

serve()