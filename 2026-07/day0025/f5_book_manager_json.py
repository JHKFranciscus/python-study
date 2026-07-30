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

    def print_info(self):
        print(
            f"[일반 도서] 제목: {self.title} | "
            f"가격: {self.price}원"
        )


class EBook(Book):
    def __init__(self, title, price, file_size):
        super().__init__(title, price)
        self.file_size = file_size

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "ebook"
        data["file_size"] = self.file_size
        return data

    def print_info(self):
        print(
            f"[전자책] 제목: {self.title} | "
            f"가격: {self.price}원 | "
            f"파일 크기: {self.file_size}MB"
        )


class AudioBook(Book):
    def __init__(self, title, price, play_time):
        super().__init__(title, price)
        self.play_time = play_time

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "audiobook"
        data["play_time"] = self.play_time
        return data

    def print_info(self):
        print(
            f"[오디오북] 제목: {self.title} | "
            f"가격: {self.price}원 | "
            f"재생 시간: {self.play_time}분"
        )


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

class BookManager:
    def __init__(self, filename):
        self.filename = filename
        self.books = load_books(filename)

    def add_book(self, book):
        self.books.append(book)
        print("도서를 등록했습니다.")

    def show_all_books(self):
        if len(self.books) == 0:
            print("등록된 도서가 없습니다.")
            return

        for book in self.books:
            book.print_info()

    def save(self):
        save_books(self.books, self.filename)
        print("도서 정보를 파일에 저장했습니다.")

    def search_book(self, title):
        search_title = title.strip()

        for book in self.books:
            if book.title == search_title:
                book.print_info()
                return book

        print("도서를 찾을 수 없습니다.")
        return None

    def update_book_price(self, title, new_price):
        search_title = title.strip()

        if search_title == "":
            print("도서 제목을 입력해야 합니다.")
            return False

        try:
            converted_price = int(new_price)

        except (ValueError, TypeError):
            print("가격은 숫자로 입력해야 합니다.")
            return False

        if converted_price < 0:
            print("가격은 0원 이상이어야 합니다.")
            return False

        for book in self.books:
            if book.title == search_title:
                book.price = converted_price
                print("도서 가격을 변경했습니다.")
                return True

        print("도서를 찾을 수 없습니다.")
        return False

    def delete_book(self, title):
        search_title = title.strip()

        for index, book in enumerate(self.books):
            if book.title == search_title:
                deleted_book = self.books.pop(index)
                print("도서를 삭제했습니다.")
                return deleted_book

        print("도서를 찾을 수 없습니다.")
        return None


manager = BookManager("managed_books.json")

if len(manager.books) == 0:
    manager.add_book(
        Book("자료구조 기초", 22000)
    )

    manager.add_book(
        EBook("알고리즘 전자책", 17000, 30)
    )

    manager.add_book(
        AudioBook("파이썬 오디오 강의", 19000, 150)
    )

