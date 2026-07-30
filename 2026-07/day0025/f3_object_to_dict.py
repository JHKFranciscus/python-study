import json


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def to_dict(self):
        return {
            "type": "book",
            "title": self.title,
            "price": self.price
        }


class EBook(Book):
    def __init__(self, title, price, file_size):
        super().__init__(title, price)
        self.file_size = file_size

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "ebook"
        data["file_size"] = self.file_size
        return data


class AudioBook(Book):
    def __init__(self, title, price, play_time):
        super().__init__(title, price)
        self.play_time = play_time

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "audiobook"
        data["play_time"] = self.play_time
        return data

def create_book_from_dict(data):
    book_type = data["type"]

    if book_type == "book":
        return Book(
            data["title"],
            data["price"]
        )

    elif book_type == "ebook":
        return EBook(
            data["title"],
            data["price"],
            data["file_size"]
        )

    elif book_type == "audiobook":
        return AudioBook(
            data["title"],
            data["price"],
            data["play_time"]
        )

    else:
        return None


book = Book("파이썬 기초", 20000)

book_data = book.to_dict()

print(book)
print(type(book))
print(book_data)
print(type(book_data))
print()

json_text = json.dumps(
    book_data,
    ensure_ascii=False,
    indent=4
)

print(json_text)
print(type(json_text))
#region
# 1. book의 자료형은 무엇인가?
# 답: Book 자료형
# 2. book_data의 자료형은 무엇인가?
# 답: dict 자료형
# 3. book과 book_data는 어떤 차이가 있는가?
# 답: type에서 차이가 있다.
#[보완]
#book은 Book class의 객체로서 속성을 가지고 클래스에 정의된 메서드를 사용할 수 있다.
#book_data는 JSON 저장에 필요한 값만 담은 일반 dictionary이다.
#boo_data에는 Book의 method가 들어 있지 않다.
# 4. to_dict() 안에서 새로운 딕셔너리를 return하는 이유는 무엇인가?
# 답: 그 만들어진 dict 자료형 반환값으로 JSON형식으로 변환하고 저장하기 위하여
#[표현 수정]
#to_dict()는 JSON이 처리 할 수 있는 dictionary 형태로 바꾸기 위한 메서드이다.
# 5. 저장 데이터에 "type": "book"을 포함한 이유는 무엇인가?
# 답: 다른 class 객체와 구분하기 위하여
#endregion
ebook = EBook("파이썬 전자책", 15000, 25)
audiobook = AudioBook("파이썬 오디오북", 18000, 120)

books = [book, ebook, audiobook]

books_data = []

for item in books:
    books_data.append(item.to_dict())

print(books_data)
print(type(books_data))
print(type(books_data[0]))
print(type(books_data[1]))
print(type(books_data[2]))

all_json_text = json.dumps(
    books_data,
    ensure_ascii=False,
    indent=4
)

print(all_json_text)
print(type(all_json_text))
#region
# 1. item이 EBook 객체를 가리킬 때 어느 클래스의 to_dict()가 먼저 실행되는가?
# EBook class의 to_dict()가 먼저 실행된다.
# 2. EBook.to_dict()에서 super().to_dict()를 호출하는 이유는 무엇인가?
# Book에 이미 작성되어 있는 method code의 중복 작성을 막기 위하여
#[보완]
#Book.to_dict()가 만드는 공통 데이터인 type, title, price 딕셔너리를 재사용하여 같은 코드를 자식 클래스에 중복작성하지 않기 위해서다.
# 3. data["type"]을 "ebook"으로 변경하면 원래 book 객체의 속성도 변경되는가? 그 이유는 무엇인가?
# 변경되지 않는다. dict의 type이라는 키워드의 값을 변경해주는 것이라서 book객체의 속성에는 직접적인 영향을 미치지 않는다.
#[보완]
#변경되지 않는다. Book.to_dict()가 새로 만들어 반환한 dict의 값을 변경하는 것이며, 원래 객체의 속성을 직접 변경하는 것이 아니기 때문이다.
# 4. books_data의 자료형은 무엇이며, 그 안의 각 요소의 자료형은 무엇인가?
# books_data의 자료형은 list 자료형이며, 그 안의 각 요소들은 dict 자료형이다.
# 5. Python의 books_data는 JSON으로 변환되었을 때 JSON object와 JSON array 중 어떤 형태가 되는가?
# books_data는 직렬화하기 전에는 list형식이었으므로 JSON array 형태가 된다.
#[보완]
#JSON object 여러 개가 들어있는 JSON array방식
#endregion
#region
print()
loaded_books_data = json.loads(all_json_text)

restored_books = []

for data in loaded_books_data:
    restored_book = create_book_from_dict(data)

    if restored_book is not None:
        restored_books.append(restored_book)


print(type(loaded_books_data))
print(type(loaded_books_data[0]))
print(type(loaded_books_data[1]))
print(type(loaded_books_data[2]))

print(type(restored_books))
print(type(restored_books[0]))
print(type(restored_books[1]))
print(type(restored_books[2]))

print(
    restored_books[0].title,
    restored_books[0].price
)

print(
    restored_books[1].title,
    restored_books[1].price,
    restored_books[1].file_size
)

print(
    restored_books[2].title,
    restored_books[2].price,
    restored_books[2].play_time
)

# 1. json.loads(all_json_text)의 결과 안에는
# Book 객체와 dict 중 무엇이 들어 있는가?
# dict
# 2. "type" 값이 "ebook"이라면 create_book_from_dict()는 어느 클래스의 객체를 반환하는가?
# EBook class object를 반환한다.
# 3. 객체 복원 과정에서 "type" 데이터가 필요한 이유는 무엇인가?
# "type"의 값과 비교하여 알맞은 클래스의 객체로 반환하기 위해서
# 4. loaded_books_data와 restored_books는 모두 list이지만
# 내부 요소에는 어떤 차이가 있는가?
# loaded_books_data의 내부 요소는 dict 자료형으로 되어 있지만, restored_books의 내부 요소는 각 클레스의 instance의 참조로 구성되어있다.
# 5. 원래 ebook 객체와 restored_books[1]은 같은 객체인가? 아니면 같은 데이터를 가진 서로 다른 객체인가?
# 같은 데이터를 가진 서로 다른 객체이다.
#endregion




