name = input("이름을 입력하세요: ")

age = int(input("나이를 입력하세요: "))

# n_age라는 새로운 변수를 만들고 그 변수가 age + 1이라면
# n_age = age + 1, str안에는 n_age가 되어야한다
age += 1
print(name + "님의 내년 나이는 " + str(age) + "살입니다.")