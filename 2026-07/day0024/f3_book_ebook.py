class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        return f"제목: {self.title}, 저자: {self.author}, 가격: {self.price}원"

    def change_price(self, new_price):
        # if new_price >= 0:
        if type(new_price) is int and new_price >= 0:
            self.price = new_price
            return True

        return False


class EBook(Book):
    def __init__(self, title, author, price, file_size, file_format):
        super().__init__(title,author, price)
        self.file_size = file_size
        self.file_format = file_format

    def show_info(self):
        basic_info = super().show_info()
        return f"{basic_info}, 파일 크기: {self.file_size}MB, 형식: {self.file_format}"

    def download(self):
        return f"{self.title}.{self.file_format.lower()} 파일을 다운로드합니다."


book = Book("파이썬 기초", "홍길동", 18000)

ebook = EBook(
    "알고리즘 입문",
    "김개발",
    22000,
    25,
    "PDF"
)

#region
print(book.show_info())
print(ebook.show_info())
print(ebook.download())
print()
print(book.change_price(20000))
print(book.price)
print()
print(ebook.change_price(-1000))
print(ebook.price)


# 1. Book과 EBook 양쪽에 title, author, price 초기화 코드를 모두 작성하지 않은 이유는 무엇인가?
# super()를 사용하여 method overiding에 부모 클래스 method를 호출했기 때문이다.
#[수정 후]
# title, author, price는 Book과 EBook이 공통으로 가지는 속성이므로 Book.__init__()에 한 번만 작성했다.
# EBook은 super().__init__()으로 부모의 초기화 코드를 재사용하여 같은 코드를 중복해서 작성하지 않는다.
# 2. EBook 객체가 Book.change_price()를 호출할 수 있는 이유는 무엇인가?
# EBook은 Book 클래스의 자식 클래스로 자식 클래스의 instance가 method를 호출했을 때 없다면, 부모 클래스의 method에서 찾아서 호출하기 때문이다.
# 3. ebook.change_price() 내부에서 self는 Book 객체와 EBook 객체 중 무엇을 가리키는가?
# 부모 클래스 생성자에서 별도로 instace를 만드는 것이 아니라 자식 클래스 생성자로 만드는 것이기 때문에 ebook 객체를 가리킨다.
#[짧게]
# self는 Book의 별도 객체가 아니라 change_price()를 호출한 ebook을 가리킨다.
# 4. EBook.show_info()를 오버라이딩한 이유는 무엇인가?
# Book.show_info()에는 존재하지 않는 자료를 첨가하기 위해서이다.
#[정확하게]
# 전자책은 일반 도서 정보 외에도 file_size와 file_format을 함께 표시해야 하므로 show_info()를 오버라이딩했다.
# 5. EBook.show_info()에서 super().show_info()를 사용하지 않고 제목, 저자, 가격을 전부 다시 작성해도 실행은 되는가? 실행된다면 그래도 super()를 사용한 이유는 무엇인가?
# self라는 것은 호출한 메서드를 실행하는 instance이기 때문이다. 자식 클래스에서 instance를 생성하여 부모 클래스의 메소드로 초기화를 하여도 결국 자식 클래스에서 생성한 instance이기 때문에 그 속성과 속성 값은 instance안에 그대로 남아 있기 때문이다.
#[수정 후]
#제목, 저자, 가격을 EBook.show_info()에서 전부 다시 작성해도 실행은 된다. 하지만 부모와 같은 코드를 중복해서 작성하게 된다.
#super().show_info()를 사용하면 부모의 공통 출력 코드를 재사용할 수 있고, 나중에 Book.show_info()가 변경되어도 그 변경 내용을 함계 사용할 수 있다.
# 6. file_size와 file_format을 Book에 두지 않은 이유는 무엇인가?
# EBook class로 생성한 instance만 사용가능하게 하기 위함이다.
#[수정 후]
#모든 도서가 공통으로 가지는 정보가 아니라, 전자책에만 필요한 정보이므로 Book이 아니라 EBook에 두었다.

print()
test_book1 = Book("테스트 도서", "테스트 저자", 10000)
print(test_book1.change_price(0))
print(test_book1.price)

test_book2 = Book("테스트 도서", "테스트 저자", 10000)
print(test_book2.change_price(15000))
print(test_book2.price)

print()
test_book3 = Book("테스트 도서", "테스트 저자", 10000)
print(test_book3.change_price("15000"))
print(test_book3.price)

test_book4 = Book("테스트 도서", "테스트 저자", 10000)
print(test_book4.change_price(True))
print(test_book4.price)
#endregion
