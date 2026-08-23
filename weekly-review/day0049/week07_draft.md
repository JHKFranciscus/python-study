# 7주차 주간 학습 기록 — JavaScript에서 Ajax까지, 웹의 흐름 연결하기

## 이번 주 3줄 요약

* JavaScript의 DOM과 event부터 객체·배열, JSON, jQuery, Ajax, HTTP까지 학습했다.
* 이번 주에 어려웠던 것은 새로운 문법 하나가 아니라, **코드 여러 부분이 연결될 때 무엇이 언제 실행되고 어떤 값이 이동하는지 판단하는 것**이었다.
* 그래서 이번 주에 얻은 기준은 **함수는 "지금 실행"과 "나중에 실행할 함수 등록"을 구분하고, 변수는 이름이 아니라 안에 들어 있는 값의 종류로 판단한다**는 것이다.

이번 주 전체를 하나로 연결하면 다음 흐름이었다.

```text
HTML 요소 → DOM / jQuery 객체 → 사용자 event → input 값
→ JavaScript 데이터 처리 → Ajax request → Server response
→ 배열과 객체에서 값 추출 → 조건 판단 → 화면 출력
```

각 개념을 따로 배우는 것에서 끝내지 않고, 한 기능 안에서 이 흐름을 연결하는 것이 이번 주의 중심이었다.

---

## 1. 이번 주에 배운 내용

**DOM과 event** — DOM으로 HTML 요소를 찾고 내용을 변경했다. 이 과정에서 함수 자체와 함수 호출을 구분하고, event가 발생했을 때 등록해 둔 callback이 실행되는 구조를 확인했다. 함수의 argument와 parameter, return, scope도 다시 연결해서 복습했다.

**객체와 배열** — 여러 객체가 들어 있는 배열에서 객체 하나를 선택하고, 다시 그 객체의 property 값에 접근하는 과정을 반복했다. `배열 → 객체 하나 → property 값` 단계로 구분했다.

**JSON** — JSON 문자열과 JavaScript의 객체·배열을 구분하고 `JSON.parse()`, `JSON.stringify()`로 변환했다. 이때 `JSON.parse()`는 원본 문자열을 바꾸는 것이 아니라 **새로운 JavaScript 값을 만들어 반환**한다는 점도 확인했다. 원본은 그대로 문자열로 남아 있기 때문에, 같은 데이터라도 parsing 전인지 후인지에 따라 변수 안의 값의 종류가 다르다.

**jQuery** — `$()`로 jQuery 객체를 만들고 `.val()`, `.text()`, `.on()`으로 input 값을 읽거나 화면의 text를 변경하고 event handler를 등록했다. `document.querySelector()`가 반환하는 DOM 요소와 `$()`가 반환하는 jQuery 객체도 구분했다.

**Ajax** — `$.ajax()`의 `url`, `type`, `data`, `success`를 사용해 JSON 데이터를 GET으로 조회하고, POST request에 데이터를 담아 보내는 코드도 작성했다.

**HTTP** — request와 response, GET과 POST, `200`, `404`, `405`, `500` status code를 학습하면서 지금까지 작성한 JavaScript 코드가 실제 Client와 Server의 통신과 어떻게 연결되는지 확인했다.

---

## 2. 이번 주에 만든 것

DOM과 event로 버튼 클릭 시 화면 내용을 바꾸는 기능부터 시작해, 객체와 배열에서 필요한 값을 찾는 코드, jQuery로 input 값을 읽어 출력하는 기능을 거쳐, `user.json`, `products.json`, `books.json` 등에 Ajax GET request를 보내는 연습까지 이어 붙였다.

이 모든 것을 하나로 합친 결과물이 **도서 조회 기능**이다. 주간 복습에서 답 코드를 보지 않고 처음부터 다시 구현했다.

사용자가 도서 번호를 입력하고 조회 버튼을 누르면 `books.json`의 배열에서 해당 도서 객체를 찾아 제목, 가격, 재고를 표시하고, 재고에 따라 구매 가능 / 품절을 구분한다.

**`books.json`** — 객체 3개가 들어 있는 배열이다. 별도의 id 없이 배열 순서 자체가 도서 번호가 된다.

```json
[
    { "title": "파이썬 입문",      "price": 15000, "stock": 3 },
    { "title": "자바스크립트 기초", "price": 20000, "stock": 0 },
    { "title": "웹 개발",         "price": 25000, "stock": 5 }
]
```

**HTML** — 값을 입력받을 input, event를 발생시킬 button, 결과를 출력할 `p` 요소를 준비했다.

```html
<input id="bookNumber" type="number" placeholder="도서번호">
<button id="findBook">조회</button>

<div>
    <p id="title">제목</p>
    <p id="price">가격</p>
    <p id="stock">재고</p>
    <p id="order">구매 상태</p>
</div>
```

