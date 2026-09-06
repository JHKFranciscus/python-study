# 9주차 학습 기록 — Flask와 MongoDB에서 브라우저 CRUD까지 연결하기

## 한 줄 요약

이번 주에는 Flask에서 MongoDB를 다루는 것에서 시작해, JavaScript `fetch()`로 브라우저에서 직접 조회·등록·수정·삭제까지 연결했다.

**이번 주 핵심 3줄**

1. 등록 하나에도 값은 `HTML input → DOM element → .value → JavaScript object → JSON string → HTTP request → Python dictionary → MongoDB document` 순으로 형태를 바꾼다.
2. `_id`는 MongoDB 안에서는 ObjectId, URL·JSON에서는 string이라서 방향에 따라 두 번 변환해야 한다.
3. CRUD가 끝나면 화면을 직접 고치지 않고, 다시 GET을 보내 DB의 현재 상태로 화면을 만든다.

---

## 1. 이번 주 진행 흐름

한 주 동안 CRUD를 네 단계로 구현하면서 연결 범위를 점차 넓혔다.

**1단계 — Flask + PyMongo CRUD**
브라우저는 아직 없고 서버와 DB만 연결한 단계다. 서버의 route와 MongoDB 작업이 어떻게 이어지는지를 중심으로 확인했다.

**2단계 — 영화 데이터: fetch()와 Flask JSON API 연결**
여기서 브라우저가 붙었다. MongoDB의 데이터를 GET으로 받아 화면을 만들고, POST·PATCH·DELETE로 브라우저에서 데이터를 변경한 뒤 다시 조회해 DOM을 갱신했다.

**3단계 — 메모 CRUD 웹**
메모 등록, 전체 조회, important 상태 변경, 삭제를 GET / POST / PATCH / DELETE와 연결했다. 각 작업이 끝난 뒤 다시 MongoDB의 데이터를 조회하는 방식을 한 번 더 적용했다.

**4단계 — 주간 복습: 상품 재고 관리 웹**
앞의 프로그램을 그대로 다시 작성하지 않고 주제를 바꿔 처음부터 구성했다.

---

## 2. 이번 주에 배운 것

### MongoDB와 PyMongo

database → collection → document 구조를 확인하고 PyMongo로 기본 CRUD를 다뤘다. Flask에서 MongoDB에 접근하며 `find()`, `insert_one()`, `update_one()`, `delete_one()`을 사용했다.

조회 결과가 바로 Python list가 아니라 Cursor라는 점, 필요한 경우 `list()`로 변환해야 한다는 점도 이때 확인했다.

### _id — ObjectId와 string

특정 document를 수정하거나 삭제하려면 `_id`가 필요했다. 그런데 MongoDB 안에서 `_id`는 ObjectId지만, URL이나 JSON을 거치면 string으로 다뤄진다.

그래서 방향에 따라 두 번의 변환이 필요했다.

```python
# MongoDB → JSON response : ObjectId를 string으로
item["_id"] = str(item["_id"])

# URL → MongoDB : string을 ObjectId로
{"_id": ObjectId(item_id)}
```

이번 주에 반복해서 쓴 것은 사실상 이 두 줄이었다.

### fetch()로 브라우저와 서버 연결

JavaScript에서 만든 데이터는 `JSON.stringify()`로 직렬화해 request body에 담아 보내고, Flask에서는 `request.get_json()`으로 Python에서 쓸 수 있는 형태로 받았다.

반대로 Flask에서 `jsonify()`로 response를 보내면 JavaScript에서 `response.json()`으로 읽어 DOM을 다시 구성했다.

### HTTP method와 status code

GET, POST, PATCH, DELETE를 각각 조회, 등록, 수정, 삭제와 연결했다. 같은 path라도 method에 따라 처리가 달라지므로, 한 route 안에서 `request.method`로 분기하기도 했다.

status code는 200 OK, 201 Created, 404 Not Found, 405 Method Not Allowed, 500 Internal Server Error의 의미를 학습했고, path 자체가 없는 경우와 path는 있지만 method가 허용되지 않은 경우를 구분했다.

### CRUD 후 재조회

CRUD가 끝난 직후 화면의 일부만 임의로 고치는 대신, 다시 GET request를 보내 MongoDB의 최신 데이터를 기준으로 화면을 재생성하는 방식으로 구현했다.

---

## 3. 가장 많이 막힌 부분 — 값 추적

