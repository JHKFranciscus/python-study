# 1. nonlocal이 없을 때
def make_counter():
    count = 0

    def increase():
        count = count + 1
        return count

    return increase


counter = make_counter()

print(counter())

# 첫 번째 코드 예상: 정상 실행되는가, 오류가 발생하는가?
# 정상실행 된다.
# 예상 결과 또는 예상 오류:
# 1
# 이유:
# 내부 함수인 increase가 enclosing 영역의 값인 count = 0의 값을 기억하고 있기 떄문이다.
#[수정]
#실제 실행
# 오류가 발생한다.
# UnboundLocalError
# 파이썬은 increase() 내부의 count를 기본적으로 Local 변수라고 판단한다.
# 그런데 오른쪽의 count + 1을 계산할 때 아직 Local count에는 값이 들어 있지 않다.
# 따라서 오류가 발생한다.

# 2. nonlocal 적용
def make_fixed_counter():
    count = 0

    def increase():
        nonlocal count
        count = count + 1
        return count

    return increase


counter_a = make_fixed_counter()
counter_b = make_fixed_counter()

print(counter_a())
print(counter_a())
print(counter_a())
print(counter_b())
print(counter_b())

# 두 번째 코드 예상 결과:
# 1
# 2
# 3
# 1
# 2

# 판단 질문
# 1. nonlocal count는 새로운 count 변수를 만드는 코드인가?
# 아니다. nonlocal count라는 코드가 들어있는 함수를 감싸는 함수의 영역에 있는 count를 사용하고 변경하겠다는 의미의 코드이다.
# 2. increase()에서 변경되는 count는 어느 영역의 변수인가?
# make_fixed_counter 영역의 변수이다.
# 3. counter_a를 세 번 호출했을 때 값이 누적되는 이유:
# counter_a는 같은 함수 호출이므로 동일한 count를 사용하여 누적하기 때문이다.
# 4. counter_b의 첫 호출 결과가 4가 아니라 1인 이유:
# counter_b는 counter_a와는 다른 함수 호출이기 때문이다.
#[보완]
#counter_b는 make_fixed_counter()를 새로 호출해 만든 별도의 클로저이므로 counter_a의 count와 관계없이 자신의 count = 0에서 시작한다.
# 5. counter_a와 counter_b는 같은 count를 공유하는가?
# 다른 count를 공유한다.
#[수정]
#counter_a와 counter_b는 같은 count를 공유하지 않는다.
#make_fixed_counter()를 각각 호출하면서 만들어진 별도의 count를 기억한다.


#3. 상품 판매 횟수 클로저
def make_sales_counter(product_name):
    sales_count = 0

    def sell(quantity):
        nonlocal sales_count
        sales_count += quantity
        return f"{product_name}: 누적 {sales_count}개 판매"

    return sell


book_sales = make_sales_counter("책")
keyboard_sales = make_sales_counter("키보드")

print(book_sales(2))
print(book_sales(3))
print(keyboard_sales(1))
print(book_sales(5))

# 세 번째 코드 예상 결과:
# 책: 누적 2개 판매
# 책: 누적 5개 판매
# 키보드: 누적 1개 판매
# 책: 누적 10개 판매

# 판단 질문
# 1. product_name은 내부 함수에서 읽기만 하는가, 변경하는가?
# 읽기만 한다.
# 2. sales_count에만 nonlocal이 필요한 이유:
# enclosing영역에서 정의된 값을 사용하고 변경하기 떄문이다.
# 3. book_sales가 마지막에 기억하는 sales_count:
# 10
# 4. keyboard_sales가 마지막에 기억하는 sales_count:
# 1

# 실제 결과:
# 첫 번째 코드:
# 오류 종류:UnboundLocalError
# 핵심 원인:
# cannot access local variable 'count' where it is not associated with a value
# 두 번째 코드:
# 1
# 2
# 3
# 1
# 2
# 세 번째 코드:
# 책: 누적 2개 판매
# 책: 누적 5개 판매
# 키보드: 누적 1개 판매
# 책: 누적 10개 판매
# 예상 결과와 실제 결과의 차이:
# 처음 코드에서는 오류가 발생됐다.




























