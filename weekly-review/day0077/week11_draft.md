# Flask application을 EC2 운영 환경까지 연결하다 — 11주차

이번 주에는 Flask + MongoDB로 만든 application을 local에서만 실행하는 단계를 넘어, AWS EC2에 배포하고 실제 server 형태로 운영하는 흐름을 처음 연결했다.

이번 주가 끝난 시점에 만들어진 구조는 다음과 같다.

```
Browser → Public IPv4:80 → Nginx → 127.0.0.1:5000 → Gunicorn → Flask → MongoDB
```

이 구조를 어떤 순서로 만들고 어떻게 검증했는지가 이번 기록의 중심이다.

## 주 초반 — Flask + MongoDB CRUD 복습

주 초반에는 기존 Flask + MongoDB CRUD를 다시 확인했다. GET / POST / PATCH / DELETE, validation, filter, 날짜 범위 조회, 정렬, partial PATCH를 복습하면서 request가 처리되고 MongoDB의 data가 변경된 뒤 다시 화면에 반영되는 흐름을 정리했다.

특히 세 가지를 다시 확인했다.

- ObjectId 형식이 잘못된 경우는 `400`, 형식은 정상이지만 document가 존재하지 않는 경우는 `404`로 구분된다.
- 동일한 값으로 PATCH하면 `matched_count = 1`, `modified_count = 0`이 될 수 있다. 조건에 맞는 document를 찾은 것과 실제로 값이 바뀐 것은 다르다.
- filter를 유지한 채 document의 값을 변경한 뒤 다시 GET하면, 조건에서 벗어난 document가 화면에서 사라질 수 있다.

세 번째가 특히 중요했다. MongoDB의 현재 상태와 DOM이 자동으로 연결되어 있는 것이 아니라, GET response를 기준으로 화면을 다시 만들기 때문이다.

## local에서 EC2로 — 배포의 시작

이렇게 local에서 동작하던 application을 이번 주의 주력 학습인 AWS 배포로 연결했다.

AWS에서 Ubuntu 24.04 기반 EC2 instance를 생성했다. 처음 SSH 접속에서는 Security Group의 SSH 허용 IP와 현재 접속 IP가 맞지 않아 timeout이 발생했고, inbound source를 수정한 뒤 접속에 성공했다. 이후 GitHub에 저장된 application code를 EC2로 가져와 실행했다.

이 과정에서 가장 먼저 확인한 것은 local computer와 EC2가 서로 다른 computer라는 점이었다. local의 `app.py`나 virtual environment가 EC2에 자동으로 존재하는 것이 아니었다.

처음에는 EC2 terminal에서 Flask application을 직접 실행하는 단계에서 시작했다. 이후 Gunicorn을 이용해 Flask application을 실행하고, 이를 `flask-study`라는 systemd service로 등록했다.

## systemd — terminal을 닫아도 계속 실행되는 구조

systemd를 적용하면서 terminal에서 직접 실행하던 application을 service 형태로 운영할 수 있게 되었다. terminal을 종료해도 Gunicorn process가 계속 실행되는 구조를 만들었다.

이때 service의 `ExecStart`는 virtual environment 안에 설치된 Gunicorn을 실행하도록 구성했다. 앞에서 확인한 대로 EC2에는 local의 virtual environment가 그대로 존재하지 않기 때문에, 실행할 Gunicorn의 위치를 service에 직접 지정해야 했다.

또한 service를 `enabled` 상태로 설정한 뒤 EC2를 reboot하고, Gunicorn과 Flask application이 다시 자동으로 실행되는 것까지 확인했다.

이 과정에서 각 도구의 역할도 구분했다.

- Flask는 application logic을 담당한다.
- Gunicorn은 Flask application을 실행하는 application server이다.
- systemd는 Gunicorn service의 시작, 중지, restart, 부팅 시 자동 실행을 관리한다.

## Nginx — 외부 request를 받는 앞단

그 다음에는 Gunicorn을 외부에 직접 노출하지 않고 `127.0.0.1:5000`에서만 LISTEN하도록 변경한 뒤, 앞단에 Nginx를 추가했다.

Nginx는 외부의 HTTP request를 `:80`에서 받고, 내부의 Gunicorn이 LISTEN하는 `127.0.0.1:5000`으로 전달한다. 설정에서 이 전달을 담당하는 부분은 다음 한 줄이다.

```
proxy_pass http://127.0.0.1:5000;
```

이에 맞춰 Security Group에서도 web application용 `:5000` 외부 진입을 제거하고, 외부에서는 Nginx를 통해서만 application에 접근하도록 구성했다.

그래서 최종 request 흐름은 다음과 같이 정리됐다.

```
Browser → Public IPv4:80 → Nginx → 127.0.0.1:5000 → Gunicorn → Flask → MongoDB
```

MongoDB 역시 같은 EC2 instance 내부에서 `mongod` service로 실행했고, Flask application은 `127.0.0.1:27017`을 통해 MongoDB와 통신하도록 구성했다.

Nginx 구성 이후에도 EC2를 reboot하고 각 service가 정상적으로 다시 올라오는지 확인했다. 단순히 한 번 browser에서 page가 열리는 것으로 끝내지 않고, reboot 이후에도 같은 구조가 유지되는지를 확인하면서 service 운영과 network 경로를 함께 보게 되었다.

## 재배포 — disk의 code를 바꾸는 것과 process가 새 code를 쓰는 것은 다르다

이번 주 후반에는 이미 운영 중인 application의 code를 수정한 뒤 다시 배포하는 과정도 진행했다.

