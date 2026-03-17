import argparse

import grpc

try:
    import helloworld_pb2
    import helloworld_pb2_grpc
except ImportError as exc:
    raise SystemExit(
        "Generated files are missing. Run the protoc command in README.md first."
    ) from exc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="world")
    args = parser.parse_args()

    channel = grpc.insecure_channel("127.0.0.1:50051")
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    reply = stub.SayHello(helloworld_pb2.HelloRequest(name=args.name))
    print(reply.message)


if __name__ == "__main__":
    main()
