1. 11주차에 새롭게 연결된 가장 큰 흐름을 3~5문장으로 설명하세요.
이번 주에는 local에서 만든 Flask + MongoDB application을 Git으로 EC2에 배포하고, Gunicorn·systemd·Nginx를 이용해 실제 server process로 운영한 뒤, code 변경 시 GitHub를 기준으로 다시 배포하는 흐름까지 연결했습니다.

2. 이번 주에 이해는 했지만 아직 독립 숙련이라고 보기 어려운 것을 2~4개 적으세요.
AWS/Linux/Git 명령을 상황에 맞게 자유롭게 선택하는 것, service/network 장애를 처음부터 독립 진단하는 것, Git working tree가 꼬였을 때 정리하는 것 등입니다.

3. 이번 주에 실제로 독립적으로 할 수 있게 된 것 또는 이전보다 연결이 명확해진 것을 2~4개 적으세요.
Git을 이용해 local code를 GitHub에 올리고 EC2에서 pull해 배포하는 기본 흐름, 그리고 Browser → Nginx → Gunicorn → Flask → MongoDB의 request 흐름은 이전보다 명확해졌습니다.

4. 다음 문장을 완성하세요.
11주차를 한 문장으로 요약하면:
Flask application을 EC2에 배포하고 Gunicorn·systemd·Nginx로 운영한 뒤 Git을 통해 재배포하는 기본 흐름을 연결했다.