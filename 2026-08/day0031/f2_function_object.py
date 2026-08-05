def greet():
    return "안녕하세요"

#코드 실행 시 greet라는 이름에 함수 객체가 연결된다.
#()가 없으면 함수를 실행하는 것이 아니라 함수 객체 자체를 가리킨다.
#()가 있으면 함수를 실행하고 반환값을 얻는다.

def add_one(number):
    print("add_one 함수 실행")
    return number + 1


a = add_one
b = add_one(10)

print("a:", a)
print("a의 자료형:", type(a))
print("b:", b)
print("같은 함수 객체인가:", a is add_one)
print("a 호출 결과:", a(20))

# 예상
# 1. "add_one 함수 실행"은 전체 실행 중 몇 번 출력되는가?
## 답: b = add_one(10), print("b:", b), print("a 호출 결과:", a(20))에서 3번
#[수정]
#b = add_one(10), print("a 호출 결과:", a(20))에서 2번
# 2. 처음으로 "add_one 함수 실행"이 출력되는 시점은 어느 줄인가?
# 답: b = add_one(10)
# 3. a에는 무엇이 저장되어 있는가?
# 답: add_one이라는 이름을 가진 함수 객체 그 자체
# 4. b에는 무엇이 저장되어 있는가?
## 답: add_one 함수의 반환값
#[보완]
#b에는 add_one(10)의 반환값인 정수 11이 저장된다.
# 5. type(a)의 결과는 무엇인가?
# 답: <class_'function'>
# 6. a is add_one의 결과는 무엇인가?
# 답: True
# 7. a(20)의 반환값은 무엇인가?
# 답: 21
# 예상 출력 순서:
# add_one 함수 실행
# a: <function add_one ...>
## a의 자료형: <class_'function'>
#[수정]
#a의 자료형: <class 'function'>
## add_one 함수 실행
## b: 12
#[수정]
#b: 11
# 같은 함수 객체인가: True
# add_one 함수 실행
# a 호출 결과: 21