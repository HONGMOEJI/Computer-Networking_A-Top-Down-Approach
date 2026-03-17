from concurrent import futures

import grpc

try:
    import helloworld_pb2
    import helloworld_pb2_grpc
except ImportError as exc:
    raise SystemExit(
        "Generated files are missing. Run the protoc command in README.md first."
    ) from exc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message=f"Hello, {request.name}!")


def main() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    print("gRPC server listening on 127.0.0.1:50051")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("\nServer stopped.")


if __name__ == "__main__":
    main()
