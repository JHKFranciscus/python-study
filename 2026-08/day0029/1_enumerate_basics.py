students = ["민수", "지수", "현우"]

for index in range(len(students)):
    print(index + 1, students[index])

    
# 예상 결과:
# 1 민수
# 2 지수
# 3 현우
# 실제 결과:
# 1 민수
# 2 지수
# 3 현우

print("--- enumerate 사용 ---")

for number, student in enumerate(students, start=1):
    print(number, student)

print("---직접 수정 문제---")

students = ["서준", "유나", "도윤", "하린"]

for number, student in enumerate(students, start=1):
    print(f"{number}번 학생: {student}")

# enumerate()를 사용하면 range(len(students)) 방식보다 어떤 부분이 간단해지는가?
#답: 직접 번호를 계산할 필요 없이 번호를 붙여준다.