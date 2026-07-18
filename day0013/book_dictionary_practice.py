# 1. 딕셔너리 안전 조회
book = {
    "title": "파이썬 기초",
    "price": 18000,
    "author": "김개발"
}

print(book["title"])
print(book.get("title"))
#region
#실행결과
# 파이썬 기초
# 파이썬 기초
#endregion

# print(book["publisher"])
#region
#실행결과
# Traceback (most recent call last):
#   File "/home/jhk-franciscus/projects/python-study/day0013/book_dictionary_practice.py", line 13, in <module>
#     print(book["publisher"])
#           ~~~~^^^^^^^^^^^^^
# KeyError: 'publisher'
#endregion

print(book.get("publisher"))
print(book.get("publisher", "출판사 정보 없음"))
# region
#실행결과
# None
# 출판사 정보 없음
#endregion

#region
# [확인 결과]
# book["publisher"]를 실행했을 때:
# KeyError가 뜬다
# book.get("publisher")를 실행했을 때:
# None
# book.get("publisher", "출판사 정보 없음")을 실행했을 때:
# 출판사 정보 없음
# [] 조회와 get()의 가장 큰 차이:
# 존재하지 않는 key를 조회하면
# []는 KeyError가 발생하고,
# get()은 오류 없이 None 또는 지정한 기본값을 반환한다.
#endregion

# 2. items()로 key와 value 함께 반복하기
print()
print("[딕셔너리 자체 반복]")

for data in book:
    print(data)
#region
# 예상:
# data에는 key가 들어갈지, value가 들어갈지:
# data
#endregion

print()
print("[items() 반복]")

for key, value in book.items():
    print(key, value)
#region
# 예상출력
# title 파이썬 기초
# price 18000
# author 김개발
#endregion

def print_book_information(book):
    for key, value in book.items():
        print(f"{key}: {value}")

print()
print_book_information(book)

# 3. 리스트 안의 딕셔너리 삭제하기
books = [
    {"title": "파이썬 기초", "price": 18000},
    {"title": "자료구조 입문", "price": 22000},
    {"title": "웹 개발 시작", "price": 25000}
]

def delete_book(books, target_title):
    for book in books:
        if target_title == book["title"]:
            books.remove(book)
            return True
    
    return False

delete_result = delete_book(books, "자료구조 입문")

print()
print(delete_result)
print(books)
#region
# [예상]
# delete_result:
# True
# 삭제 후 books:
# [{"title": "파이썬 기초", "price": 18000}, {"title": "웹 개발 시작", "price": 25000}]
#endregion





