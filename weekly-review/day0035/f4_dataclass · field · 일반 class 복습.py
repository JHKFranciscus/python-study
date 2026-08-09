# 문제 1 — 일반 class와 dataclass
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score



from dataclasses import dataclass

@dataclass
class Student:
    name: str
    score: int

# 1. 두 코드에서 Student("민수", 90)으로 객체를 만들 수 있는 이유는 각각 무엇인가?
# 위의 것은 '__init__'메서드가 인스턴스 속성을 초기화하여 객체를 만들기 때문이고,
# 아래의 것은 dataclasses 디렉터리 안의 dataclass를 사용하여 __init__과 같은 특수 메서드를 자동으로 생성하여 사용하기 때문이다. 
#[수정 후]
#위의 것은 직접 작성한 __init__이 객체 생성을 처리한다.
#아래의 것은 @dataclass가 필드를 바탕으로 __init__같은 특수 메서드를 자동 생성한다.

# 2. @dataclass를 사용했을 때 자동 생성되는 대표적인 특수 메서드 3개는?
# __init__, __repr__, __eq__


# 문제 2 — field()의 역할
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    scores: list[int] = field(default_factory=list)


# 1. 여기서 name과 scores는 무엇인가?
# field
# 2. field()는 무엇을 하기 위해 사용하는가?
# 속성의 값을 설정해준다.
#[수정 후]
#field는 dataclass의 field에 대한 설정을 지정하는 함수이다.
# 3. default_factory=list를 사용하는 이유는 무엇인가?
# 인스턴스를 만들 때 마다 scores 속성 값을 다른 list 자료형 객체로 만들기 위하여

# 문제 3 — 객체끼리 list를 공유하는가?
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    scores: list[int] = field(default_factory=list)


student1 = Student("민수")
student2 = Student("지수")

student1.scores.append(100)

print(student1.scores)
print(student2.scores)
print(student1 == student2)


# 예상 결과:
# [100]
# []
# False

# student1.scores에 100을 추가했는데 student2.scores에는 100이 추가되지 않는 이유:
# default_factory는 그 속성 값에 새로운 객체를 생성하다는 의미이므로 student1.scores와 student2.scores의 속성 값은 서로 다른 객체가 생성되어 있다.


# 문제 4 — __repr__, __eq__
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int


product1 = Product("키보드", 50000)
product2 = Product("키보드", 50000)

print(product1)
print(product1 == product2)
print(product1 is product2)


# 예상 결과:
# Product(name='키보드', price='50000')
# True
# False
# 실제 결과:
# Product(name='키보드', price=50000)
# True
# False

# product1 == product2가 그렇게 나오는 이유:
# dataclass가 __eq__ 특수 메서드를 자동으로 설정해두었기 때문이다.
#[보완]
#@dataclass가 만든 __eq__가 두 객체의 field값들을 비교하고, name과 price가 모두 같으므로 True

# product1 is product2가 그렇게 나오는 이유:
# 그 둘은 서로 다른 객체인데 그 둘의 객체 동일성 비교 조건은 따로 설정해 두지 않았기 때문이다.
#field값들을 비교하는 것이 아니라 두 변수가 동일한 객체를 가리키는지 확인한다. product1과 product2는 각각 따로 생성된 객체이므로 False
