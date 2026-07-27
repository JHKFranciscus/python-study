class Book:
    pass

book1 = Book()
book2 = Book()
print(Book)
print(type(book1))
print(type(book2))
print(book1 is book2)
print()
print(type(book1) is Book)
print(type(book2) is Book)
print(isinstance(book1, Book))
print(isinstance(book2, Book))
print()

book1.title = "파이썬 기초"
book1.price = 15000

book2.title = "자료구조 입문"
book2.price = 20000

print(book1.title)
print(book1.price)
print(book2.title)
print(book2.price)
print()

book1.price = 12000

print(book1.price)
print(book2.price)
print()

print(book1.__dict__)
print(book2.__dict__)