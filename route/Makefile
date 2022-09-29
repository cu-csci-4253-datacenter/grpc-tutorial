#
# Generate gRPC 
#

grpc-client.py:
	protoc --python_out=. route_guide.proto
	python3 -m grpc_tools.protoc --proto_path=./ --python_out=./ --grpc_python_out=./ route_guide.proto

tools:
	pip3 install grpcio grpcio_tools

clean::
	-rm -f route_guide_pb2.py route_guide_pb2_grpc.py
	-rm -rf __pycache__
