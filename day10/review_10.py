# 복습 1 — 반환값 전달과 실행 순서

def calculate_total(price, quantity):
    total = price * quantity
    return total


def apply_discount(total, discount_rate):
    discounted_total = total * (1 - discount_rate)
    return discounted_total


def calculate_payment(price, quantity, discount_rate):
    book_total = calculate_total(price, quantity)
    final_total = apply_discount(book_total, discount_rate)
    return final_total


payment = calculate_payment(12000, 3, 0.1)
print(payment)

# 1. 함수 정의가 모두 끝난 뒤 가장 먼저 실행되는 일반 명령:
# payment = calculate_payment(12000, 3, 0.1)
# 2. 처음 호출되는 함수:
# calculate_payment
# 3. calculate_payment 안에서 호출되는 첫 번째 함수:
# calculate_total
# 4. calculate_total이 반환하는 값:
# 36000
# 5. 반환된 값이 calculate_payment의 어떤 변수에 저장되는지:
# book_total
# 6. apply_discount에 전달되는 인자 2개:
# 36000, 0.1
# 7. apply_discount가 반환하는 값:
# 32400.0
# 8. calculate_payment가 최종적으로 반환하는 값:
# 32400.0
# 9. print로 출력되는 값:
# 32400.0
# 10. calculate_total의 지역 변수 total과
#     apply_discount의 매개변수 total은 같은 변수인지:
# 다른 변수이다. 전자는 지역변수로 함수 내에서 그 값이 정해졌다. 그리고 그 값을 매개변수 total에 반환하는 것이다. 매개변수 total은 그 값의 주소에 연결이 되는 것이지 전자인 total과 같은 주소지를 가지는 것은 아니다.
# [수정]
# 두 total은 서로 다른 함수 안의 지역 변수이므로 같은 변수가 아니다.
# calculate_total의 total 값 36000은 return되어 book_total에 저장된다.
# 이후 book_total이 apply_discount의 인자로 전달되고,
# apply_discount의 매개변수 total이 그 값을 받는다.


# 함수 복습 2 — 호출 스택과 역할 분리

def calculate_total(scores):
    total = 0

    for score in scores:
        total += score

    return total


def calculate_average(scores):
    total = calculate_total(scores)
    average = total / len(scores)
    return average


def print_result(scores):
    average = calculate_average(scores)
    print(average)


scores = [80, 90, 70]
print_result(scores)

# 1. 함수 정의가 끝난 뒤 가장 먼저 실행되는 일반 명령: scores = [80, 90, 70]
# 2. 처음 호출되는 함수: print_result(scores)
# 3. calculate_total이 실행되는 순간 호출 스택을
#    아래쪽부터 위쪽 순서로 작성: 프로그램 본문, print_result, calculate_average, calculate_total
# 4. calculate_total의 지역 변수: total, score
# [수정 후]
# scores, total, score
# 5. calculate_total이 종료되면 지역 변수 total은 어떻게 되는지: None의 값을 가진다.
# [수정 후]
# calculate_total이 종료되면 지역 변수 total이 None이 되는 것이 아니다.
# calculate_total의 호출 스택과 지역 변수 영역이 제거되면서 그 함수 안의 지역 변수 이름 total도 더는 존재하지 않는다.
# 6. calculate_total이 반환한 값은
#    calculate_average의 어떤 변수에 저장되는지: total
# 7. 각 함수의 역할:
#    calculate_total: scores의 값을 더한 후 반환한다.
#    calculate_average: calculate_total에서 반환 받은 값을 scores 길이만큼 나눈 후 반환한다.
#    print_result: calculate_average에서 반환 반은 값을 출력한다.

# 8. 최종 출력값: 80.0