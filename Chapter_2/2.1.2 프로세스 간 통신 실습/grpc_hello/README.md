# gRPC Hello

gRPC가 소켓보다 한 단계 높은 추상화라는 점을 확인하기 위한 최소 예제다.

## 파일

- `helloworld.proto`: 서비스와 메시지 정의
- `server.py`: gRPC 서버
- `client.py`: gRPC 클라이언트
- `requirements.txt`: 필요한 패키지

## 준비

```bash
cd "Chapter_2/2.1.2 프로세스 간 통신 실습/grpc_hello"
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

## `.proto`가 하는 일

`helloworld.proto`는 이 gRPC 예제의 **인터페이스 설계도**다.

```proto
syntax = "proto3";

package helloworld;

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply);
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
```

여기서 각각의 의미는 다음과 같다.

- `service Greeter`
  - gRPC 서비스 이름
- `rpc SayHello (HelloRequest) returns (HelloReply)`
  - `SayHello`라는 RPC 메서드를 정의
  - 요청 타입은 `HelloRequest`
  - 응답 타입은 `HelloReply`
- `message`
  - 요청/응답 데이터 구조를 정의

## `= 1`은 무엇인가?

예를 들어 아래 부분을 보자.

```proto
message HelloRequest {
  string name = 1;
}
```

여기서 `= 1`은 `return 1` 같은 의미가 아니라, **필드 번호(field number)** 다.

즉,

- `name` 필드의 번호가 `1`
- `message` 필드의 번호도 `1`

라는 뜻이다.

프로토콜 버퍼는 데이터를 직렬화할 때 필드 이름 그 자체를 계속 보내는 것이 아니라,  
**필드 번호를 기준으로 인코딩**한다.

즉 내부적으로는 대략 이런 느낌이다.

- `1번 필드에 "moeji"라는 문자열이 들어있음`
- `1번 필드에 "Hello, moeji!"라는 문자열이 들어있음`

그래서 필드 번호는 다음 이유로 중요하다.

- 바이너리 직렬화를 효율적으로 하기 위해
- 메시지 구조가 나중에 확장되어도 호환성을 유지하기 위해

예를 들어 이렇게 확장할 수 있다.

```proto
message HelloRequest {
  string name = 1;
  int32 age = 2;
}
```

그러면 protobuf는

- `1번 필드` = `name`
- `2번 필드` = `age`

로 해석한다.

중요한 점은 **한번 사용한 필드 번호는 함부로 바꾸면 안 된다**는 것이다.  
번호를 바꾸면 이전 버전과의 호환성이 깨질 수 있다.

## 코드 생성 후 무슨 일이 생기나?

`grpc_tools.protoc`를 실행하면 두 종류의 코드가 생성된다.

### 1. `helloworld_pb2.py`

이 파일에는 protobuf 메시지 타입이 들어 있다.

즉,

- `HelloRequest`
- `HelloReply`

같은 Python 객체를 만들 수 있게 된다.

예를 들어 클라이언트는 이런 객체를 만든다.

```python
helloworld_pb2.HelloRequest(name=args.name)
```

이 객체는 나중에 gRPC가 내부적으로 protobuf 바이너리 형식으로 직렬화해서 전송한다.

### 2. `helloworld_pb2_grpc.py`

이 파일에는 gRPC 서비스 관련 코드가 들어 있다.

예를 들면:

- 서버가 구현해야 하는 `GreeterServicer`
- 클라이언트가 호출할 `GreeterStub`
- 서버에 서비스를 등록하는 함수

즉, 이 파일은 **"이 RPC 서비스를 어떻게 호출하고 어떻게 구현할지"** 를 Python 코드 형태로 만들어준다.

## 실제 호출 흐름

이 예제에서 실제 흐름은 아래와 같다.

### 1. 클라이언트가 요청 객체를 만든다.

클라이언트 코드:

```python
reply = stub.SayHello(helloworld_pb2.HelloRequest(name=args.name))
```

여기서 일어나는 일:

1. `HelloRequest(name="moeji")` 객체 생성
2. gRPC stub이 이 객체를 protobuf 바이너리로 직렬화
3. 직렬화된 데이터를 서버로 전송

### 2. 서버가 요청을 받아 메서드를 실행한다.

서버 코드:

```python
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message=f"Hello, {request.name}!")
```

여기서 일어나는 일:

1. gRPC 서버가 들어온 바이트 데이터를 받음
2. protobuf 규칙에 따라 `HelloRequest` 객체로 역직렬화
3. `SayHello()` 메서드 호출
4. 서버는 `HelloReply` 객체를 만들어 반환

### 3. 응답이 다시 직렬화되어 클라이언트로 돌아간다.

서버가 반환한:

```python
helloworld_pb2.HelloReply(message="Hello, moeji!")
```

는 다시 protobuf 형식으로 직렬화되어 네트워크를 통해 전송된다.

클라이언트는 이를 `HelloReply` 객체로 받아서:

```python
print(reply.message)
```

처럼 사용할 수 있다.

## 한 번에 정리하면

gRPC의 흐름은 아래처럼 이해하면 된다.

1. `.proto`에 서비스와 메시지 구조를 정의한다.
2. `protoc`가 Python 코드를 생성한다.
3. 클라이언트는 `Stub`를 통해 함수를 호출하듯 RPC를 호출한다.
4. 내부적으로는 요청 객체가 protobuf 바이너리로 직렬화되어 전송된다.
5. 서버는 이를 역직렬화해 메서드를 실행한다.
6. 응답 객체를 다시 직렬화해서 클라이언트로 돌려보낸다.

즉, 개발자가 보기에는 **함수 호출처럼 보이지만**, 실제 내부에서는 **메시지 직렬화/역직렬화와 네트워크 전송**이 일어나고 있는 것이다.

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
