import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8080
BUFFER_SIZE = 4096


def build_response() -> bytes:
    body = f"""
    <html>
      <head><title>Minimal HTTP Server</title></head>
      <body>
        <h1>HTTP server is running</h1>
        <p>Current time: {datetime.now().isoformat()}</p>
      </body>
    </html>
    """.strip()
    headers = [
        "HTTP/1.1 200 OK",
        "Content-Type: text/html; charset=utf-8",
        f"Content-Length: {len(body.encode('utf-8'))}",
        "Connection: close",
        "",
        "",
    ]
    return ("\r\n".join(headers) + body).encode("utf-8")


def main() -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"HTTP server listening on http://{HOST}:{PORT}")

    try:
        while True:
            conn, addr = server.accept()
            with conn:
                request = conn.recv(BUFFER_SIZE).decode("utf-8", errors="replace")
                print(f"\n[request from {addr}]")
                print(request)
                conn.sendall(build_response())
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.close()


if __name__ == "__main__":
    main()
