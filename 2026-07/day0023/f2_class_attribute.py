class Student:
    school_name = "파이썬 학습반"

    def __init__(self, name, score):
        self.name = name
        self.score = score


student1 = Student("홍길동", 85)
student2 = Student("김철수", 90)

print(Student.school_name)
print(student1.school_name)
print(student2.school_name)

print(student1.name)
print(student2.name)

Student.school_name = "SSAFY 준비반"

print(Student.school_name)
print(student1.school_name)
print(student2.school_name)
print()
#예상 결과:
# 파이썬 학습반
# 파이썬 학습반
# 파이썬 학습반
# 홍길동
# 김철수
# SSAFY 준비반
# SSAFY 준비반
# SSAFY 준비반

# 1. school_name은 각 객체에 별도로 저장된 속성인가?
# 아니다 클래스에 공통으로 저장 되어있다.
# [수정 후]
# school_name은 각 인스턴스에 복사되어 저장된 것이 아니다.
# Student class에 하나의 class attribute로 저장되어 있다.
# instance에 같은 이름의 속성이 없다면 클래스에서 찾아 사용한다.
# 2. name은 클래스가 공통으로 사용하는 속성인가?
# 아니다 instance마다 개별적으로 사용하는 속성이다.
# 3. Student.school_name을 변경하면 두 인스턴스에서 조회한 값도 바뀌는가?
# 맞다.


class Student:
    school_name = "파이썬 학습반"

    def __init__(self, name):
        self.name = name


student1 = Student("홍길동")
student2 = Student("김철수")

student1.school_name = "홍길동 개인반"

print(Student.school_name)
print(student1.school_name)
print(student2.school_name)



