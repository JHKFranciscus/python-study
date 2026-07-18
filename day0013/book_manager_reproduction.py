books = [
    {"title": "파이썬 입문", "price": 17000},
    {"title": "자료구조 연습", "price": 23000},
    {"title": "웹 기초", "price": 20000}
]

def find_book(books, target_title):
    for book in books:
        if target_title == book["title"]:
            return book
    
    return None

def add_book(books, new_title, new_price):
    found_book = find_book(books, new_title)
    if found_book is not None:
        return False
    else:
        new_book = {"title": new_title, "price": new_price}
        books.append(new_book)
        return True

def update_book_price(books, target_title, new_price):
    found_book = find_book(books, target_title)
    if found_book is None:
        return False
    else:
        found_book["price"] = new_price
        return True

def delete_book(books, target_title):
    found_book = find_book(books, target_title)
    if found_book is None:
        return False
    else:
        books.remove(found_book)
        return True

print(add_book(books, "자바 입문", 21000))
print(add_book(books, "파이썬 입문", 30000))

print(update_book_price(books, "웹 기초", 25000))
print(update_book_price(books, "C 기초", 19000))

print(delete_book(books, "자료구조 연습"))

print(books)
#region
# [실행 전 예상]
# "자바 입문" 추가 결과:
# True
# 중복된 "파이썬 입문" 추가 결과:
# False
# "웹 기초" 가격 수정 결과:
# True
# 없는 "C 기초" 수정 결과:
# False
# "자료구조 연습" 삭제 결과:
# True
# 최종 books:
# books = [{"title": "파이썬 입문", "price": 17000}, {"title": "웹 기초", "price": 25000}, {"title": "자바 입문", "price": 21000}]
#endregion