from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: int


student1 = Student("민수", 80)
student2 = Student("민수", 80)

print(student1)
print(student1 == student2)
#region
# 1. Student에서 dataclass의 field는 무엇인가?
# 답: name, score
# 2. student1이 생성된 뒤 student1.name에서 name은 무엇이라고 부를 수 있는가?
# 답: attribute
# 3. 첫 번째 print의 예상 결과
# 답: Student(name = '민수', score = 80)
#[수정 후]
#Student(name='민수', score=80)
# 4. 두 번째 print의 예상 결과
# 답: True
# 5. 직접 __repr__과 __eq__을 작성하지 않았는데도 위 코드가 동작할 것으로 예상하는 이유
# 답: dataclass에 __repr__과 __eq__가 내장되어 있기 때문이다.
#[수정 후]
#@dataclass가 field를 바탕으로 __repr__과 __eq__를 자동 생성하기 때문이다.
#endregion
print()
class NormalStudent:
    def __init__(self, name, score):
        self.name = name
        self.score = score


normal1 = NormalStudent("민수", 80)
normal2 = NormalStudent("민수", 80)

print(normal1)
print(normal1 == normal2)
#region
# 1. 첫 번째 print의 예상 결과:
# <__main__.NormalStudent at f0x....>
#[수정 후]
#<__main__.NormalStudent object at 0x7947534438c0>
# 2. 두 번째 print의 예상 결과:
# False
# 3. normal1과 normal2의 name, score 값은 같은데 왜 2번 결과가 그렇게 나올 것이라고 예상하는가?
# 따로 equality의 조건이 작성되어있지 않다면 서로 다른 객체는 attribute's value가 같아도 서로 다른 attribute를 가지므로 두 객체의 equaility가 다르게 된다.
#[수정]
#__eq__를 따로 정의하지 않았기 때문에 attribute's value가 같더라도 두 객체의 value를 기준으로 비교하지 않는다. 그래서 서로 다른 객체이므로 False가 나온다.
#endregion
print()
@dataclass
class Product:
    name: str
    price: int

# 1. 여기서 field는?
# name, price
# 2. Product("키보드", 50000)가 가능한 이유는?
# @dataclass가 field에 맞게 __init__을 실행하기 때문이다.
#[수정 후]
#@dataclass가 field를 바탕으로 __init__을 자동 생성하기 때문이다.
# 3. print(Product("키보드", 50000))가 보기 좋은 형태로 출력되는 이유는?
# @dataclass가 field에 맞게 __repr__를 실행하기 때문이다.
#[수정 후]
#@dataclass가 field를 바탕으로 __repr__을 자동 생성하기 때문이다.
# 4. 같은 name, price를 가진 두 Product 객체를 ==로 비교하면 True가 나오는 이유는?
# @dataclass가 field에 맞게 __eq__를 실행하기 때문이다.
#[수정 후]
#@dataclass가 field를 바탕으로 __eq를 자동 생성하기 때문이다.

