**JavaScript** — 이번 주에 배운 event, jQuery, Ajax, 배열·객체 접근, 조건 판단이 전부 이 한 파일 안에서 연결된다.

```javascript
$("#findBook").on("click", function () {
    const bookNumber = Number($("#bookNumber").val());

    $.ajax({
        url: "books.json",
        type: "GET",
        success: function (response) {
            const book = response[bookNumber];

            $("#title").text(book.title);
            $("#price").text(book.price);
            $("#stock").text(book.stock);

            if (book.stock > 0) {
                $("#order").text("구매 가능");
            } else {
                $("#order").text("품절");
            }
        }
    });
});
```

맨 위에 적은 흐름이 이 코드 안에 그대로 들어 있다. `.on("click", ...)`이 event 등록, `Number($(...).val())`이 input 값 읽기와 자료형 변환, `$.ajax()`가 request, `function (response)`가 response를 받는 callback, `response[bookNumber]`가 배열에서 객체 하나를 꺼내는 부분, `.text()`가 화면 출력이다.

POST에서는 도서 번호와 주문 수량을 `data`에 담아 `/orders`로 보내는 요청도 구성했다.

---

## 3. 막혔던 부분과 해결 과정

### 3-1. 함수 자체와 함수 호출, callback의 실행 시점

`changeText`는 함수 자체이고 `changeText()`는 함수를 지금 호출하는 것인데, 처음에는 이 둘을 같은 것으로 봤다.

**원인** — 함수가 보이면 모두 같은 방식으로 실행된다고 생각했다. 일반 함수 호출은 내부 실행이 끝난 뒤 다음 코드로 이동하지만, Ajax에서는 request를 보낸 뒤 response를 기다리는 동안 다음 JavaScript 코드가 실행될 수 있다.

**확인** — 일반 함수 호출에서는 실행이 끝난 뒤 다음 줄로 이동하는 것을 확인했고, Ajax에서는 request를 보낸 뒤 response가 도착하기 전에 다음 코드가 실행될 수 있음을 직접 비교했다.

**정리** — event handler나 `success`에는 지금 실행할 결과가 아니라 **나중에 실행할 함수 자체를 등록**한다. 특히 `success`는 내가 직접 호출하는 함수가 아니라, Server의 response를 받은 뒤 jQuery가 응답 처리를 성공했을 때 호출하는 callback이다. 이때 처리된 응답 데이터는 jQuery가 argument로 전달하고, `response` parameter가 그 값을 받는다.

**여기서 이어진 문제 — 값을 "언제" 읽는가**

독립 재현에서는 처음에 도서 번호를 `success` callback 안에서 읽었다. 기능 자체는 동작했지만, response가 도착하기 전에 사용자가 input을 바꾸면 클릭했을 때와 다른 값을 읽을 수 있다.

그래서 최종 코드에서는 도서 번호를 click handler 첫 줄에서 읽어 확정해 두고, callback에서는 그 값을 사용하기만 하도록 바꿨다. 비동기 코드에서는 **어떤 값을 쓰는지뿐 아니라 그 값을 언제 읽고 확정하는지도 중요하다**는 것을 알게 됐다.

### 3-2. 배열과 객체 안의 값 추적, 그리고 자료형

`response`, `response[bookNumber]`, `response[bookNumber].stock`이 각각 배열 전체인지, 객체 하나인지, property 값인지를 코드마다 직접 확인해야 했다.

**원인** — 변수 이름만 보고 판단하면 안에 배열이 들어 있는지 객체 하나가 들어 있는지 놓치기 쉬웠다. `.val()`로 가져온 값도 화면에는 숫자로 보이지만 실제로는 문자열이었다.

**정리** — 값을 추적할 때 다음 순서를 계속 사용했다.

```text
현재 변수에 무엇이 들어 있는가
→ 배열인가 객체인가
→ 객체라면 어느 property에 접근하는가
→ 최종 값의 자료형은 무엇인가
```

숫자가 필요한 경우에는 `Number($("#bookNumber").val())`로 변환했다.

### 3-3. POST `/orders`에서 발생한 `405 Method Not Allowed`

도서 번호와 주문 수량을 `data`에 담아 `/orders`로 POST request를 보냈는데 `405 Method Not Allowed`가 발생했다.

**확인 순서** — ① 요청 코드 자체의 문제인지 확인 → ② request와 HTTP status 확인, request는 서버까지 전달되고 있었다 → ③ 경로와 method 조건을 바꾸어 재요청.

**결론** — 현재 사용 중인 **Live Server는 정적 파일 제공용 서버이기 때문에 `POST /orders`를 처리할 서버 로직이 없다**는 것을 확인했다. Client 코드가 잘못돼서 발생한 것이 아니었다.

이 과정에서 status code를 숫자만 외우지 않고 **Server가 request를 어떻게 판단했는지**를 기준으로 구분하게 됐다.

