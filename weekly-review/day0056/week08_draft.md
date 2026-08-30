# [8주차] Flask에서 브라우저와 서버가 데이터를 주고받는 흐름 이해하기

8주차에는 Flask를 이용해 **브라우저의 요청이 서버에 도착하고, 서버가 데이터를 처리한 뒤 다시 브라우저로 응답이 돌아오는 과정**을 집중적으로 공부했다.

이전까지는 HTML, JavaScript처럼 브라우저 안에서 일어나는 동작을 주로 다뤘다면, 이번 주부터는 브라우저 바깥의 서버까지 범위가 넓어졌다.

처음에는 route 하나를 만들어 문자열을 반환하는 정도였는데, 마지막에는 브라우저에서 입력한 값이 서버의 데이터를 바꾸고 그 결과가 다시 화면에 나오는 데까지 이어졌다.

이번 주에 다룬 것을 순서대로 정리하면 이렇다.

1. **route와 HTTP request** — 요청한 URL과 실행되는 함수가 어떻게 연결되는가
2. **render_template과 Jinja** — HTML은 누가, 언제 완성하는가
3. **HTML form과 GET / POST** — 데이터는 어디에 실리는가
4. **서버 메모리** — request가 끝나도 데이터가 남는 이유
5. **Flask와 JavaScript / Ajax** — 연결 지점이 늘어날 때 생기는 일

이번 주를 지나면서 가장 크게 달라진 점은 Flask 코드를 문법 하나하나로 보는 대신,

**request → route → 함수 실행 → 데이터 처리 → return → response**

라는 하나의 흐름으로 보기 시작했다는 것이다.

---

## 1. route와 HTTP request

브라우저가 Flask 서버에 URL을 요청하면, Flask는 먼저 요청받은 URL path와 일치하는 route를 찾는다.

```python
@app.route("/hello/<name>")
def hello(name):
    return f"안녕하세요, {name}!"
```

브라우저가 `/hello/minsu`를 요청하면 URL의 동적 부분인 `minsu`가 함수의 argument로 전달되고, `name` parameter가 그 값을 받는다.

전체 흐름은 이렇다.

```text
GET /hello/minsu
→ /hello/<name> route와 연결
→ name에 "minsu" 전달
→ 함수 실행
→ return 값 생성
→ Flask가 HTTP Response 생성
→ 브라우저로 전달
```

처음에는 `return`이 브라우저로 데이터를 직접 보내는 것이라고 생각했다. 하지만 내가 작성한 함수는 응답에 들어갈 내용을 만들어 넘길 뿐이고, **그 값을 가지고 실제 HTTP Response를 만드는 쪽은 Flask**였다.

---

## 2. render_template과 Jinja — HTML은 누가, 언제 완성하는가

이번 주에는 `render_template()`을 이용해서 Python의 데이터를 HTML에 전달했다.

```python
return render_template(
    "profile.html",
    name=username
)
```

HTML에서는 Jinja 문법으로 전달받은 값을 사용할 수 있다.

```html
<h1>{{ name }}</h1>
```

여기서 중요한 것은 **Jinja가 브라우저에서 실행되는 것이 아니라는 점**이다. `render_template()`이 호출되면 Jinja가 서버에서 HTML 문자열을 완성하고, 브라우저는 이미 완성된 HTML을 받는다.

JavaScript도 HTML 파일 안에 작성할 수 있다 보니, 처음에는 Jinja와 실행 시점이 헷갈리기도 했다. 하지만 두 가지는 실행되는 위치부터 다르다.

```text
Jinja
→ 서버에서 실행
→ Response를 보내기 전에 처리

JavaScript
→ 브라우저에서 실행
→ Response를 받은 뒤 처리
```

브라우저가 받은 HTML에는 이미 Jinja가 처리된 결과만 남아 있는 셈이다. 이 구분은 뒤에서 Flask와 JavaScript를 함께 사용할 때 특히 중요했다.

