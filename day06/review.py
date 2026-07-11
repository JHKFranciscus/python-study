# for: iterable에서 요소를 꺼내어 반복하는 반복문
# while: 조건이 참인 동안 반복하는 반복문 
# break: 현재 실행중인 가장 가까운 반복문을 즉시 종료한다.
# continue: 현재 실행중인 반복문의 남은 코드를 건너뛰고 다음 반복으로 넘어간다.


# 문제1
total = 0

for i in range(1, 11):
    total += i

print(total)

# 문제2

for j in range(1, 21):
    if j % 3 == 0:
        continue

    print(j)