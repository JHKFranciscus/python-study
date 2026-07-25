#1. 이름을 입력받는다.

name = input("이름을 입력하세요: ")

#2. 나이를 숫자로 입력받는다.

age = int(input("나이를 입력하세요: "))

#3. 첫 번째 숫자와 두 번째 숫자를 입력받는다.

f_num = int(input("첫 번째 숫자: "))
s_num = int(input("두 번째 숫자: "))

#인사말, 내년 나이, 두 숫자의 합을 출력한다.

인사말 = "안녕하세요"
next_age = age + 1

print(인사말 + name)
print("내년 나이는 ", next_age, "살 입니다.")
print("두 숫자의 합은 ", f_num + s_num, "입니다.")
