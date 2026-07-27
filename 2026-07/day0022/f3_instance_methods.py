class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        print("show_info의 self:", self)
        print("제목:", self.title)
        print("저자:", self.author)
        print("가격:", self.price)

    def change_price(self, new_price):
        print("변경 전 가격:", self.price)

        self.price = new_price

        print("변경 후 가격:", self.price)

    def increase_price(self, amount):
        self.price += amount


book1 = Book("파이썬 기초", "김개발", 15000)
book2 = Book("자료구조 입문", "이코딩", 20000)
#region
book1.show_info()
book2.show_info()
#endregion
#region
print()

book1.change_price(12000)

print()

book1.show_info()
book2.show_info()
#endregion
print()

book2.increase_price(3000)

print()

book1.show_info()
book2.show_info()