# 파이썬 객체지향 프로그래밍 복습: 상속·캡슐화·다형성과 JSON 저장

이번 주에는 데이터를 함수와 딕셔너리로만 관리하던 방식에서 벗어나, 관련된 데이터와 동작을 하나의 객체 안에 묶는 객체지향 프로그래밍을 학습했다.

단순히 클래스 문법을 익히는 데서 끝내지 않고, 도서 관리 프로그램과 상품 관리 프로그램을 만들면서 각 객체가 어떤 데이터를 가지고 어떤 동작을 책임져야 하는지 확인했다.

**이번 주 요약**

- 배운 것: 클래스와 객체, 상속과 객체 구성, 오버라이딩과 다형성, 캡슐화, 추상 클래스
- 만든 것: 도서 관리 프로그램, 상품 관리 프로그램(JSON 저장·불러오기 포함)
- 막힌 것: 예외가 발생했을 때 객체 내부의 상태가 어떻게 남는지 판단하는 부분

---

## 이번 주에 배운 내용

### 클래스, 객체, 인스턴스

클래스는 객체가 가질 속성과 수행할 메서드를 정의한 설계도이다. 객체는 상태와 행동을 가지며 메모리에 실제로 존재하는 대상이고, 인스턴스는 특정 클래스를 바탕으로 실제로 생성된 객체를 뜻한다.

처음에는 인스턴스를 클래스와 객체 사이의 연결처럼 이해했지만, 복습을 통해 특정 클래스로부터 생성된 객체 자체를 의미한다는 점을 다시 정리했다.

### 인스턴스 속성과 클래스 속성

```python
class Product:
    category = "상품"

    def __init__(self, name):
        self.name = name
```

`category`는 클래스에 속하는 클래스 속성이고, `name`은 각각의 인스턴스에 따로 저장되는 인스턴스 속성이다.

인스턴스에서 클래스 속성과 같은 이름에 값을 대입하면, 클래스 속성이 직접 변경되는 것이 아니라 해당 인스턴스에 같은 이름의 새로운 속성이 만들어질 수 있다.

```python
product1.category = "전자기기"
```

이 경우 `product1`의 인스턴스 속성이 기존 클래스 속성을 가린다.

### 상속과 객체 구성

공통 속성과 동작은 부모 클래스에 두고, 자식 클래스에서 필요한 기능을 추가하거나 기존 메서드를 다시 구현하는 상속을 학습했다.

```python
class DownloadProduct(Product):
    pass
```

`DownloadProduct`는 `Product`의 한 종류이므로 `is-a` 관계이다.

반면 관리자가 상품 객체를 리스트에 보관하고 사용하는 관계는 객체 구성에 해당한다.

```python
class ProductManager:
    def __init__(self):
        self.products = []
```

`ProductManager`는 상품의 한 종류가 아니라 상품 객체들을 가지고 사용하므로 `has-a` 관계이다.

### 오버라이딩과 다형성

부모 클래스에 이미 존재하는 메서드를 자식 클래스에서 다시 정의하는 것을 메서드 오버라이딩이라고 한다.

```python
class NormalProduct(Product):
    def show_info(self):
        print("일반 상품")


class DownloadProduct(Product):
    def show_info(self):
        print("다운로드 상품")
```

호출하는 쪽에서는 두 객체 모두 같은 방식으로 처리할 수 있다.

```python
for product in products:
    product.show_info()
```

같은 `show_info()`를 호출해도 실제 객체의 타입에 따라 서로 다른 메서드가 실행된다. 이것이 다형성이고, 실행 시점에 실제 객체를 기준으로 호출할 메서드가 결정되는 과정이 동적 디스패치이다.

### 캡슐화와 프로퍼티

가격을 외부에서 아무 값으로나 변경하지 못하도록 프로퍼티 setter에서 값을 검사했다.

```python
@property
def price(self):
    return self._price


@price.setter
def price(self, new_price):
    if new_price < 0:
        raise ValueError("잘못된 가격입니다.")

    self._price = new_price
```

생성자에서도 같은 검사를 적용하려면 내부 속성에 직접 저장하지 않고 프로퍼티를 사용해야 한다.

```python
def __init__(self, name, price):
    self.name = name
    self.price = price
```

`self._price = price`로 직접 저장하면 생성 시점에는 setter를 거치지 않는다.

