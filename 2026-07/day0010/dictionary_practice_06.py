product_prices = {
    "노트": 1500,
    "볼펜": 1000,
    "지우개": 500
}

purchase_quantities = {
    "노트": 2,
    "볼펜": 3,
    "지우개": 1
}

total_payment = 0

#[수정 전]
# for product_name, price in product_prices.items():
#     price = product_prices["노트"]
#     quantity = purchase_quantities["노트"]
#     print(f"{product_name}는 {price}원이고, {quantity}개이다.")
#     item_total = price * quantity
#     total_payment += item_total

for product_name, price in product_prices.items():
    quantity = purchase_quantities[product_name]
    item_total = price * quantity
    print(f"{product_name}: {price}원 * {quantity}개 = {item_total}원")
    total_payment += item_total

print(f"전체 결제 금액은 {total_payment}원.")

#예상 출력
# 노트: 1500원 * 2개 = 3000원
# 볼펜: 1000원 * 3개 = 3000원
# 지우개: 500원 * 1개 = 500원
# 전체 결제 금액은 6500원.

# [수정]
# 반복문 안에서 "노트"라는 키를 직접 사용했기 때문에
# 모든 상품에 노트의 가격과 수량이 적용되었다.
# price는 product_prices.items()에서 이미 전달받는다.
# 수량은 purchase_quantities[product_name]으로
# 현재 반복 중인 상품의 값을 조회해야 한다.