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

def save_books(books, filename):
    books_data = []

    for book in books:
        books_data.append(book.to_dict())

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            books_data,
            file,
            ensure_ascii=False,
            indent=4
        )

def load_books(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            loaded_data = json.load(file)

    except FileNotFoundError:
        print("저장 파일이 없어 빈 목록으로 시작합니다.")
        return []

    except json.JSONDecodeError:
        print("저장 파일이 비어 있거나 JSON 형식이 올바르지 않습니다.")
        return []

    restored_books = []

    for data in loaded_data:
        restored_book = create_book_from_dict(data)

        if restored_book is not None:
            restored_books.append(restored_book)

    return restored_books


books = [
    Book("파이썬 기초", 20000),
    EBook("파이썬 전자책", 15000, 25),
    AudioBook("파이썬 오디오북", 18000, 120)
]

save_books(books, "books_data.json")

loaded_books = load_books("books_data.json")

print(type(loaded_books))
print(type(loaded_books[0]))
print(type(loaded_books[1]))
print(type(loaded_books[2]))

for book in loaded_books:
    print(book.to_dict())

#region
# 1. save_books() 안에서 books를 json.dump()에 바로 전달하지 않고 각 객체에 to_dict()를 호출하는 이유는 무엇인가?
# 클래스 type의 객체를 바로 JSON 문자열로 직렬화할 수 없기 때문이다.
# 2. json.load(file)이 반환한 loaded_data의 전체 자료형과 내부 요소의 자료형은 각각 무엇인가?
# 전체 자료형은 list 자료형이고, 내부 요소는 dict의 자료형이다.
# 3. load_books()가 loaded_data를 그대로 return하지 않고 restored_books를 만들어 반환하는 이유는 무엇인가?
# loaded_data는 dict 자료형으로 클래스의 method를 사용할 수가 없기 때문에 restored_books를 만들어 반환하여 내부요소를 클래스 instance로 만들어 각 요소가 클래스 method를 사용할 수 있게 하기 위함이다.
#[표현 수정 후]
#load_data는 dict들을 내부 요소로 가진 list이므로 각 요소에서 Book 클래스 계열의 method를 사용할 수 없다.
#각 dict를 Book, EBook, audioBook 객체로 복원하여 속성과 클래스 메서드를 다시 사용할 수 있게 하기 위해 restored_books를 만들어 반환한다. 
# 4. save_books()에는 return문이 없다. 따라서 save_books()의 반환값은 무엇인가?
# None이다.
# 5. load_books() 실행이 끝난 뒤 loaded_books[1]은 dict와 EBook 객체 중 무엇인가?
# EBook 객체이다.
#endregion
print()
print("=== 존재하지 않는 파일 테스트 ===")

missing_books = load_books("missing_books.json")

print(missing_books)
print(type(missing_books))
print(len(missing_books))
#region
# 1. missing_books.json이 없을 때 load_books()의 어느 except가 실행되는가?
# except FileNotFoundError:
# 2. missing_books의 자료형은 무엇인가?
# list 자료형이다.
# 3. len(missing_books)의 결과는 얼마인가?
# 0
# 4. 오류가 발생했는데도 프로그램이 강제로 종료되지 않는 이유는 무엇인가?
# 예외 처리를 하여 오류가 발생하여도 반환값으로 이어 실행할 수 있게 만들었다.
#[표현 보충]
#FileNotFoundError를 except에서 잡아 처리했으므로 예외가 함수 밖으로 전달되지 않는다.
#그리고 빈 리스트를 반환하므로 이후 코드가 계속 실행된다.
# 5. except에서 None이 아니라 빈 list를 반환하는 이유는 무엇인가?
# 빈 list를 반환하여 list안에 요소를 넣어 파일이 없어도 사용할 수 있게 만들기 위해서
#[표현 보충]
#도서 목록을 사용하는 이후 코드가 항상 list를 받도록 하기 위해서다.
#빈 list는 반복하거나 len()을 사용하고 요소를 추가할 수 있지만, None에는 이러한 list 연산을 바로 사용할 수 없다.
#endregion
print()
print("=== 비어 있는 파일 테스트 ===")

empty_books = load_books("empty_books.json")

print(empty_books)
print(type(empty_books))
print(len(empty_books))
#region
# 1. empty_books.json은 존재하는데도 왜 정상적으로 데이터를 읽지 못하는가?
# 파일 안의 내용이 비어있기 때문이다.
# 2. 파일을 여는 open()과 json.load() 중 어느 부분에서 오류가 발생하는가?
# json.load()에서 오류가 발생한다.
# 3. 발생하는 예외의 종류는 무엇인가?
# json.JSONDecodeError
# 4. empty_books의 자료형과 길이는 각각 무엇인가?
# list 자료형으로 길이는 0이다.
# 5. 내용이 []인 파일과 완전히 비어 있는 파일은 json.load()의 결과에서 어떤 차이가 있는가?
# 내용이 []인 파일은 빈 리스트가 내용으로 들어있는 정상적인 파일이지만, 완전히 비어있는 파일은 예외처리 등 어떠한 조치도 취하지 않으면 파일 내용을 역직렬화하는 과정에서 오류가 발생하는 결과가 발생하는 차이가 있다.
#[명확하게]
#내용이 []인 파일은 정상적인 JSON 배열이므로 json.load()가 빈 list를 반환한다.
#완전히 비어 있는 파일은 유효한 JSON 데이터가 없으므로 json.load()가 값을 반환하지 못하고 JSONDecodeError를 발생시킨다.
#endregion









