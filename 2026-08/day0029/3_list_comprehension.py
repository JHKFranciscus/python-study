numbers = [1, 2, 3, 4, 5]

squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)

print(squared_numbers)

# 예상 결과
# [1, 4, 9, 16, 25]
# 실제 결과
# [1, 4, 9, 16, 25]
# 원본 numbers가 변경되는가: 변경되지 않는다.
# squared_numbers에는 무엇이 들어가는가: numbers의 각 값을 제곱한 값이 들어간다.

print("--- 리스트 컴프리헨션 ---")

squared_numbers_comprehension = [
    number ** 2
    for number in numbers
]
#squared_numbers_comprehension = [number ** 2 for number in numbers]
#[새 리스트에 넣을 값 for 반복 변수 in 반복할 자료]
# [number ** 2 for number in numbers]
#   ↑ 넣을 값         ↑ numbers의 값을 하나씩 받음

print(squared_numbers_comprehension)

# 예상 결과
# [1, 4, 9, 16, 25]
# 실제 결과
# [1, 4, 9, 16, 25]

print("--- 조건 필터링 ---")

scores = [55, 82, 71, 48, 90, 66]

passed_scores = [
    score
    for score in scores
    if score >= 60
]
# passed_scores = [score for score in scores if score >= 60]
# [넣을 값 for 반복 변수 in 반복할 자료 if 조건]

print(passed_scores)

# 예상 결과:
# [82, 71, 90, 66]
# 실제 결과:
# [82, 71, 90, 66]

# 55가 포함되는가: 되지 않는다.
# 82가 포함되는가: 된다.
# 원본 scores가 변경되는가: 원본 scores가 변경되는 것이 아니다

print("--- 필터링 후 변환 ---")

prices = [3000, 7000, 12000, 4500, 15000]

expensive_prices_with_tax = [
    price * 1.1
    for price in prices
    if price >= 10000
]

print(expensive_prices_with_tax)

# 예상 결과
# [13200, 16500]
# 실제 결과
# [13200.000000000002, 16500.0]

# 조건 검사와 값 변환 중 논리적으로 어느 것이 먼저 적용되는가?
# 가장 우측에 존재하는 것 먼저 된다.
#[수정]
#반복할 값을 하나 꺼낸 뒤 if 조건을 먼저 검사하고, 조건이 참일 때만 앞의 변환식을 계산하여 새 리스트에 넣는다.

print("===직접 작성===")

minutes = [15, 42, 8, 60, 35, 90]

seconds = [
    minute * 60
    for minute in minutes
]
print(seconds)

long_minutes = [
    minute
    for minute in minutes
    if minute >= 30
]
print(long_minutes)

long_seconds = [
    minute *60
    for minute in minutes
    if minute >= 30
]
print(long_seconds)

# 1. 리스트 컴프리헨션은 기존 리스트를 변경하는가, 새로운 리스트를 만드는가?
# 새로운 리스트를 만든다
# 2. [값 for 변수 in 자료 if 조건]에서 if 조건은 어떤 역할을 하는가?
# 변수에 들어가는 자료의 조건을 설정한다.
# 3. 일반 반복문이 리스트 컴프리헨션보다 더 적절한 경우는 언제라고 생각하는가?
# 모르겠다.
#[수정]
#처리 과정이 여러 단계이거나 조건 분기가 복잡해서 리스트 컴프리헨션으로 작성하면 읽기 어려워지는 경우이다.