def make_multiplier(multiplier):
    def multiply(number):
        return number * multiplier

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))
print(triple(10))
print(double(5))

# 첫 번째 코드 예상 결과:
# 20
# 30
# 10

# 판단 질문
# 1. make_multiplier(2)의 반환값은 숫자인가, 함수 객체인가?
# 함수 객체
# 2. return multiply에서 multiply 뒤에 괄호가 없는 이유는 무엇인가?
# 함수의 결과값이 아닌 함수 객체를 반환하기 위해서
# 3. double(10)을 호출했을 때 multiplier와 number의 값:
# multiplier: 2
# number: 10
# 4. triple(10)을 호출했을 때 multiplier와 number의 값:
# multiplier: 3
# number: 10
# 5. make_multiplier(2)의 호출이 이미 끝났는데도 double이 multiplier의 값 2를 사용할 수 있는 이유:
# make_multiplier가 double에 multiply를 closing했기 때문이다.
# [수정]
# make_multiplier(2)가 실행될 때 만들어진 multiply 함수가 자신을 감싸는 make_multiplier의 multiplier = 2를 기억하기 때문이다.
# 반환된 multiply 함수 객체가 double에 저장된 뒤에도 이 값을 사용할 수 있다.
# 6. double과 triple은 완전히 같은 함수 객체인가? 예상과 이유:
# double은 multiply 함수의 multiplier에 2를 대입한 함수 객체이고, triple은 multiply 함수의 multiplier에 3을 대입한 함수 객체이기 때문에 다른 함수 객체이다.

def make_discount(rate):
    def apply_discount(price):
        return int(price * (1 - rate))

    return apply_discount


discount_10 = make_discount(0.1)
discount_20 = make_discount(0.2)

prices = [10000, 15000, 20000]

result_10 = list(map(discount_10, prices))
result_20 = list(map(discount_20, prices))

print(result_10)
print(result_20)


# 두 번째 코드 예상 결과:
# [9000, 13500, 18000]
# [8000, 12000, 16000]

# 판단 질문
# 1. discount_10이 기억하는 rate:
# 0.1
# 2. discount_20이 기억하는 rate:
# 0.2
# 3. map()에 전달된 함수 객체:
# apply_discount
# [수정]
# 3. map()에 전달된 함수 객체:
# discount_10
# discount_20
# 두 변수에는 각각 make_discount()가 반환한 apply_discount 함수 객체가 저장되어 있다.
# 4. 다음 코드가 함수 객체를 반환하는 부분인지, 함수를 호출한 결과를 반환하는 부분인지 작성:
# return apply_discount
# 함수 객체를 반환하는 부분이다.
# 5. apply_discount()가 price뿐 아니라 rate도 사용할 수 있는 이유:
# make_discount가 apply_discount를 discount_10나, discount_20에 closing 했기 때문이다.
# [수정]
# apply_discount가 make_discount 내부에서 만들어졌기 때문에 반환된 뒤에도 자신을 감싸는 영역의 rate를 기억한다.
# discount_10은 0.1을, discount_20은 0.2를 기억한다.

# 실제 결과:
# 20
# 30
# 10
# [9000, 13500, 18000]
# [8000, 12000, 16000]

# 예상 결과와 실제 결과의 차이:
# 차이 없음
