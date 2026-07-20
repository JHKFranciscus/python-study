def find_book(books, search_title):
    normalized_search_title = search_title.strip().lower()

    for book in books:
        normalized_book_title = book["title"].strip().lower()

        if normalized_book_title == normalized_search_title:
            return book
    
    return None

books = [
    {"title": "Python Basic", "price": 15000},
    {"title": "Java Programming", "price": 18000},
    {"title": "Data Structure", "price": 22000},
]

search_title = input("검색할 도서 제목: ")

found_book = find_book(books, search_title)

if found_book is None:
    print("도서를 찾지 못했습니다.")
else:
    print("도서를 찾았습니다.")
    print("제목:", found_book["title"])
    print("가격:", found_book["price"])