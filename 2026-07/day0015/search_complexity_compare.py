def get_book_by_index(books, index):
    # for book in books:
    #     if book == books[index]:
    #         return book
    # return None
    #[수정 후]
    return books[index]


def find_book_by_title(books, target_title):
    normalized_target_title = target_title.strip().lower()
    checked_count = 0

    for book in books:
        checked_count += 1

        nomalized_book_title = book["title"].strip().lower()

        if nomalized_book_title == normalized_target_title:
            return book, checked_count
        
    return None, checked_count


books = [
    {"title": "Python Basic", "price": 15000},
    {"title": "Advanced Python", "price": 24000},
    {"title": "Java Programming", "price": 18000},
    {"title": "Data Structure", "price": 22000},
    {"title": "Python Data Analysis", "price": 27000},
]

indexed_book = get_book_by_index(books, 3)

print("[인덱스 접근]")
print("제목:", indexed_book["title"])
print("가격:", indexed_book["price"], "원")

# found_book, checked_count = find_book_by_title(books,"Python Basic")

# found_book, checked_count = find_book_by_title(books,"Data Structure")

found_book, checked_count = find_book_by_title(books,"C Programming")

print()
print("[순차 탐색]")

if found_book is not None:
    print("제목:", found_book["title"])
    print("가격:", found_book["price"])
else:
    print("도서를 찾지 못했습니다.")

print("확인한 도서 수:", checked_count)

# 1. books[3]과 같은 인덱스 접근이 O(1)인 이유:
# 순차탐색을 하지 않고, 인덱스로 바로 접근해서
#[수정 후]
# 반복문으로 탐색하지 않고 알고 있는 위치로 바로 접근하며,
# 도서 수가 증가해도 접근 과정이 크게 증가하지 않기 때문이다.
# 2. 제목 순차 탐색이 O(n)인 이유:
# 인덱스로 접근하기 때문에
#[수정 후]
# 찾는 도서의 위치를 모르기 때문에 리스트의 도서를 처음부터 하나씩 확인해야 하기 때문이다.
# 3. 찾는 도서가 첫 번째에 있으면 확인 횟수는:
# 1회
# 4. 찾는 도서가 없으면 확인 횟수는:
# 5회
# 5. 순차 탐색의 최선의 경우와 최악의 경우:
# 최선의 경우는 첫번째 발견이고, 최악의 경우는 마지막요소에서 발견 하거나 발견을 하지 못 한 경우이다.