print("=== 전체 도서 조회 ===")
manager.show_all_books()
#region
# 1. BookManager 객체를 생성할 때 managed_books.json이 없다면 self.books에는 무엇이 저장되는가?
# 빈 리스트
# 2. manager.add_book()을 세 번 실행한 뒤 manager.books의 자료형과 길이는 각각 무엇인가?
# list 자료형이고, 길이는 3이다.
# 3. manager.books 안의 세 요소는 모두 같은 클래스의 객체인가? 각 요소의 실제 클래스는 무엇인가?
# 아니다. Book class, EBook class, AudioBook class이다.
# 4. show_all_books()에서 모든 객체에 똑같이 book.print_info()를 호출할 수 있는 이유는 무엇인가?
# book이 가리키는 객체는 여러 class로부터 생산된 객체들의 원본이기 때문이다.
#[수정 후]
#Book, EBook, AudioBook이 모두 print_info() 메서드를 가지고 있기 때문이다.
# 반복문에서는 같은 이름의 메서드를 호출하지만, 실제로 book이 가리키는 객체의 클래스에 따라 오버라이딩된 print_info()가 각각 실행된다.
# 5. 현재 코드에서는 add_book()을 실행한 직후 managed_books.json에도 도서가 저장되는가? 그 이유는 무엇인가?
# 저장되지 않는다. managed_books.json에 저장하는 것은 save()이기 때문이다. add_book()은 여러 Book class의 instance를 dict 자료형으로 반환 한 것을 list에 담을 뿐이다. 
#[수정 후]
#저장되지 않는다. 
#add_book()은 Book 계열 객체를 self.books 리스트에 추가할 뿐이며, save()가 호출되어야 각 객체가 dict로 변환된 뒤 managed_books.json에 기록된다.
#endregion
manager.save()
#region
# 1. manager.save()를 호출하면 managed_books.json이 새로 생성되는가?
# 빈 list가 반환될 뿐 새로 생성되지는 않는다.
#[수정 후]
# save_books()가 managed_books.json을 w 모드로 열기 때문에 파일이 없으면 새로 생성한 뒤 JSON 데이터를 기록한다.
# 2. managed_books.json의 최상위 구조는 JSON object와 JSON array 중 무엇인가?
# JSON array
# 3. managed_books.json 안에는 Python의 Book 객체 자체가 저장되는가? 아니면 객체에서 변환된 데이터가 저장되는가?
# 객체에서 변환된 데이터가 저장된다.
# 4. manager.save()를 호출해도 manager.books 안의 객체들이 dict로 바뀌는가?
# 그렇다. save는 save_books를 호출하고, save_books가 안의 객체들을 dict으로 바꾼다.
#[수정 후]
# 바뀌지 않는다.
# 각 객체의 to_dict()가 새로운 dict를 반환하고, 그 dict는 별도의 books_data 리스트에 저장된다.
# 따라서 manager.books에는 기존의 Book 계열 객체들이 그대로 남는다.
# 5. 저장된 전자책 데이터에는 공통 속성 외에 어떤 추가 속성이 포함되는가?
# file_size라는 추가 속성이 포함된다.
#endregion
print()
print("=== 저장 파일 다시 불러오기 ===")

reloaded_manager = BookManager("managed_books.json")

print(type(reloaded_manager.books))

for book in reloaded_manager.books:
    print(type(book))

reloaded_manager.show_all_books()
#region
# 1. reloaded_manager.books의 전체 자료형은 무엇인가?
# list 자료형
# 2. reloaded_manager.books 안에는 dict와 Book 계열 객체 중 무엇이 들어 있는가?
# Book 계열 객체가 들어있다.
# 3. reloaded_manager.books[1]의 실제 클래스는 무엇인가?
# EBook class이다.
# 4. manager.books[1]과 reloaded_manager.books[1]은 같은 객체인가, 같은 데이터를 가진 서로 다른 객체인가?
# 같은 데이터를 가진 서로 다른 객체이다.
# 5. reloaded_manager를 생성할 때 "저장 파일이 없어 빈 목록으로 시작합니다."가 출력되는가? 그 이유는 무엇인가?
# 출력되지 않는다. 그 이유는 그 위에 있는 manager.save()가 파일에 목록들을 생성해놓았기 때문이다.
#endregion
print()
print("=== 존재하는 도서 검색 ===")

found_book = reloaded_manager.search_book("알고리즘 전자책")

print(type(found_book))


print()
print("=== 존재하지 않는 도서 검색 ===")

not_found_book = reloaded_manager.search_book("존재하지 않는 책")

print(not_found_book)
#region
# 1. "  알고리즘 전자책  "을 전달해도 검색할 수 있는가? 그 이유는 무엇인가?
# 검색할 수 있다. search_book method가 알고리즘 전자책 옆의 공백을 지워버린 후에 비교하기 때문이다.
# 2. 제목이 일치하는 도서를 찾으면 search_book()은 dict와 Book 계열 객체 중 무엇을 반환하는가?
# Book 계열 객체를 반환한다.
# 3. found_book의 실제 클래스는 무엇인가?
# Book 계열의 클래스이다.
#[구체화 필요]
#found_book의 실제 클래스는 EBook이다.
# 4. 제목이 일치하는 도서를 찾은 뒤 즉시 return하는 이유는 무엇인가?
# 이 method는 도서가 존재하는지 검색하는 기능만을 담당하고 있기 때문이다.
#[수정 후]
#제목이 일치하는 객체를 이미 찾았으므로 이후 요소를 불필요하게 더 비교하지 않고, 찾은 객체를 반환하면서 함수 실행을 종료하기 위해서다.
# 5. 검색 결과가 없을 때 not_found_book에는 무엇이 저장되는가?
# None
# 6. 이 검색의 시간 복잡도는 최악의 경우 무엇인가?
# O(n)이다. 이 검색은 list에 저장된 Book계열 클래스의 instance를 하나씩 순차적으로 비교하는 검색으로 시간 복잡도는 최악의 경우 O(n)이다.
#endregion
print()
print("=== 존재하는 도서 가격 변경 ===")

