# 1. return과 예외 전파의 차이:
# 답: return은 함수를 종료하고 그 값을 함수호출에 반환하지만, 예외 전파는 함수를 종료하지 않고, 예외가 나왔을 때 그 예외를 처리할 except를 구하지 못해 직접 실행하는 파일의 함수호출로 타고 올라가다가 마지막까지 처리하지 못하면 traceback을 발생시킨다.
# [수정 후]
# return은 함수를 정상적으로 종료하고 반환값을 함수 호출 결과로 전달한다.
# 예외 전파는 함수에서 발생한 예외를 내부에서 처리하지 못해 함수의 정상 실행이 중단되고, 예외가 호출한 쪽의 더 바깥 예외 처리 범위로 넘어가는 것이다.
# 끝까지 처리되지 않으면 traceback이 출력되고 프로그램이 종료된다.

# 2. 같은 try에 연결된 except가 예외를 처리하는 것과 예외 전파의 차이:
# 답: try에 있는 코드에서 예외가 발생하면 그 아래 코드는 실행이 중단되고, 예외에 맞는 except를 찾아 그 안의 코드를 실행한다. 하지만 예외 전파는 예외에 맞는 except를 찾지 못해 직접 실행하는 파일의 함수호출로 올라가고, 그 곳에서도 예외를 처리하지 못하면, 더 높은 호출로 타고 올라가는데 마지막까지 처리하지 못하면 traceback을 발생시킨다.

# 3. load_books가 오류 상황에서 None이 아니라 빈 리스트 []를 반환하는 이유:
# 답: 오류가 FileNotFindError나 json.JSONDecodeError인데 try-except를 통해 오류 상황이 발생하면 return[]가 되도록 했기 때문이다. 
# [수정 후]
# load_books를 호출한 쪽은 반환값을 도서 목록인 list로 사용한다.
# 따라서 오류가 발생해도 같은 자료형인 빈 리스트 []를 반환해야 len(), 반복문, 도서 추가 등의 리스트 연산을 계속 사용할 수 있다.
# None을 반환하면 이후 리스트 연산에서 TypeError가 발생할 수 있다.

# 4. FileNotFoundError와 json.JSONDecodeError가 발생하는 코드 위치의 차이:
# 답: FileNotFoundError은 with open(FILE_NAME, "r", encoding="utf-8") as file:에서 발생하고, json.JSONDecodeError은 books = json.load(file)에서 발생한다.

# 5. add_book에서 try의 범위를 price = int(input_price)만 포함하도록 좁힌 이유:
# 답: 오류 범위를 값으로 한정하기 위해서
# [수정 후]
# 실제로 ValueError가 발생할 가능성이 있는 코드는 price = int(input_price)이므로 그 줄만 try에 포함했다.
# try 범위를 넓히면 다른 코드에서 발생한 ValueError까지 가격 변환 오류로 잘못 처리할 수 있다.
# 범위를 좁히면 예외 발생 위치와 처리 목적도 명확해진다.

# 6. main에서 직접 조회 코드를 작성하지 않고 service.show_books()를 호출하도록 바꾼 이유:
# 답: 역할이 중복되는 것을 막고, 역할분담을 확실히 하기 위해서