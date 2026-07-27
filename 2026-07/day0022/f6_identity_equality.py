class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __eq__(self, other):
        return self.title == other.title and self.price == other.price

#region
book1 = Book("파이썬 기초", 15000)
book2 = book1

print("book1 is book2:", book1 is book2)
print("book1:", book1)
print("book2:", book2)

print()

book2.price = 12000

print("book1 가격:", book1.price)
print("book2 가격:", book2.price)
#endregion
#region
print()

book3 = Book("자료구조 입문", 20000)
book4 = Book("자료구조 입문", 20000)

print("book3 is book4:", book3 is book4)
print("book3 == book4:", book3 == book4)

print("book3:", book3)
print("book4:", book4)

print("제목이 같은가:", book3.title == book4.title)
print("가격이 같은가:", book3.price == book4.price)
#endregion
