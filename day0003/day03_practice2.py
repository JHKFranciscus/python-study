num = int(input("정수 하나를 입력하세요: "))

if num == 0:
    print("0입니다.")
elif num > 0 and num % 2 == 0:
    print("양의 짝수입니다.")
elif num > 0 and num % 2 != 0:
    print("양의 홀수입니다.")
elif num < 0 and num % 2 == 0:
    print("음의 짝수입니다.")
else:
    print("음의 홀수입니다.")

