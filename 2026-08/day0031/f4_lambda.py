def apply_operation(number, operation):
    return operation(number)

def normal_double(number):
    print("normal_double 실행")
    return number * 2


lambda_double = lambda number: number * 2
add = lambda first, second: first + second

a = normal_double
b = lambda_double

print("a의 자료형:", type(a))
print("b의 자료형:", type(b))
print("a와 normal_double:", a is normal_double)
print("b 호출 결과:", b(5))
print("add 호출 결과:", add(3, 4))

result = apply_operation(6, lambda_double)
print("result:", result)
#region
# 예상
# 1. lambda_double에는 무엇이 저장되는가?
# 답: number를 매개변수로 가지고, number * 2를 본문으로 가지는 함수 객체
# 2. lambda_double을 만드는 줄에서 number * 2 계산이 바로 실행되는가?
# 답: lambda는 함수 객체를 만들 뿐 실행하지는 않는다.
# 3. type(a)의 결과는 무엇인가?
# 답: <class 'function'>
# 4. type(b)의 결과는 무엇인가?
# 답: <class 'function'>
# 5. a is normal_double의 결과는 무엇인가?
# 답: True
# 6. b(5)의 반환값은 무엇인가?
# 답: 10
# 7. add(3, 4)의 반환값은 무엇인가?
# 답: 7
# 8. apply_operation(6, lambda_double)에서 lambda_double은 함수 객체인가, 호출 결과인가?
# 답: lambda_double에는 함수 객체가 들어가 있다.
# 9. result에 저장되는 값은 무엇인가?
# 답: 12
# 예상 출력 순서:
# a의 자료형: <class 'function'>
# b의 자료형: <class 'function'>
# a와 normal_double: True
# b 호출 결과: 10
# add 호출 결과: 7
# result: 12
#endregion