이번 주에 가장 많이 막힌 것은 개별 문법이 아니라, 한 코드에서 다른 코드로 넘어갈 때 **지금 이 값이 무엇인지** 추적하는 일이었다.

반복해서 실수한 구분은 다음과 같다.

- `querySelector()`로 얻은 DOM element ↔ 그 element의 `.value`
- 여러 element가 들어 있는 collection ↔ 그 안에서 꺼낸 element 하나
- JavaScript object ↔ `JSON.stringify()`한 JSON string
- MongoDB ObjectId ↔ URL과 JavaScript에서 사용하는 string
- dataset에서 읽은 string ↔ boolean이나 number로 실제 사용할 값

각 문법을 따로 알고 있어도, 여러 단계를 연결하면 지금 variable에 무엇이 들어 있는지를 놓치는 경우가 있었다.

### 원인

처음에는 코드를 주로 "이 함수는 무엇을 한다"는 식으로 봤다. 하지만 Flask, MongoDB, JavaScript를 함께 쓰면서는 함수 하나의 역할만 아는 것으로 부족했다.

등록 하나에도 데이터는 실제로 이만큼 형태를 거친다.

```
HTML input
 → DOM element
 → .value
 → JavaScript object
 → JSON string
 → HTTP request
 → Python dictionary
 → MongoDB document
```

각 단계에서 값의 type과 역할이 달라지는데, 이 중간을 생략하고 생각한 것이 여러 오류의 원인이었다.

---

## 4. 직접 확인한 오류 세 가지

오류를 한 종류의 문제로 뭉뚱그리지 않고, 발생 위치를 나눠서 확인했다.

**(1) 실행 환경 문제 — DB 연결이 되지 않음**
코드를 계속 수정하는 대신 실행 환경을 확인했고, Flask와 mongod가 서로 다른 WSL 환경에서 실행되고 있다는 것을 찾았다.

**(2) 요청 경로 문제 — 의도하지 않은 URL로 request가 전달됨**
Flask route가 아니라 HTML form의 작성 상태를 확인했고, 따옴표와 `>`가 빠진 부분을 찾았다.

**(3) 데이터 type 문제 — ObjectId is not JSON serializable**
이 오류를 통해 MongoDB의 ObjectId가 일반 JSON으로 바로 직렬화되지 않는다는 것을 확인했다.

비슷하게 보이는 오류라도 **실행 환경 / 요청 경로 / 데이터 type**으로 원인이 서로 다를 수 있다는 점을 이번 주에 확인했다.

---

## 5. 수정한 방법

데이터가 어느 지점에서 어떤 형태인지 하나씩 추적하는 방식으로 수정했다.

- MongoDB에서 조회한 `_id`는 JSON response로 보내기 전에 `str()`로 변환했다.
- URL을 통해 Flask에 들어온 `_id`는 MongoDB 작업 전에 다시 `ObjectId()`로 변환했다.
- JavaScript에서는 서버로 보내려는 것이 DOM element 자체인지 사용자가 입력한 값인지 구분해 `.value`를 사용했다.
- JSON request를 보낼 때는 object를 그대로 body에 넣지 않고 `JSON.stringify()`를 사용했고, Flask에서는 `request.get_json()`으로 읽었다.
- document의 일부 field만 수정할 때는 `update_one()`과 `$set`을 사용했다.
- 등록·수정·삭제가 성공한 뒤에는 화면만 직접 고치지 않고 조회 함수를 다시 실행해 MongoDB의 현재 상태를 기준으로 DOM을 다시 만들었다.

정리하면 method별로 이런 흐름이 된다.

| method | 흐름 |
| --- | --- |
| GET | MongoDB 조회 → JSON response → DOM 생성 |
| POST | 입력값 → JSON request → document 생성 → GET 재조회 → 화면 갱신 |
| PATCH | `_id`로 대상 식별 → 특정 field 수정 → GET 재조회 → 화면 갱신 |
| DELETE | `_id`로 대상 식별 → 해당 document 삭제 → GET 재조회 → 화면 갱신 |

---

## 6. 코드로 본 브라우저 ↔ 서버 흐름

브라우저 쪽은 2단계의 영화 데이터 코드로, 서버 쪽은 4단계의 재고 관리 코드로 나눠서 정리했다.

### 6-1. 브라우저 쪽 — 영화 데이터 (2단계)

**조회하고 화면을 만드는 부분**

