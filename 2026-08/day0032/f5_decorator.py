def add_message(original_function):
    def wrapper(number):
        print("함수 실행 전")
        result = original_function(number)
        print("함수 실행 후")
        return result

    return wrapper


def double_number(number):
    return number * 2


decorated_double = add_message(double_number)

print(decorated_double(5))

# 첫 번째 코드 예상 결과:
# 함수 실행 전
# 함수 실행 후
# 10

# 판단 질문
# 1. add_message()가 인자로 받은 것은 함수 객체인가, double_number(5)의 호출 결과인가?
# wrapper 함수 객체이다.
#[수정]
#1. add_message()가 인자로 받은 것은: double_number 함수 객체이다.
#double_number(5)의 호출 결과를 받은 것이 아니다.
# 2. add_message(double_number)의 반환값은 무엇인가?
# wrapper 함수 객체이다.
# 3. decorated_double에 저장된 함수 객체는 double_number인가, wrapper인가?
# wrapper
# 4. decorated_double(5)를 호출했을 때 실제로 가장 먼저 실행되는 함수는 double_number인가, wrapper인가?
# wrapper
# 5. wrapper 내부에서 원래 함수가 호출되는 부분:
# result = original_function(number)
# 6. wrapper가 original_function을 사용할 수 있는 이유:
# 내부 함수가 이 함수를 감싸는 바깥 함수 영역의 변수를 기억하고 있기 때문


# 3. @ 문법으로 변경하기
print()
def add_log(original_function):
    def wrapper(number):
        print(f"{original_function.__name__} 실행 시작")
        result = original_function(number)
        print(f"{original_function.__name__} 실행 종료")
        return result

    return wrapper


@add_log
def add_ten(number):
    return number + 10


print(add_ten(7))

# 두 번째 코드 예상 결과:
# add_ten 실행 시작
# add_ten 실행 종료
# 17

# 판단 질문
# 1. @add_log가 적용된 시점은 add_ten(7)을 호출할 때인가,add_ten 함수를 정의한 직후인가?
# add_ten 함수를 정의한 직후이다.
# 2. 다음 @ 문법과 같은 의미의 코드를 작성:
# @add_log
# def add_ten(number):
#     return number + 10
# 같은 의미:
# def add_ten(number):
#     return number + 10

# add_ten = add_log(add_ten)
# 3. 데코레이터 적용 후 add_ten이라는 이름에는 원래 add_ten 함수와 wrapper 중 무엇이 저장되는가?
# wrapper
# 4. 원래 add_ten 함수 객체는 완전히 사라지는가? 예상과 이유:
# add_log의 original_function에 저장되었으므로 완전히 사라지지는 않는다.
# 5. original_function.__name__이 나타내는 것:
# add_ten


# 4. 실행 전과 함수 호출 시점을 구분하는 실습
print()
def trace_decorator(original_function):
    print("데코레이터 함수 실행")

    def wrapper(number):
        print("wrapper 실행")
        return original_function(number)

    return wrapper


@trace_decorator
def square(number):
    print("원래 함수 실행")
    return number * number


print("함수 호출 전")
print(square(4))

# 세 번째 코드 예상 결과:
# 함수 호출 전
# 데코레이터 함수 실행"
# wrapper 실행
# 원래 함수 실행
# 16

# 판단 질문
# 1. "데코레이터 함수 실행"은 square(4)를 호출하기 전에도 출력되는가?
# square(4)를 호출해야 출력이 된다.
#[수정]
#square(4)를 호출하기 전에도 출력이 된다.
#@trace_decorator가 적용되면서 square 함수 정의 직후 trace_decorator(square)가 실행되기 때문이다.
# 2. trace_decorator가 실행되는 시점:
# square(4)가 실행되면 실행된다.
#[수정]
#square 함수를 정의한 직후 @trace_decorator가 적용되는 시점이다.
#square(4)를 실제로 호출하는 시점이 아니다.
# 3. wrapper가 실행되는 시점:
# square(4)가 실행되면 실행된다.
# 4. 원래 square 함수가 실행되는 시점:
# original_function(number)
# 5. 다음 세 실행의 순서를 작성:
# wrapper 실행 / 원래 함수 실행 / 결과 16 출력

# 실제 결과:
# 첫 번째 코드:
# 함수 실행 전
# 함수 실행 후
# 10
# 두 번째 코드:
# add_ten 실행 시작
# add_ten 실행 종료
# 17
# 세 번째 코드:
# 데코레이터 함수 실행
# 함수 호출 전
# wrapper 실행
# 원래 함수 실행
# 16
# 예상 결과와 실제 결과의 차이:
# 뭔가 차이가 많이 난다
#[수정]
#첫 번째 코드와 두 번째 코드는 차이 없음
#세 번째 코드에서는 "데코레이터 함수 실행"의 위치를 잘못 예상했다. 예상에서는 "함수 호출 전" 뒤에 출력된다고 생각했지만, 실제로는 square 함수 정의 직후 데코레이터가 적용되므로 "함수 호출 전"보다 먼저 출력됐다.