update_result = reloaded_manager.update_book_price(
    "알고리즘 전자책",
    21000
)

print(update_result)

updated_book = reloaded_manager.search_book(
    "알고리즘 전자책"
)

print(updated_book.price)


print()
print("=== 존재하지 않는 도서 가격 변경 ===")

failed_update_result = reloaded_manager.update_book_price(
    "없는 도서",
    30000
)

print(failed_update_result)
#region
# 1. update_book_price()가 제목이 일치하는 도서를 찾으면 어떤 객체의 어떤 속성을 변경하는가?
# EBook 계열의 객체의 price 속성이 변한다.
# 2. 가격을 변경한 뒤 update_result에는 무엇이 저장되는가?
# True
# 3. updated_book.price의 예상 출력값은 얼마인가?
# 21000
# 4. book.price를 변경하면 reloaded_manager.books 안의 원본 객체에도 변경이 남는가? 그 이유는 무엇인가?
# 남는다. book은 reloaded_manager.books의 요소이고 이는 Book계열 class의 instance를 가리키고 있기 때문에 그 instance 속성의 값을 변경하기 때문이다 이는 원본 객체에도 변경이 남는다는 뜻이다.
# 5. 존재하지 않는 도서의 가격 변경을 시도하면 failed_update_result에는 무엇이 저장되는가?
# False
# 6. 현재 update_book_price()를 실행하는 것만으로 managed_books.json의 가격도 즉시 변경되는가? 그 이유는 무엇인가?
# 되지 않는다. 이는 파일 자체를 건드리는 것이 아니라 파일을 복사한 객체를 건드리는 것이기 때문에 save()작업을 진행해줘야지 직렬화와 파일 내에 쓰기가 되면서 managed_books.json의 가격도 변경된다.
#[표현 수정]
#되지 않는다. 파일 자체가 아니라 JSON 파일에 저장된 텍스트를 json.load()가 역직렬화하여 만든 딕셔너리를 담은 리스트를 이용해, 메모리에 새로운 클래스 객체를 생성한다.
# update_book_price()는 메모리에 존재하는 EBook 객체의 price 속성만 변경한다.
# JSON 파일의 내용은 자동으로 변경되지 않으므로, reloaded_manager.save()를 호출하여 현재 객체 목록을 다시 직렬화하고 파일에 기록해야 변경된 가격이 저장된다.
#endregion
print()
print("=== 저장 전 파일 가격 확인 ===")

before_save_manager = BookManager("managed_books.json")

before_save_book = before_save_manager.search_book(
    "알고리즘 전자책"
)

print(before_save_book.price)


print()
print("=== 변경된 가격 저장 ===")

reloaded_manager.save()


print()
print("=== 저장 후 파일 가격 확인 ===")

after_save_manager = BookManager("managed_books.json")

after_save_book = after_save_manager.search_book(
    "알고리즘 전자책"
)

print(after_save_book.price)
#region
# 1. before_save_book.price의 예상 출력값은 얼마인가?
# 17000
# 2. reloaded_manager에서는 가격이 21000원인데, before_save_manager에서는 왜 이전 가격이 나오는가?
# "managed_books.json"파일에 저장되어있는 가격은 17000이기 때문이다.
# 3. reloaded_manager.save()는 어느 객체 목록을 파일에 저장하는가?
# reloaded_manager에 저장된 Book 관련 class instance가 담긴 객체 목록을 저장한다.
# 4. after_save_book.price의 예상 출력값은 얼마인가?
# 21000
# 5. before_save_book과 after_save_book은 같은 객체인가? 아니면 서로 다른 객체인가?
# 서로 다른 객체이다.
# 6. JSON 파일을 수정하려면 반드시 파일 내부의 문자열을 직접 찾아 바꿔야 하는가? 현재 프로그램은 어떤 순서로 파일 내용을 갱신하는가?
# 메모리에 존재한는 관련 클래스의 instance를 통하여 instance의 attribute value를 직접 변경하고, 그 instance들이 담긴 list를 순차탐색을 이용하여 dict로 변경함과 동시에 새로만든 빈 리스트에 담아준다. 그 후 그 리스트를 이용하여 리스트 내부의 dict 요소들을 직렬화 하여 JSON 문자열로 바꾼 후 그것을 w모드를 이용하여 파일 전체를 다시 기록한다.
#[수정 후]
#JSon 파일 내부의 텍스트를 직접 찾아 수정할 필요는 없다.
#먼저 메모리에 있는 Book 계열 객체의 속성을 변경한다.
#save_books()가 각 객체의 to_dict()를 호출하여 새로운 dict를 담은 list를 만든다. 
#json.dump()가 그 list를 JSON 텍스트로 직렬화하여 w모드로 연 파일에 직접 기록한다.
#w모드는 기존 파일 내용을 비우고 현재 전체 데이터를 다시 기록한다.
#endregion
print()
print("=== 존재하는 도서 삭제 ===")

