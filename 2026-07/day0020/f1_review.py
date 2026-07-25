# main 모듈의 역할:
# 프로그램의 직접 실행
# service 모듈의 역할:
# 외부 메모리에 저장되어 있는 값을 받아오고, 외부 메모리에 값을 저장
# storage 모듈의 역할:
# 함수들을 이용하여 계산

# 메모 추가 시 함수가 호출되는 순서:
# import 모듈명, json.load, append, json.dump
# 사용자가 입력한 내용이 JSON 파일에 저장되는 과정:
# Python객체 ---직렬화---> Python 문자열(JSON형태) -> file.write()
# 함수 반환값을 이용해 저장 여부를 결정한 방법:
# 저장 성공시 return True를 쓰고, 실패시 return False를 쓴다.



# 1. JSON 파일 자체가 없다면:
# 예상 결과: FileNotFoundError
#실제 결과:
# open 과정에서 FileNotFoundError가 발생하지만 except가 처리했다.
# load_books 함수가 빈 리스트를 반환해 프로그램은 종료되지 않고 실행됐다.
# FileNotFoundError 처리 부분에는 print가 없어서 별도의 안내 문구는 나오지 않았다.
# 2. JSON 파일 안의 문법이 잘못됐다면:
# 예상 결과: json.JSONDecodeError
# 실제 결과:
# json.load 과정에서 json.JSONDecodeError가 발생했지만
# except json.JSONDecodeError가 처리했다.
# 안내 문구가 출력됐고 load_books 함수가 빈 리스트를 반환해 프로그램은 종료되지 않고 실행됐다.
# 3. 숫자를 입력해야 하는 메뉴에 문자를 입력하면:
# 예상 결과: ValueError
# 실제 결과:
# menu를 int로 변환하지 않고 문자열로 받기 때문에 ValueError가 발생하지 않았다.
# 어느 메뉴 조건에도 맞지 않아 "올바른 번호를 입력해주세요."가 출력됐고, 프로그램은 종료되지 않고 메뉴를 다시 출력했다.

