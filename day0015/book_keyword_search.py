def search_books_by_keyword(books, keyword):
    normalized_keyword = keyword.strip().lower()
    found_books = []

    for book in books:
        normalized_title = book["title"].strip().lower()

        if normalized_keyword in normalized_title:
            found_books.append(book)
    
    return found_books


books = [
    {"title": "Python Basic", "price": 15000},
    {"title": "Advanced Python", "price": 24000},
    {"title": "Java Programming", "price": 18000},
    {"title": "Data Structure", "price": 22000},
    {"title": "Python Data Analysis", "price": 27000},
]

keyword = input("검색할 제목 키워드: ")

found_books = search_books_by_keyword(books, keyword)

print("검색된 도서 수:", len(found_books))

if found_books:
    print("검색 결과:")
    for book in found_books:
        print()
        print("제목:", book["title"])
        print(f"가격: {book["price"]}원")
else:
    print("검색 결과가 없습니다.")