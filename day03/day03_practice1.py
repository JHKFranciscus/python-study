score = int(input("점수를 입력하세요.: "))
check_rate = int(input("출석률을 입력하세요.: "))

if score < 0 or score > 100 or check_rate <0 or check_rate > 100:
    print("잘못된 입력입니다.")
elif score >=70 and check_rate >=80:
    print("수료입니다.")
else:
    print("미수료입니다.")
