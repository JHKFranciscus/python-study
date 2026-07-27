class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self. price = price

    # def show_info(self, title, author, price):
    def show_info(self):
        print("title: ", self.title)
        print("author: ", self.author)
        print("price: ", self.price)

    def change_price(self, new_price):
        self.price = new_price

def add_book(books, title, author, price):
    new_book = Book(title, author, price)

    books.append(new_book)
    return new_book

def show_all_books(books):
    if not books:
        return False
    
    for book in books:
        # book.show_info(book.title, book.author, book.price)
        book.show_info()

    return True

def find_book(books, target_title):
    for book in books:
        if target_title == book.title:
            return book

    return None

def update_book_price(books, target_title, new_price):
    book = find_book(books, target_title)

    if book is not None:
        book.change_price(new_price)
        return True

    return False

books = []

print("1. 새 책 등록")
print("2. 전체 목록 조회")
print("3. 책 검색")
print("4. 책 가격 변경")
print("5. 종료")

while True:
    print()


    menu = input("메뉴 입력: ")

    if menu == "1":
        # title = input("제목을 입력해주세요: ")
        # author = input("작가를 입력해주세요: ")
        # price = input("가격을 입력해주세요: ")
        # Book.add_book(books, title, author, price)
        book1 = add_book(books, "파이썬 기초", "김개발", 15000)
        book2 = add_book(books, "자료구조 입문", "이코딩", 20000)
        book3 = add_book(books, "운영체제 기초", "박컴퓨터", 30000)

    elif menu == "2":
        print("저장된 도서 수: ", len(books))

        show = show_all_books(books)

        if show is False:
            print("책이 없습니다.")

    elif menu == "3":
        target_title = input("검색할 제목을 입력해주세요: ")
        found = find_book(books, target_title)

        if found is not None:
            # print(found)
            print("검색 성공")
            found.show_info()
        else:
            print("해당 제목과 같은 책이 없습니다.")

    elif menu == "4":
        target_title = input("가격을 변경할 책 제목을 알려주세요: ")
        # new_price = input("변경할 가격을 알려주세요: ")
        try:
            new_price = int(input("변경할 가격을 알려주세요: "))
        except ValueError:
            print("가격은 숫자로 입력해주세요.")
            continue
        
        is_update = update_book_price(books, target_title, new_price)

        if is_update is False:
            print("해당 도서는 존재하지 않습니다.")

    elif menu == "5":
        print("프로그램 종료")
        break

    else:
        print("올바른 메뉴를 입력해주세요.")
