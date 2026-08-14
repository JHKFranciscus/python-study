# 반복
# → 조건 확인
# → 합 누적 + 개수 누적

# → 조건을 만족하는 값들의 평균

# 반복문 안에서 평균을 계속 계산하는 것이 아니라, 합과 개수를 다 구한 뒤 마지막에 한 번 계산하는 것

# 뒤에서 필요한 값을 먼저 계산해야 한다면 반복을 두 번 할 수도 있다

# 문제 1
temperatures = [18, 25, 31, 22, 30, 27]

total = 0
count = 0

for temperature in temperatures:
    if temperature >= 25:
        total += temperature
        count += 1

if count == 0:
    print("25도가 된 적이 없습니다.")

else:
    average = total / count
    print(f"평균: {average}")


# 문제 2
scores = [68, 92, 75, 81, 59, 88, 73]

total = 0
count = 0

for score in scores:
    if score >= 70:
        total += score
        count += 1

if count == 0:
    print("대상 점수가 없습니다.")

else:
    average = total / count
    print(f"평균: {average}")

    average_upper = 0

    for score in scores:
        if score > average:
            average_upper += 1

    print(f"평균보다 높은 점수의 개수: {average_upper}")