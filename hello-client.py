from __future__ import print_function
import requests
import json
import time
import sys
import grpc

import hello_pb2
import hello_pb2_grpc

if len(sys.argv) < 1:
    print("usage: {} host".format(sys.argv[0]))
    sys.exit(1)
host = sys.argv[1]


channel = grpc.insecure_channel('{}:9999'.format(host))
stub = hello_pb2_grpc.GreeterStub(channel)



while (True):
    msg = input("Say hello or quit! ")
    if msg == "quit":
        break
    
    hreq = hello_pb2.HelloRequest(name = msg)
    reply = stub.SayHello(hreq)
    print("They say ", reply.message)
    
    msg = input("Say hello again! ")
    hreq.name = msg
    reply = stub.SayHelloAgain(hreq)
    print("They say ", reply.message)