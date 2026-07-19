def print_all_books(books):
    for book in books:
        print(book['title'], book['price'])

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
        found_book["price"] =  changed_price
        return True
    
    return False

def delete_book(books, target_title):
    found_book = find_book(books, target_title)
    if found_book is not None:
        books.remove(found_book)
        return True
    
    return False

books = [
    {"title": "파이썬 기초", "price": 15000},
    {"title": "자료구조 입문", "price": 20000}
]

print_all_books(books)

found_book = find_book(books, "파이썬 기초")
print(found_book)

add_book(books, "알고리즘 첫걸음", 18000)
print_all_books(books)

update_result = update_book_price(books, "자료구조 입문", 23000)
print(update_result)
print_all_books(books)

delete_result = delete_book(books, "파이썬 기초")
print(delete_result)
print_all_books(books)

not_found_result = delete_book(books, "없는 책")
print(not_found_result)