student_names = ["민수", "지수", "영희", "철수", "준호", "수진"]

student_scores = {
    "민수": 80,
    "지수": 95,
    "영희": 70,
    "철수": 90,
    "준호": 85,
    "수진": 88
}

count = 0
found = False

target_name = input("찾을 학생을 입력하세요: ")

#[수정 전]
# for target_name in student_names:
#     count += 1

#     if target_name in student_names:
#         found =True
#         break

for name in student_names:
    count += 1

    if target_name == name:
        found = True
        break
    

# if found == True:
if found:
    print(f"{target_name}학생을 찾았습니다.")
else:
    print(f"{target_name}학생을 찾지 못 했습니다.")

print(f"리스트 비교 횟수: {count}")

if target_name not in student_scores:
    print("해당 학생은 존재하지 않습니다.")
else:
    print(f"{target_name}: {student_scores[target_name]}점")
#region
# 1. 리스트에서 첫 번째 학생을 찾을 때와 마지막 학생을 찾을 때 비교 횟수가 다른 이유는 무엇인가?
# list는 앞에서부터 순차적으로 요소를 탐색하기 때문이다
# 2. 존재하지 않는 학생을 찾을 때 리스트의 모든 요소를 확인해야 하는 이유는 무엇인가?
# list는 앞에서부터 순차적으로 요소를 탐색하기 때문이다
# 3. 학생 수가 6명에서 6000명으로 늘어나면 리스트 순차 탐색의 최대 비교 횟수는 어떻게 변하는가?
# 학생 수가 6000명이라면 리스트 순차 탐색의 최대 비교 횟수는 6000회가 된다.
# 4. 딕셔너리 조회의 평균 O(1)은 항상 정확히 한 번만 작업한다는 뜻인가?
# 아니다. 
# 5. 평균 O(1)에서 데이터 수가 증가해도 작업량이 데이터 수에 비례해 증가하지 않는다는 말은 무슨 뜻인가?
# hash를 통하여 key 주변을 확인하고, 그 주변에서 key를 조회하기 때문에 데이터 수에 비례해 증가하는 것은 아니다.
# 수정:
# 딕셔너리는 key의 hash 값을 계산하여 후보 위치를 찾고,
# 그 위치에서 실제 key가 같은지 확인한다.
# 따라서 데이터 수가 늘어나도 평균 조회 작업량이
# 데이터 수에 비례하여 늘어나지는 않는다.
#endregion

# 독립 구현에서 처음 빠뜨린 것:
# 입력값 target_name과 각 리스트 요소를 구분할 for문의 반복 변수 name
# 원본과 달랐지만 동작에는 문제없던 것: if found == True로 작성해도 if found와 같은 결과가 나온다.
# 처음 코드가 잘못된 이유:
# 사용자 입력을 저장한 target_name을 for문의 반복 변수로 다시 사용했고, 리스트에서 꺼낸 값을 같은 리스트 안에 있는지 검사했기 때문이다.

