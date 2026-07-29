class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def change_price(self, new_price):
        self.price = new_price


class EBook(Book):
    def __init__(self, title, price, file_size):
        super().__init__(title, price)
        self.file_size = file_size


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


book = Book("파이썬 기초", 15000)
ebook = EBook("알고리즘 입문", 20000, 15)

manager = BookManager()
manager.add_book(book)
manager.add_book(ebook)

print(isinstance(ebook, EBook))
print(isinstance(ebook, Book))
print(isinstance(manager, Book))

print(manager.books[0] is book)
print(manager.books[1] is ebook)

manager.books[0].change_price(18000)

print(book.price)
print(manager.books[0].price)
#예상 결과
# True
# False     #실제 결과: True
# False
# True
# True
# 18000
# 18000

# 1. EBook과 Book은 왜 상속 관계인가?
# EBook이 Book을 매개변수로 받아서 Book 객체가 사용하는 함수들을 EBook에서도 쓸 수 있기 때문이다.
#[수정 후]
#EBook은 Book의 한 종류이고, class EBook(Book):으로 Book을 부모 클래스로 상속했기 때문이다.
#따라서 EBook은 Book의 속성과 메서드를 물려받을 수 있다.
# 2. BookManager와 Book은 왜 상속 관계가 아닌가?
# BookManager는 Book의 객체들을 가지고 있다가 그 객체들을 통해 호출을 하는 것이지 Book클래스의 method들을 쓸 수 없기 때문이다.
#[정리 후]
#BookManager는 Book의 한 종류가 아니라 Book 객체들을 관리하는 클래스이다.
#BookManager는 Book 객체를 속성으로 가지고 있을 뿐, Book을 상속하지 않았으므로 Book의 메서드를 자동으로 물려받지 않는다.
# 3. BookManager가 Book을 상속하도록 만들면 의미상 왜 부자연스러운가?
# 층이 달라서
#[수정 후]
#BookManager는 Book의 한 종류가 아니기 때문이다.
#"도서 관리자는 도서이다"라는 관계가 성립하지 않으므로 BookManager가 Book을 상속하는 것은 의미상 부자연스럽다.
# 4. manager.books에 Book과 EBook 객체를 저장한 것은 상속과 객체 구성 중 어느 관계인가?
# 객체 구성 관계이다.
# 5. “A는 B의 한 종류이다”는 코드로 어떻게 표현하는가?
# A is -B
#[수정 후]
# class A(B):
#     pass
# 6. “A는 B를 가지고 있다”는 코드로 어떻게 표현하는가?
# A has -B
#[수정 후]
# class A:
#     def __init__(self, b)
#         self.b = b
# 7. manager.books[0]과 book이 같은 객체를 가리킨다는 것은 어떤 의미인가?
# manager의 books 리스트에는 원본 객체의 참조가 들어간다는 의미이다.
# 8. EBook은 Book의 기능을 상속받지만, BookManager는 Book의 기능을 자동으로 사용할 수 없는 이유는 무엇인가?
# BookManger는 상속을 받은 것이 아니라 객체를 가지고 있는 것 뿐이므로, 그 객체를 이용해서 함수를 호출하기 때문이다.
#[정리 후]
#EBook은 Book을 상속했으므로 Book의 기능을 자동으로 물려받는다.
#BookManager는 Book을 상속하지 않고 Book 객체를 가지고만 있으므로, BookManager 자신의 메서드처럼 Book의 기능을 자동으로 사용할 수 없다.
#가지고 있는 객체를 통해 book.change_price()처럼 호출해야 한다.