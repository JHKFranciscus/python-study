# Python 학습 5주차 — 문법을 아는 것과 코드를 직접 만드는 것의 차이

이번 주에는 파이썬의 자료 처리 방식부터 iterator와 generator,
함수 심화, dataclass, module/package, 가상환경과 pathlib까지 학습했다.

개념을 하나씩 확인하는 문제에서는 어느 정도 답할 수 있었다.
그러나 주간 복습에서 여러 개념을 하나의 프로그램으로 조합하려고 하자 독립 재현에 실패했다.
이번 주에 확인한 것은 **문법을 이해하는 것과 코드를 스스로 구성하는 것은 다른 능력**이라는 점이다.

---

## 이번 주 요약

- **배운 것**: iterator / generator, 함수 심화와 decorator, dataclass, module/package, 가상환경, pathlib
- **막힌 것**: collection과 객체 하나의 구분, `map()`에서 값과 함수의 구분, 인수를 받는 함수의 decorator
- **바꾼 것**: 코드를 쓰기 전에 `하나인가 여러 개인가 → 무엇이 들어 있는가 → 값인가 함수인가`를 먼저 확인

---

## 이번 주 배운 내용

- `enumerate()`, `zip()`, comprehension
- iterable / iterator, `iter()`, `next()`
- generator, `yield`, 지연 계산
- 함수 객체, callback, `lambda`, `map()`, `filter()`
- decorator
- `dataclass`, `field(default_factory=...)`
- module / package / import
- 가상환경과 `requirements.txt`
- `pathlib.Path`

그중에서도 함수 이름 자체와 함수 호출 결과의 차이를 반복해서 확인했다.

```python
func    # 함수 객체 자체
func()  # 함수를 호출한 결과
```

또 `map()`처럼 함수를 인수로 받는 코드에서
지금 자리에 값이 필요한지 함수가 필요한지 구분하는 것도 함께 확인했다.

---

## 작성한 코드

각 개념을 확인하기 위해 작은 코드를 여러 개 작성했다.

- generator에서는 `yield`로 값을 하나씩 만들어 내는 흐름을 확인했다.
- `map()`과 `filter()`에서는 iterator가 지연 계산되고 소비되는 과정을 실행 결과로 비교했다.
- module과 package를 나누어 import하는 방법을 연습했다.

dataclass에서는 mutable 기본값이 객체마다 따로 생성되도록 작성했다.

```python
@dataclass
class Student:
    name: str
    scores: list[int] = field(default_factory=list)
```

`pathlib.Path`로는 경로를 직접 만들고 각 정보를 확인했다.

```python
file_path = Path("data") / "students" / "scores.json"
```

---

## 가장 많이 막힌 부분

5주차 전체 복습에서 이번 주 내용을 하나의 프로그램으로 조합해
독립 재현을 시도했지만 실패했다. 막힌 부분은 세 가지였다.

1. 여러 객체가 들어 있는 collection과 객체 하나를 구분하지 못했다.
2. `map()`을 작성하면서 값이 필요한지 함수가 필요한지 판단하지 못했다.
3. 인수를 받는 함수에 decorator를 적용할 때 wrapper와 원래 함수의 인수를 연결하지 못했다.

예를 들어 여러 기록을 의미하는 `records`에 다음과 같이 접근했다.

```python
records.minutes
```

실제로는 여러 기록 중 하나를 먼저 꺼낸 뒤 접근해야 했다.

```python
for record in records:
    record.minutes
```

---

## 원인

주된 문제는 개별 문법 자체보다,
코드를 작성하는 순간 각 변수에 무엇이 들어 있는지를 추적하고
여러 문법을 연결하지 못한 것이었다.

또 개념을 하나만 사용하는 문제와 달리
generator, `map()`, decorator를 동시에 사용해야 하자
각 문법을 어떤 순서와 역할로 연결해야 하는지 판단하지 못했다.

---

## 다시 확인한 과정

처음 독립 재현에 실패한 코드는 그대로 실패로 기록했다.
정답이나 설명을 본 뒤 고친 코드는 독립적으로 작성한 것으로 처리하지 않았다.

대신 막힌 부분을 새로운 Product 예제로 나누어 다시 확인했다.

먼저 Product 객체 여러 개에서 조건에 맞는 객체를 하나씩 반환하는 generator를 직접 작성했다.

```python
def expensive_products(products, min_price):
    for product in products:
        if product.price >= min_price:
            yield product
```

다음으로 `map()`에는 값이 아니라 함수가 필요하다는 것을 확인한 뒤
이름만 추출하는 함수도 직접 작성했다.

```python
def get_names(products):
    return list(map(lambda product: product.name, products))
```

decorator를 적용한 함수는 다음과 같이 실행되는 것을 확인했다.

```text
처리 시작
처리 끝
['키보드', '마우스', '모니터']
```

wrapper에서 원래 함수를 호출하고,
원래 함수의 반환값을 보존해 다시 반환하는 흐름까지 실행 결과로 확인했다.
다만 이 코드는 단계적인 설명을 받은 뒤 작성했기 때문에
독립 재현에 성공한 것으로 기록하지 않았다.

---

## 앞으로 적용할 확인 순서

이번 실패를 기준으로, 코드를 작성하기 전에 다음 세 가지를 먼저 확인하기로 했다.

1. 지금 다루는 것은 하나인가, 여러 개인가?
2. 이 변수에는 실제로 무엇이 들어 있는가?
3. 이 자리에 필요한 것은 값인가, 함수인가?

문법을 외운 뒤 바로 코드를 작성하기보다,
변수와 인수의 역할을 먼저 확인한 다음 코드를 작성하는 방식으로 바꾸려고 한다.

---

## 아직 부족한 부분

개별 개념이나 짧은 코드의 실행 결과는 어느 정도 판단할 수 있지만,
여러 개념을 사용하는 프로그램의 구조를 처음부터 스스로 설계하는 것은 아직 어렵다.

새로운 문제에서 별도 힌트 없이 다음을 할 수 있는지는 아직 확인이 필요하다.

- collection과 요소 하나를 구분할 수 있는지
- 값과 함수가 필요한 자리를 판단할 수 있는지
- 인수를 받는 함수의 decorator를 작성할 수 있는지

---

## 다음 주 목표

다음 주에는 예정된 학습 진도를 그대로 진행한다.

새로운 문법을 배우면서 단순히 사용법만 외우지 않고,
코드를 작성할 때
`하나인가 여러 개인가 → 변수에는 무엇이 들어 있는가 → 값과 함수 중 무엇이 필요한가`
를 함께 판단하는 연습을 이어갈 예정이다.