```javascript
function loadMovies() {
    fetch("/api/movies")
        .then(response => response.json())
        .then(data => {
            const movie_list = document.querySelector("#movie-list");

            movie_list.innerHTML = '';

            data.movies.forEach(movie => {
                movie_list.innerHTML += `<li>
                ${movie.title}
                <button type="button" class="delete-movie" data-movie-id=${movie._id}>삭제</button>
                <button type="button" class="update-movie" data-movie-id="${movie._id}" data-movie-title="${movie.title}">수정</button>
                </li>`;
            });

            // (수정 버튼 처리 부분은 생략)

            const deleteButton = document.querySelectorAll(".delete-movie");

            deleteButton.forEach(button => {
                button.addEventListener("click", () => {
                    deleteMovie(button.dataset.movieId)
                });
            });
        });
}
```

`response.json()`으로 읽은 데이터로 `<li>`를 만들면서, 삭제·수정 버튼에 `data-movie-id`로 `_id`를 같이 심었다. 나중에 그 버튼을 눌렀을 때 어떤 document를 대상으로 할지 알아야 하기 때문이다.

`querySelectorAll()`이 돌려주는 것은 여러 element가 들어 있는 collection이라서, `forEach`로 하나씩 꺼내 event를 붙여야 한다. 이 구분이 앞에서 적은 "collection인가 element 하나인가"에 해당한다.

**등록하는 부분**

```javascript
function addMovie() {
    const movieTitle = document.querySelector("#movie-title").value;

    fetch("/api/movies", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "title": movieTitle
        })
    }).then(response => response.json())
        .then(data => { loadMovies(); })
}

const addButton = document.querySelector("#add-movie")

addButton.addEventListener("click", addMovie)
```

이 짧은 함수 안에 이번 주 내용이 거의 다 들어 있다.

`querySelector("#movie-title")`까지는 input element지만, 서버로 보낼 것은 element가 아니라 사용자가 입력한 값이므로 `.value`가 필요하다. 그렇게 만든 object는 그대로 body에 넣을 수 없어서 `JSON.stringify()`로 JSON string으로 바꾸고, 무엇을 보내는지 알리기 위해 `Content-Type`을 `application/json`으로 지정했다.

등록이 끝난 뒤에는 화면에 `<li>`를 직접 하나 더 붙이지 않고 `loadMovies()`를 다시 호출했다. 화면을 DB의 현재 상태로 다시 만드는 방식이다.

**삭제하는 부분**

```javascript
function deleteMovie(movie_id) {
    fetch(`/api/movies/${movie_id}`, {
        method: 'DELETE'
    })
        .then(response => response.json())
        .then(data => {
            loadMovies();
        })
}
```

여기서 넘어오는 `movie_id`는 `button.dataset.movieId`에서 읽은 값이라 string이다. 서버가 `str()`로 바꿔서 보냈고 `dataset`에서 읽은 값도 string이기 때문에, 이번 구현에서 브라우저 쪽 `_id`는 처음부터 끝까지 string이었다. 이 값이 URL을 타고 서버로 넘어가면, 서버에서는 다시 ObjectId로 되돌려야 MongoDB가 해당 document를 찾을 수 있다.

### 6-2. 서버 쪽 — 상품 재고 관리 웹 (4단계)

**등록과 조회 — 같은 path, 다른 method**

```python
@app.route("/item", methods=["POST", "GET"])
def add_find_item():
    if request.method == "POST":
        item = request.get_json()

        new_item = {
            "name": item["name"],
            "quantity": int(item["quantity"])
        }

        items.insert_one(new_item)

        return jsonify({
            "result": "add success"
        })

    elif request.method == "GET":
        items_list = list(items.find())

        for item in items_list:
            item["_id"] = str(item["_id"])

        return jsonify({
            "items": items_list
        })
```

`/item`이라는 같은 path를 쓰지만, POST면 등록이고 GET이면 조회라서 `request.method`로 나눴다.

조회 쪽에서는 `find()`의 결과가 Cursor이므로 `list()`로 바꾼 뒤, 각 document의 `_id`를 `str()`로 변환해서 response로 보냈다. 이 변환을 빼면 앞에서 이야기한 `ObjectId is not JSON serializable` 오류가 난다.

등록 쪽에서 `int(item["quantity"])`를 쓴 이유는, 브라우저에서 입력한 값이 숫자처럼 보여도 string으로 전달되기 때문이다. 여기서 숫자로 바꿔 저장했기 때문에 MongoDB에도 숫자 값으로 들어간다.

**수정과 삭제 — URL로 대상 특정하기**