* `200` : 요청이 정상적으로 처리됨
* `404` : 요청한 resource를 찾지 못함
* `405` : 해당 resource에서 요청한 HTTP method를 허용하지 않음
* `500` : Server가 요청을 처리하는 과정에서 내부 오류 발생

또한 `data`, request, response, `success` callback을 처음에는 각각 따로 생각했지만, 이 과정을 거치면서 **Client가 request를 보내고 response가 돌아온 뒤 jQuery가 callback을 호출하는 하나의 흐름**으로 연결해서 보게 됐다.

### 3-4. 선언하지 않은 변수에 값을 대입한 문제

함수 안에서 `price = ...`처럼 선언 키워드 없이 값을 대입하는 코드를 작성해서 문제를 확인했다.

여기서 중요한 건 오류를 없애는 게 아니라 **어떤 키워드를 쓸지 판단하는 기준**이었다. 새로 만드는 변수면 선언이 필요하고, 이후 재할당하지 않으면 `const`, 재할당하면 `let`이다.

"에러가 났으니까 일단 `let`"이 아니라 **재할당 여부를 보고 고른다**는 순서로 정리했다. 실제로 도서 조회 코드의 `bookNumber`와 `book`은 한 번 값을 정한 뒤 바꾸지 않기 때문에 둘 다 `const`로 선언했다.

---

## 4. 실제 실행 결과

주간 복습에서 도서 조회 기능을 독립적으로 다시 구현하고, 실제 브라우저에서 도서 번호 `0`, `1`, `2`를 각각 입력해 확인했다.

* `0` 입력 → 파이썬 입문 / 15000 / 재고 3 / 구매 가능
* `1` 입력 → 자바스크립트 기초 / 20000 / 재고 0 / 품절
* `2` 입력 → 웹 개발 / 25000 / 재고 5 / 구매 가능

맨 위에 적은 흐름이 실제 코드에서 처음부터 끝까지 동작하는 것을 확인했다.

---

## 5. 아직 부족한 부분

* 개념을 각각 설명하는 것은 이전보다 나아졌지만, 여러 개념이 한 코드에 함께 들어오면 실행 순서를 바로 판단하지 못하는 경우가 아직 있다.
* 일반 함수와 비동기 작업을 구분하고, callback이 어느 시점에 실행되는지를 코드만 보고 빠르게 판단하는 연습이 더 필요하다.
* DOM 요소와 jQuery 객체, JSON 문자열과 JavaScript 객체·배열처럼 비슷하게 보이지만 실제 값의 종류가 다른 경우도 계속 구분해야 한다.
* 현재 도서 조회는 입력한 번호를 배열 index로 그대로 사용한다. `books.json`에 id가 없어서 가능한 방식이므로, 데이터에 id가 생기면 찾는 방법 자체가 달라져야 한다.
* 확인한 입력은 `0`, `1`, `2` 세 가지뿐이다. 배열에 없는 번호나 빈 입력이 들어왔을 때의 동작은 아직 확인하지 않았다.

---

## 6. 다음 주 목표

다음 주에 어떤 내용을 배우게 되든, 학습 방식에서는 다음 세 가지를 지킬 생각이다.

1. **정상 입력만 확인하고 끝내지 않는다.** 이번 주 도서 조회에서는 `0`, `1`, `2`만 넣어봤다. 다음 주에는 만든 기능마다 정상적이지 않은 입력도 최소 2개 넣어보고 결과를 기록한다.
2. **오류가 나면 바로 고치지 않고 원인 가설을 먼저 적는다.** 이번 주 `405`에서 코드 문제인지 → request가 전달되는지 → 서버 쪽 문제인지 순서로 좁혀갔던 방식이 실제로 통했다.
3. **변수를 이름이 아니라 안에 들어 있는 값으로 판단한다.** 이번 주에 만든 판단 기준을 새로 배우는 코드에도 그대로 적용한다.

### 미해결 과제

해결될 때까지 매주 기록에 남겨두고, 가능해지는 시점에 확인한다.

* **`POST /orders`가 `405`에서 멈춰 있다.** 현재 Live Server에는 POST를 처리할 서버 로직이 없다. 서버 쪽을 다룰 수 있게 되면 같은 요청이 `200`을 받는 것까지 확인한다.
* **배열에 없는 번호나 빈 입력이 들어왔을 때의 동작.** 지금 코드는 입력한 번호를 배열 index로 그대로 사용하기 때문에, 범위를 벗어난 값이 들어오면 어떻게 되는지 확인이 필요하다.

이번 주에 개별적으로 배운 JavaScript, DOM, 객체와 배열, JSON, jQuery, Ajax, HTTP를 다음 학습에서는 **Server까지 이어지는 하나의 흐름**으로 연결하는 것이 방향이다.

---

*학습 시간 기록 — 월~토 10:00~23:00, 일요일 11:00~18:00. 50분 학습 + 10분 휴식 사이클로 진행했고 식사 시간은 제외했다. 순수 학습 시간 기준 주 60시간.*
