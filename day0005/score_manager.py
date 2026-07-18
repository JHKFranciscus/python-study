# 만들 프로그램
# 여러 학생의 점수를 계속 입력받는다.
# -1을 입력하면 점수 입력을 종료한다.
# 입력이 끝나면 정상 점수의 개수, 합계, 평균을 출력한다.
# 잘못된 점수는 통계에서 제외한다.

# 풀이 순서
# 1. 정상 점수의 합계를 저장할 total을 0으로 만든다.
# 2. 정상 점수의 개수를 저장할 count를 0으로 만든다.
# 3. while True를 사용해 점수 입력을 계속 반복한다.
# 4. 입력값을 정수로 바꾸어 score에 저장한다.
# 5. score가 -1이면 break로 반복문을 종료한다.
# 6. score가 0보다 작거나 100보다 크면 오류 문구를 출력한다.
# 7. 잘못된 점수인 경우 continue로 다음 입력으로 넘어간다.
# 8. 정상 점수이면 total에 score를 더한다.
# 9. 정상 점수이면 count를 1 증가시킨다.
# 10. 반복 종료 후 count가 0인지 확인한다.
# 11. count가 0이면 정상 점수가 없다는 문구를 출력한다.
# 12. count가 0보다 크면 평균 total / count를 계산한다.
# 13. 학생 수, 합계, 평균을 출력한다.

total = 0
count = 0

while True:
    score = int(input("점수를 입력하세요. 종료하려면 -1: "))
    if score == -1:
        break
    elif score < 0 or score > 100:
        print("0부터 100 사이의 점수만 입력하세요.")
        continue
    else:
        total += score
        count += 1

if count == 0:
    print("입력된 정상 점수가 없습니다.")
else:
    print(f"입력한 학생 수: {count}명")
    print(f"점수 합계: {total}점")
    print("점수 평균: " + str(total/count) + "점")

# if score == -1:
#     break
# elif score < 0 or score > 100:
# -1도 0보다 작지만, 
# 먼저 종료 신호인지 검사하기 때문에
# 오류 점수로 처리되지 않고 정상적으로 종료된다.