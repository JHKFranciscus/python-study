for number in range(1, 6):
    print(number)
#시작값: 1, 끝값: 6, 증가값: 1, 끝값이 포함되는지:x

for number in range(2, 11, 2):
    print(number)
#시작값: 2, 끝값: 11, 증가값: 2, 끝값이 포함되는지:x

for number in range(10, 0, -1):
    print(number)
#시작값: 10, 끝값: 0, 증가값: -1, 끝값이 포함되는지:x

#------------------------------------------------------------
#실습 2
count = 1

while count <= 5:
    print(count)
    count += 1

# count += 1을 지우면 문제가 발생하는 이유:
# count += 1을 지우면 count의 값이 계속 1로 유지된다.
# 따라서 count <= 5가 계속 참이 되면서 반복문이 끝나지 않는다.

#------------------------------------------------------------
#실습 3

while True:
    number = int(input("숫자를 입력하세요. 0이면 종료: "))

    if  number == 0:
        break

    print("입력한 숫자: ", number)

for number in range(1,11):
    if number % 2 == 1:
        continue

    print(number)

# 1. for와 while의 차이
# for는 특정 데이터 집합 안의 모든 요소들을 하나씩 다 꺼내거나 정해진 횟수만큼 반복
# while은 조건이 참인 동안 계속 반복

# 2. range(1, 6)에서 6이 출력되지 않는 이유
# range(1, 6)은 1부터 6바로 직전까지를 의미하기 때문이다.

# 3. 무한 반복이 생기는 이유
# 반복문 내의 코드들이 조건을 계속 만족시켜 반복문이 끝나지 않는다.

# 4. break의 역할
# break가 발동 시 현재 실행 중인 가장 가까운 반복문을 즉시 종료한다

# 5. continue의 역할
# continue가 발동 시 현재 실행 중인 가장 가까운 반복문의 다음 회차로 넘어간다.
