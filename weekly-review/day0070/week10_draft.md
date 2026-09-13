# Flask + MongoDB CRUD 확장과 통합 — 10주차

이번 주에는 9주차에 만든 Flask + MongoDB CRUD를 기반으로 조건 조회, 날짜 범위, 정렬, PATCH, 수정 UI를 확장하고, 마지막에는 흩어져 있던 기능을 하나의 프로그램으로 통합했다.

주 후반에는 공부 기록 프로그램을 그대로 다시 만드는 대신 구조가 다른 작업 관리 프로그램을 빈 프로젝트에서 구현했다. 같은 코드를 기억하고 있는지가 아니라, 지금까지 배운 CRUD 흐름을 다른 요구사항에서도 다시 구성할 수 있는지 확인하기 위해서였다.

## 조건 조회 — 하나의 GET으로 처리하기

GET에서는 JavaScript의 filter 값을 query string으로 만들어 Flask에 전달하고, `request.args.get()`으로 받아 MongoDB 조회 조건으로 사용했다.

조건이 항상 모두 들어오는 것은 아니기 때문에 실제로 전달된 값만 query에 추가했다. 덕분에 다음 조회를 하나의 GET 구조에서 처리할 수 있었다.

- 전체 조회
- 과목별 조회
- 시작일 / 종료일 조회
- 날짜 범위 조회
- 여러 조건의 복합 조회
- 최신순 / 오래된순 정렬

## 부분 수정 — "값이 없는 것"과 "빈 값"은 다르다

PATCH에서는 정해진 field 하나만 수정하는 것이 아니라, request에 실제로 들어온 field만 골라서 수정하는 구조를 다뤘다.

이 과정에서 다음 두 경우의 차이가 특히 중요했다.

- `memo` field가 아예 없음 → 이번 PATCH에서는 memo를 수정하지 않는다
- `"memo": ""` → memo를 빈 문자열로 수정한다

그래서 optional field는 값의 truthy / falsy만 보고 처리하면 안 되는 경우가 있었다. 빈 문자열도 falsy지만, 실제로 전달된 수정 값일 수 있기 때문이다.

같은 이유로 HTML의 number input도 주의해야 했다. `.value`로 읽으면 값이 string이고 `Number("")`은 `0`이 되기 때문에, 빈 값인지 먼저 확인한 뒤 변환해야 했다.

## 수정 UI — 두 가지 구조

수정 UI는 두 가지 구조를 만들어 봤다.

처음에는 각 record가 자기 수정 input과 `_id`를 함께 가지는 구조를 사용했다.

이후에는 목록과 수정 영역을 분리해 **공용 수정 form + `editingId`** 구조로 바꿨다.

`editingId`는 어느 document를 수정할 것인지 기억하고, 공용 form의 DOM value는 어떤 값으로 바꿀 것인지를 담당했다.

## 통합한 프로그램 — 공부 기록 관리

주 후반에는 따로 구현했던 기능을 하나의 공부 기록 관리 프로그램으로 통합했다.

API의 큰 구조는 다음과 같다.

```text
POST   /record
GET    /records
PATCH  /record/<record_id>
DELETE /record/<record_id>
```

GET에서는 `subject`, `start_date`, `end_date`, `sort`를 optional query parameter로 사용했다.

수정이나 삭제가 끝난 뒤에는 현재 filter 값을 그대로 이용해 GET을 다시 보내도록 했다.

```text
PATCH / DELETE 성공
→ 현재 filter 값으로 GET 재조회
→ 최신 MongoDB data
→ render
```

덕분에 수정이나 삭제를 해도 사용자가 보고 있던 과목, 날짜, 정렬 조건을 유지할 수 있었다.

## 가장 많이 막힌 부분

이번 주에 가장 많이 막힌 것은 CRUD의 큰 구조 자체가 아니었다. 여러 기능을 합친 뒤에 **세부 계약과 state를 끝까지 일관되게 유지하는 것**이 더 어려웠다.

실제로 다음과 같은 오류가 있었다.

- API에서 정한 route와 실제 route가 달랐다
- DELETE의 HTTP method를 빠뜨렸다
- optional field의 존재 여부를 확인하기 전에 값을 읽었다
- 빈 문자열과 field 부재를 제대로 구분하지 못했다
- 비슷한 field를 반복해서 작성하다 다른 field 이름을 사용했다
- `response.json()` Promise를 return하지 않은 부분이 있었다
- 수정 완료 후 `editingId`를 초기화하지 않은 부분이 있었다

하나하나는 작아 보이지만 client, Flask, MongoDB가 연결된 상태에서는 전체 동작에 영향을 줬다.

## 원인 — 값이 어디에 있는지 끝까지 구분하지 못했다

공통적인 원인은 프로그램 안에 존재하는 여러 값의 위치와 역할을 끝까지 구분하지 못한 것이었다.

공부 기록 프로그램에서 state는 다음처럼 나뉘어 있었다.

- 실제 저장된 기록 → MongoDB
- 현재 조회 조건 → filter의 DOM value
- 현재 수정 값 → 공용 수정 form의 DOM value
- 현재 수정 대상 → `editingId`
- 현재 화면 목록 → 마지막 GET 결과를 기반으로 만들어진 DOM

MongoDB의 값이 바뀌어도 이미 만들어진 DOM이 저절로 바뀌지는 않는다.

그래서 DB를 수정하는 과정과 화면을 갱신하는 과정을 별개로 생각해야 했다.

## 직접 확인한 과정

문제가 생겼을 때는 한 request가 이동하는 전체 흐름을 처음부터 끝까지 따라갔다.

