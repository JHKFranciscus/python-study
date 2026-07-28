class Book:
    category = "도서"
    book_count = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Book.book_count += 1

    def show_info(self):
        # print(f"[{Book.category}] 제목: {self.title}, 가격: {self.price}원")
        print(f"[{type(self).category}] 제목: {self.title}, 가격: {self.price}원")

    @staticmethod
    def is_valid_title(title):
        return len(title.strip()) != 0

    @staticmethod
    def is_valid_price(price):
        return price >= 0

    def change_price(self, new_price):
        is_valid = self.is_valid_price(new_price)

        if is_valid is True:
            self.price = new_price
            return True

        return False

    @classmethod
    def show_book_count(cls):
        # print(f"생성된 도서 수: {Book.book_count}")
        print(f"생성된 도서 수: {cls.book_count}")

#region
# book1 = Book("파이썬 기초", 20000)
# book2 = Book("자료구조 입문", 25000)

# book1.show_info()
# book2.show_info()
# Book.show_book_count()

# print(Book.is_valid_title("알고리즘 기초"))
# print(Book.is_valid_title("   "))

# print(book1.change_price(18000))
# book1.show_info()

# print(book1.change_price(-1000))
# book1.show_info()


# [도서] 제목: 파이썬 기초, 가격: 20000원
# [도서] 제목: 자료구조 입문, 가격: 25000원
# 생성된 도서 수: 2
# True
# False
# True
# [도서] 제목: 파이썬 기초, 가격: 18000원
# False
# [도서] 제목: 파이썬 기초, 가격: 18000원
#endregion
def find_book(books, target_title):
    target_title = target_title.strip().lower()    #target_title은 전부 이 method를 이용해서 검사를 할 것이므로 여기에서 입력 정규화를 해주게 더 간단해진다.

    for book in books:
        if target_title == book.title.strip().lower():
            return book

    return None

def add_book(books):
    title = input("제목: ").strip()

    # if len(title) == 0:
    #     print("제목은 비워 둘 수 없습니다.")
    #     return False
    if Book.is_valid_title(title) is False:
        print("제목은 비워 둘 수 없습니다.")
        return

    try:
        price = int(input("가격: "))

    except ValueError:
        print("가격은 정수로 입력해야합니다.")
        # return False
        return

    # if price < 0:
    #     print("가격은 0 이상이어야 합니다.")
    #     return False
    if Book.is_valid_price(price) is False:
        print("가격은 0 이상이어야 합니다.")
        return

    book = Book(title, price)
    books.append(book)
    print("도서가 등록되었습니다.")

def show_all_books(books):
    if len(books) == 0:
        print("등록된 도서가 없습니다.")
        return None

    for book in books:
        book.show_info()

def search_book(books):
    # target_title = input("찾을 책 제목: ").strip().lower()
    target_title = input("찾을 책 제목: ")

    found = find_book(books, target_title)

    if found is None:
        print("해당 도서를 찾을 수 없습니다.")
    else:
        found.show_info()
    
def update_book_price(books):
    # target_title = input("변경할 책 제목: ").strip().lower()
    target_title = input("변경할 책 제목: ")

    found = find_book(books, target_title)

    if found is None:
        print("해당 도서를 찾을 수 없습니다.")
    else:
        try:
            new_price = int(input("새 가격: "))

        except ValueError:
            print("가격은 0 이상의 정수로 입력해주세요.")
            return False

        # if new_price < 0:
        #     print("가격은 0 이상의 정수로 입력해주세요.")
        #     return False

        changed = found.change_price(new_price)

        if changed is True:
            print("가격이 변경되었습니다.")
        else:
            print("가격은 0 이상이어야합니다.")

def delete_book(books):
    target_title = input("삭제할 도서 제목: ")

    found_book = find_book(books, target_title)

    if found_book is None:
        print("해당 도서를 찾을 수 없습니다.")
        return

    books.remove(found_book)
    print("도서가 삭제되었습니다.")
        

books = []

print("1. 도서 등록")
print("2. 전체 도서 조회")
print("3. 제목 검색")
print("4. 가격 변경")
print("5. 생성된 도서 수 조회")
print("6. 도서 삭제")
print("0. 종료")

while True:
    print()

    menu = input("메뉴 선택: ")

    if menu == "1":
        add_book(books)

    elif menu == "2":
        show_all_books(books)

    elif menu == "3":
        search_book(books)

    elif menu == "4":
        update_book_price(books)

    elif menu == "5":
        Book.show_book_count()

    elif menu == "6":
        delete_book(books)

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴를 선택해 주세요.")