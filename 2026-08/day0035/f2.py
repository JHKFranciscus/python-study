def apply_discount(price, rate):
    discounted = price - price * rate
    return discounted


def add_shipping(amount, shipping):
    total = amount + shipping
    return total


price = 50000
discount_rate = 0.2
shipping_fee = 3000

price = apply_discount(price, discount_rate)
final_price = add_shipping(price, shipping_fee)

print(final_price)



# 1. apply_discount() 호출 직전
# price = 50000
# discount_rate = 0.2
# shipping_fee = 3000

# 2. apply_discount(price, discount_rate) 호출 시
# apply_discount의 price = 50000
# apply_discount의 rate = 0.2

# 3. apply_discount 내부에서
# discounted = 40000.0

# 4. apply_discount가 끝난 직후
# 바깥쪽 price = 40000.0

# 5. add_shipping(price, shipping_fee) 호출 시
# add_shipping의 amount = 40000.0
# add_shipping의 shipping = 3000

# 6. add_shipping 내부에서
# total = 43000.0

# 7. 함수 호출이 모두 끝난 후
# price = 40000.0
# final_price = 43000.0

# 1. 처음의 price = 50000과 마지막의 price는 같은 값을 가지고 있는가?
# False

# 2. apply_discount() 내부의 price와 함수 밖의 price는 같은 변수인가?
# False 내부의 price는 매개변수이고, 함수 밖의 price는 전역변수로 값을 인자로 전달해주기는 해도 별개의 변수이다.

# 3. add_shipping(price, shipping_fee)에서 amount에 들어가는 값은 어디에서 나온 것인가?
# 함수 호출부인 add_shipping(price, shipping_fee)의 price인자에서 나온 것이다.
