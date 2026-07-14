def add_fee(amount):
    print("A")
    result = amount + 2000
    return result


def apply_coupon(amount):
    print("B")
    result = amount - 3000
    return result


def calculate_payment(price):
    print("C")
    discounted_price = apply_coupon(price)
    final_price = add_fee(discounted_price)
    print("D")
    return final_price


print("E")
payment = calculate_payment(20000)
print("F")
print(payment)

# 문제 1. 출력되는 문자 순서:E, C, B, A, D, F
# 문제 2. apply_coupon의 반환값:17000
# 문제 3. add_fee의 amount에 전달되는 값: 17000
# 문제 4. add_fee의 반환값: 19000
# 문제 5. calculate_payment의 반환값: 19000
# 문제 6. payment의 최종 값: 19000
# 문제 7. 마지막 화면 출력값: 19000