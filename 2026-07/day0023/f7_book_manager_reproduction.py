class Book:
    category = "도서"
    book_count = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Book.book_count += 1

    def show_info(self):
        print(f"[{type(self).category}] 제목: {self.title}, 가격: {self.price}원")

    @staticmethod
    def is_valid_title(target_title):
        clean_title = target_title.strip()

        if clean_title == "":
            return None

        return clean_title
    
    @staticmethod
    def is_valid_price(price):
        #region
        # new_price = new_price.strip()
        # try:
        #     clean_price = int(new_price)

        # except ValueError:
        #     return None

        # if clean_price < 0:
        #     return False

        # return clean_price
        #endregion
        return price >= 0

    def change_price(self, new_price):
        # self.price = new_price
        # return
        if self.is_valid_price(new_price):
            self.price = new_price
            return True

        return False

    @classmethod
    def show_book_count(cls):
        print(f"생성된 도서 수: {cls.book_count}")


def find_book(books, target_title):
    found_title = Book.is_valid_title(target_title)

    if found_title == None:
        return False

    for book in books:
        if book.title.strip().lower() == found_title.lower():
            return book

    return None
    
def add_book(books):
    new_title = input("새 도서 제목: ")
    title = Book.is_valid_title(new_title)

    if title is None:
        print("공백은 입력할 수 없습니다.")
        return
    #region
    # new_price = input("새 도서 가격: ")
    # price = Book.is_valid_price(new_price)

    # if price == None:
    #     print("0 이상의 정수를 입력해주세요.")
    #     return
    
    # elif price == False:
    # elif price is False:
    #     print("0 이상의 정수를 입력해주세요.")
    #     return
    #endregion
    try:
        price = int(input("새 도서 가격: "))
    except ValueError:
        print("가격은 정수로 입력해주세요.")
        return

    if Book.is_valid_price(price) is False:
        print("가격은 0 이상이어야 합니다.")
        return

    new_book = Book(title, price)
    books.append(new_book)
    print("새로운 도서를 추가했습니다.")


def show_all_books(books):
    if len(books) == 0:
        print("등록된 도서가 없습니다.")

    for book in books:
        book.show_info()

def search_book(books):
    target_title = input("찾을 도서 제목: ")

    book = find_book(books, target_title)

    if book is False:
        print("공백은 입력할 수 없습니다.")

    elif book is None:
        print("해당 도서는 존재하지 않습니다.")

    else:
        book.show_info()


def update_book_price(books):
    target_title = input("바꿀 도서 제목: ")

    book = find_book(books, target_title)

    if book is False:
        print("공백은 입력할 수 없습니다.")
        return

    if book is None:
        print("해당 도서는 존재하지 않습니다.")
        return
    #region
    # new_price = input("바꿀 가격: ")
    # change_price = Book.is_valid_price(new_price)

    # book.change_price(new_price)

    # if change_price == None:
    #     print("0 이상의 정수를 입력해주세요.")
    #     return
    
    # elif change_price == False:
    #     print("0 이상의 정수를 입력해주세요.")
    #     return

    # book.change_price(new_price)
    #endregion
    try:
        new_price = int(input("바꿀 가격: "))
    except ValueError:
        print("가격은 정수로 입력해주세요.")
        return

    changed = book.change_price(new_price)

    if changed:
        print("가격이 변경되었습니다.")
    else:
        print("가격은 0 이상이어야 합니다.")



books = []

print("1. 도서 등록")
print("2. 전체 도서 조회")
print("3. 제목 검색")
print("4. 가격 변경")
print("5. 생성된 도서 수 조회")
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

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴를 선택해 주세요.")