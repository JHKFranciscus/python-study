# 문제 1. 종류 분류
class Member:
    group_name = "파이썬 스터디"
    member_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Member.member_count += 1

    def change_level(self, new_level):
        self.level = new_level

    @classmethod
    def show_member_count(cls):
        print(cls.member_count)

    @staticmethod
    def is_valid_level(level):
        return 1 <= level <= 5

# # 1. group_name: class attribute
# # 2. member_count: class attribute
# # 3. self.name: instance attribute
# # 4. self.level: instance attribute
# # 5. __init__: instance method
# # 6. change_level: instance method
# # 7. show_member_count: class method
# # 8. is_valid_level: static method


# 문제 2. 어떤 메서드가 적절한지 판단
# 기능 A
# 특정 회원 한 명의 level을 변경한다.
# 적절한 메서드 종류: instance method
# 이유: 특정 회원 한 명의 level은 특정 instance의 attribute이므로 이를 변경할 때는 instance method가 좋다.

# 기능 B
# 현재까지 만들어진 전체 회원 객체 수를 출력한다.
# 적절한 메서드 종류: class method
# 이유: class로부터 만들어진 전체 회원 객체 수는 특정 instance의 attribute가 아닌 class attribute이므로 이를 조회하거나 변경할 때는 class method가 좋다ㅏ.

# 기능 C
# 전달받은 레벨이 1 이상 5 이하인지 검사한다.
# 적절한 메서드 종류: static method
# 이유: instance나 class attribute를 직접 사용할 필요가 없을 때는 static method가 좋다.


# 기능 D
# 모든 회원이 공통으로 조회하는 스터디 이름을 변경한다.
# 적절한 메서드 종류: class method
# 이유: 모든 회원이 공통으로 조회한다는 것은 class attribute인데 이를 조회하거나 변경할 때는 class method가 좋다.


# 문제 3. 실행 결과 예측
# 다음 코드를 이어서 작성하고, 실행 전에 예상 결과를 적습니다.
member1 = Member("홍길동", 1)
member2 = Member("김철수", 2)

member1.change_level(3)

print(member1.name, member1.level)
print(member2.name, member2.level)
Member.show_member_count()

print(Member.is_valid_level(5))
print(Member.is_valid_level(7))

# 예상 결과
# 홍길동 3
# 김철수 2
# 2
# True
# False


# 문제 4. 잘못된 설계 찾기
#다음 메서드는 동작할 수는 있지만 메서드 종류의 선택이 적절하지 않습니다.

class Member:
    @classmethod
    def is_valid_level(cls, level):
        return 1 <= level <= 5

#다음 두 질문에 답합니다.
# 1. 이 메서드에서 cls를 실제로 사용하는가?
# 매개변수에 들어가긴하지만 실제로 사용하지는 않는다.
#[수정 후]
#cls를 실제로 사용하지는 않는다.
#전달받은 level만으로 결과를 판단하고, instance attribute나 class attribute가 필요하지 않으므로 static method로 만드는 것이 적절하다.
# 2. 클래스 메서드보다 어떤 메서드로 만드는 것이 적절한가? 그 이유는 무엇인가?
# static method
# instance도 class attribute를 직접 사용할 필요가 없기 때문에