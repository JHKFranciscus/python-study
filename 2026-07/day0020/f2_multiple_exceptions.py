first_input = input("첫 번째 숫자: ")
second_input = input("두 번째 숫자: ")

try:
    first_number = int(first_input)
    second_number = int(second_input)

    result = first_number / second_number
    print("계산 결과:", result)

except ValueError:
    print("숫자로 변환할 수 없는 값이 있습니다.")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

print("프로그램을 계속 실행합니다.")

# 10과 2를 입력하면:
# 예상: 5.0
# abc와 2를 입력하면:
# 예상: ValueError
# 10과 0을 입력하면:
# 예상: ZeroDivisionError

# 실제 결과:
# 10과 2를 입력하면 예외가 발생하지 않아 계산 결과 5.0이 출력됐다.
# 두 except는 실행되지 않았고 마지막 print가 실행됐다.

# abc와 2를 입력하면 첫 번째 int 변환에서 ValueError가 발생했다.
# try 내부의 남은 코드는 건너뛰고 except ValueError가 실행됐다.
# 예외 처리 후 마지막 print도 실행됐다.

# 10과 0을 입력하면 두 int 변환은 성공했지만
# 나눗셈 과정에서 ZeroDivisionError가 발생했다.
# except ZeroDivisionError가 실행된 뒤 마지막 print도 실행됐다.