def issue_waiting_numbers():
    print("번호 발급을 시작합니다.")

    yield 101

    print("두 번째 번호를 준비합니다.")

    yield 102

    print("번호 발급을 종료합니다.")


waiting_number_generator = issue_waiting_numbers()

print(waiting_number_generator)
#region
# 예상 1:
# issue_waiting_numbers()를 호출하는 순간 "번호 발급을 시작합니다."가 출력되는가?
# 답: 호출하는 순간 제일 첫번째 문장부터 출력된다.
# 실제 출력:
# <generator object issue_waiting_numbers at 0x7d713f4b6200>
# [수정]
# yield가 있는 generator 함수는 호출하는 순간 함수 본문을 실행하지 않고, generator 객체만 만들어서 반환한다.

# 예상 2:
# waiting_number_generator를 출력하면 101과 102가 바로 출력되는가?
# 답: yield가 뭔지 모르는데 내가 어떻게 아는가?
# 실제 출력:
# 출력되지 않는다.
#endregion
print()

first_number = next(waiting_number_generator)

print("받은 번호:", first_number)
#region
# next(waiting_number_generator)를 처음 호출하면 어떤 문장과 값이 어떤 순서로 출력되는가?
# 예상 출력:
# 번호 발급을 시작합니다.
# 받은 번호: 101
# 실제 출력
# 번호 발급을 시작합니다.
# 받은 번호: 101
#endregion
print()

second_number = next(waiting_number_generator)

print("받은 번호:", second_number)
#region
# 두 번째 next()를 호출하면 어떤 문장과 값이 어떤 순서로 출력되는가?
# 예상 출력:
# 두 번째 번호를 준비합니다.
# 102
# 실제 출력:
# 두 번째 번호를 준비합니다.
# 102
#endregion
print()

# third_number = next(waiting_number_generator)

# print("받은 번호:", third_number)
#region
# 세 번째 next()를 호출하면 어떤 문장이 출력되고 어떤 결과가 발생하는가?
# 예상:
# 번호 발급을 종료합니다.
# 받은 번호: None
# 실제:
# 번호 발급을 종료합니다
# StopIteration가 뜬다
# 1. "번호 발급을 종료합니다."가 출력되는가?
# 그렇다
# 2. third_number에 저장될 값이 존재하는가?
# 존재하지 않는다.
# 3. 함수 본문이 끝나면 정상 반환되는가, StopIteration이 발생하는가?
# return None이 컴파일 과정에서 자동으로 들어가져 정상 반환 될 것이다.
#[수정]
#generator가 더 이상 yield할 값 없이 종료되면 next()는 정상적인 값 대신 StopIteration을 발생시킨다.
# 4. "받은 번호:" 출력문까지 실행되는가?
#[수정]
#next()에서 StopIteration이 발생해 실행이 중단되므로 그 아래 print()까지 도달하지 않는다.
# 될 것이다.
#endregion
print()

safe_number_generator = issue_waiting_numbers()

while True:
    try:
        number = next(safe_number_generator)
        print("발급된 번호:", number)

    except StopIteration:
        print("모든 번호 발급이 끝났습니다.")
        break
#region
# 예상 결과:
# 번호 발급을 시작합니다.
# 발급된 번호: 101
# 두 번째 번호를 준비합니다.
# 발급된 번호: 102
# 번호 발급을 종료합니다.
# 모든 번호 발급이 끝났습니다.
# 실제 결과:
# 번호 발급을 시작합니다.
# 발급된 번호: 101
# 두 번째 번호를 준비합니다.
# 발급된 번호: 102
# 번호 발급을 종료합니다.
# 모든 번호 발급이 끝났습니다.

# 문제 1:
# 첫 번째 yield에서 실행이 멈췄을 때 generator는 함수의 어느 위치를 기억하는가?
# 답: "두 번째 번호를 준비합니다."의 시작 위치를 기억한다.
#[보완]
# next()는 iterator의 __next__()를 호출한다.
# 일반 iterator는 __next__() 안에서 다음 값과 내부 위치를 관리한다.
# generator는 next()가 호출되면 정지된 실행을 재개하고, 다음 yield까지 실행한 뒤 값을 전달하고 다시 정지한다.

# 문제 2:
# 일반 함수의 return과 generator의 yield는 실행을 끝내는 방식에서 어떤 차이가 있는가?
# 답: return은 값을 호출에 반환하여 실행을 끝내지만, yield는 실행을 멈출 뿐 끝내지는 않는다.

# 문제 3:
# 위 while문에서 StopIteration을 처리하지 않으면 마지막에 어떤 일이 발생하는가?
# 답: "번호 발급을 종료합니다."출력 이후에 StopIteration 오류가 뜨며 프로그램이 종료된다.
#endregion
