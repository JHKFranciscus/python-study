# 문제 1. dumps, loads
import json

books = [
    {
        "title": "파이썬 기초",
        "price": 20000,
        "available": True
    },
    {
        "title": "자료구조 입문",
        "price": 25000,
        "available": False
    }
]

# 변환 전 자료형 출력
print(type(books))
print()
# Python 객체를 JSON 문자열로 변환
# json_text = json.dumps(books)
json_text = json.dumps(books, ensure_ascii = False, indent = 4)
# JSON 문자열과 변환 후 자료형 출
print(json_text)
print(type(json_text))
print()
# JSON 문자열을 Python 객체로 복원
restored_books = json.loads(json_text)
# 복원된 자료형과 첫 번째 도서 제목 출력
print(type(restored_books))
print(restored_books[0]["title"])

# 문제2 변환 전 객체와 복원된 객체의 관계
print()
print("원본과 복원본이 같은 객체인가?")
print(books is restored_books)

print()
print("수정 전 가격")
print("원본 가격:", books[0]["price"])
print("복원본 가격:", restored_books[0]["price"])

restored_books[0]["price"] = 30000

print()
print("복원본 수정 후 가격")
print("원본 가경:", books[0]["price"])
print("복원본 가경:", restored_books[0]["price"])

# 예상
# books is restored_books의 결과: False
# 복원본의 가격을 수정했을 때 원본 가격: 20000
# 복원본의 가격: 30000

print()
print("복원된 available 값:", restored_books[0]["available"])
print("복원된 available 자료형:", type(restored_books[0]["available"]))