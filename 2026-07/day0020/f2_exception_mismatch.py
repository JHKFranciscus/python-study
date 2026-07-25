user_input = input("숫자를 입력하세요: ")

try:
    number = int(user_input)
    print("숫자 변환에 성공했습니다.")
    print(number * 2)

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

print("프로그램을 계속 실행합니다.")


# abc를 입력했을 때 예상:
# int 변환 과정에서 ValueError가 발생한다.
# 하지만 except에는 FileNotFoundError가 지정되어 있어
# ValueError를 처리하지 못할 것 같다.
# 마지막 print의 실행 여부에 대한 예상:
# 실행되지 않는다.
# 실제 결과:
# int 변환 과정에서 ValueError가 발생했다.
# except에는 FileNotFoundError만 지정되어 있어 발생한 ValueError를 처리하지 못했다.
# traceback이 출력되고 프로그램이 종료되어 마지막 print는 실행되지 않았다.