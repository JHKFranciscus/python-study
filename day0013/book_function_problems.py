# 문제 1 — 특정 가격 이상의 도서 개수 구하기
books = [
    {"title": "파이썬 기초", "price": 18000},
    {"title": "자료구조 입문", "price": 22000},
    {"title": "웹 개발 시작", "price": 25000},
    {"title": "알고리즘 연습", "price": 20000}
]

def count_expensive_books(books, minimum_price):
    count = 0

    for book in books:
        if minimum_price <= book["price"]:
            count += 1

    return count 

result = count_expensive_books(books, 22000)
print(result)
#예상 결과: 2
print(count_expensive_books(books, 22000))
print(count_expensive_books(books, 20000))
print(count_expensive_books(books, 30000))
#region
# [예상]
# 22000 이상: 2
# 20000 이상: 3
# 30000 이상: 0
#endregion

# 문제 2 — 가장 비싼 도서 찾기
def find_most_expensive_book(books):
    most_expensive_book = books[0]

    # for book in books:
    for book in books[1:]:
    #첫 번째 도서를 최고가 도서로 저장했으니 반복은 두 번째 도서부터 시작하면 된다.
        # if most_expensive_book["price"] <= book["price"]:
        if most_expensive_book["price"] < book["price"]: 
            # 요구사항은 현재 도서가 더 비쌀 때만 교체하는 것이기 때문에            
            most_expensive_book = book

    return most_expensive_book

most_expensive_book = find_most_expensive_book(books)

print(most_expensive_book)
print(most_expensive_book["title"])
print(most_expensive_book["price"])
#region
# [예상]
# 반환되는 딕셔너리:
# {'title': '웹 개발 시작', 'price': 25000}
# title:
# 웹 개발 시작
# price:
# 25000
#endregion

# 문제 3 — 가격 범위에 해당하는 도서 목록 만들기
def find_books_in_price_range(books, minimum_price, maximum_price):
    ranged_books = []

    for book in books:
        if minimum_price <= book["price"] <= maximum_price:
            ranged_books.append(book)

    return ranged_books

result = find_books_in_price_range(books, 19000, 23000)
print(result)

print(find_books_in_price_range(books, 19000, 23000))
print(find_books_in_price_range(books, 25000, 30000))
print(find_books_in_price_range(books, 30000, 40000))
#region
# [예상]
# 19000원 이상 23000원 이하:
# [{"title": "자료구조 입문", "price": 22000}, {"title": "알고리즘 연습", "price": 20000}]
# 25000원 이상 30000원 이하:
# [{"title": "웹 개발 시작", "price": 25000}]
# 30000원 이상 40000원 이하:
# []
#endregion

# 문제 4 — 전체 도서의 평균 가격 구하기
def calculate_average_price(books):
    total = 0
    
    if len(books) == 0:
        return 0
    else:
        for book in books:
            total += book["price"]
        
        # average = total / len(books) #상관은 없다만, 
    average = total / len(books)
    return average

average_price = calculate_average_price(books)
print(average_price)

empty_books = []
print(calculate_average_price(empty_books))
#region
# [예상]
# books의 평균 가격:
# 21250.0
# 빈 리스트의 평균 가격:
# 0
#endregion


