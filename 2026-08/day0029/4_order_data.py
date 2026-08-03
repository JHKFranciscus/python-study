order_ids = ["A101", "A102", "A103", "A104", "A105"]
customers = ["민수", "지수", "현우", "서연", "도윤"]

unit_prices = [8000, 12000, 5000, 15000, 7000]
quantities = [2, 1, 3, 2, 4]
delivery_fees = [3000, 0, 3000, 0, 3000]

payment_statuses = [True, False, True, True, False]

order_totals = [unit_price * quantity + delivery_fee for unit_price, quantity, delivery_fee in zip(unit_prices, quantities, delivery_fees)]

#1단계 — 주문별 최종 금액 계산
print(order_totals)

#2단계 — 전체 주문에 번호를 붙여 출력
print()
orders_zip = zip(order_ids, customers, order_totals, payment_statuses)

# 예상 결과:
# [19000, 12000, 18000, 30000, 31000]
# 실제 결과:
# [19000, 12000, 18000, 30000, 31000]

for number, (order_id, customer, order_total, is_paid) in enumerate(orders_zip, start=1):

    if is_paid:
        status_text = "결제 완료"
    else:
        status_text = "결제 대기"

    print(f"{number}번 주문 / {order_id} / {customer} / {order_total}원 / {status_text}")

#3단계 — 결제가 완료된 주문번호만 선택
print()
# paid_order_ids = [order_id for order_id, payment_statuse in zip(order_ids, payment_statuses) if payment_statuse is True]
paid_order_ids = [order_id for order_id, payment_statuse in zip(order_ids, payment_statuses) if payment_statuse]


print(paid_order_ids)

# 예상 결과: ['A101', 'A103', 'A104']
# 실제 결과: ['A101', 'A103', 'A104']


#4단계 — 결제 완료이면서 2만 원 이상인 주문 선택
print()
# high_value_paid_order_ids = [order_id for order_id, order_total, payment_statuse in zip(order_ids, order_totals, payment_statuses) if order_total >= 20000 and payment_statuse is True]
high_value_paid_order_ids = [order_id for order_id, order_total, payment_statuse in zip(order_ids, order_totals, payment_statuses) if order_total >= 20000 and payment_statuse]

print(high_value_paid_order_ids)

# 예상 결과: ['A104']
# 실제 결과: ['A104']

#5단계 — 결제가 완료된 주문의 매출 합계
print()
paid_order_totals = [order_total for order_total, payment_statuse in zip(order_totals, payment_statuses) if payment_statuse is True]
paid_order_totals = [order_total for order_total, payment_statuse in zip(order_totals, payment_statuses) if payment_statuse]


print(paid_order_totals)

total_paid_sales = sum(paid_order_totals)
print(f"결제 완료 매출: {total_paid_sales}원")

# 예상 결과: [19000, 18000, 30000]
# 실제 결과: [19000, 18000, 30000]

# 예상 결과: 결제 완료 매출: 67000원
# 실제 결과: 결제 완료 매출: 67000원

# 1. order_totals는 기존 리스트 중 하나를 수정한 것인가, 새로 만든 리스트인가?
# 새로 만든 리스트
# 2. zip() 안에 리스트 네 개를 넣으면 반복할 때 몇 개의 값이 한 묶음으로 제공되는가?
# 4개의 값이 1묶음으로 제공된다.
# 3. 고액 주문을 찾을 때 결제 여부와 금액 조건을 모두 검사해야 하는 이유는 무엇인가?
# 두 조건을 모두 충족해야 원하는 결과를 얻을 수 있기 때문이다.
#[보완]
# 결제가 완료되지 않은 31000원 주문 A105를 제외하고, 결제는 완료됐지만 20000원 미만인 주문도 제외해야 하기 때문이다.