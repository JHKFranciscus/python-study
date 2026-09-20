1. Code 변경과 service
local에서 app2.py를 수정하고 GitHub에 push했습니다.
EC2에서 git pull도 성공했습니다.
그런데 browser에서는 여전히 이전 화면이 나옵니다.
현재 다음 중 이미 최신 상태인 것과 아직 이전 상태일 수 있는 것을 각각 구분하고 이유를 설명하세요.

GitHub = 최신 상태, git push를 하면 변경된 데이터가 GitHub에 저장되기 때문이다.
EC2 disk의 app2.py = 최신상태, git pull은 별도의 설정이 없으면 가장 최신 GitHub에 저장되어 있는 것을 받아오기 때문이다.
실행 중 Gunicorn/Flask = 이전 상태, restart 전이므로 이전에 읽었던 Flask code로 계속 실행 중일 수 있다.
Nginx = 이전 version이라고 보는 대상이 아니다. Nginx는 application code version을 들고 있지 않다. restart할 필요도 없고, old/new application version이라는 식으로 구분하지도 않는다.

2. 장애 위치
다음 결과가 나왔습니다.

curl http://127.0.0.1:5000/
→ 정상

curl http://127.0.0.1/
→ 정상

Windows browser → Public IPv4
→ 접속 실패

이 상황에서 Flask code부터 다시 살펴보는 것이 비효율적인 이유와 가장 먼저 확인할 영역을 설명하세요.

Flask/Gunicorn과 Nginx 경유 요청까지 모두 성공했으므로 Flask code부터 확인하는 것은 비효율적이고, 외부 network 영역을 먼저 확인해야한다.

3. PATCH의 전체 위치
Browser에서 다음 request를 보냈습니다.
`PATCH /application/abc`
abc는 올바른 ObjectId가 아닙니다.

이 request가:
`Nginx → Gunicorn → Flask`
까지 간 뒤 어디에서 처음 application-level 오류로 판정되는지, 그리고 왜 MongoDB의 resource 존재 여부까지 검사할 필요가 없는지 설명하세요.

abc가 잘못된 ObjectId라는 판단은 Flask application code에서 ObjectId 변환을 시도할 때 처음 이루어지고, 여기서 400으로 끝나므로 MongoDB에서 document 존재 여부를 확인할 필요가 없다.

4. 동일값 PATCH
DB에 현재:
`stage = finished`
인 document가 있습니다.

client가 다시:
`stage = finished`
로 PATCH했습니다.

ObjectId도 정상이고 해당 document도 존재합니다.
matched_count와 modified_count가 각각 어떻게 나올 수 있는지, 그리고 이것을 404로 처리하면 안 되는 이유를 설명하세요.

matched_count는 1로 나올 수 있고, modified_count는 0으로 나올 수 있다.
이것은 해당 resource를 요구하는 route도 정상적으로 존재하고, 해당 resouce인 document도 정상적으로 존재하기 때문에 이것을 404로 처리하면 안 된다.

5. process와 endpoint
Gunicorn을 restart한 뒤:
`PID 4337, 4338`
이:
`PID 5001, 5002`
로 바뀌었습니다.

그런데 다음은 그대로입니다.
`127.0.0.1:5000`
PID가 바뀌었는데 endpoint는 왜 그대로일 수 있는지 설명하세요.

restart로 PID가 바뀌어도 새 Gunicorn process가 똑같이 127.0.0.1:5000을 LISTEN하도록 실행되므로 endpoint는 그대로일 수 있습니다.

6. 이번 주 전체 연결
아래 요소를 모두 사용해서 11주차에 만든 시스템을 하나의 설명으로 연결하세요.
`Git / EC2 disk / systemd / Gunicorn / Flask / MongoDB / Nginx / Public IPv4`

명령어를 나열하는 문제가 아닙니다.
code가 배포되고 → process로 실행되고 → 외부 request가 처리되고 → data가 저장되는 전체 구조가 드러나게 설명하면 됩니다.

systemd = Gunicorn service 관리
Gunicorn = Flask application
Flask = application logic 처리

GIT의 code를 EC2 disk로 배포한 뒤, 
systmed가 Gunicorn service를 관리하고
Gunicorn이 Flask application을 실행한다.
외부 request는 Public IPv4 → Nginx → Gunicorn → Flask 순서로 전달되고,
Flask가 application logic을 처리하면서 MongoDB에 data를 저장하거나 조회한다.


1. app2.py만 수정해서 배포했습니다. 왜 Gunicorn은 restart해야 하지만 Nginx는 restart하지 않아도 되는지 2문장 이내로 설명하세요.
Gunicorn은 Flask application code를 실제로 실행하고 있으므로 새 code를 읽게 하려면 restart가 필요하다.
Nginx는 application code를 실행하거나 version을 들고 있지 않고, request를 Gunicorn으로 전달하므로 Flask code만 바뀌었다면 resatart할 필요가 없다.

2. 아래 문장을 올바르게 고치세요.
`systemd가 EC2 disk의 Flask code를 process로 실행한다.`

systmed는 flask-study service를 관리하고, 그 service를 통해 Gunicorn을 실행하며,
Gunicorn이 EC2 disk의 Flask application code를 읽어 process로 실행한다.

3. PATCH /application/abc에서 abc가 ObjectId 형식 자체가 잘못됐다면,
어디에서 몇 번 HTTP status로 처리가 끝나며 왜 MongoDB 조회까지 가지 않는지 2문장 이내로 답하세요.

잘못된 ObjectId는 Flask에서 400으로 끝나므로 DB resource 조회까지 가지 않는다.