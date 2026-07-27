class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        print("제목:", self.title)
        print("저자:", self.author)
        print("가격:", self.price)

    def change_price(self, new_price):
        self.price = new_price


def add_book(books, title, author, price):
    new_book = Book(title, author, price)
    books.append(new_book)

    print("도서 등록 완료:", new_book.title)

def show_all_books(books):
    print("저장된 도서 수:", len(books))
    print()

    for book in books:
        book.show_info()
        print()

def find_book(books, target_title):
    for book in books:
        if book.title == target_title:
            return book

    return None

def update_book_price(books, target_title, new_price):
    found_book = find_book(books, target_title)

    if found_book is not None:
        found_book.change_price(new_price)
        return True

    return False

books = []
#region
# book1 = Book("파이썬 기초", "김개발", 15000)
# book2 = Book("자료구조 입문", "이코딩", 20000)

# books.append(book1)
# books.append(book2)
#endregion
add_book(books, "파이썬 기초", "김개발", 15000)
add_book(books, "자료구조 입문", "이코딩", 20000)
#region
# print("저장된 도서 수:", len(books))

# print()

# for book in books:
#     book.show_info()
#     print()
#endregion
#region
# show_all_books(books)
# print()
# print("빈 목록 조회")
# empty_books = []
# show_all_books(empty_books)
#endregion
#region
# print()
# found_book = find_book(books, "자료구조 입문")
# if found_book is not None:
#     print("검색 성공")
#     found_book.show_info()
# else:
#     print("검색 결과가 없습니다.")

# print()
# found_book = find_book(books, "운영체제 입문")
# if found_book is not None:
#     print("검색 성공")
#     found_book.show_info()
# else:
#     print("검색 결과가 없습니다.")
#endregion
#region
print()
is_updated = update_book_price(books, "자료구조 입문", 25000)

if is_updated:
    print("가격 변경 성공")
else:
    print("변경할 도서가 없습니다.")

show_all_books(books)

is_updated = update_book_price(books, "운영체제 입문", 30000)

if is_updated:
    print("가격 변경 성공")
else:
    print("변경할 도서가 없습니다.")
#endregion
