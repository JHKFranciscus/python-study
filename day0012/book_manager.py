def print_books(books):
    print("[도서목록]")

    for book in books:        
        print(f"{book["title"]} / {book["price"]}원")

def find_book(books, target_title):
    for book in books:
        if target_title == book["title"]:
            return book
        
    return None

def add_book(books, title, price):
        new_book = {"title": title, "price": price}
        books.append(new_book)

def update_book_price(books, target_title, changed_price):
    found_book = find_book(books, target_title)
    
    if found_book is not None:
        found_book["price"] = changed_price
        return True
    else:
        return False

        
books = [
    {"title": "파이썬 기초", "price": 18000},
    {"title": "자료구조 입문", "price": 22000},
    {"title": "알고리즘 연습", "price": 25000}
]

print_books(books)

new_title = input("추가할 책 제목: ")
new_price = int(input("추가할 책 가격: "))
add_book(books, new_title, new_price)
print_books(books)

target_title = input("가격을 수정할 책 제목: ")
changed_price = int(input("새 가격: "))
update_result = update_book_price(books, target_title, changed_price)

if update_result:
    print("가격을 수정했습니다.")
    print_books(books)
else:
    print("해당 책이 없습니다.")