```text
DOM value
→ JavaScript
→ HTTP request
→ Flask
→ MongoDB
→ HTTP response
→ JavaScript
→ render
→ DOM
```

같은 request 안에서도 값이 어디에 실려 있느냐에 따라 Flask에서 읽는 방법이 달랐다.

- path → route function의 parameter
- query string → `request.args.get()`
- JSON body → `request.get_json()`

response에서도 각 값의 역할을 구분했다.

- `response.ok` → HTTP status가 성공 범위인지 확인
- `response.status` → 실제 status 번호
- `response.json()` → response body를 JavaScript 값으로 parsing

그리고 server가 `400`, `404` response를 정상적으로 반환한 경우에는 `fetch()`가 자동으로 rejected 되는 것이 아니라는 점도 확인했다. 필요한 경우에는 직접 `throw`해서 `.catch()` 흐름으로 보내야 했다.

## 수정한 방법

client와 server가 사용할 URL, HTTP method, query parameter, request body를 다시 맞췄다.

optional PATCH에서는 값의 truthy / falsy보다 field가 실제로 존재하는지를 먼저 판단했다.

작업이 끝난 뒤에는 관련된 state만 초기화하고, 유지해야 하는 filter state는 그대로 두었다.

그리고 PATCH나 DELETE가 성공하면 GET을 다시 보내 최신 MongoDB 상태를 화면에 반영했다.

다만 이 과정을 전부 완전히 독립적으로 해결했다고 기록하지는 않는다.

큰 CRUD 구조와 복합 조회, 공용 수정 form + `editingId` 구조는 직접 구성했지만, 통합 과정에서 나온 server 세부 오류 일부는 피드백을 받고 제시된 수정 코드를 적용했다.

## 주간 독립 재현 — 작업 관리 프로그램

주 마지막에는 공부 기록 프로그램을 다시 만드는 대신 작업 관리 프로그램을 빈 프로젝트에서 구현했다.

각 작업은 `title`, `priority`, `status`를 가지고, status와 priority filter, 정렬, POST / GET / PATCH / DELETE를 연결했다.

이번에는 공용 수정 form이나 `editingId`를 사용하지 않았다.

각 task를 render할 때 button의 event가 이미 해당 task의 `_id`와 현재 status를 가지고 있었기 때문이다.

- `task._id` → 어느 document를 수정할 것인가
- `task.status` → 다음 status는 무엇인가

이 두 값을 click 시점에 바로 사용할 수 있어서 수정 대상을 별도로 저장해 둘 필요가 없었다.

status는 다음 순서로 변경했다.

```text
todo → doing → done → todo
```

처음 구현에서는 최신순·오래된순을 `priority` 기준으로 정렬했고, status 변경 UI와 invalid priority의 HTTP status 처리에도 오류가 있었다.

피드백을 받아 수정한 뒤 browser에서 다시 검증했다.

따라서 이번 독립 재현은 **완전 독립 성공이 아니라 부분 독립 성공**으로 평가한다.

다만 공부 기록 프로그램과 구조가 다른 프로그램에서도 CRUD와 client-server 연결의 큰 흐름을 다시 구성할 수 있다는 것은 확인했다.

## 실제 실행 결과

공부 기록 관리 프로그램에서는 browser에서 다음 동작을 확인했다.

- 등록
- 조건별 조회와 복합 조회
- 날짜 범위 및 정렬
- 특정 document 수정
- 수정 취소
- 빈 memo로 수정
- filter를 유지한 상태에서 삭제와 재조회
- 잘못된 날짜 범위에 대한 `400` 처리

주간 독립 재현에서는 잘못된 `priority`와 `status`가 `400 Bad Request`로 처리되는 것을 확인했다.

또 ObjectId 형식은 정상이지만 실제 document가 존재하지 않는 경우에는 PATCH와 DELETE 모두 `404 Not Found`가 반환되는 것도 확인했다.

즉 잘못된 request와 존재하지 않는 resource를 HTTP status로 구분해 처리할 수 있었다.

## 아직 부족한 부분

지금 부족한 부분은 Flask + MongoDB CRUD의 큰 구조를 시작하지 못하는 것이 아니다.

코드가 길어졌을 때 다음과 같은 **세부 일관성을 끝까지 유지하는 부분**에서 아직 오류가 나온다.

- optional field의 존재 여부
- 빈 문자열과 field 부재의 차이
- API 계약과 실제 route의 일치
- HTTP method
- field 이름의 일관성
- HTTP status와 response body의 역할 구분
- Promise 처리
- 작업 후 필요한 state만 초기화하기
- sort / filter가 실제 요구사항과 같은 기준으로 동작하는지 확인하기

특히 이번 독립 재현에서 `.sort()` 코드는 정상적으로 실행됐지만 요구사항과 다른 field를 기준으로 정렬했다.

코드가 실행되는 것과 요구사항대로 동작하는 것은 다르다는 점을 다시 확인했다.

## 다음 주 목표

현재 4단계의 목표는 CRUD가 한 번 동작하는 것이 아니라, 빈 프로젝트에서도 다음 흐름을 스스로 구성할 수 있는 상태가 되는 것이다.

```text
Flask
→ MongoDB
→ API
→ JavaScript fetch()
→ CRUD
→ 조건 조회
→ response
→ render
```

이번 주에는 큰 구조를 다른 프로그램에서도 다시 만들 수 있다는 것을 확인했다.

남은 것은 같은 기능을 이유 없이 반복하는 것이 아니라, **API 계약과 state까지 포함해 긴 코드에서도 세부 일관성을 스스로 유지할 수 있는지 확인하는 것**이다.