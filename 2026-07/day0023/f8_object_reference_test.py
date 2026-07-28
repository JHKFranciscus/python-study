class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price


print("질문 1")
book1 = Book("파이썬 기초", 20000)
book2 = book1

book2.price = 18000

print(book1.price)
print(book2.price)
print(book1 is book2)


print("\n질문 2")
book1 = Book("파이썬 기초", 20000)
book2 = Book("파이썬 기초", 20000)

print(book1 is book2)
print(book1 == book2)


print("\n질문 3")
book1 = Book("파이썬 기초", 20000)
books = []

books.append(book1)
found_book = books[0]

found_book.price = 17000

print(book1.price)
print(books[0].price)
print(found_book is book1)