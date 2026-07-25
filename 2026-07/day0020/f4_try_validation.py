input_price = input("가격을 입력하세요: ").strip()

try:
    price = int(input_price)

    if price <0:
        print("가격은 0 이상의 정수로 입력해주세요.")
    else:
        print("입력된 가격:", price)

except ValueError:
    print("가격은 0 이상의 정수로 입력해주세요.")

print("프로그램을 종료합니다.")

# abc를 입력하면:
# 예상:
# int("abc")에서 ValueError가 발생해 except ValueError로 이동한다.
# "가격은 0 이상의 정수로 입력해주세요."가 출력된다.
# 마지막의 "프로그램을 종료합니다."도 출력된다.

# -100을 입력하면:
# 예상:
# int("-100")은 성공해 정수 -100이 만들어진다.
# price < 0이 True여서 if 내부의 안내 문구가 출력된다.
# except는 실행되지 않고 마지막 문장도 출력된다.

# 8000을 입력하면:
# 예상:
# int("8000")이 성공하고 price < 0이 False여서 else가 실행된다.
# "입력된 가격: 8000"과 마지막 문장이 출력된다.

# 3.5를 입력하면:
# 예상:
# int("3.5")에서 ValueError가 발생해 except ValueError로 이동한다.
# 안내 문구와 마지막 문장이 출력된다.