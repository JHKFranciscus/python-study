student_scores = {
    "민수": 80,
    "지수": 95,
    "영희": 70
}

target_name = "지수"

if target_name in student_scores:
    print(target_name, student_scores[target_name])
else:
    print("학생을 찾을 수 없습니다.")

student_scores["민수"] = 85
student_scores["철수"] = 90

removed_score = student_scores.pop("영희")

print(student_scores)
print(removed_score)

# 예상
# 첫 번째 출력: 지수 95
# 마지막 student_scores: 철수 : 90
# removed_score: 영희 :70

# 실제 결과: 
# 지수 95
# {'민수': 85, '지수': 95, '철수': 90}
# 70
# 예상과 달랐던 이유: 변수.pop()은 value를 반환한다.

# 수정:
# print(student_scores)는 철수만 출력하는 것이 아니라
# 변경과 삭제가 끝난 딕셔너리 전체를 출력한다.
# {'민수': 85, '지수': 95, '철수': 90}

# 1. target_name in student_scores에서 검사하는 것은 키인가, 값인가?
# key
# 2. student_scores["민수"] = 85가 수정인 이유는 무엇인가?
# dict_var["key"] = value는 key가 이미 존재한다면 value를 최신 것으로 바꾸는 구문이기 때문이다.
# 3. student_scores["철수"] = 90이 추가인 이유는 무엇인가?
# dict_var["key"] = value는 key가 없다면 새로운 key와 value를 추가한다.

# 4. pop("영희")를 실행한 후 removed_score에는 무엇이 저장되는가?
# dict에서 마지막에 위치한 값이 제거되어 removed_score에 반환된다.
# 수정:
# pop("영희")는 마지막 항목을 삭제하는 것이 아니라
# "영희"라는 키와 그에 연결된 값 70을 딕셔너리에서 삭제한다.
# 그리고 삭제된 값 70을 removed_score에 반환한다.

# 5. 딕셔너리에서 target_name을 찾을 때 리스트처럼 직접 for문을 작성하지 않아도 되는 이유는 무엇인가?
# 리스트에서는 원하는 값을 찾기 위해 직접 앞에서부터 비교하는 순차 탐색을 작성할 수 있다.
# 딕셔너리는 키로 값을 조회할 수 있도록 만들어졌으므로 사용자가 직접 for문으로 모든 키를 비교할 필요가 없다.