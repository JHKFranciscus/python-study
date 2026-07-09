# 1

num = int(input("숫자를 입력하세요: "))

if num >= 0:
    print("양수")
elif num ==0:
    print("0")
else:
    print("음수")

# 2

score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# 3

age = int(input("나이를 입력하세요: "))

if age >= 20:
    print("성인")
else:
    print("미성년자")

# 4

number = int(input("숫자를 입력하세요: "))

if number % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 5

age2 = int(input("나이를 입력하세요: "))
ticket = input("티켓 여부를 알려주세요. yes/no: ")

if age2 >= 20 and ticket == "yes":
    print("입장 가능")
else:
    print("입장 불가")