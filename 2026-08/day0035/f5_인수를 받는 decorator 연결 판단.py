# repeat(3)
#    ↓
# decorator
#    ↓
# announce 함수가 들어감
#    ↓
# wrapper가 만들어짐
#    ↓
# announce 대신 wrapper가 연결됨
def repeat(times):
    def decorator(func):
        def wrapper(message):
            for _ in range(times):
                func(message)

        return wrapper

    return decorator


@repeat(3)
def announce(message):
    print(message)


announce("출발")

# # 문제 A — 각 인수 역추적

# 다음 코드 기준으로 답해라.

# @repeat(3)
# def announce(message):
#     print(message)

# announce("출발")

# 다음을 채워라.

# 1. repeat의 times = 3

# 2. decorator의 func = 함수 자체

# 3. wrapper의 message = "출발"

# 4. wrapper 내부의 func = announce
#[수정]
#4. wrapper 내부의 func = 원래 announce 함수

# 5. func(message)는 실제로 어떤 호출이 되는가?
# announce("출발")
#[수정]
#원래 announce("출발")


# # 문제 B — func와 func() 판단

# 다음 반환문이 왜 맞는지 설명해라.

# return decorator

# 왜 아래가 아닌가?

# return decorator()

# 그리고:

# return wrapper

# 는 왜 wrapper()가 아닌가?

# 각각 “지금 필요한 것이 값인지, 나중에 호출할 함수 자체인지”를 기준으로 설명해라.

# 둘 다 각각 인자가 들어온 시점에 계산을 할 수 있는 함수 객체 자체가 필요한 것이지 함수가 계산을 한 값이 필요한 것이 아니었기 때문이다.

# # 문제 C — 전체 연결

# 다음 빈칸을 채워라.

# @repeat(3)

# repeat(3)
# ↓
# times = 3
# repeat가 반환 = decorator

# 그 반환된 함수에
# 원래 함수 announce 가 들어감
# ↓
# func = announce
# ↓
# decorator가 반환 = wrapper

# 따라서 이후

# announce("출발")

# 실제로 먼저 호출되는 것 = wrapper("출발")
# ↓
# message = "출발"
# ↓
# func(message)
# = announce("출발")
#[수정]
#원래 announce("출발")


#region
#오답
# print()
# def is_adult(func):
#     def wrapper(age):
#         if age >= 20:
#             func(age)
#         else:
#             return "입장 불가"
        
#     return wrapper

# @is_adult
# def show_ticket(age):
#     return "입장권 발급"


# show_ticket(25)


# # 1. decorator에 전달한 것은 is_adult인가 is_adult()인가? 왜 그런가?
# # 아니다 is_adult()는 특정 값으로 특정 값을 전달하면 오류가 나기 때문이다.

# # 2. show_ticket(25)를 호출했을 때 장식된 함수 쪽에서 처음 받는 age는 몇인가?
# # 25

# # 3. 검사에 사용되는 함수는 실제로 어떤 함수인가?
# # wrapper(age)

# # 4. 검사가 통과했을 때 최종적으로 실행되는 원래 함수는 무엇인가?
# # show_ticket(age)
#endregion
def something(func):
    def decorate(func2):
        def wrapper(age):
            result = func(age)

            if result:
                return func2(age)
            else:
                return "입장 불가"

        return wrapper
    
    return decorate

def is_adult(age):
    return age >= 20

@something(is_adult)
def show_ticket(age):
    return "입장권 발급"
