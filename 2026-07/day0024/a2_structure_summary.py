# 1. EBook과 AudioBook을 Book과 완전히 별개의 클래스로 만들지 않고 Book을 상속하게 만든 이유는 무엇인가?
# Book의 method와 공통된 부분이 존재하여 Book 클래스와의 중복을 막기 위하여

# 2. title, author, price를 Book에 두고 file_size, file_format, running_time, narrator를 자식 클래스에 둔 기준은 무엇인가?
# Book에는 공통된 속성을 두었고, 나머지는 각 클래스에서만 사용하는 속성이기 때문이다.

# 3. EBook과 AudioBook이 Book의 change_price()를 별도로 작성하지 않고 사용할 수 있는 이유는 무엇인가?
# EBook과 AudioBook은 Book으로부터 상속을 받아서 자식 클래스에 method가 존재하지 않아도 부모 클래스의 method를 사용할 수 있다.

# 4. EBook과 AudioBook에서 show_info()를 오버라이딩한 이유는 무엇인가?
# EBook과 AudioBook에서는 상속받은 속성 외의 속성이 존재하기 때문이다.
#[수정 후]
#EBook과 AudioBook은 일반 도서 정보 외에 각각의 파일 정보와 재생 정보를 함께 표시해야 한다.
#따라서 부모의 show_info()와 다른 결과를 반환하도록 오버라이딩했다.

# 5. BookManager가 Book을 상속하지 않고 self.books에 도서 객체들을 저장한 이유는 무엇인가?
# 도서를 관리하는 도서가 이상하듯이 BookManager는 Book과 상속을 받은 객체들을 속성으로 저장하여 객체들을 관리하기 때문이다.

# 6. 상속 관계와 객체 구성 관계를 오늘 프로그램의 실제 클래스로 각각 한 문장씩 설명한다.
# 상속 관계: A가 B의 한 종류이다.
# class A(B):
#     pass
# 객체 구성 관계: A가 B를 가지고 있다.
# class A():
#     def __init__(self, b):
#         self.b = b
#[수정 후]
# 상속관계: EBook과 AudioBook은 Book의 한 종류이므로 Book을 상속한다.
# 객체 구성 관계: BookManager는 Book, EBook, AudioBook 객체들을 self.books에 가지고 관리한다.

# 7. manager.find_book()이 반환한 객체가 Book, EBook, AudioBook 중 무엇이든 show_info()를 호출할 수 있는 이유는 무엇인가?
# 파이썬의 list 객체는 모든 자료형을 다 받을 수 있다. 그래서 받은 자료형은 모든 class의 instance의 참조이므로 manager.find_book()이 반환한 객체는 특정 instance이므로 전부 show_info()를 호출할 수 있다.
#[수정 후]
#Book에는 show_info()가 정의되어 있고, EBook과 AutioBook은 Book을 상속하면서 show_info()를 오버라이딩했다.
#따라서 find_book()이 어느 도서 객체를 반환하더라도 show_info()가 존재하며, 실제 객체의 클래스에 맞는 show_info()가 실행된다.

# 8. 새로운 도서 종류를 추가했는데도 BookManager의 등록·검색·가격 변경 코드를 수정하지 않아도 된 이유는 무엇인가?
# BookManager는 새로운 도서 종류와도 객체 구성 관계이므로 BookManager에서 작동을 하기 때문이다.
#[수정 후]
# 모든 도서가 공통으로 제공하는 기능만 사용하도록 작성됐기 때문이다
# BookManager는 특정 자식 클래스의 전용 기능에 의존하지 않고, 모든 도서가 공통으로 가지는 title, show_info(), change_price()를 사용한다.
# AudioBook도 Book을 상속해 이 공통 기능을 가지므로, 새로운 도서 종류를 추가해도 등록·검색·가격 변경 코드를 수정할 필요가 없다.