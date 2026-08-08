from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    scores: list = field(default_factory=list)
#region
# 1. name은 dataclass의 field인가?
# yes
# 2. scores는 dataclass의 field인가?
# yes
# 3. Student("민수")처럼 scores를 전달하지 않고 객체를 생성하면 scores에는 무엇이 들어갈 것 같은가?
# None
#[수정 후]
#default_factory=list에서 list는 list를 만드는 함수 역할을 하고, scores 값이 주어지지 않으면 dataclass가 이것을 호출한다.
#list()가 실행되고, []가 만들어진다.
# 4. field(default_factory=list)가 무슨 역할을 할 것 같은가?
# Student라는 클래스로 만든 객체들의 scores의 값을 따로 모아두는 list 자료형 객체를 생성할 것 같다
#[수정 후]
#scores값이 전달되지 않을 때 새로운 빈 리스트를 생성해서 그 객체의 scores에 넣도록 설정한다.
#endregion
student1 = Student("민수")
student2 = Student("영희")

print(student1)
print(student2)

student1.scores.append(90)

print(student1)
print(student2)

print(student1.scores is student2.scores)
#region
# 1. 처음 student1 출력 예상:
# Student(name='민수', scores=[])
# 2. 처음 student2 출력 예상:
# Student(name='영희', scores=[])
# 3. student1.scores에 90을 추가한 뒤 student1 출력 예상:
# Student(name='민수', scores=[90])
# 4. 그때 student2 출력 예상:
# Student(name='영희', scores=[])
# 5. student1.scores is student2.scores 예상:
# False
# 6. 5번처럼 예상한 이유:
# student1.scores에 90이 추가되었으므로 값이 다르기 때문이다.
#[수정 후]
#default_factory=list가 객체를 생성할 때마다 새로운 리스트 객체를 만들어 주기 때문에 student1.scores와 student2.scores는 서로 다른 리스트 객체이다.
#endregion
print()
@dataclass
class User:
    name: str
    level: int = field(default=1)
    tags: list = field(default_factory=list)
#region
# 1. User("민수")를 만들면 level에는 어떤 값이 들어가는가?
# 1
# 2. User("민수")를 만들면 tags에는 어떤 값이 들어가는가?
# []
# 3. default=1에서 1은 '값'인가, '호출할 함수'인가?
# 값
# 4. default_factory=list에서 list는 '값'인가, '필요할 때 호출할 대상'인가?
# 필요할 때 호출할 대상
# 5. user1 = User("민수")
#    user2 = User("영희")
#    일 때 user1.tags is user2.tags의 예상 결과와 이유는?
# User의 객체가 생성될 때마다 새로운 list 객체를 생성해줘서 서로 다른 객체를 비교하는 객체를 비교하는 것이기 때문에 False가 뜬다.
#[수정 후]
#default_factory=list가 각 User 객체를 생성할 때마다 새로운 리스트 객체를 생성하므로 user1.tag와 user2.tags는 서로 다른 리스트 객체를 가리킨다. 따라서 is로 비교하면 Fasle가 나온다.
#endregion
print()
@dataclass
class Account:
    name: str
    password: str = field(repr=False)
    login_count: int = field(default=0, compare=False)


account1 = Account("민수", "abc", 1)
account2 = Account("민수", "xyz", 100)

print(account1)
print(account1.password)
print(account1 == account2)
#region
# 1. account1을 print한 예상 결과:
# Account(name='민수', login_count=1)
# 2. account1.password의 예상 결과:
# abc
# 3. account1 == account2의 예상 결과:
# False
# 4. password 값이 서로 다른 것이 3번 비교 결과에 영향을 주는가? 그 이유는?
# 그렇다. field(repr=False)는 field를 바탕으로 __repr__를 실행하던 것을 하지 않도록 만드는 것이지 field 자체를 삭제하는 것은 아니기 때문이다.
#[수정 후]
#그렇다. repr=False는 password를 __repr__의 출력에서만 제외한다. compare=False는 설정하지 않았으므로 password는 객체 비교에는 포함된다. 따라서 account1과 account2의 password 값이 달라 Fasle가 나온다.
# 5. login_count 값이 서로 다른 것이 3번 비교 결과에 영향을 주는가? 그 이유는?
# field(compare=False)는 해당 field를 객체 비교 대상에서 제외하기 때문이다.
#endregion







