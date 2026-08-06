title = "파이썬 학습"


def outer():
    category = "함수 심화"

    def inner():
        student = "홍길동"

        print(student)
        print(category)
        print(title)
        print(len([10, 20, 30]))

    inner()


outer()

# 실행 전 예상 결과:
# 홍길동
# 함수 심화
# 파이썬 학습
# 3

# 이름이 정의된 영역:
# student: 현재 실행 중인 inner() 안에서 정의됐으므로 Local이다.
# category: inner() 바깥을 감싸는 outer()에 있으므로 inner()를 기준으로 Enclosing이다.
# title: 모든 함수 바깥에 있으므로 Global이다.
# len: 코드에서 직접 정의하지 않았지만 파이썬이 기본으로 제공하므로 Built-in이다.

value = 100


def check_outer():
    value = 200

    def check_inner():
        value = 300
        print("inner:", value)

    check_inner()
    print("outer:", value)


check_outer()
print("global:", value)

# 두 번째 코드 예상 결과:
# inner: 300
# outer: 200
# global: 100

# 판단 질문
# 1. check_inner()의 print가 사용하는 value는 어느 영역의 변수인가?
# Local영역의 변수이다.
# 2. check_inner()가 끝난 뒤 check_outer()의 value가 300이 되는가? 예상과 이유:
# 파이썬은 함수 안에서 어떤 변수 이름을 만나면 가장 가까운 범위부터 바깥쪽으로 찾아가기 때문에 300으로 바뀌지 않는다.
# 3. check_outer()가 끝난 뒤 전역 value가 200이 되는가? 예상과 이유:
# 파이썬은 함수 안에서 어떤 변수 이름을 만나면 가장 가까운 범위부터 바깥쪽으로 찾아가기 때문에 200으로 바뀌지 않는다.
# 4. 세 value는 이름만 같은 하나의 변수인가, 아니면 서로 다른 영역에 만들어진 별개의 변수인가?
# 세 value는 이름만 같은 서로 다른 영역에 만들어진 별개의 변수이다.
# 실제 결과:
# 홍길동
# 함수 심화
# 파이썬 학습
# 3
# inner: 300
# outer: 200
# global: 100

# 예상 결과와 실제 결과의 차이:
# 차이 없음