### 추상 클래스

`ABC`와 `@abstractmethod`를 사용해 자식 클래스가 반드시 구현해야 하는 메서드를 정했다.

```python
from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def show_info(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
```

추상 클래스의 목적은 단순히 공통 메서드를 한곳에 모으는 것이 아니라, 자식 클래스가 반드시 제공해야 할 동작의 형식과 규칙을 강제하는 것이다.

---

## 이번 주에 만든 프로그램

### 도서 관리 프로그램

클래스 기반으로 다음 기능을 만들었다.

- 도서 등록
- 전체 조회
- 이름 검색
- 가격 변경
- 삭제
- 일반 도서·전자책·오디오북 상속 구조

### 상품 관리 프로그램

`Product`를 추상 클래스로 만들고, `NormalProduct`와 `DownloadProduct`가 이를 상속하도록 구성했다. 각 상품 클래스는 자신의 출력 방식(`show_info()`)과 JSON 저장용 딕셔너리 변환 방식(`to_dict()`)을 직접 구현했다.

`ProductManager`는 상품 객체들을 리스트에 보관하면서 다음 기능을 담당했다.

- 상품 추가
- 전체 조회
- 이름 검색
- 가격 변경
- 삭제
- JSON 저장
- JSON 불러오기

전체 조회에서는 `isinstance()` 조건문으로 상품 종류를 나누지 않고 각 객체의 `show_info()`를 호출했다.

### 저장과 불러오기

저장할 때는 상품 객체를 딕셔너리로 변환했다.

```python
products_dict = []

for product in self.products:
    products_dict.append(product.to_dict())
```

불러올 때는 JSON에서 읽은 딕셔너리의 `type` 값을 확인하여 알맞은 클래스 객체로 복원했다.

```python
def create_product(data):
    if data["type"] == "normal":
        return NormalProduct(
            data["name"],
            data["price"],
            data["stock"]
        )

    if data["type"] == "download":
        return DownloadProduct(
            data["name"],
            data["price"],
            data["file_size"]
        )

    return None
```

---

## 가장 많이 막힌 부분과 해결 과정

가장 많이 막힌 부분은 정상 실행 코드 자체보다, 오류나 예외가 발생했을 때 객체 내부의 상태가 어떻게 남는지를 판단하는 것이었다.

### 문제 1. 불러오기에 실패해도 기존 상품이 남았다

**증상**

상품 목록을 JSON에서 불러오는 과정에서 파일이 없거나 JSON 형식이 잘못된 경우를 처리했지만, 처음에는 예외 처리에서 `return`만 실행했다.

```python
except FileNotFoundError:
    return
```

함수는 종료되었지만 기존의 `self.products`는 그대로 남아 있었다.

**원인**

함수를 종료하는 것과 객체의 상태를 변경하는 것을 같은 것으로 생각한 것이 원인이었다. `return`이나 `return []`을 실행해도 함수가 끝나거나 값이 반환될 뿐, 기존의 `self.products`가 자동으로 빈 리스트로 바뀌지는 않는다.

**수정**

`load()`가 시작될 때 기존 상품 목록을 먼저 비우도록 수정했다.

```python
def load(self, filename):
    self.products = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            products_dict = json.load(file)

    except FileNotFoundError:
        return

    except json.JSONDecodeError:
        return
```

이렇게 하면 파일을 읽는 데 실패하더라도 기존 상품이 남지 않고 빈 상태로 시작한다.

### 문제 2. 가격 변경이 실패한 원인을 구분할 수 없었다

**증상**

가격 변경 메서드에서 `ValueError`를 잡아 `False`로 바꾸면, 상품을 찾지 못한 경우와 가격이 잘못된 경우를 구분하기 어려웠다.

**원인**

서로 다른 실패 원인을 같은 반환값으로 처리한 것이 원인이었다.

- 상품이 존재하지 않음
- 상품은 존재하지만 가격이 잘못됨

두 경우를 모두 `False`로 처리하면 호출하는 쪽에서 실패 원인을 구분할 수 없다.

**수정**

상품이 없는 경우에만 `False`를 반환하고, 잘못된 가격은 setter의 `ValueError`가 그대로 전달되게 했다.

```python
def update_price(self, name, new_price):
    product = self.search_product(name)

    if product is None:
        return False

    product.price = new_price
    return True
```

---

## 직접 확인한 결과

