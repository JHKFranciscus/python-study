#문제 1
print("===문제 1===")
records = [1, 1, 0, 1, 1, 1, 0, 1, 1]

count = 0
max_count = 0

for record in records:
    if record == 1:
        count += 1

    elif record == 0:
        count = 0

    if max_count <= count:
        max_count = count

print(max_count)

#문제 2
print()
print("===문제 2===")
stock = {
    "keyboard": 4,
    "mouse": 2,
    "monitor": 3
}

orders = [
    {"name": "keyboard", "count": 2},
    {"name": "mouse", "count": 3},
    {"name": "monitor", "count": 1},
    {"name": "speaker", "count": 1}
]

for order in orders:
    if order["name"] in stock:
        if stock[order["name"]] < order["count"]:
            print(f"{order["name"]}: 재고 부족")
        elif stock[order["name"]] >= order["count"]:
            print(f"{order["name"]}: 주문 가능")

    else:
        print(f"{order["name"]}: 상품 없음")
