user_input = input("숫자를 입력하세요: ")

try:
    number = int(user_input)
    print("숫자 변환에 성공했습니다.")
    print(number * 2)

except ValueError:
    print("숫자로 변환할 수 없는 값입니다.")

print("프로그램을 계속 실행합니다.")

# 25를 입력했을 떄:
# int 변환이 성공해 try 내부의 나머지 코드가 실행됐다.
# ValueError가 발생하지 않아 except는 실행되지 않았다.
# try-except 다음의 마지막 print도 실행됐다.

# abc를 입력했을 떄:
# int 변환 과정에서 ValueError가 발생했다.
# try 내부의 남은 코드는 실행되지 않고 except로 이동했다.
# except가 예외를 처리한 뒤 마지막 print가 실행됐다.