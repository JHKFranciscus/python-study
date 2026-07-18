books = [
    {"title": "파이썬 기초", "price": 18000},
    {"title": "자료구조 입문", "price": 22000},
    {"title": "알고리즘 연습", "price": 25000}
]

for book in books:
    print(f"책 제목: {book["title"]} / 가격: {book["price"]}원")