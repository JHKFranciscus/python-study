# f1_book_storage.py의 load_books 실행 순서

## 1. 다음 코드의 역할: 
## with open(FILE_NAME, "r", encoding="utf-8") as file:
## 답:
## FILE_NAME에 해당하는 파일을 읽기 모드("r")와 UTF-8 인코딩으로 연다.
## 열린 파일의 객체를 만들고 그 객체를 file이라는 변수로 가리킨다.
## with 블록이 끝나면 파일은 자동으로 닫힌다.

## 2. 파일이 존재하지 않을 경우 예외가 발생하는 위치:
## 답: FileNotFoundError
##[수정 후]
## with open(FILE_NAME, "r", encoding="utf-8") as file:
## 위 코드에서 존재하지 않는 파일을 열려고 할 때 발생한다.

## 3. 다음 코드의 역할:
## books = json.load(file)
## 답: json형식으로 적혀있는 file을 파이썬 문자열(JSON형식)로 읽어 온 후 역직렬화를 하여 Python 문자열 객체를 만든다.
##[수정 후]
#3 file의 JSON 형식 문자열을 읽고 역직렬화하여 JSON 구조에 대응하는 Python 객체로 변환한다.

## 4. 파일은 존재하지만 JSON 문법이 잘못된 경우 예외가 발생하는 위치: 
## 답: json.JSONCodeError
##[수정 후]
# books = json.load(file)
# 파일은 열렸지만 파일 내용이 올바른 JSON 문법이 아닐 때
# 위 코드의 JSON 해석 과정에서 발생한다.

## 5. FileNotFoundError가 처리된 뒤 load_books의 반환값:
## 답: []

## 6. json.JSONDecodeError가 처리된 뒤 load_books의 반환값:
## 답: []

## 7. 두 예외가 모두 처리된 뒤 main 모듈이 계속 실행될 수 있는 이유:
## 답: try-except를 이용하여 try 내부의 코드가 작동 중 오류가 발생하면 try의 남은 내부 코드는 실행되지 않고 except를 실행하여 except 내부의 코드를 실행하기 때문이다.
##[수정 후]
# 7. 두 예외 중 하나가 발생해 해당 except에서 처리된 뒤 main 모듈이 계속 실행될 수 있는 이유:
# 답:
# 두 예외 중 하나가 발생하면 load_books 내부의 해당 except가 실행된다.
# 해당 except에서 빈 리스트 []를 반환하므로 main의 books 변수에 빈 리스트가 저장되고, 프로그램은 종료되지 않은 채 다음 메뉴 코드를 계속 실행한다.

# 예외 전파:
# 함수에서 발생한 예외를 그 함수 내부에서 처리하지 못하면, 해당 함수를 호출한 쪽으로 예외가 올라가는 것이다.
# 호출한 쪽에서도 처리하지 않으면 더 바깥 호출로 계속 올라가며, 끝까지 처리되지 않으면 traceback이 출력되고 프로그램이 종료된다.