---

## 3. HTML form과 GET / POST — 데이터는 어디에 실리는가

HTML form을 Flask와 연결하면서 GET과 POST 요청도 직접 다뤘다.

GET 요청에서는 form 데이터가 URL의 query string에 포함된다.

```html
<form action="/search" method="get">
    <input name="keyword">
</form>
```

`flask`를 입력하면 요청은 `/search?keyword=flask` 형태가 되고, Flask에서는 `request.args`로 값을 읽는다.

```python
keyword = request.args.get("keyword")
```

반면 POST 요청에서는 form 데이터가 request body에 실린다. Flask에서는 request.form으로 값을 읽는다.

```html
<form action="/add" method="post">
    <input name="title">
</form>
```

```python
title = request.form.get("title")
```

정리하면 이렇게 된다.

| 방식 | 데이터가 실리는 곳 | Flask에서 읽는 방법 |
| --- | --- | --- |
| GET | URL query string | `request.args` |
| POST | request body | `request.form` |

데이터가 실리는 위치뿐 아니라 용도도 나뉜다. 일반적으로 GET은 서버의 데이터를 **조회**하는 요청에, POST는 서버의 데이터를 추가하거나 **변경**하는 요청에 사용한다.

다만 이건 Flask가 강제하는 규칙이라기보다 약속에 가깝다. GET을 처리하는 route 안에서 데이터를 변경하는 코드를 써도 동작 자체는 한다. 그런데도 이 구분을 지키는 이유는, GET 요청은 값이 URL에 그대로 남기 때문에 주소창에 노출되고 새로고침이나 뒤로가기만으로도 쉽게 다시 실행되기 때문이다. 조회는 여러 번 반복돼도 상관없지만, 데이터를 변경하는 요청이 그렇게 반복되면 문제가 된다.

그리고 이 과정에서 HTML의 `name`과 Flask에서 사용하는 key가 서로 정확히 일치해야 한다는 것도 알게 됐다. 위처럼 `<input name="title">`이라고 썼다면 Flask에서도 `request.form.get("title")`로, 같은 이름으로 읽어야 한다.

단순한 문자열 하나지만 HTML과 Python이라는 서로 다른 파일 사이의 연결 지점이기 때문에, 이름이 다르면 데이터 흐름 자체가 끊어진다. 이 "이름 맞추기"는 뒤에서 Ajax까지 붙이면서 계속 신경 쓰게 되는 부분이었다.

---

## 4. 서버 메모리 — request는 끝나도 서버는 계속 살아 있다

이번 주 후반에는 서버에 데이터를 두고, 요청을 통해 그 데이터를 변경하거나 조회하는 구조를 만들었다.

예를 들어 서버가 다음 데이터를 가지고 있다고 하자.

```python
tasks = [
    {"title": "공부", "done": False}
]
```

POST 요청을 처리하는 과정에서 `done`을 `True`로 바꾼 뒤, 별도의 GET 요청으로 `tasks`를 조회하면 변경된 값이 그대로 보인다.

처음에는 POST와 GET이 서로 다른 요청인데 왜 데이터가 이어지는지가 헷갈렸다.

정리하면,

**서로 완전히 다른 HTTP request라도 Flask 서버 프로세스가 계속 실행 중인 동안에는 그 프로세스의 메모리에 존재하는 같은 데이터를 사용할 수 있다.**

따라서 POST request가 끝났다고 해서 서버 메모리의 변수가 초기화되는 것은 아니다.

```text
서버 실행 → tasks 생성
POST 요청 → tasks 변경 → 요청 종료 (서버 프로세스는 계속 실행)
GET 요청 → 변경된 tasks 조회
```

반대로 서버 프로세스를 완전히 종료하면 메모리의 변경 내용은 사라진다. 다시 실행하면 Python 파일에 작성된 초기 코드부터 실행되므로 데이터도 처음 상태로 돌아간다.

