def multiply(numer1, number2):
    print("multiply 시작")

    result = numer1 * number2

    print("multiply 종료")
    return result


def calculate_subtotal(price, quantity):
    print("calculate_subtotal 시작")

    subtotal = multiply(price, quantity)

    print("calculate_subtotal 종료")
    return subtotal


def calculate_order(price, quantity):
    print("calculate_order 시작")

    subtotal = calculate_subtotal(price, quantity)
    final_total = subtotal + 3000

    print("calculat_order 종료")
    return final_total


print("프로그램 시작")

result = calculate_order(12000, 4)

print("프로그램 종료")
print(f"최종금액: {result}")

# 문제 1. 출력 순서
# 다음 문장들이 실제로 출력되는 순서대로 적는다.
# 1. 프로그램 시작
# 2. calculate_order 시작
# 3. calculate_subtotal 시작
# 4. multiply 시작
# 5. multiply 종료
# 6. calculate_subtotal 종료
# 7. calculate_order 종료
# 8. 프로그램 종료
# 9. 최종금액: 51000

# 문제 2
# multiply()가 실행되는 동안 아직 끝나지 않은 실행 단위를 아래에서 위 순서로 적는다.
# 호출 스택 아래:
# 프로그램 본문
# calculate_order(12000, 4)
# calculate_subtotal(price, quantity)
# multiply(price, quantity)
# 호출 스택 위:

# 문제 3
# multiply가 반환한 값: 48000
# calculate_subtotal에서 값이 저장되는 변수: subtotal
# 다음으로 실행되는 코드: print("calculate_subtotal 종료")

# 문제 4
# multiply의 반환값: 48000
# calculate_subtotal의 반환값: 48000
# calculate_order의 subtotal: 48000
# calculate_order의 final_total: 51000
# 함수 밖 result: 51000
# 최종 출력 금액: 51000


# 문제 5. 함수가 반환될 때 호출 스택 변화

# 1. multiply가 실행 중일 때
# 호출 스택 아래:
# 프로그램 본문
# calculate_order(12000, 4)
# calculate_subtotal(price, quantity)
# multiply(price, quantity)
# 호출 스택 위:


# 2. multiply가 48000을 반환한 직후
# 호출 스택 아래:
# 프로그램 본문
# calculate_order(12000, 4)
# calculate_subtotal(price, quantity)
# 호출 스택 위:
# calculate_subtotal에서 다시 실행되는 코드: subtotal = multiply(price, quantity)
# calculate_subtotal에서 완성되는 대입문:
# subtotal = multiply(price, quantity)
# subtotal에 저장되는 값: 48000
# 다음으로 실행되는 코드:
# print("calculate_subtotal 종료")


# 3. calculate_subtotal이 48000을 반환한 직후
# 호출 스택 아래:
# 프로그램 본문
# calculate_order(12000, 4)
# 호출 스택 위:

# calculate_order에서 완성되는 대입문: subtotal = calculate_subtotal(price, quantity)
# subtotal에 저장되는 값: 48000

# 다음으로 실행되는 코드:
# final_total = subtotal + 3000


# 4. calculate_order가 51000을 반환한 직후
# 호출 스택 아래:
# 프로그램 본문
# 호출 스택 위:
# 프로그램 본문에서 완성되는 대입문: result = calculate_order(12000, 4)
# result에 저장되는 값: 51000
# 다음으로 실행되는 코드: print("프로그램 종료")