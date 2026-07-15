# student_names = ["민수", "지수", "철수", "영희"]
# # target_name = "철수"
# # target_name = "영희"
# target_name = "수진"

# found = False
# check_count = 0

# for name in student_names:
#     check_count += 1
#     print("확인 중:", name)

#     if name == target_name:
#         found = True
#         break

# if found:
#     print(f"{target_name} 학생을 찾았습니다.")
# else:
#     print("등록되지 않은 학생입니다.")

# print("확인한 학생 수:", check_count)
# #region
# # 예상 출력
# # 확인 중: 민수
# # 확인 중: 지수
# # 확인 중: 철수
# # 철수 학생을 찾았습니다.
# # 확인한 학생 수: 3
# #endregion

print("딕셔너리 조회")

student_scores = {
    "민수": 80,
    "지수": 90,
    "철수": 70,
    "영희": 85
}

# target_name = "철수"
target_name = "수진"

if target_name in student_scores:
    score = student_scores[target_name]
    print(f"{target_name} 학생을 찾았습니다.")
    print(f"점수: {score}")
else:
    print("등록되지 않은 학생입니다.")

#region
# 딕셔너리 조회
# 철수 학생을 찾았습니다.
# 점수: 70
#endregion

# [리스트와 딕셔너리 조회 비교]
# 리스트에서 in을 사용하면 원소를 앞에서부터 순차적으로 비교한다.
# 찾는 값이 뒤쪽에 있거나 존재하지 않으면 많은 원소를 확인한다.
# 따라서 리스트 탐색은 일반적으로 O(n)이다.
#
# 딕셔너리에서 in을 사용하면 키의 존재 여부를 확인한다.
# 리스트처럼 앞의 항목부터 하나씩 비교하는 방식은 아니며,
# 키 조회는 평균적으로 O(1)이다.
#
# 같은 in 문법이라도 오른쪽 자료형에 따라 탐색 방식이 달라진다.