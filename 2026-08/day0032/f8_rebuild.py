def log_order(original_function):
    def wrapper(order):
        print(f"{order["name"]} 처리 시작")

        result = original_function(order)

        if result is None:
            print(f"{order['name']} 처리 실패")

        else:
            print(f"{order['name']} 처리 완료")

        return result

    return wrapper

def validate_order(original_fuction):
    def wrapper(order):
        if order["price"] <= 0:
            print("가격이 0 이하")
            return None

        if order["quantity"] <= 0:
            print("수량이 0 이하")
            return None

        print("검사 통과")        
        return original_fuction(order)

    return wrapper

@log_order
@validate_order
def calculate_order(order):
    order_copy = order.copy()
    total_price = order["price"] * order["quantity"]
    order_copy["total_price"] = total_price
    return order_copy

def make_success_counter(store_name):
    success_count = 0

    def record(result):
        nonlocal success_count

        if result is not None:
            success_count += 1

        return f"{store_name}: 성공 주문 {success_count}건"
    
    return record


book_order = {
    "name": "책",
    "price": 12000,
    "quantity": 2,
}

keyboard_order = {
    "name": "키보드",
    "price": -30000,
    "quantity": 1,
}

mouse_order = {
    "name": "마우스",
    "price": 25000,
    "quantity": 2,
}

record_success = make_success_counter("파이썬 상점")

book_result = calculate_order(book_order)
print(book_result)
print(book_order)
print(record_success(book_result))

print()

keyboard_result = calculate_order(keyboard_order)
print(keyboard_result)
print(keyboard_order)
print(record_success(keyboard_result))

print()

mouse_result = calculate_order(mouse_order)
print(mouse_result)
print(mouse_order)
print(record_success(mouse_result))


