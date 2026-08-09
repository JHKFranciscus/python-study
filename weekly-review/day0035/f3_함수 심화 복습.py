# 문제 1 — 함수 객체와 callback
def double(number):
    print("double 실행")
    return number * 2


def process(func, value):
    print("process 시작")
    result = func(value)
    print("process 끝")
    return result


answer = process(double, 5)
print(answer)

# 예상 결과:
# process 시작
# double 실행
# process 끝
# 10

# double과 double() 중
# process에 double을 전달해야 하는 이유:
# 함수 객체를 전달해야 함수를 원하는 지점에서 원하는 방식으로 작동할 수 있기 때문이다.


# 문제 2 — lambda, map(), filter()
numbers = [1, 2, 3, 4, 5]

mapped = map(lambda number: number * 10, numbers)
filtered = filter(lambda number: number >= 30, mapped)

print(list(filtered))
print(list(mapped))

# 첫 번째 print 예상 결과:
# [30, 40, 50]

# 두 번째 print 예상 결과:
# []

# 이유:
# mapped와 filtered는 지연 계산하는 1회성 iterator인데 list(iterator)나 값을 요구하면 실행하여 값을 준다. 근데 list(filtered)로 mapped에서 값을 요구했었고, mapped는 값을 전부 소진했었기 때문에 두 번째 print()는 빈 리스트가 나온다.


# 문제 3 — decorator 실행 흐름
def logger(func):
    def wrapper():
        print("전")
        func()
        print("후")

    return wrapper


@logger
def hello():
    print("안녕")


hello()

# 예상 결과:
# 전
# 안녕
# 후

# @logger가 적용된 뒤
# hello라는 이름이 가리키는 함수는 무엇인가?
# hello = logger(hello)가 된다.
#수정 후
#logger가 반환한 wrapper 함수를 가리킨다.
