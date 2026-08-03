item_names = ["텐트", "침낭", "버너", "랜턴", "의자"]
daily_prices = [18000, 7000, 9000, 5000, 4000]
rental_days = [2, 4, 3, 1, 5]
returned = [True, False, True, True, False]

print("===대여료 계산===")
rental_totals = [daily_price * rental_day for daily_price, rental_day in zip(daily_prices, rental_days)]

print(rental_totals)


print()
print("===전체 대여 기록 출력===")
all_info = zip(item_names, daily_prices, rental_totals, returned)

for number, (item_name, daily_price, rental_total, is_returned) in enumerate(all_info, start=1):

    if is_returned:
        return_info = "반납 완료"
    else:
        return_info = "미반납"

    print(f"{number}번 / {item_name} / {rental_total}원 / {return_info}")


print()
print("===미반납 물품만 선택===")
unreturned_items = [item_name for item_name, is_returned in zip(item_names, returned) if not is_returned]

print(unreturned_items)


print()
print("===2만 5천 원 이상인 반납 완료 물품===")
high_value_returned_items = [item_name for item_name, rental_total, is_returned in zip(item_names, rental_totals, returned) if is_returned and rental_total >= 25000]

print(high_value_returned_items)

print()
print("===미반납 대여료 합계===")
unreturned_totals = [rental_total for rental_total, is_returned in zip(rental_totals, returned) if not is_returned]

print(unreturned_totals)
print(f"미반납 대여료 합계: {sum(unreturned_totals)}원")


# 1. 문제 3에서는 returned가 True인 값을 선택해야 하는가, False인 값을 선택해야 하는가?
# False
# 2. 문제 4에서 zip()으로 함께 묶어야 하는 세 리스트는 무엇인가?
# item_names, rental_totals, returned
# 3. rental_totals를 만든 뒤 원본 daily_prices와 rental_days는 변경되는가?
# 그 둘을 계산하여 새로운 리스트를 만든 것이지 둘의 원본을 건드린 것은 아니므로 원본은 변경되지 않는다.