이번 과정을 통해 **메모리에만 존재하는 데이터와 파일이나 DB 등에 영구 저장되는 데이터는 다르다**는 것도 실제 동작으로 확인할 수 있었다. request 하나의 수명과 서버 프로세스의 수명이 다르다는 것도 이때 처음 구분이 됐다.

---

## 5. Flask와 JavaScript / Ajax — 연결 지점이 늘어날 때

후반에는 Flask와 jQuery Ajax도 함께 사용했다.

서버가 HTML 전체를 다시 보내는 방법뿐 아니라, JSON 데이터를 반환하고 JavaScript가 이를 받아 브라우저의 DOM을 변경하는 방식도 연습했다.

이 과정에서는 Flask 코드만 작성할 때보다 확인해야 할 연결 지점이 훨씬 많아졌다.

```text
HTML
↕
JavaScript
↕
HTTP request
↕
Flask
↕
Python 데이터
```

HTML의 `id`와 JavaScript selector가 일치해야 하고, form의 `name`과 Flask에서 읽는 key가 일치해야 하며, 서버가 반환한 JSON 구조와 JavaScript가 기대하는 구조도 맞아야 했다.

앞에서 이름 하나만 어긋나도 흐름이 끊긴다고 정리했는데, 그런 지점이 한 번에 여러 곳으로 늘어난 셈이다.

그중에서도 `this` 때문에 이번 주에 가장 오래 헤맸다.

### 이번 주에 가장 오래 붙잡았던 문제 — parameter 이름을 `this`로 쓴 경우

**상황**

JavaScript로 만든 여러 기능이 동시에 아무 반응도 하지 않았다. 처음에는 기능마다 각각 문제가 있는 줄 알고 하나씩 들여다봤다.

**원인**

버튼을 눌렀을 때 클릭된 요소를 함수에 넘기려고 HTML을 이렇게 작성했다.

```html
<button onclick="changeDone(this)">
```

여기까지는 문제가 없다. `this`를 argument로 넘기는 것은 가능하다.

문제는 그것을 받는 JavaScript 쪽이었다.

```javascript
function changeDone(this) {
    ...
}
```

받는 parameter 이름까지 `this`로 썼는데, JavaScript에서 `this`는 일반 변수 이름이 아니라 예약된 키워드라서 parameter 이름으로 쓸 수 없다. 그래서 JavaScript가 이 파일을 읽는 단계에서 바로 SyntaxError를 냈다.

```text
function changeDone(this)
→ SyntaxError
→ JavaScript 파일 파싱 실패
→ 파일 아래쪽 코드도 실행되지 않음
→ 다른 함수들도 정의되지 않은 것처럼 보임
```

parameter 이름만 바꾸니 해결됐다.

```javascript
function changeDone(el) {
    ...
}
```

**정리**

HTML에서 `this`를 argument로 넘기는 것은 되지만, JavaScript 함수의 parameter 이름을 `this`로 만드는 것은 안 된다. 넘어온 값을 받는 parameter는 내가 정하는 이름이고, HTML에서 넘긴 `this`와 이름이 같을 필요가 없다.

그리고 여러 기능이 한꺼번에 고장 난 것처럼 보인다고 해서 원인도 기능 개수만큼 있는 것은 아니었다. 파일이 파싱 단계에서 멈추면 그 아래 코드는 전부 실행되지 않기 때문에, 실제 원인은 한 곳일 수 있다.

그래서 JavaScript가 전혀 작동하지 않을 때는 기능을 하나씩 고치기 전에 **console에서 가장 먼저 발생한 오류부터 확인해야 한다**는 점을 배웠다.

---

## 주간 복습 — JavaScript 없이 Flask + HTML form + Jinja로 다시 구현하기

