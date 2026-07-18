books = [
    {"title": "파이썬 기초", "price": 18000},
    {"title": "자료구조 입문", "price": 22000},
    {"title": "알고리즘 연습", "price": 25000}
]

new_title = input("추가할 책 제목: ")
new_price = int(input("추가할 책 가격: "))

new_book = {
    "title": new_title,
    "price": new_price
}

books.append(new_book)

print("[추가 후 목록]")

for book in books:
    print(f"{book["title"]} / {book["price"]}원")

target_title = input("가격을 수정할 책 제목: ")
changed_price = int(input("새 가격: "))

found = False

for book in books:
    #[수정 전]
    # if target_title == book:
    if target_title == book["title"]:
        print(f"기존 가격: {book["price"]}원")
        book["price"] = changed_price
        print(f"변경 가격:{book["price"]}원")
        found = True
        break

if not found :
    print("해당 책이 없습니다.")