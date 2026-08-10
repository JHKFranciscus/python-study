def double(number):
    return number * 2


def add_ten(number):
    return number + 10


def process(number, action):
    result = action(number)
    return result


# # A
# 7을 double 방식으로 처리해서 14를 만들려고 한다.

# answer = process(7, ______)

# 빈칸에 들어가는 것은:
# double 인지 double() 인지 선택하고 왜 그런지 설명해라.

# double이다. double은 함수를 집어 넣지만 double()을 호출하여 실행하는 것이기 때문이다.

# # B
# 다음 코드에서:

# result = action(number)

# action과 action(number)는 각각 무엇인지 적어라.

# action = double
# action(number) = double(7)

# 여기서는 단순히 "함수" / "값"만 쓰지 말고, 첫 번째 호출을 기준으로 실제로 무엇인지까지 적어라.


# # C
# 아래 흐름을 호출부부터 역추적해라.

# answer = process(7, double)

# 다음을 채우면 된다.

# process의 number = 7
# process의 action = double

# action(number)
# 실제로 실행되는 함수 호출 = double(7)

# 그 함수의 반환값 = 14

# process의 result = 14

# process가 반환하는 값 = 14

# answer = 14