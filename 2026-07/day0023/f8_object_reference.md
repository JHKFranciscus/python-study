```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price


book1 = Book("파이썬 기초", 20000)
book2 = book1
```
# 질문 1
```python
book2.price = 18000
```

실행 후 다음 값은 각각 무엇인지 예상합니다.
```python
print(book1.price)
print(book2.price)
print(book1 is book2)
```
그리고 book1.price까지 바뀌는 이유를 한 문장으로 설명합니다.

## 질문 1 답:
18000
18000
True

book2라는 객체를 새로 생성한 것이 아니라 book1이 가리키는 객체를 book2도 가리키는 것이기 때문이다.

# 질문 2. 서로 다른 객체와 비교
```python
book1 = Book("파이썬 기초", 20000)
book2 = Book("파이썬 기초", 20000)
```

다음 결과를 예상합니다.
```python
print(book1 is book2)
print(book1 == book2)
```
아직 __eq__()를 작성하지 않은 상태입니다.

답안에 다음 내용을 포함합니다.

내용이 같아도
별도로 생성된 객체
is
기본적인 ==

## 질문 2 답:
False
False

<!-- 별도로 생성된 객체는 서로 다른 attribute를 가진다. 따라서 attribute value가 같아도, 객체의 동일성을 비교하는 is에서도, 값의 동등성을 비교하는 ==에서도 False가 나온다. -->
[수정 후]
book1과 book2는 내용이 같더라도 Book(...)을 각각 호출해 별도로 생성한 객체이므로 is의 결과는 False이다.

 또한 Book 클래스에 __eq__()를 작성하지 않았으므로, 기본적인 == 비교도 두 객체가 동일한 객체인지를 기준으로 판단하여 False가 나온다.

# 질문 3. 리스트가 객체를 저장할 때
```python
book1 = Book("파이썬 기초", 20000)
books = []

books.append(book1)
found_book = books[0]

found_book.price = 17000

print(book1.price)
print(books[0].price)
print(found_book is book1)
```
결과를 예상하고 다음 질문에 답합니다.

1. 리스트 안에 객체의 복사본이 들어간 것인가?
2. found_book은 새로운 객체인가?
3. found_book.price 변경이 book1.price에도 반영되는 이유는 무엇인가?
4. 오늘 작성한 find_book()이 반환한 객체의 가격을 변경하면 리스트 안의 객체도 바뀌는 이유는 무엇인가?

## 질문 3 답:
1. 아니다 객체를 가리키는 참조가 들어갔다.
<!-- 2. 아니다 book1이 가리키는 주소가 들어가있다. -->
[수정 후]
2. found_book은 새로운 객체가 아니다. books[0]에 저장된 객체의 참조가 found_book에도 연결된 것이다.
3. found_book이 가리키는 객체와 book1이 가리키는 객체가 동일하기 때문이다.
4. 리스트 안의 객체와 found_book()이 반호나한 객체가 동일하기 때문이다.

# 질문 4. 최종 정리 문장

아래 빈칸을 직접 완성합니다.

<!-- 변수는 객체 자체를 저장한다기보다 객체를 가리키는 ___주소___를 가진다. -->
변수는 객체 자체를 저장한다기보다 객체를 가리키는 ___참조___를 가진다.

book2 = book1은 새로운 객체를 생성하는 것이 아니라,
두 변수가 ___동일한___ 객체를 가리키게 한다.

리스트에 Book 객체를 append하면 객체의 독립적인 복사본이 아니라
<!-- 해당 객체를 가리키는 ___주소___가 리스트에 저장된다. -->
해당 객체를 가리키는 ___참조___가 리스트에 저장된다.

find_book()이 반환한 객체의 속성을 변경했을 때 원본 리스트에도
변경이 보이는 이유는 둘이 ___동일한___ 객체를 가리키기 때문이다.