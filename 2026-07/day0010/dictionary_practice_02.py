# 딕셔너리 기초 문제 2 — 재고 수정과 상품 추가

product_stock = {
    "노트": 5,
    "볼펜": 10,
    "지우개": 8
}

product_stock["볼펜"] = 15
product_stock["연필"] = 20

for product_name in product_stock:
    stock = product_stock[product_name]
    print(f"{product_name}의 재고는 {stock}개입니다.")

# 예상출력결과
# 노트의 재고는 5개입니다.
# 볼펜의 재고는 15개입니다.
# 지우개의 재고는 8개입니다.
# 연필의 재고는 20개입니다.

