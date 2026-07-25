# 상품 금액을 계산하는 함수
def calculate_subtotal(price, quantity):
    return price * quantity

# 할인 후 금액을 계산하는 함수
def apply_discount(subtotal, discount_rate):
    # return subtotal * discount_rate
    # 수정 전 위의 식은 할인하는 금액을 계산하는 것이지 할인된 금액을 계산하는 게 아니다.
    return subtotal * (1 - discount_rate)
# 가격 저장
price = 12000
# 수량 저장
quantitiy = 3
# 할인율 저장
discount_rate = 0.1
# 상품 금액 계산 함수 호출
subtotal = calculate_subtotal(price, quantitiy)
# 할인 함수 호출
discout_total = apply_discount(subtotal, discount_rate)
# 상품 금액 출력
print(f"상품 금액: {subtotal}")
# 할인 후 금액 출력
print(f"할인 후 금액: {discout_total}")


#문제1
# 호출 시 각각 무엇이 매개변수이고 무엇이 인수인지 적어라.
# subtotal = calculate_subtotal(price, quantity)

# 매개변수: def calculate_subtotal(price, quantity): 의 price, quantity
# 인수: subtotal = calculate_subtotal(price, quantity) 의 price, quantity

#문제2
# 호출 직후 함수 안에서 각 매개변수에 연결된 값을 적어라.
# discount_total = apply_discount(subtotal, discount_rate)

# 함수 안 subtotal: 36000
# 함수 안 discount_rate: 0.1

#문제 3
# 다음 두 subtotal은 같은 변수인가?
# def apply_discount(subtotal, discount_rate):
# subtotal = calculate_subtotal(price, quantity)

# 같은 변수인지: 아니다
# 이유: 
# 위의 subtotal은 apply_discount가 호출될 때 값이 연결되는 지역 변수이고,
# 아래 subtotal은 함수 밖 전역 범위의 변수이다.
# 이름은 같지만 서로 다른 범위에 있으므로 서로 다른 변수이다.

# 문제 4
# 다음 값과 자료형을 적어라.
# 예시는 다음 형식으로 적는다.
# price: 12000, int

# price: 12000, int
# quantity: 3, int
# discount_rate: 0.1, float
# subtotal: 36000, int
# 수정 전discount_total: 32400, float
# 수정 후 discount_total: 32400.0, float
# 수학적 크기는 같지만 python 자료형으로는 32400 != 32400.0

# 문제 5
# apply_discount()에서 return을 지우고 아래처럼 작성하면 discount_total에는 무엇이 저장되는가?
# def apply_discount(subtotal, discount_rate):
#     subtotal * (1 - discount_rate)

# discount_total에 저장되는 값: None
# 이유: return이 없거나 return만 있으면 None을 반환하기 때문이다.



# def check_scope(value):
#     doubled = value * 2
#     return doubled

# scope_result = check_scope(5)
# print(scope_result)
# print(doubled)

# print(scope_result)의 예상 결과: 10
# print(doubled)의 예상 결과: 오류 
# 두 번째 출력에서 그렇게 되는 이유: doubled라는 것은 함수 내에 선언된 지역변수였기에 함수 밖에서는 선언이 되어 있지 않아서 print를 하려고 하면 오류가 뜰 것이다.
# 좀 더 정확한 답
# print(doubled)의 예상 결과: NameError: name 'doubled' is not defined 
# 두 번째 출력에서 그렇게 되는 이유: 선언이라기 보다는 대입되어 만들어졌다고 하는 편이 정확하다
# 정확한 오류 원인:
# doubled는 check_scope 함수의 지역 변수이므로
# 함수 밖에서는 직접 사용할 수 없다.
# 함수가 반환한 값은 scope_result에 저장되어 있다.