local에서 수정한 code를 GitHub에 push한 뒤 EC2에서 pull했다. 그런데 disk의 code file이 변경된 것과, 현재 실행 중인 process가 새 code를 사용하는 것은 별개의 문제였다.

기존 Gunicorn process는 이전에 읽은 Flask application을 계속 실행하고 있을 수 있다. 그래서 Flask code를 새 version으로 바꾼 뒤에는 `flask-study` service를 restart해서, 새로운 Gunicorn process가 최신 code를 다시 읽도록 해야 했다. 실제로 restart 전후로 Gunicorn의 PID가 변경되는 것을 확인했다.

반면 Gunicorn의 PID가 바뀌어도 `127.0.0.1:5000`이라는 endpoint는 그대로 유지됐다. Nginx는 특정 Gunicorn PID를 찾아가는 것이 아니라, `127.0.0.1:5000`이라는 address와 port로 request를 전달하기 때문이다.

최종적으로 재배포 과정은 다음과 같이 연결됐다.

```
local code 수정 → 변경 확인 → Git commit → GitHub push → EC2 pull
→ flask-study restart → 내부 검증 → 외부 검증
```

## 검증을 단계별로 나누기

검증도 한 번에 하지 않고 단계별로 나눴다.

먼저 다음 명령으로 Nginx를 거치지 않고 Gunicorn과 Flask application이 정상적으로 동작하는지 확인했다.

```
curl http://127.0.0.1:5000/
```

그 다음 Nginx가 request를 받아 Gunicorn으로 전달하는 경로까지 확인했다.

```
curl http://127.0.0.1/
```

마지막으로 Windows browser에서 Public IPv4로 접속해, 외부 network에서도 application이 정상적으로 열리고 기존 MongoDB data가 유지되는 것을 확인했다.

이렇게 나누면 장애 위치도 기본적인 수준에서 구분할 수 있다.

- `127.0.0.1:5000` 요청부터 실패하면 Gunicorn / Flask 쪽을 먼저 확인한다.
- `:5000`은 정상인데 `:80`이 실패하면 Nginx 쪽을 확인한다.
- EC2 내부 `:80`까지 정상인데 외부 browser에서 실패하면 Public IPv4, Security Group, 외부 network 쪽을 확인한다.

이번 주 초의 SSH timeout도 port는 달랐지만 Security Group의 inbound rule이 원인이었다.

## Git — 운영 중인 server의 working tree

Git에서도 실제 운영 환경에서 고려해야 할 상황을 경험했다.

EC2의 working tree에는 과거 AWS 배포 과정에서 EC2에서 직접 수정한 file과, untracked 상태의 virtual environment directory가 남아 있었다. 이 상태로 바로 `git pull`을 하면 EC2에만 있는 수정 내용이 어떻게 되는지 알 수 없었다.

그래서 pull을 먼저 하지 않고 현재 상태를 확인하는 쪽을 선택했다. `git fetch`로 원격 상태를 가져온 뒤 `origin/main`과 EC2의 상태를 `diff`로 비교해서, EC2에만 있는 변경이 무엇인지 확인했다.

확인한 뒤에는 EC2에서 바로 고치지 않고, 필요한 수정 내용을 local repository에 정식으로 반영한 다음 다시 GitHub를 거쳐 배포했다. 배포 server에서 직접 고친 내용은 GitHub에 남지 않기 때문에, 기준을 GitHub 쪽에 두는 편이 맞다고 판단했다.

## 아직 부족한 부분

위의 장애 위치 구분은 각 연결 지점을 기준으로 문제 범위를 좁히는 기본적인 수준이다. 아무것도 보지 않고 AWS / Linux 운영 장애를 자유롭게 진단할 수 있는 수준으로 보지는 않는다.

Git 쪽도 마찬가지다. 위에서 `git fetch`와 `diff`로 상태를 비교하고 working tree를 정리한 과정은 안내를 참고해 진행했다. 따라서 이를 독립적인 Git 문제 해결 능력으로 과장하지 않는다.

AWS / Linux / Git 운영 전반을 독립적으로 다룰 수 있는 수준도 아니고, 각 명령어나 장애 상황을 아무것도 보지 않고 자유롭게 처리할 수 있는 상태도 아니다.

## 이번 주에 달라진 점

이번 주에 가장 크게 달라진 점은 Flask application을 단순히 Python code와 CRUD 기능으로만 보지 않게 된 것이다.

```
code → Git → EC2 disk → process → service
→ reverse proxy → network → application → database
```

이 전체가 연결된 하나의 시스템으로 보기 시작했다.

부족한 부분은 위에 적은 대로지만, local에서 작성한 Flask application code가 GitHub를 통해 EC2에 배포되고, systemd가 Gunicorn service를 관리하며, Gunicorn이 Flask application을 실행하고, Nginx가 외부 request를 내부 application으로 전달하며, Flask가 MongoDB와 통신하는 기본 구조를 직접 구성하고 검증했다.

또한 이미 운영 중인 application의 code를 수정했을 때 GitHub를 기준으로 EC2의 code를 갱신하고, process를 다시 실행한 뒤 내부와 외부에서 새 version이 실제로 적용됐는지 확인하는 재배포 흐름까지 경험했다.

11주차는 Flask + MongoDB application의 기능을 만드는 단계에서 한 걸음 더 나아가, 그 application이 실제 server에서 어떤 process와 service, network 구조를 거쳐 실행되고 운영되는지를 처음 연결한 한 주였다.
