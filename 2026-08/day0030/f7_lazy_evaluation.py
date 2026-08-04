def create_square(number):
    print(f"{number}의 제곱을 계산합니다.")
    return number ** 2


print("=== 리스트 생성 시작 ===")

eager_values = [
    create_square(number)
    for number in range(1, 4)
]

print("=== 리스트 생성 완료 ===")
print(eager_values)


print()
print("=== generator 생성 시작 ===")

lazy_values = (
    create_square(number)
    for number in range(1, 4)
)

print("=== generator 생성 완료 ===")
print(lazy_values)
#region
# 문제 1:
# eager_values를 만드는 순간 create_square()는 몇 번 실행되는가?
# 답: 3번

# 문제 2:
# lazy_values를 만드는 순간 create_square()는 몇 번 실행되는가?
# 답: 1번
#[수정]
#실제 결과: lazy_values를 만드는 순간 create_square()는 0번 실행되었다.
# generator 표현식을 만드는 것만으로는 내부 계산을 실행하지 않는다.
# next()나 for문이 값을 요청할 때 create_square()가 실행된다.

# 문제 3:
# print(eager_values)는 실제 숫자들이 담긴 리스트를 출력하는가?
# 답: 그러하다

# 문제 4:
# print(lazy_values)는 1, 4, 9를 바로 출력하는가?
# 답: 아니다 값을 1번 집어 넣을 때 마다 멈춘다.
#[보완]
#print(lazy_values)는 값을 요청하는 동작이 아니므로 1, 4, 9를 계산하거나 출력하지 않는다. generator 객체 정보만 출력한다.

# 예상 실행 결과:
# === 리스트 생성 시작 ===
# 1의 제곱을 계산합니다.
# === 리스트 생성 완료 ===
# [1, 4, 9]
# === generator 생성 시작 ===
# 1의 제곱을 계산합니다.
# 2의 제곱을 계산합니다.
# 3의 제곱을 계산합니다.
# === generator 생성 완료 ===
# (1, 4, 9)
# 실제 결과:
# === 리스트 생성 시작 ===
# 1의 제곱을 계산합니다.
# 2의 제곱을 계산합니다.
# 3의 제곱을 계산합니다.
# === 리스트 생성 완료 ===
# [1, 4, 9]

# === generator 생성 시작 ===
# === generator 생성 완료 ===
# <generator object <genexpr> at 0x7567a0d38580>
#endregion
print()
print("=== 첫 번째 값 요청 시작 ===")
#region
# 예상:
# 아래 next()를 실행하면 create_square()는 몇 번 실행되며, 어떤 값이 first_value에 저장되는가?
# 답: 1번 실행되며, 1이 저장된다.
#endregion
first_value = next(lazy_values)

print("첫 번째 값:", first_value)
print("=== 첫 번째 값 요청 완료 ===")

print()
print("=== 두 번째 값 요청 시작 ===")
#region
# 예상:
# 처음부터 1을 다시 계산하는가? 아니면 다음 숫자를 계산하는가?
# 답: generator이므로 다음 숫자를 계산한다.
#endregion
second_value = next(lazy_values)

print("두 번째 값:", second_value)
print("=== 두 번째 값 요청 완료 ===")

print()
print("=== 남은 값 for문 처리 시작 ===")
#region
# 예상:
# 앞에서 1과 2를 next()로 이미 꺼냈다.
# 같은 lazy_values를 for문으로 순회하면 어떤 계산과 출력이 발생하는가?
# 답: 3부터 꺼내게 되어 9라는 계산이 발생하고 "남은 값: 9"와 "=== 남은 값 for문 처리 완료 ==="를 출력한다.
# 실제 출력:
# === 남은 값 for문 처리 시작 ===
# 3의 제곱을 계산합니다.
# 남은 값: 9
# === 남은 값 for문 처리 완료 ===
#[보완]
# [보완]
# 남아 있는 입력값 3에 대해 create_square(3)이 실행되고, 계산 결과인 9가 for문에 전달된다.
#endregion
for value in lazy_values:
    print("남은 값:", value)

print("=== 남은 값 for문 처리 완료 ===")

#4단계: 리스트와 generator의 메모리 차이
import sys

print()
print("=== 큰 데이터 생성 ===")

large_eager_values = [
    number ** 2
    for number in range(1, 100001)
]

large_lazy_values = (
    number ** 2
    for number in range(1, 100001)
)

print(
    "리스트 객체 크기:",
    sys.getsizeof(large_eager_values),
    "bytes",
)

print(
    "generator 객체 크기:",
    sys.getsizeof(large_lazy_values),
    "bytes",
)
#region
# 문제 1:
# large_eager_values를 생성할 때 제곱 결과 100,000개를 즉시 계산하는가?
# 답: 그러하다

# 문제 2:
# large_lazy_values를 생성할 때 제곱 결과 100,000개를 즉시 계산하는가?
# 답: large_lazy_values를 생성할 때는 그냥 generator만 생성이 될 뿐 계산이 진행되지는 않는다.

# 문제 3:
# 리스트 객체와 generator 객체 중 어느 쪽의 sys.getsizeof() 결과가 더 클 것으로 예상하는가?
# 답: 리스트 객체

# 문제 4:
# generator가 메모리를 적게 사용할 수 있는 이유는 무엇인가?
# 답: next나 for문을 실행시켜야지만 메모리상에서 하나씩 실행하기 때문이다.
# [보완]
# generator는 모든 결과를 미리 계산하여 저장하지 않고, next()나 for문이 값을 요청할 때 필요한 값만 하나씩 계산하여 전달한다.
# 따라서 앞으로 생성할 결과 전체를 메모리에 저장할 필요가 없다.
#endregion