1. 현재 운영 중인 application의 전체 흐름을 아래 시작점부터 끝까지 완성하세요.
Windows browser → Public IPv4:80 → Nginx → 126.0.0.1:5000 → Gunicorn → Flask → MongoDB

2. 다음 각각의 역할을 한 문장씩 설명하세요.
Flask / Gunicorn / systemd / Nginx / MongoDB
Python으로 web application의 route와 application logic을 작성하는 web framework
Falsk applilcation을 실제 process로 실행하고 HTTP request를 받아 Flask에 전달하는 application server(Flask를 실행한다.)
Linux의 service manager로, Gunicorn service의 시작, 중지, restart, 부팅 시 자동 시작 등을 관리한다.(service/process를 관리한다.)
외부 reqeust를 먼저 받고 내부의 Gunicorn으로 전달하는 web server / reverse proxy
application의 데이터를 저장하고 조회, 수정, 삭제하는 database server

3. 다음 문장이 왜 틀렸는지 설명하세요.
“app2.py를 수정했으므로 실행 중인 Flask application도 자동으로 새 code로 바뀐다.”
app2.py는 disk에 존재하는 code file이고,
실행 중인 Flask application은 메모리 상에서 진행 중인 process 이므로,
별도의 설정을 해두지 않는 이상 실행 중인 Flask application이 진행 중인 process는 수정 이전의 code를 사용한다.

4. Gunicorn을 restart하면 PID가 바뀌는데도 왜 Nginx의
proxy_pass http://127.0.0.1:5000;
은 그대로 사용할 수 있습니까?
Gunicorn이 5000번 port를 LISTEN하기 때문이다.

5. 다음 네 가지를 서로 구분해서 설명하세요.
127.0.0.1 / Public IPv4 / 5000 / Gunicorn
현재 computer 자기 자신을 가리키는 loopback address
외부 network에서 EC2 instance에 접근하기 위해 사용하는 public IP address
현재 실행 중인 process가 request를 받는 port number
Flask application을 실행하면서 request를 받아 Flask에 전달하는 application server/process

6. 아래 세 상황에서 가장 먼저 확인할 영역을 각각 적으세요.
A. curl http://127.0.0.1:5000/ 실패
B. :5000 성공, curl http://127.0.0.1/ 실패
C. EC2 내부 :80 성공, Windows browser 실패
Gunicorn / Flask
Nginx
Network

7. local에서 Flask code 하나만 수정하여 새 version을 배포한다고 가정합니다. 명령어 자체가 아니라 작업 단계의 순서를 처음부터 외부 검증까지 작성하세요.
local PC에서 Flask code 수정
변경 내용 검증
git commit
git push
EC2에서 git pull
Flask application restart
EC2 내부에서 curl로 확인
EC2 외부에서 browser로 확인


1. EC2를 reboot했다. flask-study가 enabled라면 systemd / Gunicorn / Flask 중 무엇이 무엇을 다시 실행시키는지 설명하세요.
systemd가 Gunicorn을 실행, 재시작 등을 관리하므로, systemd가 Guniconr을 다시 실행시킨다. 그 후 Gunicorn이 Flask application을 실행한다.

2. Nginx는 정상인데 Gunicorn process가 완전히 죽었다. Windows browser에서 request가 들어오면 어디까지 도달하고, 어느 연결에서 실패할지 설명하세요.
Nginx가 127.0.0.1:5000으로 연결하려 하지만, 그 port를 LISTEN하는 Gunicorn process가 없어서 연결이 실패한다.

3. MongoDB가 죽었지만 Nginx와 Gunicorn은 정상이다. 이것은 curl :5000 자체가 반드시 connection 실패한다는 뜻입니까? 왜 그런지 설명하세요.
아니다. :5000은 Gunicorn이 LISTEN하는 port인 것이고 Gunicorn이 Flask application을 실행하여 MongoDB와 connection하는 것이지 connection이 실패한다는 뜻은 아니다. Gunicorn의 network connection 자체는 성공할 수 있다.

4. 개발자가 app2.py만 수정하고 EC2에서 git pull까지 했지만 flask-study를 restart하지 않았다.
다음 중 disk와 실행 중 process가 각각 어느 version을 가지고 있는지 설명하세요.

EC2 disk의 app2.py = disk는 수정된 version을 가지고 있고,
실행 중 Gunicorn/Flask = process는 수정되지 않은 version을 가지고 있다.

5. 다음 표현을 각각 올바른 범주에 넣으세요.

Nginx / 127.0.0.1 / 80 / Gunicorn / systemd

범주: revesr proxy & web server / address / port / application server(process) / serviece manager

address / port / application server(process) / service manager / reverse proxy(web server)