student_scores = {
    "민수": 80,
    "지수": 90,
    "철수": 70
}

print(student_scores)
print(student_scores["민수"])
print(student_scores["지수"])

# 예상 출력
# 첫 번째: 민수: 80, 지수: 90, 철수:70
#[수정 후]
# 첫 번째: {'민수': 80, '지수': 90, '철수': 70}
# 두 번째: 민수: 80
# 세 번째: 지수: 90

student_scores["민수"] = 85
student_scores["영희"] = 95

print(student_scores)
print(student_scores["민수"])
print(student_scores["영희"])

# 수정과 추가 이후 예상 출력
# 첫 번째: {'민수': 85, '지수': 90, '철수': 70, '영희': 95}
# 두 번째: 85
# 세 번째: 95

# 1. "민수"의 값이 80에서 85로 바뀐 이유:
# dictionary[key] = 값은 원래 key가 존재하면 기존에 있던 key의 값을 변경하기 때문이다.
# 2. "영희": 95가 새로 추가된 이유: dictionary[key] = 값은 원래 key가 존재하지 않으면 새로운 항목을 추가하기 때문이다.
# 3. 같은 키를 두 번 대입하면 기존 항목이 하나 더 생기는지:
# 아니다. 기존에 key가 있으면 새로 대입해도 값만 변할 뿐이다.
# 4. 딕셔너리에서 특정 값을 가져올 때 사용하는 것은 키인지 인덱스인지: dictionary는 특정 값을 가져올 떄 key를 사용하고, list는 특정값을 가져올 때 index를 사용한다.


print("민수" in student_scores)
print("수진" in student_scores)

name = "영희"

if name in student_scores:
    print(student_scores[name])
else:
    print("등록되지 않은 학생입니다.")

name = "수진"

if name in student_scores:
    print(student_scores[name])
else:
    print("등록되지 않은 학생입니다.")


# 예상 출력
# 첫 번째: True
# 두 번째: False
# 세 번째: 95
# 네 번째: 등록되지 않은 학생입니다.

print("전체 학생 점수")

for name in student_scores:
    score = student_scores[name]
    print(name, score)

# 예상 출력
# 전체 학생 점수
# 민수 85
# 지수 90
# 철수 70
# 영희 95

print("점수만 출력")

for score in student_scores.values():
    print(score)

total = 0

for score in student_scores.values():
    total += score

average = total / len(student_scores)

print("합계:", total)
print("평균:", average)

# 예상 출력
# 점수만 출력
# 85
# 90
# 70
# 95
# 합계: 340
# 평균: 85.0

# [딕셔너리 기초 정리]
# 딕셔너리는 키와 값을 한 쌍으로 저장한다.
#
# student_scores["민수"]처럼 대괄호 안에 키를 넣어 값을 조회한다.
#
# 이미 존재하는 키에 값을 대입하면 기존 값이 수정된다.
# 존재하지 않는 키에 값을 대입하면 새로운 항목이 추가된다.
#
# key in student_scores를 사용하면
# 해당 키가 딕셔너리에 존재하는지 확인할 수 있다.
#
# 딕셔너리를 그대로 for문으로 반복하면 키가 하나씩 나온다.
# student_scores.values()를 반복하면 값이 하나씩 나온다.
#
# len(student_scores)는 저장된 키와 값의 쌍의 개수를 구한다.
#
# 리스트는 주로 인덱스로 값을 찾고,
# 딕셔너리는 키로 값을 찾는다.