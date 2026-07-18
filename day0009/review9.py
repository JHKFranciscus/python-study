# 문제1
# 프로그램이 위에서 아래로 실행될 때 다음 항목을 실제로 처리되는 순서대로 적어라.

def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def calculate_average(numbers):
    total = calculate_total(numbers)
    average = total / len(numbers)

    return average


scores = [80, 90, 70]
result = calculate_average(scores)
print(result)

# calculate_total 함수객체 생성 및 객체에 이름이 연결
# calculate_average 함수객체 생성 및 객체에 이름이 연결
# scores = [80, 90, 70] 실행
# calculate_average(scores)함수호출
# calculate_total(numbers)함수호출
# print(result)출력


# 문제2
# 다음 각각에서 매개변수와 인수를 구분해 적어라.

# def calculate_average(numbers):

# calculate_average(scores)

# 매개변수: numbers
# 인수: scores


# 문제3
# calculate_total(numbers)가 실행되는 동안 다음 변수의 값을 적어라.

# 반복 시작 전 total:
# 0
# 첫 번째 반복 후 total:
# 80
# 두 번째 반복 후 total:
# 170
# 세 번째 반복 후 total:
# 240
# return 되는 값:
# 240


# 문제4
# 다음 변수들의 최종 값을 적어라.

# calculate_average 함수 안의 total:
# 240
# calculate_average 함수 안의 average:
# 80.0
# 함수 밖의 result:
# 80.0
# 화면에 출력되는 값:
# 80.0
# average = 240 / 3
# /의 결과는 float이다.
# calculate_total의 total: 0 → 80 → 170 → 240
# calculate_total의 반환값: 240          int

# calculate_average의 total: 240         int
# calculate_average의 average: 80.0      float
# 함수 밖의 result: 80.0                 float
# 출력값: 80.0

# 문제5

# calculate_total 함수 안에서 사용한 total과
# calculate_average 함수 안에서 사용한 total은 같은 변수인가?

# 같은 변수인지:
# 아니다
# 그렇게 판단한 이유:
# 둘 다 지역변수로 calculate_total에서 계산된 total의 값만 반환되어 함수 calculate_average에 있는 calculate_total(numbers)로 반환되어 다시 그 값이 total에 대입된 것이다.