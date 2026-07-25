# 상품 금액을 계산하는 함수
def calculate_subtotal(price, quantity):
    return price * quantity
# 할인 후 금액을 계산하는 함수
def apply_discount(subtotal, discount_rate):
    return subtotal * (1 - discount_rate)
# 배송비를 계산하는 함수
def calculate_shipping_fee(subtotal):
    if subtotal < 50000:
        return 3000
    else:
        return 0
# 최종 결제 금액을 계산하는 함수
def calculate_final_total(discounted_total, shipping_fee):
    return discounted_total + shipping_fee
# 가격 저장
price = 15000
# 수량 저장
quantity = 4
# 할인율 저장
discount_rate = 0.1
# 테스트1
# price = 12000
# quantity = 4
# discount_rate = 0.1
# 테스트2
# price = 10000
# quantity = 5
# discount_rate = 0.1
# 상품 금액 계산
subtotal = calculate_subtotal(price, quantity)
# 할인 후 금액 계산
discounted_total = apply_discount(subtotal, discount_rate)
# 배송비 계산
shipping_fee = calculate_shipping_fee(subtotal)
# 최종 결제 금액 계산
final_total = calculate_final_total(discounted_total, shipping_fee)
# 모든 결과 출력
print(f"상품 금액: {subtotal}")
print(f"할인 후 금액: {discounted_total}")
print(f"배송비: {shipping_fee}")
print(f"최종 결제 금액: {final_total}")

# 예상 결과
# subtotal: 60000
# discounted_total: 54000.0
# shipping_fee: 0
# final_total: 54000.0

# 테스트 1 예상 결과
# subtotal: 48000
# discounted_total: 43200.0
# shipping_fee: 3000
# final_total: 46200.0

# 테스트 2 예상 결과
# subtotal: 50000
# discounted_total: 45000.0
# shipping_fee: 0
# final_total: 45000.0