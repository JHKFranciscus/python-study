age = int(input("나이를 입력하세요: "))
has_ticket = input("티켓이 있나요? yes/no: ")

if age >= 19 and has_ticket == "yes": # = 연산자가 아니고, ==연산자이다.
    print("입장 가능")
else:
    print("입장 불가")