deleted_book = after_save_manager.delete_book(
    "파이썬 오디오 강의"
)

print(type(deleted_book))
print(len(after_save_manager.books))

after_save_manager.show_all_books()


print()
print("=== 존재하지 않는 도서 삭제 ===")

not_deleted_book = after_save_manager.delete_book(
    "없는 도서"
)

print(not_deleted_book)
#region
# 1. enumerate(self.books)를 사용하는 이유는 무엇인가?
# 목록에서 제거하고 반환한 요소의 순번을 확인하기 위해서이다.
#[수정 후]
#각 도서 객체와 그 객체가 들어 있는 리스트의 인덱스를 함께 얻고, 제목이 일치할 때 해당 인덱스를 pop()에 전달하여 삭제하기 위해서다.
# 2. self.books.pop(index)는 리스트에서 객체를 삭제하기만 하는가? 아니면 삭제한 객체를 반환하기도 하는가?
# 삭제만 하는 것이 아니라 삭제한 객체를 deleted_book에 반환한다.
# 3. "파이썬 오디오 강의"를 삭제한 뒤 deleted_book의 실제 클래스는 무엇인가?
# AudioBook 클래스
# 4. 삭제 후 len(after_save_manager.books)의 예상 결과는 얼마인가?
# 2
# 5. 삭제 후 after_save_manager.show_all_books()에는 어떤 두 도서만 출력되는가?
# 자료구조 기초와 알고리즘 전자책
# 6. 존재하지 않는 도서를 삭제하려 하면 not_deleted_book에는 무엇이 저장되는가?
# None
# 7. 현재 delete_book()만 실행한 상태에서 managed_books.json에서도 오디오북이 즉시 삭제되는가? 그 이유는 무엇인가?
# 삭제되지 않는다. 이는 JSON 파일에 담긴 텍스트를 복사한 객체를 json.load()로 역직렬화하여 만든 dictionary를 Book관련 instance로 만든 요소들을 담은 list를 이용하기 때문에 파일 원본의 내용에는 변화를 주지 않는다.
#[추가]
# delete_book()은 메모리에 있는 after_save_manager.books에서 AudioBook 객체를 제거할 뿐 JSON 파일을 직접 변경하지 않는다.
# after_save_manager.save()를 호출해야 남은 두 객체가 dict로 변환되고, JSON 파일 전체가 다시 기록되어 삭제 결과가 파일에도 반영된다.
#endregion
print()
print("=== 삭제 전 파일 도서 수 확인 ===")

before_delete_save_manager = BookManager(
    "managed_books.json"
)

print(len(before_delete_save_manager.books))
before_delete_save_manager.show_all_books()


print()
print("=== 삭제 결과 저장 ===")

after_save_manager.save()


print()
print("=== 삭제 후 파일 도서 수 확인 ===")

after_delete_save_manager = BookManager(
    "managed_books.json"
)

print(len(after_delete_save_manager.books))
after_delete_save_manager.show_all_books()

deleted_search_result = (
    after_delete_save_manager.search_book(
        "파이썬 오디오 강의"
    )
)