```python
@app.route("/item/<item_id>", methods=["PATCH"])
def update_item(item_id):
    update_data = request.get_json()

    items.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {"quantity": int(update_data["quantity"])}}
    )

    return jsonify({
        "result": "update success"
    })


@app.route("/item/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    items.delete_one(
        {"_id": ObjectId(item_id)}
    )

    return jsonify({
        "result": "delete success"
    })
```

앞에서 브라우저가 string으로 보낸 `_id`가 도착하는 지점이 여기다. URL의 `<item_id>`로 대상을 특정하되, 들어온 값은 string이므로 `ObjectId()`로 되돌려서 MongoDB에 넘겼다.

수정에서는 `$set`을 사용해 document 전체를 덮어쓰지 않고 `quantity` field만 바꿨다.

---

## 7. 실행 결과 — 화면 말고 DB에서 확인하기

처음에는 브라우저 화면에서 값이 바뀐 것을 보고 확인을 마쳤다. 그런데 화면이 바뀐 것과 DB가 실제로 바뀐 것은 다르다는 생각이 들어서, mongosh를 켜고 처음부터 다시 확인했다. 아래는 그 두 번째 시도의 결과다.

```
test0906> db.items.find()
[
  {
    _id: ObjectId('6a9d341595f0b2d9809ff7fc'),
    name: '어린왕자',
    quantity: 7
  }
]

test0906> db.items.find()
[
  {
    _id: ObjectId('6a9d341595f0b2d9809ff7fc'),
    name: '어린왕자',
    quantity: 5
  },
  { _id: ObjectId('6a9d348d95f0b2d9809ff7fd'), name: '여우', quantity: 3 }
]

test0906> db.items.find()
[
  { _id: ObjectId('6a9d348d95f0b2d9809ff7fd'), name: '여우', quantity: 3 }
]
```

**첫 번째 조회** — '어린왕자'를 재고 7로 등록한 상태다. `quantity: 7`이 따옴표 없이 숫자로 저장된 것을 확인했다. 등록할 때 `int()`로 변환한 결과다.

**두 번째 조회** — 상품이 하나뿐이면 "다른 상품은 영향을 받지 않는다"를 확인할 수 없어서 '여우'를 재고 3으로 추가로 등록했다. 그리고 '어린왕자'의 재고만 5로 변경했다. 수정 대상이 아니었던 '여우'의 `quantity: 3`은 그대로 유지됐다. `$set`으로 해당 document의 `quantity` field만 바꿨기 때문이다.

**세 번째 조회** — '어린왕자'를 삭제한 상태다. `_id`로 지정한 document만 사라지고 '여우'는 그대로 남아 있는 것을 확인했다.

수정과 삭제가 다른 document에 영향을 주지 않는다는 것을, 화면이 아니라 DB 쪽에서 직접 확인한 셈이다.

---

## 8. 직접 구성한 부분과 교정이 필요했던 부분

프로그램이 정상 동작했다는 것과, 모든 코드를 처음부터 혼자 정확하게 작성했다는 것은 구분할 필요가 있다.

- **메모 CRUD 웹**: DOM element와 value, collection과 element, `JSON.stringify()`, JSON key, dataset, scope의 연결에서 교정을 받았다.
- **재고 관리 웹**: GET / POST / PATCH / DELETE 전체 구조, `_id`를 이용한 document 연결, CRUD 후 재조회 방식 같은 큰 구조는 직접 구성했다. 다만 `.value`, `JSON.stringify()`, `$set`, 초기 조회 호출 같은 세부 연결에서는 수정이 필요했다.

지금은 Flask·MongoDB·JavaScript 사이의 전체 흐름을 설명할 수 있고, 큰 구조는 직접 구성할 수 있다. 다만 여러 기술을 한 번에 연결할 때 type과 값의 이동을 처음부터 실수 없이 판단하는 부분은 더 익숙해져야 한다.

---

## 9. 다음 주 목표

코드를 작성하기 전에 지금 variable에 무엇이 들어 있는지부터 확인하려 한다. 습관으로 만들 것은 세 가지다.

1. 지금 다루는 것이 collection인지, element 하나인지
2. 지금 필요한 것이 DOM element인지, 실제 value인지
3. 다른 함수나 서버로 전달되는 값의 type이 무엇인지

단순히 프로그램이 실행되는 것에서 끝내지 않고, 왜 이 값이 이 위치에 들어가는지까지 설명할 수 있는 상태를 유지하면서 다음 학습을 이어가려 한다.
