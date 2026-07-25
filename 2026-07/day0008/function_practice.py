# 첫 번째 함수 — 매개변수 없는 함수

def print_menu():
    print("1. 점수 입력")
    print("2. 점수 계산")
    print("3. 종료")

print_menu()

#함수 안에서 프린트 할려면 print_munu("1. 점수입력")이 아니라 그냥 print해야한다.

# 두 번째 함수 — 매개변수가 있는 함수

def print_sum(number1, number2):
    print(f"합계: {number1 + number2}")

print_sum(10, 20)
print_sum(7, 5)

# 세 번째 함수 — return 사용

def add(number1, number2):
    result = number1 + number2
    return result

answer = add(30, 40)
print(answer)

answer2 = add(30, 40)
final_answer = answer2 * 2
print(final_answer)

# 문제 1 — 큰 수 반환

def find_larger(number1, number2):
    largest = number1
    if number1 < number2:
        largest = number2
    return largest

result = find_larger(15, 27)
print(result)

# 문제 2 — 합격 여부 반환

def is_pass(score):
    if score >= 60:
        result = True
    else:
        result = False
    return result

print(is_pass(80))
print(is_pass(45))

# score를 pass로하면 오류가 뜬다.
# pass는 Python이 이미 특별한 용도로 사용하는 예약어다.
# if score >= 60:
#     pass
# 이때 pass는 “아무 작업도 하지 않고 넘어간다”는 명령어다. 따라서 변수나 매개변수 이름으로 쓸 수 없다.
# def is_pass(score):
#     return score >= 60
#로 줄일 수도 있다

# 문제 3 — 리스트 합계 반환

def calculate_total(scores):
    total = 0
    for i in scores:
        total += i
    
    return total

scores = [70, 90, 60, 100, 80]
total = calculate_total(scores)
print(total)
