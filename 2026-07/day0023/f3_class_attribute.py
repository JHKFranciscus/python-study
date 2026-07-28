class Book:
    category = "도서"
    book_count = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price
        # book_count += 1
        Book.book_count += 1

book1 = Book("파이썬 기초", 20000)
book2 = Book("자료구조 입문", 25000)
book3 = Book("알고리즘 기초", 30000)

print("분류:", Book.category)
print("제목:", book1.title, "가격:", book1.price)
print("제목:", book2.title, "가격:", book2.price)
print("제목:", book3.title, "가격:", book3.price)
print("생성된 도서 수:", Book.book_count)