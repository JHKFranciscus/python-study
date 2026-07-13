def calcualte_total(numbers):
    total = 0
    for t_number in numbers:
        total += t_number
    return total

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if largest < number:
            largest = number
    return largest

def count_even(numbers):
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    return even_count

def print_analysis(numbers):
    total = calcualte_total(numbers)
    find_largest(numbers)
    print(f"숫자 목록: {numbers}")
    print(f"합계: {total}")
    print(f"최대값: {find_largest(numbers)}")
    print(f"짝수 개수: {count_even(numbers)}")
# 변수에 대입해서 호출해도 된다.
# 호출하고 다시 print에 호출을 넣어도 된다.(이거는 의미 없어서 빼야하나 실행이 가능하다는 것을 보여주기 위해 남겨둔다.)
# print에 바로 호출해도 된다.
# count_even = count_even(numbers)를 쓰면 안 된다.

numbers = [12, 5, 27, 8, 19]

print_analysis(numbers)


# 1. 프로그램이 처음 시작할 때 가장 먼저 실행되는 줄:
# numbers = [12, 5, 27, 8, 19]인줄 알았으나
# def calculate_total(numbers): 이다
# 2. print_analysis(numbers)를 호출하면 들어가는 함수:
# def print_analysis(numbers):
# 3. print_analysis 안에서 호출되는 함수들의 순서
# calcualte_total(numbers)
# -> find_larges(numbers)
# -> find_larges(numbers)
# -> count_even(numbers)
# 4. return으로 돌려받은 값이 어디에서 사용되는지
# 함수호출에 반환하여 삽입된다.
# 5. 함수 정의만 했을 때는 왜 실행되지 않는지
# def문을 만나면 함수가 만들어질 뿐이고, 함수 본문은 함수 이름 뒤에 ()를 붙여 호출해야 실행되기 때문이다.