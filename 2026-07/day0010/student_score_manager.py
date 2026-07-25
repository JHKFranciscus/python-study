def print_all_scores(scores):
    for name, score in scores.items():
        print(f"{name}: {score}점")

def calculate_average(scores):
    total = 0
    for score in scores.values():
        total += score
    
    average = total / len(scores)

    return average

def print_student_score(scores, name):
    if name in scores:
        score = scores[name]
        print(f"{name}의 점수는 {score}점입니다.")
    else:
        print("등록되지 않은 학생입니다.")

def add_student(scores, name, score):
    if name in scores:
        print("이미 등록된 학생입니다.")
    else:
        scores[name] = score
        print(f"{name} 학생을 추가했습니다.")

def update_student_score(scores, name, new_score):
    if name in scores:
        scores[name] = new_score
        print(f"{name}의 점수를 {new_score}점으로 수정했습니다.")
    else:
        print("등록되지 않은 학생입니다.")

student_scores = {
    "민수": 80,
    "지수": 90,
    "철수": 70
}

print_all_scores(student_scores)
average = calculate_average(student_scores)
print(f"평균 점수: {average}")
#region
# 예상출력
# 민수: 80점
# 지수: 90점
# 철수: 70점
# 평균 점수: 80.0
#endregion
print_student_score(student_scores, "지수")
print_student_score(student_scores, "영희")
#region
# 예상출력
# 지수의 점수는 90점입니다.
# 등록되지 않은 학생입니다.
#endregion
add_student(student_scores, "영희", 85)
add_student(student_scores, "민수", 95)

print_all_scores(student_scores)
#region
# 영희 학생을 추가했습니다.
# 이미 등록된 학생입니다.
# 민수: 80점
# 지수: 90점
# 철수: 70점
# 영희: 85점
#endregion
update_student_score(student_scores, "민수", 95)
update_student_score(student_scores, "수진", 100)

print_all_scores(student_scores)
#region
# 민수의 점수를 95점으로 수정했습니다.
# 등록되지 않은 학생입니다.
# 민수: 95점
# 지수: 90점
# 철수: 70점
# 영희: 85점
#endregion
updated_average = calculate_average(student_scores)
print(f"수정 후 평균 점수: {updated_average}")