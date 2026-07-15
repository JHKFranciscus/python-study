product_prices = {
    "노트": 1500,
    "볼펜": 1000,
    "지우개": 500
}

product_name = "볼펜"

if product_name in product_prices:
    price = product_prices[product_name]
    print(f"{product_name}의 가격은 {price}원입니다.")
else:
    print("등록되지 않은 상품입니다.")

product_name = "연필"

if product_name in product_prices:
    price = product_prices[product_name]
    print(f"{product_name}의 가격은 {price}원입니다.")
else:
    print("등록되지 않은 상품입니다.")

product_name = "노트"

if product_name in product_prices:
    price = product_prices[product_name]
    print(f"{product_name}의 가격은 {price}원입니다.")
else:
    print("등록되지 않은 상품입니다.")


# [수정]
# 딕셔너리의 값을 먼저 조회하면 없는 키에서 KeyError가 발생한다.
# 따라서 if와 in으로 키의 존재를 먼저 확인한 뒤
# product_prices[product_name]으로 값을 조회해야 한다.
