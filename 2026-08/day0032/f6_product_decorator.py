def validate_product(original_function):
    def wrapper(product):
        if product["price"] <= 0:
            print("검사 실패: 가격은 0보다 커야 합니다.")
            return None

        if not 0 <= product["discount_rate"] <= 1:
            print("검사 실패: 할인율은 0부터 1 사이여야 합니다.")
            return None

        print("검사 통과")
        return original_function(product)

    return wrapper


def log_process(original_function):
    def wrapper(product):
        print(f"{product['name']} 처리 시작")

        result = original_function(product)

        if result is None:
            print(f"{product['name']} 처리 실패")
        else:
            print(f"{product['name']} 처리 종료")

        return result

    return wrapper


@log_process
@validate_product
def apply_discount(product):
    discounted_product = product.copy()

    discounted_product["final_price"] = int(
        product["price"] * (1 - product["discount_rate"])
    )

    print("할인 계산 실행")
    return discounted_product


book = {
    "name": "책",
    "price": 20000,
    "discount_rate": 0.1,
}

keyboard = {
    "name": "키보드",
    "price": -5000,
    "discount_rate": 0.2,
}


book_result = apply_discount(book)

print(book_result)
print(book)

print()

keyboard_result = apply_discount(keyboard)

print(keyboard_result)
print(keyboard)

# 예상 결과:
# 책 처리 시작
# 검사 통과
# 할인 계산 실행
# 책 처리 종료
# 18000
# {"name": "책", "price": 20000, "discount_rate": 0.1, "final_price": 18000}
#
# 키보드 처리 시작
# 검사 실패: 가격은 0보다 커야 합니다.
# 키보드 처리 실패
# None
# {"name": "키보드", "price": -5000, "discount_rate": 0.2,}

# 판단 질문
# 1. @log_process와 @validate_product는 어느 쪽부터 원래 apply_discount 함수에 적용되는가?
#@validate_product
# 2. 최종 apply_discount라는 이름에 저장된 것은 어느 데코레이터가 반환한 wrapper인가?
# @log_process
# 3. book을 처리할 때 함수 실행 순서:
# apply_discount(book)로 호출 -> log_process(original_function)의 내부 함수인 def wrapper(product)실행 -> result = original_function(product)에서 def validate_product(original_function)의 wrapper(product)을 호출하여 실행 -> return original_function(product)에서 def apply_discount(product)을 실행 -> discounted_product를 validate_product(original_function)의 original_function(product)에 반환 -> result = original_function(product)의 original_function(product)에 반환 -> return result로 result를 apply_discount(book)에 반환 후 book_result에 대입
#[수정]
#log_process가 반환한 wrapper 실행
#→ validate_product가 반환한 wrapper 실행
#→ 검사 통과
#→ 원래 apply_discount 실행
#→ 할인된 딕셔너리 반환
#→ log_process의 wrapper가 처리 종료 출력
#→ 최종 딕셔너리 반환
# 4. keyboard를 처리할 때 원래 apply_discount 함수까지 실행되는가? 예상과 이유:
# if product["price"] <= 0: 라는 조건 때문에 return None이 되어 함수가 실행되지 못하고 종료된다.
# 5. keyboard 처리에서 "할인 계산 실행"이 출력되는가?
# 원래 apply_discount 함수가 실행되지 않아 출력되지 않는다.
# 6. validate_product의 wrapper가 잘못된 상품에서 반환하는 값:
# None
# 7. log_process의 wrapper는 성공과 실패를 무엇으로 판단하는가?
# log_process의 wrapper는 성공과 실패를 판단하지 않는다. 다만 result의 값이 None인지 아닌지를 판단할 뿐이다.
#[수정]
#original_function(product)의 반환값인 result가 None인지 아닌지로 판단한다. result가 None이면 실패, None이 아니면 성공으로 판단한다.
# 8. apply_discount 안에서 product.copy()를 사용한 이유:
# 원본 객체를 유지하기 위해서 
# 9. book_result와 book은 같은 딕셔너리 객체인가? 예상과 이유:
# copy()이기 때문에 다른 객체이다.
# 10. keyboard_result의 예상값:
# None

# 실제 결과:
# 책 처리 시작
# 검사 통과
# 할인 계산 실행
# 책 처리 종료
# {'name': '책', 'price': 20000, 'discount_rate': 0.1, 'final_price': 18000}
# {'name': '책', 'price': 20000, 'discount_rate': 0.1}
# 
# 키보드 처리 시작
# 검사 실패: 가격은 0보다 커야 합니다.
# 키보드 처리 실패
# None
# {'name': '키보드', 'price': -5000, 'discount_rate': 0.2}

# 예상 결과와 실제 결과의 차이:
# book_result를 구하는 과정에서 생성한 값만 구했었다.
#[수정]
#book_result가 final_price 숫자 18000이라고 예상했지만, 실제로는 final_price가 추가된 복사본 딕셔너리 전체가 반환됐다.
#apply_discount()의 return 값이 discounted_product이기 떄문이다.
#그 외 실행 순서는 예상과 같았다.
