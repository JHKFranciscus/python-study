score = int(input("점수를 입력하세요: "))

if score > 100 or score < 0:
    print("잘못된 점수입니다.")
elif score >= 90:
    print("A등급입니다.")
elif score >= 80:
    print("B등급입니다.")
elif score >= 70:
    print("C등급입니다.")
else:
    print("D등급입니다.")