def calculate_book_total(book_price, quantity):
    return book_price * quantity


def apply_discount(book_total, discount_rate):
    return book_total * (1 - discount_rate)


def calculate_shipping_fee(book_total):
    if book_total < 30000:
        return 2500
    else:
        return 0

def calculate_final_payment(discounted_total, shipping_fee):
    return discounted_total + shipping_fee


book_price = 12000
quantity = 3
discount_rate = 0.1

book_total = calculate_book_total(book_price, quantity)
print("도서 금액:", book_total)
discounted_total = apply_discount(book_total, discount_rate)
print("할인 금액:", discounted_total)
shipping_fee = calculate_shipping_fee(book_total)
print("배송비:", shipping_fee)
final_payment = calculate_final_payment(discounted_total, shipping_fee)
print("최종 결제 금액:", final_payment)
