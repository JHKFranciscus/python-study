# 도서 금액을 계산하는 함수
def calculate_book_total(book_price, quantity):
    return book_price * quantity
# 할인 후 금액을 계산하는 함수
def apply_discount(book_total, discount_rate):
    return book_total *(1 - discount_rate)
# 배송비를 계산하는 함수
def calculate_shipping_fee(book_total):
    if book_total >= 30000:
        return 0
    else:
        return 2500    
# 최종 결제 금액을 계산하는 함수
def calculate_final_payment(discounted_total, shipping_fee):
    return discounted_total + shipping_fee
# 책 가격 저장
book_price = 12000
# 수량 저장
quantity = 3
# 할인율 저장
discount_rate = 0.1
# 도서 금액 계산
book_total = calculate_book_total(book_price, quantity)
# 할인 후 금액 계산
discounted_total = apply_discount(book_total, discount_rate)
# 배송비 계산
shipping_fee = calculate_shipping_fee(book_total)
# 최종 결제 금액 계산
final_payment = calculate_final_payment(discounted_total, shipping_fee)
# 결과 출력
print(final_payment)

# 예상값
# book_total: 36000
# discounted_total: 32400.0
# shipping_fee: 0
# final_payment: 32400.0