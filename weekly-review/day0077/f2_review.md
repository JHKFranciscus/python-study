1. browser에서 PATCH /application/<id> request를 보냈다고 가정합니다. 아래 요소를 사용해서 전체 흐름을 순서대로 연결하세요.
browser / Nginx / Gunicorn / Flask route / MongoDB / JSON response

browser는 Public IPv4를 통하여 Nginx에게 데이터를 전송하고 Nginx가 그 데이터를 정해진 port로 연결하여 전송하면 Gunicorn이 그 port를 LISTEN하여 데이터를 받고, Flask route가 실행되고, MongoDB에 준다. 그러면 MongoDB는 DB 처리 결과를 Flask에 주고, Flask가 jsonify() 등으로 HTTP response를 구성한다.

2. Flask의 request.get_json()은 다음 중 어디에서 동작합니까?
- Nginx
- Gunicorn
- Flask application code
- MongoDB

그리고 그 이유를 한 문장으로 설명하세요.

Flask application code
이것은 Flask server가 받은 JSON 형식의 request를 역직렬화하여 Flask가 사용할 수 있도록 만드는 것이기 때문이다.

3. ObjectId 변환에 실패해서 400을 반환하는 판단은 어디에서 이루어집니까?
Flask applicaiton code

4. 다음 두 상황의 차이를 설명하세요.
ObjectId 문자열 형식 자체가 잘못됨
ObjectId 형식은 맞지만 DB에 해당 document가 없음

각각 400 / 404 중 무엇인지도 함께 적으세요.
전자는 400으로 request가 잘못된 경우이다.
후자는 404로 요청한 resource 자체가 잘못되거나 없는 경우이다.

5. 사용자가 stage=interview filter를 적용한 상태에서 어떤 항목을 finished로 PATCH했습니다. PATCH는 성공했는데 화면에서 그 항목이 사라졌습니다. 이것이 오류가 아닐 수 있는 이유를 설명하세요.
PATCH로 document.stage가 interview에서 finished로 바뀌었기 때문에, 기존 stage=interview filter로 다시 조회하면 그 document가 결과에서 빠져 화면에서 사라질 수 있다. filter가 바뀐 것이 아니라 document의 값이 filter의 조건과 맞지 않게 바뀐 것이기 때문이다.

6. PATCH 후 화면을 최신 상태로 만들기 위해 왜 다시 GET request를 보내는지 설명하세요.
답변에는 반드시 DB source of truth와 DOM이라는 단어를 넣어주세요.
MongoDB의 현재 상태가 source of truth이고, DOM은 마지막 GET response를 기반으로 만들어진 화면 표현이다. DB가 source of truth이고, DOM은 마지막으로 받아서 렌더링한 화면 상태일 뿐이므로 DB 변경이 DOM에 자동으로 반영되지 않는다.