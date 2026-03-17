# 1.8 etc

`1.8 etc`는 1장에서 배운 내용을 손으로 직접 확인해보기 위한 작은 실습 모음이다.

## 구성

- `tcp_socket_chat`
  - TCP 소켓으로 클라이언트와 서버가 어떻게 연결되는지 확인
- `http_server`
  - 브라우저와 `curl`이 실제로 HTTP 요청을 보내는 구조를 확인
- `grpc_hello`
  - gRPC가 소켓보다 더 높은 추상화라는 점을 확인

## 권장 순서

1. `tcp_socket_chat`
2. `http_server`
3. `grpc_hello`

## 공통 준비

- Python 3.10+
- 터미널 2개 이상
- 같은 PC에서 실행 가능

가상환경을 쓰고 싶다면 아래처럼 시작하면 된다.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 학습 포인트

- `tcp_socket_chat`
  - IP, 포트, 연결 수립, 송수신
- `http_server`
  - 요청 라인, 헤더, 응답 본문
- `grpc_hello`
  - `proto` 정의, 코드 생성, RPC 호출
