class Book:
    def __init__(self, title, author, price, published_year):
        # print("__init__ 실행:", title)
        # print("__init__의 self:", self)

        self.title = title
        self.author = author
        self.price = price
        self.published_year = published_year


book1 = Book("파이썬 기초", "김개발", 15000, 2025)
book2 = Book("자료구조 입문", "이코딩", 20000, 2024)
#region
# print()

# print(book1.title)
# print(book1.author)
# print(book1.price)
print(book1.published_year)

# print(book2.title)
# print(book2.author)
# print(book2.price)
print(book2.published_year)
#endregion
print()

print(book1.__dict__)
print(book2.__dict__)
# print()

# print("book1:", book1)
# print("book2:", book2)