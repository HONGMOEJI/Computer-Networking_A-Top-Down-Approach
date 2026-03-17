import argparse
import socket
import threading

HOST = "127.0.0.1"
PORT = 9001
BUFFER_SIZE = 4096


def receive_loop(sock: socket.socket) -> None:
    while True:
        try:
            data = sock.recv(BUFFER_SIZE)
        except OSError:
            break
        if not data:
            break
        print(data.decode("utf-8", errors="replace").strip())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="guest")
    args = parser.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    thread = threading.Thread(target=receive_loop, args=(sock,), daemon=True)
    thread.start()

    print(f"Connected to {HOST}:{PORT} as {args.name}")
    print("Type messages and press Enter. Ctrl+C to exit.")

    try:
        while True:
            line = input()
            message = f"{args.name}: {line}\n"
            sock.sendall(message.encode("utf-8"))
    except (KeyboardInterrupt, EOFError):
        print("\nDisconnected.")
    finally:
        sock.close()


if __name__ == "__main__":
    main()
