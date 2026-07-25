# 현재 add_book의 가격 입력 처리 방식

# 1. abc를 입력했을 때 int 변환까지 도달하는가?
# 예상: 도달하지 못한다.

# 2. -100을 입력했을 때 int 변환까지 도달하는가?
# 예상: 도달하지 못한다.

# 3. 8000을 입력했을 때 int 변환까지 도달하는가?
# 예상: 도달한다

# 4. 현재 코드는 ValueError를 except로 처리하는 방식인가,
#    ValueError가 발생하기 전에 입력을 검사하는 방식인가?
# 답: ValueError가 발생하기 전에 입력을 검사한다

# 5. 현재 add_book의 int 변환에서 처리되지 않은 ValueError가
#    실제로 발생한다면 어디로 전파되는가?
# 답: f1_book_manager_main.py에 있는 함수호출로 전파된다.
#[수정 후]
# add_book 내부에서 처리되지 않은 ValueError는 add_book을 호출한 main 모듈의 호출 지점으로 전파된다.
# main에서도 처리하지 않으면 traceback이 출력되고 프로그램이 종료된다.

# 실제 결과:
# abc는 isdigit() 결과가 False여서 int 변환에 도달하지 않았다.
# -100도 '-' 문자가 포함되어 isdigit() 결과가 False였고 int 변환에 도달하지 않았다.
# 8000은 isdigit() 결과가 True여서 int 변환에 도달했고, 정수 8000으로 변환되어 도서가 정상적으로 추가됐다.
# 현재 코드는 ValueError가 발생한 후 처리하는 방식이 아니라, int 변환 전에 입력 문자열을 검사하여 ValueError 발생을 막는 방식이다.