subjects = ["Python", "CS", "Git", "Algorithm"]
study_minutes = [95, 40, 25, 70]
completed = [True, False, True, False]

print("===과목별 공부 시간 딕셔너리===")
minutes_by_subject = {subject: study_minute for subject, study_minute in zip(subjects, study_minutes)}
print(minutes_by_subject)

print()
print("===60분 이상 공부한 과목===")
long_study_subjects = {subject: study_minute for subject, study_minute in zip(subjects, study_minutes) if study_minute >= 60}

print(long_study_subjects)

print()
print("===아직 완료하지 않은 과목===")
incomplete_subjects = {subject: study_minute for subject, study_minute, is_completed in zip(subjects, study_minutes, completed) if not is_completed}

print(incomplete_subjects)

print()
print("===공부 시간을 시간 단위로 변환===")
hours_by_subject = {subject: round(study_minute / 60, 2) for subject, study_minute in zip(subjects, study_minutes)}

print(hours_by_subject)

# 1. 딕셔너리 컴프리헨션에서 콜론(:) 왼쪽과 오른쪽은 각각 무엇인가?
# 키와 값
# 2. 문제 2의 if 조건은 키와 값을 변환하는가, 결과에 포함할 항목을 선택하는가?
# 결과에 포함할 항목을 선택하는 것이다.
# 3. 딕셔너리 컴프리헨션은 원본 리스트를 수정하는가, 새로운 딕셔너리를 만드는가?
# 새로운 딕셔너리를 만드는 것이다.