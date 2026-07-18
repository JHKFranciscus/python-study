# [복습 예상]

# 1. 함수 안에서 만든 지역 변수는 함수가 끝나면 어떻게 되는가?
# 함수가 끝남과 동시에 지역변수는 사라진다.
# 2. 함수가 딕셔너리를 반환했고, 반환받은 딕셔너리의 값을 수정했더니 원본 리스트까지 바뀔 수 있는 이유는 무엇인가?
# 반환받은 딕셔너리의 값이 가리키는 것과 원본 리스트가 가리키는 것이 같기 때문에, 반환받은 딕셔너리를 통해 수정을 해도 원본 리스트까지 바뀔 수 있다.
# 3. return found_book와 return found_book.copy()의 차이는 무엇인가?
# return found_book은 원본과 같은 것을 가리키지만, found_book.copy는 원본과 다른 객체를 생성하여 그것을 가리키는 것이다.
# 4. 함수 안에서 원본 딕셔너리의 price를 수정하면 함수가 종료된 뒤에도 수정 결과가 남는가? 남는다면 그 이유는 무엇인가?
# 함수 내에서 했을 지라도 함수 내있는 매개변수가 가리키는 것과 원본 딕셔너리가 가리키는 것이 같기 때문에 원본 딕셔너리를 수정하여, 함수가 종료된 후에도 계속된다.




def find_book(books, target_title):
    for book in books:
        if target_title == book["title"]:
            return book
        
    return None

def update_book_price(books, target_title, changed_price):
    found_book = find_book(books, target_title)
    if found_book is not None:
        found_book["price"] = changed_price
        return True
    else:
        return False

def find_book_copy(books, target_title):
    for book in books:
        if target_title == book["title"]:
            return book.copy()
        
    return None


books = [
    {"title": "파이썬 기초", "price": 18000},
    {"title": "자료구조 입문", "price": 22000},
    {"title": "웹 개발 시작", "price": 25000}
]

found_book = find_book(books, "파이썬 기초")
found_book["price"] = 30000

print(found_book)
print(books)
#region
#예상 출력 결과
#{'title': '파이썬 기초', 'price': 30000}
#[{'title': '파이썬 기초', 'price': 30000}, {'title': '자료구조 입문', 'price': 22000}, {'title': '웹 개발 시작', 'price': 25000}]
#함께 바뀐다.
# find_book()이 books 안의 원본 딕셔너리 객체를 그대로 반환했기 때문이다.
# found_book과 books 안의 해당 원소는 같은 딕셔너리 객체를 가리킨다.
# 따라서 found_book을 통해 price를 수정하면 원본 books에도 수정 결과가 남는다.
copied_book = find_book_copy(books, "자료구조 입문")
copied_book["price"] = 50000

print(copied_book)
print(books)
#region
# 예상
# copied_book의 가격
# 50000
# 원본 books안의 "자료구조 입문"가격
# 22000













