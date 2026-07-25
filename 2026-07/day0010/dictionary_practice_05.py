menu_prices = {
    "김밥": 3000,
    "라면": 4000,
    "떡볶이": 4500,
    "순대": 5000
}

discontinued_menu = "라면"

if discontinued_menu in menu_prices:
    del menu_prices[discontinued_menu]
    print(f"{discontinued_menu} 메뉴를 삭제했습니다.")
else:
    print("등록되지 않은 메뉴입니다.")

# continued_menu = 0

for menu, price in menu_prices.items():
    print(f"{menu}: {price}원")
    # continued_menu += 1

# print("남은 메뉴 수:", continued_menu)
print("남은 메뉴 수:", len(menu_prices))
#그냥 menu_prices의 길이를 쓰면 된다.

#예상출력
# 라면메뉴를 삭제했습니다.
# 김밥: 3000원
# 떡볶이: 4500원
# 순대: 5000원
# 남은 메뉴 수: 3