def print_all_scores(scores):
    for name, score in scores.items():
        print(f"{name}: {score}점")

def print_student_score(scores, name):
    if name in scores:
        score = scores[name]
        print(f"{name}: {score}점")
    else:
        print("등록된 학생이 없습니다.")

def update_student_score(scores, name, new_score):
    if name in scores:
        scores[name] = new_score
        print(f"{name}의 점수가 {new_score}로 변경되었습니다.")
    else:
        print("등록된 학생이 없습니다.")

student_scores = {
    "민수": 75,
    "지수": 88,
    "철수": 92
}

print("전체 점수 출력")
print_all_scores(student_scores)
print("지수 점수 조회")
print_student_score(student_scores, "지수")
print("영희 점수 조회")
print_student_score(student_scores, "영희")
print("민수 점수 수정")
update_student_score(student_scores, "민수", 95)
print("수정 후 전체 점수 출력")
# [수정 전]
# update_student_scores = print_all_scores(student_scores)
# print_all_scores는 출력만 하고 반환값이 없으므로
# 호출 결과를 변수에 저장하지 않는다.
print_all_scores(student_scores)
