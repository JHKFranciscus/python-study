student_names = ["민수", "지수", "영희", "철수", "준호"]

student_scores = {
    "민수": 80,
    "지수": 95,
    "영희": 70,
    "철수": 90,
    "준호": 85
}

target_name = input("찾을 학생 이름을 입력하세요: ")


# 리스트 순차 탐색
comparison_count = 0
found = False

for name in student_names:
    comparison_count += 1

    if name == target_name:
        found = True
        break

if found:
    print("리스트에서 학생을 찾았습니다.")
else:
    print("리스트에서 학생을 찾지 못했습니다.")

print("리스트 비교 횟수:", comparison_count)


# 딕셔너리 키 조회
if target_name in student_scores:
    print("딕셔너리에서 학생을 찾았습니다.")
    print("점수:", student_scores[target_name])
else:
    print("딕셔너리에서 학생을 찾지 못했습니다.")

#region
# 예상 1: "철수" 입력
# 리스트 비교 횟수: 4
# 딕셔너리 출력 점수: 90
#
# 예상 2: "하늘" 입력
# 리스트 비교 횟수: 5
# 딕셔너리에서는 찾을 수 있는가: 없다
#endregion
#region
# 1. 리스트에서 "철수"를 찾을 때 비교 횟수가 4인 이유는 무엇인가?
# 철수는 student_names의 list에서 첫번째 요소로부터 4번째이기 때문이다.
# 2. 리스트에서 존재하지 않는 "하늘"을 찾을 때 비교 횟수가 5인 이유는 무엇인가?
# in문법을 list에서 사용할 경우 list의 요소를 앞에서부터 비교하는 순차탐색을 실시하기 때문이다.
# 3. target_name in student_scores는 딕셔너리의 key와 value 중 무엇을 검사하는가?
# key
# 4. 딕셔너리 키 조회에서 사용자가 직접 for문으로 모든 key를 비교하지 않아도 되는 이유는 무엇인가?
# 딕셔너리는 hash를 만들기 때문에 키 조회를 하면 hash 근처로 가서 key를 비교하기 때문이다.
# 수정:
# 딕셔너리는 key의 hash 값을 계산하고, 그 결과를 이용해 key가 저장된 후보 위치를 찾는다.
# 그 위치에서 실제 key가 같은지 확인하므로 사용자가 모든 key를 for문으로 순차 비교할 필요가 없다.
# 5. 딕셔너리 조회가 평균 O(1)이라는 말은 아무 작업도 하지 않는다는 뜻인가?
# 수정:
# 아니다.
# hash 계산, 후보 위치 확인, 실제 key 비교 등의 작업을 한다.
# 평균 O(1)은 데이터가 많아져도 조회에 필요한 작업량이 데이터 개수에 비례해 늘어나지 않는다는 뜻이다.
#endregion