# 문제 1
#region
# 다음 코드에서 각각의 변수에 들어가는 객체의 종류를 적어라.

numbers = [10, 20, 30]

a = numbers
b = iter(numbers)
c = (number * 2 for number in numbers)

# a: iterable이다.
# b: iterator이다.
# c: generator이다.
#[수정]
# a:
# - iterable인가: O
# - iterator인가: X
# - generator인가: X

# b:
# - iterable인가: O
# - iterator인가: O
# - generator인가: X

# c:
# - iterable인가: O
# - iterator인가: O
# - generator인가: O

# 1. next(a)를 바로 호출할 수 있는가? 이유는?
# iterable은 next를 사용할 수 없다.
#[보완]
#iterable이지만 iterator가 아니므로 next()로 직접 값을 꺼낼 수 없다.
# 2. next(b)를 두 번 호출하면 각각 무엇이 나오는가?
# 처음 호출에 b에 바인딩 된 generator 객체가 생성되고, 두 번째 호출에 10이 출력된다.
#[수정]
#b = iter(numbers)가 실행될 때 이미 list iterator 객체가 생성되어 b에 저장된다.
#10, 20 이다.
# 3. next(c)를 한 번 호출하면 무엇이 나오는가?
# c에 바인딩 된 gnerator 객체가 생성이된다.
#[수정]
#c = (number * 2 for number in numbers)가 실행될 때 이미 generator 객체가 생성된다.
#20이다.
# 4. b와 c의 값이 모두 소진된 뒤 next()를 호출하면 어떤 일이 발생하는가?
# 처리되지 않은 StopIteration이 발생하여 프로그램이 오류 메세지와 함께 종료된다.
#endregion

# 실제 실행 확인
try:
    print("next(a):", next(a))
except TypeError as error:
    print("next(a) 오류:", type(error).__name__)

print("next(b) 1회:", next(b))
print("next(b) 2회:", next(b))

print("next(c) 1회:", next(c))

# 남은 값까지 꺼내서 소진시키기
print("next(b) 3회:", next(b))
print("next(c) 2회:", next(c))
print("next(c) 3회:", next(c))

try:
    next(b)
except StopIteration:
    print("b: StopIteration 발생")

try:
    next(c)
except StopIteration:
    print("c: StopIteration 발생")
