def first():
    print("first 시작")
    second()
    print("first 종료")

def second():
    print("second 실행")

print("프로그램 시작")
first()
print("프로그램 종료")

# #예상 출력 순서
# 프로그램 시작
# first 시작
# second 실행
# first 종료
# 프로그램 종료

# #실제 실행 결과
# 프로그램 시작
# first 시작
# second 실행
# fist 종료
# 프로그램 종료

# #실행 순서 설명
# def first(): 실행
# def second(): 실행
# print("프로그램 시작")로 인해 프로그램 시작이 출력된다.
# first()로 함수호출을 한다.
# 함수 def first()가 실행된다.
# print("first 시작")로 인해 first 시작이 출력된다.
# second()로 함수호출을 한다.
# 함수 def second()가 실행된다.
# print("second 실행")로 인해 second 실행이 출력된다.
# def second()가 return None으로 종료된다.
# print("first 종료")로 인해 first 종료가 출력된다.
# def first()가 return None으로 종료된다.
# print("프로그램 종료")로 인해 프로그램 종료가 출력된다.