### 1. 정상 저장 후 복원

정상적인 JSON 파일을 저장한 뒤 새로운 `ProductManager` 객체를 만들고 다시 불러왔다.

```python
new_manager = ProductManager()
new_manager.load("rebuild_products.json")
new_manager.show_all()
```

```
[일반] 키보드 / 35000원 / 재고 10개
[다운로드] 게임 / 50000원 / 80MB
```

일반 상품과 다운로드 상품이 각각 원래 클래스 객체로 복원되었다.

### 2. 복원된 상품 삭제

다운로드 상품을 삭제한 뒤에는 일반 상품만 남았다.

```
[일반] 키보드 / 35000원 / 재고 10개
```

### 3. 존재하지 않는 파일

기존 상품이 들어 있는 관리자에서 존재하지 않는 파일을 불러왔다.

```python
test_manager.load("not_found_products.json")
test_manager.show_all()
```

```
등록된 상품이 없습니다.
```

### 4. 잘못된 JSON 파일

닫히지 않은 JSON 파일도 직접 만들어 같은 방식으로 테스트했다.

```json
[
  {
```

이 경우에도 기존 상품이 남지 않았다.

```
등록된 상품이 없습니다.
```

### 5. 음수 가격

음수 가격을 전달하여 프로퍼티 setter의 `ValueError`가 실제로 호출자에게 전달되는지 확인했다.

```python
try:
    manager.update_price("키보드", -1)
except ValueError as error:
    print(type(error).__name__)
    print(error)
```

```
ValueError
잘못된 가격입니다.
```

---

## 이번 주에 확실히 남은 것

- 인스턴스는 클래스와 객체를 이어주는 무언가가 아니라, 특정 클래스로부터 생성된 객체 자체다.
- 인스턴스에서 클래스 속성과 같은 이름에 값을 대입하면 클래스 속성이 바뀌는 것이 아니라 인스턴스 속성이 새로 만들어져 기존 값을 가린다.
- 값 검증은 객체 안에서 한다. 생성 시점에도 검사하려면 생성자에서 `self._price`가 아니라 `self.price`를 사용해야 한다.
- 타입을 밖에서 판별하지 않고 각 객체가 자신의 `show_info()`를 구현하게 하면, 호출하는 쪽 코드는 그대로 둘 수 있다.
- JSON에 저장하려면 객체를 딕셔너리로 바꾸고, 불러온 뒤에는 다시 클래스 객체로 되돌려야 한다.
- 값을 반환하는 것과 객체의 상태를 바꾸는 것은 다른 동작이다. 그리고 실패 원인이 다르면 알리는 방법도 달라야 한다.

---

## 아직 부족한 부분

코드를 보고 객체지향 개념을 구분하는 것은 가능하지만, 클래스·객체·인스턴스·캡슐화·다형성 같은 용어를 코드 없이 설명할 때 표현이 흔들린다.

상속과 객체 구성도 단순한 관계에서는 판단할 수 있지만, 클래스 사이의 관계가 복잡해지면 어느 구조를 선택해야 하는지 바로 판단하기 어렵다.

프로그램의 정상 동작은 먼저 고려할 수 있었지만, 예외가 발생했을 때 기존 객체 상태가 어떻게 되어야 하는지는 처음부터 설계하지 못했다.

---

## 다음 주 목표

다음 주에는 지금까지 배운 파이썬 내용을 문제 풀이와 복습으로 유지하면서, 새로운 학습 영역으로 HTML과 CSS를 시작할 예정이다.

HTML에서는 문서의 기본 구조와 주요 태그가 각각 어떤 의미와 역할을 가지는지 학습하고, CSS에서는 선택자와 기본 스타일을 적용해 작은 웹 페이지를 직접 만들어 본다.

파이썬 객체지향은 기존 도서·상품 관리 프로그램을 그대로 반복하지 않고, 처음 보는 요구사항에서 클래스와 객체의 책임을 직접 나누는 방식으로 복습한다. 클래스 구조가 미리 주어지지 않은 문제에서 상속과 객체 구성 중 적절한 관계를 판단하고, 새로운 기능이 추가됐을 때 기존 코드의 수정 범위도 확인할 예정이다.

또한 알고리즘 문제 풀이와 SSAFY 문제 학습을 계속 진행하여 파이썬 코드 작성 감각을 유지한다.

