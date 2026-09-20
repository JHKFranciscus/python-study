1. HTTP request의 세 위치
다음 세 값이 각각 path / query parameter / JSON body 중 어디에 들어가는 것이 자연스러운지 적고 이유를 간단히 설명하세요.

- 수정할 document의 id = path, 대상
- 현재 선택된 stage=interview filter = query parameter, 조회 조건
- PATCH로 새롭게 바꿀 stage=finished = JSON body, 변경할 data

2. fetch()와 HTTP 오류
server가 404 response를 반환했습니다.
이때 JavaScript의 fetch() Promise가 자동으로 rejected되는지 아닌지 먼저 답하세요.
그 다음 우리가 왜 response.ok를 확인하고 필요하면 throw new Error()를 사용했는지 설명하세요.

되지 않는다. response 자체는 정상적으로 전달이 되기 때문에 Promise는 fulfilled이어서 자동으로 rejected가 되지 않는다. response.ok는 HTTP status가 성공 범위인지를 나타내는 boolean이다. 그러므로 만약 필요하면 response.ok를 통하여 조건식을 세워서 throw new Error()를 통하여 reject 흐름으로 바꿀 수 있기 때문이다.

3. IP address와 port
다음을 각각 address / port / address+port(endpoint)로 분류하세요.

`127.0.0.1` = address
`5000` = port
`127.0.0.1:5000` = address+port(endpoint)

그리고 address와 port가 각각 무엇을 구분하는지 설명하세요.

address는 현재 실행중인 computer의 주소를 나타낸다.
port는 특정 process가 LISTEN하고 있는 number이고, OS가 그 port로 온 traffic을 해당 socket/process에 전달한다.

4. 127.0.0.1과 0.0.0.0
우리가 배포 과정에서 두 값을 모두 봤습니다.
다음 문장을 완성하세요.

127.0.0.1은 현재 computer 자기 자신을 가리키는 loopback address
0.0.0.0은 server가 사용 가능한 모든 network interface에서 connection을 받도록 bind하는 의미

정확한 의미를 설명하면 되고 문구를 외울 필요는 없습니다.

5. program / process
gunicorn이라는 program을 실행한 뒤 PID가 존재한다고 가정합니다.
program과 process의 차이를 설명하세요.
그리고 Gunicorn을 restart했을 때 PID가 바뀌는 이유도 연결해서 설명하세요.

program은 disk에 저장되어 있는 code를 뜻하고, process는 program을 실행하여 진행 중인 상태를 의미한다.
Gunicorn을 restart하면 실행 중이던 Gunicorn process는 종료되고, 새로운 Gunicorn process가 시작되므로, Gunicorn process ID가 변경되기 때문에 PID가 바뀌게 된다.

6. service와 process
다음 문장이 맞는지 틀린지 판단하고 이유를 설명하세요.
`"flask-study.service와 Gunicorn process는 완전히 같은 것이다."`
systemd, service, process 세 단어를 사용하세요.

틀렸다. flask-study.service와 Gunicorn process는 같은 것이 아니다.
systemd가 flask-study service를 관리하고, 그 service를 통해 Gunicorn을 실행하며,
Gunicorn 자체가 process로 실행되고, 그 Gunicorn process가 Flask application을 실행한다.

7. start와 enable
다음을 구분해서 설명하세요.

`systemctl start flask-study`
`systemctl enable flask-study`

특히 현재 실행 상태와 다음 reboot 이후라는 관점에서 차이를 설명하세요.

start는 지금 flask-study라는 service를 시작하는 것이고,
enable은 flask-study를 다음부터 EC2가 reboot 될 때 마다 동시에 시작되도록 한다.

8. 이번 주 CS 전체 연결

다음 상황에서 각 결과가 무엇을 증명하는지 설명하세요.
```
systemctl status flask-study
→ active
flask-study service가 현재 active 상태라는 것을 확인한다.

ss
→ 127.0.0.1:5000 LISTEN
어떤 process/socket이 127.0.0.1:5000에서 LISTEN 중이라는 것을 확인한다.

curl http://127.0.0.1:5000/
→ 정상 HTML
Gunicorn에서 Flask application으로 가는 경로가 정상적으로 동작한다는 것을 확인한다.

curl http://127.0.0.1/
→ 정상 HTML
Nginx가 :80에서 request를 받고 Gunicorn으로 전달한 뒤 Flask response가 돌아오는 경로가 정상이라는 것을 확인한다.
```
단순히 "정상이다"라고 하지 말고 각각:

service / process·port / Flask application / Nginx 경로

중 무엇을 확인하는 것인지 연결해서 답하세요.