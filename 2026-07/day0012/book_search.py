books = [
    {"title": "파이썬 기초", "price": 18000},
    {"title": "자료구조 입문", "price": 22000},
    {"title": "알고리즘 연습", "price": 25000}
]

target_title = input("찾을 책 제목: ")
found = False

for book in books:
    if target_title == book["title"]:
        print(f"검색 결과: {book["title"]} / {book["price"]}원")
        found = True
        break

if found == False:
#if not found 라고 쓰면 더 간단하다.
    print("해당 책이 없습니다.")
