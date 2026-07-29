class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def show_info(self):
        return f"제목: {self.title}, 가격: {self.price}원"


class EBook(Book):
    def __init__(self, title, price, file_size):
        super().__init__(title, price)
        self.file_size = file_size

    def show_info(self):
        basic_info = super().show_info()
        return f"{basic_info}, 파일 크기: {self.file_size}MB"

    def download(self):
        return f"{self.title} 전자책을 다운로드합니다."


book = Book("파이썬 기초", 15000)
# ebook = EBook("알고리즘 입문", 20000)
ebook = EBook("알고리즘 입문", 20000, 15)

print(book.show_info())
print(ebook.show_info())
#region
# book.show_info()의 결과:
# 제목: 파이썬 기초", 가격: 15000원
# ebook.show_info()의 결과:
# 제목: 알고리즘 입문, 가격: 20000원

# 1. EBook 안에는 __init__()이 없는데 EBook("알고리즘 입문", 20000)으로 객체를 만들 수 있는 이유는 무엇인가?
# EBook이 Book을 상속받아서
#Ebook 안에 __init__()이 없으므로 부모 클래스인 Book의 __init__()을 찾아 실행하기 때문이다.
# 2. EBook 안에는 show_info()가 없는데 ebook.show_info()를 호출할 수 있는 이유는 무엇인가?
# EBook이 Boo을 상속받아서
#EBook안에 show_info()가 없으므로 부모 클래스인 Book의 show_info()를 찾아 실행하기 때문이다.
# 3. ebook은 Book 클래스의 인스턴스인가?
# 아니다 EBook class의 instance이다.
#[수정 후]
#그렇다. ebook은 EBook의 instance이면서 Ebook이 book을 상속했으므로 Book의 instance로도 취급된다.
# 4. book은 EBook 클래스의 인스턴스인가?
# 아니다. book은 Book으로 직접 생성되었으므로 EBook class의 instance가 아니라 Book class의 instance이다.
print()
print(isinstance(ebook, EBook))
print(isinstance(ebook, Book))
print(isinstance(book, Book))
print(isinstance(book, EBook))
#endregion
#region
print()
print(ebook.title)
print(ebook.price)
print(ebook.show_info())
print(ebook.download())

# 예상 결과
# ebook.title:
# 알고리즘 입문
# ebook.price:
# 20000
# ebook.show_info():
# 제목: 알고리즘 입문, 가격: 20000원
# ebook.download():
# 알고리즘 입문 전자책을 다운로드합니다.

# 1. ebook.title은 Book 클래스 자체에 저장된 값인가, 아니면 ebook 인스턴스에 저장된 값인가?
# ebook 인스턴스에 저장된 값이다
# 2. EBook 안에 title을 만드는 코드가 없는데 download()에서 self.title을 사용할 수 있는 이유는 무엇인가?
# EBook class는 Book class를 상속받아서 EBook 안에 타이틀을 만들 때 Book.__init__을 실행하여 만들지만, Book class가 아니라 Ebook 클래스의 instance에 직접 저장되기 때문에 Book method로 만들었어도 Ebook객체 자체의 attribute이므로 사용할 수 있다.
# 3. ebook은 show_info()와 download()를 모두 호출할 수 있는데, 두 메서드는 각각 어느 클래스에 작성되어 있는가?
# show_info()는 Book class에, download()는 EBook class에 작성되어 있다.
# 4. book.download()를 호출하면 정상 실행되는가? 실행되지 않는다면 그 이유는 무엇인가?
# 실행되지 않는다. book이라는 객체는 Book instance인데, Book class는 download()라는 method를 가지고 있지 않다.
# 5. 부모 클래스인 Book이 자식 클래스 EBook에 새로 작성된 download()를 자동으로 사용할 수 있는가?
# 사용할 수 없다.
#endregion
#region
print()
print(book.show_info())
print(ebook.show_info())
print(ebook.file_size)
print(ebook.download())

# 예상 결과
# book.show_info(): 제목: 파이썬 기초, 가격: 15000원
# ebook.show_info(): 제목: 알고리즘 입문, 가격: 20000원, 파일 크기: 15MB
# ebook.file_size: 15
# ebook.download(): 알고리즘 입문 전자책을 다운로드합니다.

# 1. EBook에 __init__()을 작성한 뒤에도 Book의 __init__()이 자동으로 실행되는가?
# 실행되지 않고, Book의 __init__만 작동된다.
# 2. super().__init__(title, price)는 어떤 메서드를 호출하는가?
# EBook의 부모 class인 Book의 __init__ method를 호출한다.
# 3. 부모 생성자와 자식 생성자는 각각 별개의 객체를 수정하는가, 아니면 동일한 ebook 객체를 수정하는가?
# 부모 생성자라 하여 별개의 객체를 생성하지 않고, 같은 자식 class에서 만들어진 instance를 수정한다.
# 4. self.file_size를 Book.__init__()이 아니라 EBook.__init__()에 작성한 이유는 무엇인가?
# file_size라는 attribute를 EBook 클래스로 만든 instance만 가지는 속성으로 만들기 위하여
# 5. ebook.show_info()를 호출했을 때 Book.show_info()와 EBook.show_info() 중 어느 것이 먼저 실행되는가?
# EBook.show_info()가 먼저 실행되고, Book.show_info()를 호출하면 그 때 실행이 된다.
# 6. EBook.show_info() 안에서 super().show_info()를 호출한 이유는 무엇인가?
# method overriding을 했지만 Book.show_info()에 있는 코드를 사용하기 위하여
#endregion