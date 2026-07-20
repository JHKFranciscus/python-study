book_title = "Python Basic"

raw_search_title = input("찾을 도서를 입력하세요:")

normalized_search_title= raw_search_title.strip().lower()

normalized_book_title = book_title.lower()

if normalized_search_title == normalized_book_title:
    print("도서를 찾았습니다.")
else:
    print("도서를 찾지 못했습니다.")

print(f"검색어 원본: {raw_search_title}, 정규화 결과: {normalized_search_title}")
print(f"책이름 원본: {book_title}, 정규화 결과: {normalized_book_title}")