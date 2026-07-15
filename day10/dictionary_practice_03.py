product_stock = {
    "노트": 5,
    "볼펜": 15,
    "지우개": 8,
    "연필": 20
}

minimum_stock = 10

low_stock_count = 0

print("재고 부족 상품")

for product_name in product_stock:
    stock = product_stock[product_name]
    if stock < minimum_stock:
        print(f"{product_name}의 재고는 {stock}개입니다.")
        low_stock_count +=1

print(f"재고 부족 상품 수: {low_stock_count}")

# 예상 출력
# 재고 부족 상품
# 노트의 재고는 5개입니다.
# 지우개의 재고는 8개입니다.
# 재고 부족 상품 수: 2