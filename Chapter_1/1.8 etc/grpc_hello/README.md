# gRPC Hello

gRPC가 소켓보다 한 단계 높은 추상화라는 점을 확인하기 위한 최소 예제다.

## 파일

- `helloworld.proto`: 서비스와 메시지 정의
- `server.py`: gRPC 서버
- `client.py`: gRPC 클라이언트
- `requirements.txt`: 필요한 패키지

## 준비

```bash
cd "Chapter_1/1.8 etc/grpc_hello"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 코드 생성

먼저 `.proto` 파일로부터 Python 코드를 생성해야 한다.

```bash
python3 -m grpc_tools.protoc \
  -I. \
  --python_out=. \
  --grpc_python_out=. \
  helloworld.proto
```

위 명령을 실행하면 아래 파일이 생긴다.

- `helloworld_pb2.py`
- `helloworld_pb2_grpc.py`

## 실행

터미널 1:

```bash
python3 server.py
```

터미널 2:

```bash
python3 client.py --name moeji
```

## 확인 포인트

- 직접 소켓 `send/recv`를 다루지 않아도 RPC 호출이 가능하다.
- `.proto`가 인터페이스 역할을 한다.
- 내부적으로는 네트워크 통신이 일어나지만, 애플리케이션 개발자는 함수 호출에 가까운 형태로 사용한다.
