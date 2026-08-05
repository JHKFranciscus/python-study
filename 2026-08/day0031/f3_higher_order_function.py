def double(number):
    print("double 함수 실행")
    return number * 2


def square(number):
    print("square 함수 실행")
    return number * number


def apply_operation(number, operation):
    print("apply_operation 함수 시작")
    result = operation(number)
    print("apply_operation 함수 종료")
    return result


first = apply_operation(5, double)
second = apply_operation(5, square)

print("first:", first)
print("second:", second)
#region
# 예상
# 1. apply_operation(5, double)에서 double은 함수 호출 결과인가, 함수 객체인가?
# 답: double()이 아니므로 함수 객체이다.
# 2. apply_operation 함수 안에서 operation에는 무엇이 저장되는가?
# 답: 함수 객체
# 3. result = operation(number)는 첫 번째 호출에서 어떤 코드와 같아지는가?
# 답: result = double(5)
# 4. first에 저장되는 값은 무엇인가?
# 답: 10
# 5. second에 저장되는 값은 무엇인가?
# 답: 25
# 6. 이 코드에서 고차 함수는 무엇인가?
# 답: apply_operation
# 7. 이 코드에서 콜백 함수는 무엇인가?
# 답: double, square
# 예상 출력 순서:
# apply_operation 함수 시작
# double 함수 실행
# apply_operation 함수 종료
# apply_operation 함수 시작
# square 함수 실행
# apply_operation 함수 종료
# first: 10
# second: 25
#endregion
print()
print("\n--- 함수 선택 실습 ---")

def select_operation(choice):
    if choice == "1":
        return double

    if choice == "2":
        return square

    return None

selected = select_operation("2")

if selected is not None:
    third = apply_operation(4, selected)
    print("선택된 함수:", selected.__name__)
    print("third:", third)
else:
    print("올바르지 않은 선택입니다.")
#region
# 실습 2 예상
# 1. select_operation("2")는 무엇을 반환하는가?
# 답: square함수 객체
# 2. selected에는 함수의 실행 결과가 저장되는가, 함수 객체가 저장되는가?
# 답: 함수 객체가 저장된다.
# 3. selected is not None의 결과는 무엇인가?
# 답:
#[수정]
#True
# 선택된 함수: square
# third: 16
# 4. apply_operation(4, selected)에서 operation에는 어떤 함수 객체가 저장되는가?
# 답: square 함수 객체
# 5. third에 저장되는 값은 무엇인가?
# 답: 16
# 6. selected.__name__의 값은 무엇인가?
# 답: square
# 7. select_operation도 고차 함수인가? 이유는?
# 답: 함수를 반환하는 함수이므로 고차함수이다.
# 예상 출력 순서:
##이전 단계 출력은 생략한다.
#
# \n--- 함수 선택 실습 ---
# apply_operation 함수 시작
# square 함수 실행
# apply_operation 함수 종료
# 선택된 함수: square
# third: 16
#endregion




















