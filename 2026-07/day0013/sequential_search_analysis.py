books = [
    {"title": "파이썬 기초", "price": 18000},
    {"title": "자료구조 입문", "price": 22000},
    {"title": "웹 개발 시작", "price": 25000},
    {"title": "자바 기초", "price": 24000},
    {"title": "알고리즘 연습", "price": 20000}
]

def find_book_with_count(books, target_title):
    comparison_count = 0

    for book in books:
        comparison_count += 1

        if target_title == book["title"]:
            return book, comparison_count
        
    return None, comparison_count

first_book, first_count = find_book_with_count(books, "파이썬 기초")
middle_book, middle_count = find_book_with_count(books, "웹 개발 시작")
last_book, last_count = find_book_with_count(books, "알고리즘 연습")
missing_book, missing_count = find_book_with_count(books, "C언어 기초")

print(first_book, first_count)
print(middle_book, middle_count)
print(last_book, last_count)
print(missing_book, missing_count)
# [비교 횟수 예상]
# "파이썬 기초"를 찾을 때: 1
# "웹 개발 시작"을 찾을 때: 3
# "알고리즘 연습"을 찾을 때: 5
# 존재하지 않는 "C언어 기초"를 찾을 때: 5

# [확인 결과]
# 1. 첫 번째 도서는 왜 비교 1회 만에 찾았는가?
# 순차 탐색은 첫 번째 원소부터 비교하며, 첫 번째 도서에서 제목이 일치해 즉시 반환했기 때문이다.
# 2. 마지막 도서와 존재하지 않는 도서의 비교 횟수가 같은 이유는?
# 마지막 요소는 앞의 요소를 모두 비교한 뒤 마지막으로 비교하는 것이다. 존재하지 않는 요소가 없다는 판단을 하기위해서는 모든 요소를 확인한 후에 가능하다
# 3. 도서가 5권에서 100권으로 늘어나면, 최악의 경우 확인해야 하는 도서 수는 어떻게 변하는가?
# 최악의 경우 최대 비교 회수가 100회가 된다.
# 4. 순차 탐색의 시간복잡도를 O(n)이라고 하는 이유는?
# 데이터가 n개이면 최악의 경우 n회 비교해야한다. 데이터 수가 늘어나는 만큼 최대 비교 횟수도 비례해서 늘어나므로 순차 탐색의 시간복잡도는 0(n)이다.

