#region
# 1. 할 일을 순서대로 저장하고 나중에 추가·수정하려면 어떤 자료구조를 선택해야 하는가?
# 답: list
# 이유: 순서대로 보관하고, 값을 추가하거나 요소를 수정할 수 있기 때문이다.
# 2. 가로와 세로 크기를 저장하며 만들어진 뒤 바꾸지 않으려면 어떤 자료구조를 선택해야 하는가?
# 답: tuple
# 이유: 자료구조를 저장 후 변경하지 않기 때문이다.
#[수정 후]
# 튜플은 생성한 뒤 인덱스를 이용해 요소를 직접 변경할 수 없기 때문이다.
# 3. 학생 이름으로 점수를 바로 찾으려면 어떤 자료구조를 선택해야 하는가?
# 답: dictionary
# 이유: key를 통해 조회하여 즉시 비교하기 때문이다.
# 학생 이름을 key, 점수를 value로 연결하고, 학생 이름을 key로 사용해 점수를 조회할 수 있기 때문이다.
# 핵심은 key와 value를 연결하고, key로 value를 조회하는 것
#[수정 후]
# 4. 신청 과목을 중복 없이 저장하려면 어떤 자료구조를 선택해야 하는가?
# 답: set
# 이유: 요소를 중복없이 보관하기 때문이다.
#endregion
#list code
todo_list = ["Python 복습", "SSAFY 문제풀이", "공부일지 작성"]

print("처음 할 일:", todo_list)

todo_list.append("Git 정리")
todo_list[1] = "SSAFY 오답 정리"

print("변경 후 할 일:", todo_list)

#tuple code
screen_size = (1920, 1080)

print("화면 크기:", screen_size)
print("가로:", screen_size[0])
print("세로:", screen_size[1])

#dictionary code
student_scores = {
    "민수": 85,
    "지수": 95,
    "철수": 90
}

target_name = "지수"

if target_name in student_scores:
    print(target_name, "점수:", student_scores[target_name])
else:
    print("학생을 찾을 수 없습니다.")

#set code
subjects = {"Python", "Git", "Python", "CS", "Git"}

print("중복 제거 후 과목:", subjects)

target_subject = "CS"

if target_subject in subjects:
    print(target_subject, "과목이 있습니다.")
else:
    print(target_subject, "과목이 없습니다.")

# 예상
# 1. 변경 후 todo_list:
# ["Python 복습", "SSAFY 오답 정리", "공부일지 작성", "Git 정리"]
# 2. screen_size[0]: 1920
# 3. screen_size[1]: 1080
# 4. 딕셔너리에서 출력될 학생 이름과 점수: 지수 점수: 95
# 5. subjects에 남을 서로 다른 과목의 개수: 3개
# 6. CS 과목 존재 검사 결과: CS 과목이 있습니다.