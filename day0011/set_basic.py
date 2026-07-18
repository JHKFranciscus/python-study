subjects = {"Python", "Git", "Python", "CS", "Git"}

print(subjects)
print(len(subjects))
#region
# 예상
# subjects 출력: {'Pythone', 'CS', 'Git'}
# len(subjects) 출력: 3
# 그렇게 예상한 이유: 순서를 보장하지 않고, 중복을 허용하지 않아서
#endregion
subjects.add("Algorithm")
print("추가 후:", subjects)

subjects.remove("Git")
print("삭제 후:", subjects)
#region
# 1. add("Algorithm")을 실행하면 무엇이 추가되는가?
# 'Algorithm'을 추가했으니 'Algorithm이 추가된다.
# 2. remove("Git")을 실행하면 무엇이 삭제되는가?
# 'Git을 삭제하기 때문에 'Git'이 삭제된다.
# 3. 처음 작성한 값은 5개인데 len(subjects)가 3인 이유는 무엇인가?
# set이나 dictionary는 중복을 허용하지 않기 때문이다.
# 수정:
# 세트는 같은 값을 중복해서 저장하지 않는다.
# "Python"과 "Git"이 각각 두 번 작성되었지만 하나씩만 남았으므로
# len(subjects)는 3이다.
# 딕셔너리는 키는 중복될 수 없지만 값은 중복될 수 있다.
# 4. subjects[0]처럼 첫 번째 요소를 조회할 수 있을 것으로 예상하는가?
# set과 dictionary는 index로 접근하지 못한다.
# 세트는 순서와 인덱스를 사용하지 않으므로 subjects[0]으로 조회할 수 없다.
# 딕셔너리도 위치 인덱스가 아니라 키를 사용해 값을 조회한다.
#endregion
print("중복 추가 전:", subjects)
print("중복 추가 전 개수:", len(subjects))

subjects.add("Python")

print("중복 추가 후:", subjects)
print("중복 추가 후 개수:", len(subjects))
#region
# 예상
# add("Python")을 다시 실행한 뒤 세트: {'CS', 'Python', 'Algorithm'}
# 중복 추가 전 개수: 3
# 중복 추가 후 개수: 3
# 그렇게 예상한 이유: set은 같은 element의 중복 저장을 허용하지 않기 때문이다.
#endregion
target_subject = "CS"

if target_subject in subjects:
    print(target_subject, "과목이 있습니다.")
else:
    print(target_subject, "과목이 없습니다.")

target_subject = "Git"

if target_subject in subjects:
    print(target_subject, "과목이 있습니다.")
else:
    print(target_subject, "과목이 없습니다.")
#region
# 1. 첫 번째 if문에서는 어느 출력문이 실행될 것으로 예상하는가?
# print(target_subject, "과목이 있습니다.")
# 2. 두 번째 if문에서는 어느 출력문이 실행될 것으로 예상하는가?
# print(target_subject, "과목이 없습니다.")
# 3. "Git"은 처음 세트에 있었는데 현재 없다고 예상하는 이유는 무엇인가?
# remove("Git")으로 set 내에서 삭제 시켰기 때문이다.
# 4. target_subject in subjects는 무엇을 검사하는 코드인가?
# target_subject에 저장된 값과 같은 요소가 subjects 세트 안에 존재하는지 검사한다.
#endregion
