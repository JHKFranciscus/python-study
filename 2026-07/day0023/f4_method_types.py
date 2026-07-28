class Book:
    category = "도서"
    book_count = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Book.book_count += 1

    def show_info(self):
        print(f"제목: {self.title}, 가격: {self.price}")

    @classmethod
    def show_book_count(cls):
        print(f"생성된 도서 수: {cls.book_count}")

    @classmethod
    def change_category(cls, new_category):
        cls.category = new_category

    @staticmethod
    def is_valid_price(price):
        return price >= 0

    def change_price(self, new_price):
        check_price = Book.is_valid_price(new_price)

        if check_price is True:
            self.price = new_price
            return True

        return False


book1 = Book("파이썬 기초", 20000)
book2 = Book("자료구조 입문", 25000)

book1.show_info()
Book.show_book_count()

print(Book.category)
Book.change_category("학습 도서")
print(Book.category)

print(Book.is_valid_price(15000))
print(Book.is_valid_price(-5000))
#region
#예상 결과
# 제목: 파이썬 기초, 가격: 20000
# 생성된 도서 수: 2
# 도서
# 학습도서
# True
# False
#endregion
#region
# 1. show_info()가 인스턴스 메서드인 이유는 무엇인가?
# 별도의 데코레이터가 없고,
# 특정 Book instance의 attribute를 조회하기 위한 메서드이기 때문이다.
# 2. show_book_count()에서 self가 아니라 cls를 사용하는 이유는 무엇인가?
# 위에 @classmethod가 있고,
# 이는 class method인데 특정 Book instance를 사용하는게 아닌 Book class가 메서드를 호출하기 때문이다.
#[수정 후]
# @classmethod가 붙은 클래스 메서드이므로 첫 번째 매개변수에는 특정 인스턴스가 아니라 메서드를 호출한 클래스가 전달된다.
# 클래스 속성인 book_count를 사용하므로 cls를 사용한다.
# 3. change_category()는 각 도서 객체의 속성을 변경하는가, 클래스의 공통 속성을 변경하는가?
# class의 공통 attribute를 변경한다.
# 4. is_valid_price()에 self와 cls가 필요하지 않은 이유는 무엇인가?
# 위에 @staticmethod가 있고,
# 이는 static method인데 Book instance와 class를 직접 사용하는게 아니기 때문이다.
# 5. __init__()는 인스턴스·클래스·정적 메서드 중 무엇인가?
# instance method
#endregion
print()
print(book1.change_price(18000))
book1.show_info()

print(book1.change_price(-1000))
book1.show_info()

