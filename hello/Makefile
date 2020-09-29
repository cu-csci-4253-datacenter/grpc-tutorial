#
# Generate gRPC 
#

grpc-client.py:
	protoc --python_out=. hello.proto
	python -m grpc_tools.protoc --proto_path=./ --python_out=./ --grpc_python_out=./ hello.proto

tools:
	pip install grpcio grpcio_tools

clean::
	-rm -f hello_pb2.py hello_pb2_grpc.py