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

# 도서 목록을 JSON 파일에 저장
with open("books.json", "w", encoding="utf-8") as file:
    json.dump(books, file, ensure_ascii=False, indent=4)

print("도서 목록을 books.json에 저장했습니다.")

# JSON 파일에서 도서 목록 읽기
with open("books.json", "r", encoding="utf-8") as file:
    loaded_books = json.load(file)

print()
print("불러온 전체도서:", loaded_books)
print("불러온 자료형:", type(loaded_books))
print("첫 번째 도서 제목:", loaded_books[0]["title"])
print("첫 번째 가격 자료형:", type(loaded_books[0]["price"]))
print("첫 번째 대여 가능 여부:", loaded_books[0]["available"])
print("대여 가능 여부 자료형:", type(loaded_books[0]["available"]))