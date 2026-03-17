# Minimal HTTP Server

브라우저나 `curl`이 보낸 HTTP 요청을 직접 확인하기 위한 최소 서버다.

## 파일

- `server.py`: 소켓 기반의 아주 작은 HTTP 서버

## 실행

```bash
cd "Chapter_2/2.1.2 프로세스 간 통신 실습/http_server"
python3 server.py
```

브라우저에서 아래 주소로 접속:

```text
http://127.0.0.1:8080/
```

또는:

```bash
curl -i http://127.0.0.1:8080/
```

## 확인 포인트

- 요청 라인(`GET / HTTP/1.1`)이 어떻게 생겼는지
- 헤더가 어떻게 들어오는지
- 서버가 상태 코드, 헤더, 본문을 포함해 응답을 만드는 방식
