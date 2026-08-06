def apply_twice(func, value):
    return func(func(value))


def add_three(number):
    return number + 3


result1 = apply_twice(add_three, 4)
result2 = apply_twice(lambda number: number * 2, 5)

numbers = [1, 2, 3, 4]
mapped_numbers = map(lambda number: number + 10, numbers)

print(result1)
print(result2)
print(next(mapped_numbers))
print(list(mapped_numbers))
print(list(mapped_numbers))

# 1. 함수 객체를 전달한 부분:
# add_three(number)
#[수정]
#add_three
#lambda number: number * 2

# 2. 함수를 실제로 호출한 부분:
# apply_twice(add_three, 4)
#[수정]
#apply_twice(add_three, 4)
#apply_twice(lambda number: number * 2, 5)
#apply_twice() 내부의 func(func(value))에서 func가 두 번 호출된다.

# 3. 예상 결과:
# 10
# 20
# 11
# [12, 13, 14]
# []
# 4. 마지막 list(mapped_numbers)의 예상 결과와 그 이유:
# 빈 리스트가 나오는데 mapped_numbers는 지연 계산하는 1회성 iterator이기 때문에 값을 전부 소모하였기 떄문이다.

# 4. 판단할 질문
# apply_twice(add_three, 4)에서 add_three 뒤에 괄호를 붙이지 않은 이유는 무엇인가?
# ()는 호출하는 뜻으로 호출할 수 있는 객체 뒤에 붙이면 그 객체를 실행하는 행동을 하는데 이 경우는 함수 객체만을 전달고자 하기 떄문에 뒤에 괄호를 붙이지 않았다.
# apply_twice() 내부에서 전달받은 함수는 총 몇 번 호출되는가?
# 2번 호출된다.
# lambda number: number * 2 자체는 함수 객체인가, 함수 호출 결과인가?
# 자체는 함수 객체이다.
# 첫 번째 list(mapped_numbers)가 실행된 뒤 두 번째 결과가 달라지는 이유는 무엇인가?
# mapped_numbers는 지연 계산되는 1회성 iterator이기 때문에 요소를 1번 소모되면 다시 사용할 수 없기 때문이다.

# 5. 실제 결과:
# 10
# 20
# 11
# [12, 13, 14]
# []
#
# 예상 결과와 실제 결과의 차이:
# 차이 없음