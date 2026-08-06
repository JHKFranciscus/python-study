def add_label(label):
    print(f"설정값 받음: {label}")

    def decorator(original_function):
        print(f"원래 함수 받음: {original_function.__name__}")
        print(f"기억 중인 설정값: {label}")

        def wrapper(name):
            print(f"[{label}] 처리 시작")

            result = original_function(name)

            print(f"[{label}] 처리 종료")
            return result

        return wrapper

    return decorator

@add_label("주문")
def process_product(name):
    return f"{name} 처리 결과"

print(process_product)
print(process_product("책"))
print()
@add_label("배송")
def ship_product(name):
    return f"{name} 배송 결과"

print(ship_product)
print(ship_product("키보드"))