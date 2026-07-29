# 문제 1. 인스턴스 속성과 클래스 속성
class Book:
    category = "도서"
    count = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Book.count += 1

# 다음 항목이 클래스 속성, 인스턴스 속성, 매개변수 중 무엇인지 작성한다.

# category -> class attribute
# count -> class attribute
# self.title -> instance attribute
# self.price -> instance attribute
# title -> parameter
# price -> parameter

# 그리고 다음 질문에 답한다.

# self.title은 모든 객체가 함께 공유하는가, 아니면 객체마다 별도로 가지는가?
# -> instance의 attribute로 객체마다 별도로 가진다.

#-----------------------------------------------------------------------------------------
# 문제 2. 객체별 속성 변경
book1 = Book("파이썬 기초", 15000)
book2 = Book("알고리즘 입문", 20000)

book1.price = 18000

# 다음 결과를 예상한다.

print(book1.price)
print(book2.price)
print(Book.count)

# 각 결과가 그렇게 나오는 이유도 작성한다.
# 18000 -> book1.price를 통해 book1의 price라는 attribute에 18000으로 변경되었기 때문이다.
# 20000 -> book2를 생성할 때 book2의 price라는 attribute에 20000을 넣었기 때문이다.
# 2     -> Book 클래스에서 __init__이 실행될 때 마다 count가 올라라는데 2번 실행되었기 때문이다.

#--------------------------------------------------------------------------------------------------
# 문제 3. 인스턴스 메서드

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def change_price(self, new_price):
        self.price = new_price
        return self.price
book = Book("파이썬", 15000)
result = book.change_price(18000)

# 다음 질문에 답한다.

# self가 가리키는 객체는 무엇인가?
# -> Book class를 호출한 값이 대입된 book이라는 instance이다.
#[수정 후]
#self는 change_price() 메서드를 호출한 book 인스턴스를 가리킨다.
# book.price의 최종값은 무엇인가?
# -> 18000
# result의 값은 무엇인가?
# -> 18000
# 메서드 내부에서 속성을 변경했는데 메서드가 종료된 뒤에도 변경 결과가 유지되는 이유는 무엇인가?
# -> self를 이용하여 함수가 끝나더라도 값을 유지하고 있기 때문이다.
#[수정 후]
#self가 book이 가리키는 원본 인스턴스를 가리키고, self.price를 통해 그 인스턴스의 속성을 직접 변경했기 때문이다.
#메서드가 끝난 뒤에도 book이 같은 인스턴스를 계속 가리키므로 변경이 유지된다.

#------------------------------------------------------------------------------------------------------
# 문제 4. 세 종류의 메서드 구분
class Book:
    count = 0

    def change_price(self, new_price):
        pass

    @classmethod
    def show_count(cls):
        pass

    @staticmethod
    def is_valid_price(price):
        pass

# 다음 표의 내용을 답안으로 작성한다.

# 메서드	                    자동으로 전달받는 값	               주로 다루는 대상
# change_price()		   현재 메소드를 실행 중인 instance              new_price
#[수정 후]                  현재 메소드를 호출한 instance        현재 instance의 price attribute                                
# show_count()		        현재 메소드를 실행 중인 class                  count
#[수정 후]                   현재 메소드를 호출한 class             class attribute인 count
# is_valid_price()	                없다.                                price
#[수정 후]                                                          전달 받은 price 값