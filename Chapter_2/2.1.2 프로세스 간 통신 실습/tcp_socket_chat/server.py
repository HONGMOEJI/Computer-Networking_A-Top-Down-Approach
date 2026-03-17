import socket
import threading

HOST = "127.0.0.1"
PORT = 9001
BUFFER_SIZE = 4096

clients = []
clients_lock = threading.Lock()


def broadcast(message: bytes, sender: socket.socket) -> None:
    with clients_lock:
        dead = []
        for client in clients:
            if client is sender:
                continue
            try:
                client.sendall(message)
            except OSError:
                dead.append(client)
        for client in dead:
            if client in clients:
                clients.remove(client)


def handle_client(conn: socket.socket, addr) -> None:
    print(f"[connected] {addr}")
    with clients_lock:
        clients.append(conn)
    try:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            text = data.decode("utf-8", errors="replace").strip()
            print(f"[recv] {addr}: {text}")
            broadcast(data, conn)
    finally:
        with clients_lock:
            if conn in clients:
                clients.remove(conn)
        conn.close()
        print(f"[disconnected] {addr}")


def main() -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"TCP chat server listening on {HOST}:{PORT}")

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.close()


if __name__ == "__main__":
    main()
