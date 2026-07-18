books = [
    {"title": "파이썬 기초", "price": 18000},
    {"title": "자료구조 입문", "price": 22000},
    {"title": "웹 개발 시작", "price": 25000}
]

def is_duplicate_title(books, new_title):
    for book in books:
        if new_title == book["title"]:
            return True
        
    return False

def add_book(books, new_title, new_price):
    duplicate_title = is_duplicate_title(books, new_title)

    if duplicate_title is True:
        return False
    
    # else:  #써도 상관은 없는데 안 써도 된다.
    new_book = {"title": new_title, "price": new_price}
    books.append(new_book)
    return True

def find_book(books, target_title):
    for book in books:
        if book["title"] == target_title:
            return book
        
    return None

def update_book_price(books, target_title, new_price):
    found_book = find_book(books, target_title)
    if found_book is None:
        return False
    else:
        found_book["price"] = new_price
        return True

def delete_book(books, target_title):
    found_book = find_book(books,target_title)
    if found_book is None:
        return False
    else:
        books.remove(found_book)
        return True

def calculate_average_price(books):
    if len(books) == 0:
        return 0
    
    total = 0

    for book in books:
        total += book["price"]
    
    average = total / len(books)
    return average

def print_all_books(books):
    if len(books) == 0:
        print("등록된 도서가 없습니다.")
        return
    
    for book in books:
        print(f"제목: {book["title"]}, 가격: {book["price"]}원")

#region
print(is_duplicate_title(books, "파이썬 기초"))
print(is_duplicate_title(books, "자바 기초"))
#region
# [예상]
# "파이썬 기초":
# True
# "자바 기초":
# False
#endregion
first_result = add_book(books, "자바 기초", 21000)
second_result = add_book(books, "파이썬 기초", 30000)

print(first_result)
print(second_result)
print(books)
#region
# [예상]
# "자바 기초" 추가 결과:
# True
# "파이썬 기초" 추가 결과:
# False
# 최종 books:
# [{'title': '파이썬 기초', 'price': 18000},{'title': '자료구조 입문', 'price': 22000},{'title': '웹 개발 시작', 'price': 25000}, {'title': 자바 기초, 'price': 21000}]
#endregion
found_book = find_book(books, "자바 기초")
not_found_book = find_book(books, "C언어 기초")

print(found_book)
print(not_found_book)
#region
# [예상]
# "자바 기초" 조회 결과:
# {'title': '자바 기초', 'price': 21000}
# "C언어 기초" 조회 결과:
# None
#endregion
first_update_result = update_book_price(books, "자바 기초", 24000)

second_update_result = update_book_price(books, "C언어 기초", 19000)

print(first_update_result)
print(second_update_result)
print(books)
#region
# [예상]
# "자바 기초" 수정 결과:
# True 
# "C언어 기초" 수정 결과:
# False
# 수정 후 "자바 기초" 가격:
# 24000
#endregion
first_delete_result = delete_book(
    books,
    "자료구조 입문"
)

second_delete_result = delete_book(
    books,
    "C언어 기초"
)

print(first_delete_result)
print(second_delete_result)
print(books)
#region
# [예상]
# "자료구조 입문" 삭제 결과:
# True
# "C언어 기초" 삭제 결과:
# False
# 삭제 후 books에는 "자료구조 입문"이 존재하지 않는다.
#endregion
average_price = calculate_average_price(books)

print(average_price)
print(calculate_average_price([]))
#region
# [예상]
# 현재 books의 평균 가격:
# 22,333.3
#[수정]
#22333.333333333332    #, 가 자동으로 찍히지는 않는다., 소숫점 뒤에 길게 뻗어 있다.
# 빈 리스트의 평균 가격:
# 0
#endregion
#endregion
print("[현재 전체 도서]")
print_all_books(books)

print("[빈 도서 목록]")
print_all_books([])
#region
# [예상]
# 현재 전체 도서:
# 제목: 파이썬 기초, 가격: 18000원
# 제목: 웹 개발 시작, 가격: 25000원
# 제목: 자바 기초, 가격: 24000원
# 빈 도서 목록:
# 등록된 도서가 없습니다.
#endregion
