# TCP Socket Chat

가장 기본적인 TCP 소켓 실습이다.

## 파일

- `server.py`: 여러 클라이언트를 받아 브로드캐스트하는 서버
- `client.py`: 서버에 접속해 메시지를 주고받는 클라이언트

## 실행

터미널 1:

```bash
cd "Chapter_1/1.8 etc/tcp_socket_chat"
python3 server.py
```

터미널 2:

```bash
cd "Chapter_1/1.8 etc/tcp_socket_chat"
python3 client.py --name alice
```

터미널 3:

```bash
cd "Chapter_1/1.8 etc/tcp_socket_chat"
python3 client.py --name bob
```

## 확인 포인트

- 클라이언트가 서버의 IP/포트로 접속한다.
- 서버는 각 클라이언트의 소켓을 유지한다.
- 한 클라이언트가 보낸 메시지가 다른 클라이언트에게 전달된다.

## 기본 주소

- host: `127.0.0.1`
- port: `9001`
