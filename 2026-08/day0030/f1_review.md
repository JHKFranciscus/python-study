# 문제 1
다음 두 반복문의 차이를 설명한다.
```python
students = ["민수", "지수", "현우"]

for index in range(len(students)):
    print(index, students[index])
for index, student in enumerate(students):
    print(index, student)
```
답:
첫 번째 반복문은 인덱스를 이용하여 리스트 안의 요소를 직접 다룰 때 사용하고, 
두 번째 반복문에서 enumerate는 요소에 자동으로 순번을 붙여줘서 번호와 값을 같이 다룰 때 사용한다
#보완
인덱스를 직접 순회하고 인덱스로 값을 꺼낸다.
인덱스와 값을 한 번에 받는다.

# 문제 2
다음 코드의 실행 결과를 예상한다.
```python
names = ["민수", "지수", "현우"]
scores = [80, 95]

for name, score in zip(names, scores):
    print(name, score)
```
그리고 현우가 출력되는지 판단하고 이유를 적는다.
답:
실행결과:
민수 80
지수 95
현우는 출력되지 않는데, names와 scores를 zip으로 묶었으므로 짝이 존재하지 않는 것은 묶이지가 않아서 출력이 되지 않는다. 

# 문제 3
다음 반복문을 리스트 컴프리헨션으로 바꾼다.
```python
numbers = [1, 2, 3, 4, 5]
even_squares = []

for number in numbers:
    if number % 2 == 0:
        even_squares.append(number ** 2)
```
답:
numbers = [1, 2, 3, 4, 5]
even_squares = [number ** 2 for number in numbers if % 2 == 0]
#수정
numbers = [1, 2, 3, 4, 5]
even_squares = [number ** 2 for number in numbers if number % 2 == 0]

# 문제 4
다음 반복문을 딕셔너리 컴프리헨션으로 바꾼다.
```python
subjects = ["Python", "Git", "CS"]
study_times = [90, 40, 30]

study_record = {}

for subject, study_time in zip(subjects, study_times):
    study_record[subject] = study_time
```
답:
subjects = ["Python", "Git", "CS"]
study_times = [90, 40, 30]
study_record = {subject : study_time for subject, study_time in zip(subjects, study_times)}


# 문제 5
다음 상황에서 인덱스 중심 순회와 값 중심 순회 중 무엇을 사용할지 각각 판단한다.

학생들의 이름만 한 명씩 출력한다.
답: 값 중심 순회
세 번째 주문의 내용을 변경한다.
답: 인덱스 중심 순회
상품 이름과 가격을 함께 출력한다.
답: zip을 이용한 값 중심 순회
현재 값이 목록에서 몇 번째인지 함께 출력한다.
답: enumertate를 이용한 값 중심 순회(인덱스와 값을 함께 받는 순회)