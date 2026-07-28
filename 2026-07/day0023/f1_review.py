class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def change_price(self, new_price):
        self.price = new_price


book1 = Book("파이썬 기초", 20000)
book2 = Book("자료구조 입문", 25000)

book1.change_price(18000)

print(book1.title)
print(book1.price)
print(book2.title)
print(book2.price)
print(book1 is book2)
print(book1 == book2)

#예상 결과:
# 파이썬 기초
# 18000
# 자료구조 입문
# 25000
# False
# False

# 문제 1

# class Book:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price

# 1. Book
# -> 클래스, instance 객체를 생산한다.
#[수정 후]
# 클래스이다. Book(...)처럼 호출하면 Book 클래스의 인스턴스를 생산한다.
# 2. __init__
# -> class method 중 초기화를 담당한다.
#[수정 후]
# instance의 초기화를 담당하는 특수한 instance method이다.
# instance가 생성된 뒤 자동으로 호출되어 instance 속성을 설정한다.
# 3. self
# -> 현재 실행중인 클래스의 instance
#[수정 후]
#현재 메서드를 호출한 인스턴스
# 4. title, price
# -> instance의 인자를 반환받는 매개변수
#[수정 후]
# instance의 인자를 전달받는 매개변수
# 5. self.title, self.price
# -> 클래스의 instance에 저장되는 변수
#[수정 후]
#각 instance에 저장되는 instance variable이다.

# 문제 2
# book1 = Book("파이썬 기초", 20000)
# book2 = Book("자료구조 입문", 25000)

# 1. book1과 book2는 클래스인가, 객체인가?
# 객체이다.
# 2. 두 객체는 같은 객체인가?
# 다른 객체이다.
# 3. book1.title과 book2.title은 서로 영향을 주는가?
# 서로 영향을 주지 않는다.
# 4. book1.price = 18000을 실행하면 book2.price도 바뀌는가?
# 바뀌지 않는다.

# 문제 3
# class Book:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price

#     def change_price(self, new_price):
#         self.price = new_price

# book1.change_price(18000)을 실행했을 때 실제로 내부에서 일어나는 일을 설명한다.
# chaange_price의 매개변수 self에 book1이라는 이름을 가진 Book 클래스의 instance가 들어가고, 매개변수 new_price에 인자인 18000이 들어간다.
#[수정 후]
#self에 변수 book이 가리키는 Book instance가 전달된다.
# instance의 속성 중 하나인 price의 값이 new_price로 바뀐다.
# 이 때 self는 원본 객체를 가리키고 있으므로 원본 객체의 price가 바뀌는 것이다.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_info(self):
        print(f"이름: {self.name}, 점수: {self.score}")

    def change_score(self, new_score):
        self.score = new_score

print()
student1 = Student("홍길동", 85)
student2 = Student("길동홍", 70)
student1.change_score(90)
student1.show_info()
student2.show_info()