print(deleted_search_result)
#region
# 1. before_delete_save_manager.books의 길이는 얼마인가?
# 3
# 2. 메모리의 after_save_manager.books에는 두 권만 있는데, before_delete_save_manager에는 왜 세 권이 들어 있는가?
# 파일 원본은 아직 수정되지 않았기 때문이다.
# 3. after_save_manager.save()는 삭제된 AudioBook 객체까지 다시 파일에 저장하는가?
# 삭제된 AudioBook 객체는 다시 파일에 저장하지 않는다.
# 4. after_delete_save_manager.books의 길이는 얼마인가?
# 2
# 5. 삭제 후 파일에서 다시 불러온 목록에는 어떤 두 종류의 객체가 들어 있는가?
# Book class의 객체와 EBook class의 객체가 들어있다.
# 6. deleted_search_result에는 무엇이 저장되는가?
# 삭제된 AudioBook정보가 저장된다.
#[수정 후]
#삭제 후 다시 불러온 목록에는 해당 오디오북이 없으므로 search_book()이 반환한 None이 저장된다.
# 7. 현재 프로그램의 가격 변경과 삭제가 JSON 파일 전체를 다시 기록하는 방식인 이유는 무엇인가?
#  파일을 역직렬화하여 Python 객체로 만든 후 그 list의 요소를 이용하여 수정한 후 다시 집어 넣어 그 내용 전체를 다시 기록하기 때문이다.
#[수정 후]
#프로그램은 JSON 파일의 특정 문자열을 직접 수정하지 않는다. 먼저 JSON 파일을 역직렬화한 데이터로 Book 계열 개체 목록을 만들고, 메모리에서 객체의 속성을 변경하거나 객체를 삭제한다.
#저장할 때 남아 있는 모든 객체를 dict로 변환한 뒤, json.dump()가 그 전체 목록을 w 모드의 파일에 다시 기록하기 때문이다.
#endregion
print()
print("=== 가격 입력 검증 테스트 ===")

validation_manager = BookManager(
    "managed_books.json"
)


print("--- 숫자가 아닌 가격 ---")

invalid_price_result = (
    validation_manager.update_book_price(
        "알고리즘 전자책",
        "삼만원"
    )
)

print(invalid_price_result)

checked_book = validation_manager.search_book(
    "알고리즘 전자책"
)

print(checked_book.price)
print(type(checked_book.price))


print("--- 음수 가격 ---")

negative_price_result = (
    validation_manager.update_book_price(
        "알고리즘 전자책",
        -1000
    )
)

print(negative_price_result)
print(checked_book.price)


print("--- 숫자로 된 문자열 가격 ---")

valid_string_result = (
    validation_manager.update_book_price(
        "알고리즘 전자책",
        "23000"
    )
)

print(valid_string_result)
print(checked_book.price)
print(type(checked_book.price))


print("--- 빈 제목 ---")

empty_title_result = (
    validation_manager.update_book_price(
        "   ",
        30000
    )
)

print(empty_title_result)
#region
# 1. "삼만원"을 int()로 변환할 때 어떤 예외가 발생하는가?
# TypeError
#[수정 후]
#정수로 해석할 수 없는 문자열이므로 ValueError가 발생한다.
# 2. 숫자가 아닌 가격을 전달하면 invalid_price_result에는 무엇이 저장되는가?
# False
# 3. 숫자가 아닌 가격 변경 실패 후 checked_book.price는 기존 21000과 "삼만원" 중 무엇인가?
# 21000
# 4. -1000은 int로 변환할 수 있는데도 가격을 변경하지 않는 이유는 무엇인가?
# -1000은 int로 변환이 되었으나 그 뒤에 나오는 if converted_price < 0:이라는 조건에 부합하여 False로 반환되었다.
# 5. "23000"을 전달하면 객체의 price에는 문자열과 int 중 어떤 자료형이 저장되는가?
# 어떤 자료형도 저장되지 않고, False값을 반환하고 끝난다.
#[수정 후]
#int로 변환된 정수 23000이 저장된다.
# 6. 유효한 가격 변경 후 checked_book.price와 type(checked_book.price)의 예상 출력은 무엇인가?
# checked_book.price는 유효한 가격이 출력 될 것이고, type(checked_book.price)는 int가 출력될 것이다.
#[구체적인 값]
#23000
#<class 'int'>
# 7. 제목으로 공백만 전달하면 empty_title_result에는 무엇이 저장되는가?
# False
# 8. 현재 테스트가 끝난 직후 managed_books.json의 전자책 가격은 21000원과 23000원 중 무엇인가? 그 이유는 무엇인가?
# 23000. update_book_price method는 JSON파일을 복사한 객체를 역직렬화 하여 파이썬 객체를 만들고 그 안의 요소의 속성 값을 변경하였을 뿐, 그 변경된 객체를 직렬화하여 파일에 전달하지 않았기 때문이다.
#[수정 후]
#21000
#update_book_price()는 메모리 객체의 price만 23000으로 변경하면, validation_manager.save()를 호출하지 않았으므로 변경된 값이 JSON 파일에는 기록되지 않았기 때문이다.
#endregion














