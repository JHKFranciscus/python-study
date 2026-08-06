message = "전역 영역"


def first():
    first_value = "first 지역 변수"
    print("first 시작")

    second(first_value)

    print("first 종료")


def second(received_value):
    second_value = "second 지역 변수"
    print("second 시작")
    print(received_value)
    print(second_value)
    print(message)
    print("second 종료")


print("프로그램 시작")
first()
print("프로그램 종료")

# 예상 결과:
# 프로그램 시작
# first 시작
# second 시작
# first 지역 변수
# second 지역 변수
# 전역 영역
# second 종료
# first 종료
# 프로그램 종료

# 판단 질문
# 1. 프로그램 시작 직후 호출 스택에서 실행 중인 영역:
# 프로그램 본문
# 2. first()가 호출되면 호출 스택에 새로 쌓이는 함수:
# first()
# 3. first() 실행 중 second()가 호출되면 호출 스택의 아래쪽부터 위쪽까지 순서:
# 호출 스택 위쪽
# 프로그램 본문
# first()
# second()
# 호출 스택 아래쪽
#[수정]
# 프로그램 본문, first(), second()
# 먼저 실행된 순서부터 호출 스택의 아래쪽부터 쌓인다.
# 4. second()와 first() 중 어느 함수가 먼저 종료되는가?
# second()
# 5. second()에서 first_value라는 이름을 직접 사용하는가, 아니면 전달받은 매개변수 received_value를 사용하는가?
# 전달받은 매개변수 received_value에 저장되어 있는 값을 사용한다.
# 6. second()가 first()의 지역 변수 이름을 LEGB 탐색으로 직접 찾을 수 있는가?
# 찾을 수 없다.
# 7. second()에서 message를 사용할 수 있는 이유:
# 파이썬은 함수 안에서 어떤 변수 이름을 만나면 가까운 범위부터 바깥으로 찾아가기 때문이다.
#[보완]
#second()의 Local 영역에는 message가 없으므로 LEGB 순서에 따라 Global 영역에서 정의된 message를 찾아 사용한다.
# 8. first()가 종료된 뒤 first_value를 파일 바깥에서 사용할 수 있는가?
# 파이썬은 함수 안에서 어떤 변수 이름을 만나면 가까운 범위부터 바깥으로 찾아나가는 것이지 바깥에서 안으로 찾아들어가는 것은 아니므로 되지 않는다.

# 실제 결과:
# 프로그램 시작
# first 시작
# second 시작
# first 지역 변수
# second 지역 변수
# 전역 영역
# second 종료
# first 종료
# 프로그램 종료

# 예상 결과와 실제 결과의 차이:
# 차이 없음