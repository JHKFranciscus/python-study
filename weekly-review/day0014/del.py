
def find_book(books, target_title):
    for book in books:
        if book["title"] == target_title:
            return book

    return None

books = [
    {"title": "파이썬 기초", "price": 15000},
    {"title": "자료구조 입문", "price": 20000}
]


found_book = find_book(books, "파이썬 기초")

print(found_book is books[0])
print(id(found_book) == id(books[0]))

