def add_fee(price):
    return price + 3000


def discount(price):
    return price * 0.9


def choose_action(member):
    if member:
        return discount
    else:
        return add_fee


prices = [10000, 20000, 30000]

action = choose_action(True)

results = []

for price in prices:
    result = action(price)
    results.append(result)

print(results)

# # A. 현재 무엇이 들어 있는가
# 다섯 개를 적어라.

# 1. prices =
# - collection 전체
# - [10000, 20000, 30000]

# 2. 첫 번째 반복의 price =
# - 요소 하나
# - 10000

# 3. choose_action(True)의 반환값 =
# - 함수 자체
# - discount

# 4. action =
# discount 함수 객체

# 5. 첫 번째 반복이 끝난 직후 result = 9000.0


# # B. func와 func() 판단

# 왜 choose_action() 내부에서

# return discount

# 가 맞고

# return discount()

# 가 아닌지 설명해라.

# 그리고 아래에서는 왜:

# result = action(price)

# action이 아니라 **action(price)**가 필요한지도 설명해라.

# 함수를 계산한 값이 아닌 함수 객체를 반환하여 조건을 충족시키는 값을 넣기위하여 discout()가 아닌 discount를 반환하였다.
# 또한 action에는 discount 함수 객체가 대입되어 있으므로 이를 호출하기 위해서는 인자가 필요하기 때문에 action이 아닌 action(price)가 필요하다.
# #[수정]
# return discount인 이유는 "조건을 충족시키는 값을 넣기 위해서"라기보다는, 그 시점에는 아직 처리할 price가 없고 나중에 가격을 받아 실행할 함수 자체가 필요하기 때문이다.

# # C. 호출부 역추적

# 첫 번째 반복만 대상으로 다음을 실제 값으로 채워라.

# action
# ← choose_action(True)의 반환값
# ← discount
# price
# ← prices에서 꺼낸 첫 번째 요소
# ← 10000
# action(price)
# = discount(10000)
# ↓
# 그 함수 내부의 price = 10000
# ↓
# 반환값 = 9000.0
# ↓
# result = 9000.0
# ↓
# results = [9000.0]