주간 복습에서는 이번 주 내용을 한 번에 연결해보기 위해, 서버 메모리의 데이터를 조회하고 변경하는 프로그램을 만들었다.

첫 번째 시도에서는 할 일 관리 프로그램을 만들었는데, 필요 이상으로 Ajax 구조를 추가했다. 최종적으로 동작하도록 수정하기는 했지만, 원래 독립 재현 조건이었던 **JavaScript/Ajax 없이 Flask + HTML form + Jinja로 구현하기**를 만족하지 못했기 때문에 다시 진행했다.

두 번째로는 다음과 같은 점수 데이터를 이용한 프로그램을 만들었다.

```python
scores = {
    "minsu": 70,
    "jisu": 85
}
```

구현한 기능은 다음과 같다.

* 전체 이름과 점수 표시
* 새로운 이름과 점수 추가
* 기존 사용자의 점수 수정
* 이름으로 특정 사용자 검색
* 데이터를 변경한 뒤 현재 전체 목록 다시 표시

이번에는 JavaScript 없이 HTML form과 GET/POST 요청만 이용했다.

새로운 데이터를 추가할 때는 POST 요청의 body에서 `request.form`으로 값을 읽었고, 특정 사용자를 검색할 때는 GET 요청의 query string을 `request.args`로 읽었다. 앞에서 정리한 표를 그대로 사용한 셈이다.

그리고 서버의 `scores`가 변경되면 다시

```python
render_template("index.html", scores=scores)
```

형태로 현재 데이터를 Jinja에 전달해 화면을 새로 만들었다.

### 구현 중 만난 문제 — template에 값을 다시 전달하지 않은 경우

구현 중 같은 HTML을 다시 렌더링하면서 `scores`를 전달하지 않아, Jinja에서 변수를 찾지 못하는 문제가 한 번 발생했다.

이를 통해 이전 request에서 template에 전달했던 값이 다음 request에도 자동으로 남아 있는 것이 아니라, **`render_template()`을 호출할 때마다 해당 template에서 필요한 값을 다시 전달해야 한다**는 것을 확인했다.

4번에서 정리한 "서버 메모리의 데이터는 남아 있다"와는 다른 이야기다. 데이터 자체는 서버 프로세스 안에 그대로 있지만, 그 데이터를 template으로 넘기는 일은 요청마다 새로 해줘야 한다.

최종적으로는 Flask, HTML form, Jinja와 서버 메모리만으로 추가·수정·검색·전체 목록 표시가 모두 동작하는 것을 확인했다.

---

## 8주차를 마치며

이번 주는 새로운 Flask 문법을 외우는 것보다 **서로 떨어져 있는 코드가 어떻게 하나의 요청 흐름으로 연결되는지 이해하는 과정**이 더 중요했다.

처음에는 GET, POST, Jinja, Ajax 같은 개념이 각각 따로 느껴졌지만, 결국 모두 브라우저와 서버 사이에서 데이터를 어떻게 주고받을지를 결정하는 방법이라는 점이 조금씩 연결되기 시작했다.

아직 HTML·Flask·Jinja·JavaScript처럼 여러 영역이 동시에 등장하면 변수 이름이나 실행 시점을 혼동하는 경우가 있다. 이번 주에 겪은 `this` 문제도 결국 그 연장선이었다.

그래서 다음 학습에서는 코드를 바로 작성하기 전에 먼저

```text
어떤 request가 필요한가?
GET인가 POST인가?
데이터는 어디에 실리는가?
Flask에서는 무엇으로 읽는가?
서버 데이터가 변경되는가?
누가 최종 화면을 만드는가?
```

를 판단하는 습관을 계속 연습하려고 한다.

8주차는 Flask의 기능을 많이 배운 한 주이기도 했지만, 그보다 **브라우저에서 시작한 요청이 서버를 거쳐 다시 화면으로 돌아오는 전체 과정을 처음으로 하나의 흐름으로 연결해 본 한 주**였다.
