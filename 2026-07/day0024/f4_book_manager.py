class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
         return f"[일반 도서] 제목: {self.title}, 저자: {self.author}, 가격: {self.price}원"

    def change_price(self, new_price):
        if type(new_price) is int and new_price >= 0:
            self.price = new_price
            return True

        return False


class EBook(Book):
    def __init__(self, title, author, price, file_size, file_format):
        super().__init__(title, author, price)
        self.file_size = file_size
        self.file_format = file_format

    def show_info(self):
        return f"[전자책] 제목: {self.title}, 저자: {self.author}, 가격: {self.price}원, 파일 크기: {self.file_size}MB, 형식: {self.file_format}"


class AudioBook(Book):
    def __init__(self,title,author,price,running_time,narrator):
        super().__init__(title, author, price)
        self.running_time = running_time
        self.narrator = narrator

    def show_info(self):
        return f"[오디오북] 제목: {self.title}, 저자: {self.author}, 가격: {self.price}원, 재생 시간: {self.running_time}분, 낭독자: {self.narrator}"

    def play(self):
        return f"{self.narrator}의 낭독으로 {self.title}를 재생합니다."


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return True

    def show_all_books(self):
        books = []

        for book in self.books:
            # books = []
            book_info = book.show_info()
            books.append(book_info)

        return books

    def find_book(self, target_title):
        for book in self.books:
            if book.title == target_title:
                return book

        return None

    def change_book_price(self, target_title, new_price):
        book = self.find_book(target_title)

        if book is not None:
            # book.change_price(new_price)
            return book.change_price(new_price)

        return False

    def delete_book(self, target_title):
        del_book = self.find_book(target_title)
        if del_book is not None:
            self.books.remove(del_book)
            return True

        return False


manager = BookManager()

book1 = Book("파이썬 기초", "홍길동", 18000)

ebook1 = EBook(
    "알고리즘 입문",
    "김개발",
    22000,
    25,
    "PDF"
)

book2 = Book("자료구조", "이코딩", 25000)

audio_book = AudioBook("파이썬 이야기", "박개발", 28000, 360, "김낭독")

manager.add_book(book1)
manager.add_book(ebook1)
manager.add_book(book2)
manager.add_book(audio_book)
#region
# #전체조회
# for info in manager.show_all_books():
#     print(info)
# print()
# #일반 도서 검색
# found_book = manager.find_book("파이썬 기초")

# if found_book is not None:
#     print(found_book.show_info())
# else:
#     print("도서를 찾지 못했습니다.")

# #전자책 검색
# found_ebook = manager.find_book("알고리즘 입문")

# if found_ebook is not None:
#     print(found_ebook.show_info())
# else:
#     print("도서를 찾지 못했습니다.")
# print()
# #존재하지 않는 도서 검색
# missing_book = manager.find_book("운영체제")
# print(missing_book)
# print()
# #가격 변경
# print(manager.change_book_price("알고리즘 입문", 24000))
# print(ebook1.price)

# print(manager.change_book_price("자료구조", "27000"))
# print(book2.price)

# print(manager.change_book_price("없는 도서", 30000))
# print()
# #삭제
# print(manager.delete_book("파이썬 기초"))
# print(manager.delete_book("없는 도서"))
# print()
# for info in manager.show_all_books():
#     print(info)

# 1. manager.books 하나에 Book 객체와 EBook 객체를 함께 저장할 수 있는 이유는 무엇인가?
# Book 객체도 EBook 객체도 각자 고유한 속성을 가지고 있는 하나의 서로 다른 객체이기 때문이다.
#[수정 후]
# 파이썬 리스트는 서로 다른 종류의 객체를 함께 저장할 수 있다.
# 또한 EBook은 Book을 상속한 도서의 한 종류이므로, Book 객체와 EBook 객체를 같은 도서 목록에서 공통된 방식으로 관리할 수 있다.
# 2. show_all_books()에서 모든 객체에 똑같이 book.show_info()를 호출해도 일반 도서와 전자책의 출력 내용이 서로 다르게 나오는 이유는 무엇인가?
# 호출하는 method의 class가 달라서 호출하는 함수는 다른 함수이기 때문이다.
#[수정 후]
#EBook이 show_info()를 오버라이딩했기 때문이다.
#각 객체에서 show_info()를 호출하면 실제 객체의 클래스에 맞는 메서드가 선택된다.
#따라서 Book 객체는 Book.show_info()를, EBook 객체는 EBook.show_info()를 실행한다.
# 3. find_book()이 반환한 값이 Book 객체인지 EBook 객체인지와 관계없이 change_price()를 호출할 수 있는 이유는 무엇인가?
# Book 객체이면 Book class에서 method를 호출하면 되고, EBook 객체라면 EBook class에 호출한 method가 존재하지 않는다면 그 부모 클래스로 올라가서 method를 탐색하기 때문에 EBook class를 호출해도 Book class의 method로 올라간다.
#[수정 후]
#Book에는 change_price()가 직접 작성되어 있고, EBook은 Book을 상속하므로 Book.change_price()를 물려받는다.
# 따라서 find_book()이 book 또는 EBook 객체를 반환해도 두 객체 모두 change_price()를 호출할 수 있다.
# 4. change_book_price() 안에서 가격 검사 코드를 다시 작성하지 않고 찾은 객체의 change_price()를 호출한 이유는 무엇인가?
# 코드의 중복을 막기 위하여
# 5. find_book()이 실패했을 때 None을 반환하도록 한 이유는 무엇인가?
# 검색에 성공하여 값을 보내는 것과 대조하여 검색의 값이 없다는 것을 알려주기 위함
# 6. delete_book()에서 도서를 찾지 못한 경우 False를 반환하는 이유는 무엇인가?
# 도서 삭제를 실패했다는 것을 알리기 위해서
#endregion
#region
print(audio_book.show_info())
print(audio_book.play())

found_audio_book = manager.find_book("파이썬 이야기")

if found_audio_book is not None:
    print(found_audio_book.show_info())
    print(found_audio_book.play())

#가격변경
print(manager.change_book_price("파이썬 이야기", 30000))
print(audio_book.price)
#endregion

