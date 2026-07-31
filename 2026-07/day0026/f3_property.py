# region 1단계와 2단계: getter만 있는 클래스
class ReadOnlyProduct:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price


read_only_product = ReadOnlyProduct("키보드", 50000)

try:
    read_only_product.price = 60000
except AttributeError as error:
    print(error)

print("대입 시도 후 가격:", read_only_product.price)
print()
# endregion

# region 3단계: getter와 setter가 있는 클래스
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self._price = price

#     @property
#     def price(self):
#         return self._price
    
#     @price.setter
#     def price(self, new_price):
#         self._price = new_price


# product = Product("키보드", 50000)

#region
# print("=== 내부 속성 직접 조회 ===")
# print(product._price)

# print("=== getter를 통한 조회 ===")
# print(product.price)
# @property가 붙은 getter를 실행한다.
# getter가 self._price를 반환한다.
#endregion
#region
# 예상 결과:
# === 내부 속성 직접 조회 ===
# 50000
# === getter를 통한 조회 ===
# 50000
# 실제 결과:
# === 내부 속성 직접 조회 ===
# 50000
# === getter를 통한 조회 ===
# 50000
# 문제 1
# product.price를 출력할 때 실제로 실행되는 메서드는 무엇인가?
# price()
# [수정]
# @property가 붙은 price getter 메서드가 실행된다.
# 문제 2
# _price와 price는 각각 어떤 역할을 하는가?
# _price: 실제 객체의 속성
# [수정]
# 실제 가격 값을 저장하는 내부 속성
# price: 실제 객체의 속성에 값을 전달하는 역할
# [수정]
# 외부 코드가 가격을 조회할 때 사용하는 접근 이름이며, 접근하면 getter가 실행되어 _price의 값을 반환한다.
#endregion
#region
# print("=== price에 새 값 대입 시도 ===")
# product.price = 60000
# print(product.price)

# 예상 결과:
# price에는 getter만 있고 setter가 없으므로 product.price = 60000에서 AttributeError가 발생할 것으로 예상한다.
# 실제 결과:
# === 내부 속성 직접 조회 ===
# 50000
# === getter를 통한 조회 ===
# 50000
# === price에 새 값 대입 시도 ===
# Traceback (most recent call last):
#   File "/home/jhk-franciscus/projects/python-study/2026-07/day0026/f3_property.py", line 47, in <module>
#     product.price = 60000
#     ^^^^^^^^^^^^^
# AttributeError: property 'price' of 'Product' object has no setter
#endregion
#region
# print("=== price에 새 값 대입 시도 ===")
# try:
#     product.price = 60000
# except AttributeError as error:
#     print(error)

# print("대입 시도 후 가격:", product.price)

# 예상 결과:
# setter가 없으므로 AttributeError가 발생한다.
# except가 오류를 처리한 뒤 기존 가격 50000이 출력된다.
# 실제 결과:
# === 내부 속성 직접 조회 ===
# 50000
# === getter를 통한 조회 ===
# 50000
# === price에 새 값 대입 시도 ===
# property 'price' of 'Product' object has no setter
# 대입 시도 후 가격: 50000
# 문제 1
# product.price로는 값을 읽을 수 있는데
# product.price = 60000으로는 변경할 수 없는 이유는 무엇인가?
# setter가 없어서 외부 코드로 내부 속성에 접근할 수 있는 방법이 없다.
#[수정 후]
#price에는 getter만 정의되어 있고 setter는 정의되어 있지 않다.
#따라서 product.price로 값은 읽을 수 있지만, product.price = 60000으로 값을 변경하는 경로는 존재하지 않아 AttributeError가 발생한다.
# 문제 2
# 대입이 실패한 뒤에도 기존 가격 50000이 유지되는 이유는 무엇인가?
# 내부 속성에 저장 되어 있는 값은 self._price로 저장되어 있으므로 대입에 실패해도 기존 가격이 유지된다.
# 문제 3
# 현재 상태에서 다음 코드는 실행 가능한가?

# product._price = 60000

# 실행 가능 여부와 그 이유를 작성한다.
# 실행 가능하다. _price는 객체의 실제 내부 속성을 가리키는 것이라서 내부 속성에 직접적으로 접근이 가능하다.
#endregion
#region
# print("=== setter 추가 후 가격 변경 ===")

# product.price = 60000

# print("변경 후 가격:", product.price)
# print("내부 저장 값:", product._price)

# 예상 결과:
# setter가 실행되어 _price에 60000이 저장된다.
# product.price와 product._price 모두 60000이 출력된다.
#
# 실제 결과:
# === setter 추가 후 가격 변경 ===
# 변경 후 가격: 60000
# 내부 저장 값: 60000

# 문제 1
# product.price = 60000에서 60000은 setter의 어떤 매개변수로 전달되는가?
# 답: new_price

# 문제 2
# setter가 실제 값을 저장하는 속성은 price인가, _price인가?
# 답: _price
# 문제 3
# product.price를 출력할 때 setter가 아니라 getter가 실행되는 이유는 무엇인가?
# 답: product.price는 내부에 저장된 실제 값을 불러오는 것이기 때문이다.
# [보완]
# product.price를 대입문 왼쪽이 아니라 값으로 사용했기 때문에 getter가 실행된다.
# getter는 내부 속성 _price에 저장된 값을 반환한다.
# 문제 4
# 현재 setter에는 검증이 없다.
# product.price = "육만원"을 실행하면 어떻게 될 것으로 예상하는가?
# 답: _price에 저장되는 값이 문자열 "육만원"으로 변경된다.
#endregion
#endregion

# region 4단계: 검증 기능이 있는 getter와 setter
class ValidatedProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if type(new_price) is not int:
            raise ValueError("가격은 정수여야 합니다.")

        if new_price < 0:
            raise ValueError("가격은 0 이상이어야 합니다.")

        self._price = new_price


validated_product = ValidatedProduct("키보드", 50000)

# #region
# print("=== 정상 가격 ===")
# print("생성 직후:", validated_product.price)

# validated_product.price = 60000

# print("변경 후:", validated_product.price)
# 예상 결과:
# 생성할 때 50000이 정상적으로 저장된다.
# 가격 변경 후에는 60000이 출력된다.
# 실제 결과:
# === 정상 가격 ===
# 생성 직후: 50000
# 변경 후: 60000

#region
# print("=== 문자열 가격 변경 시도 ===")

# try:
#     validated_product.price = "육만원"
# except ValueError as error:
#     print(error)

# print("문자열 변경 시도 후 가격:", validated_product.price)
# 예상 결과:
# "가격은 정수여야 합니다."가 출력된다.
# 문자열은 저장되지 않고 기존 가격 60000이 유지된다.
# 실제 결과:
# === 문자열 가격 변경 시도 ===
# 가격은 정수여야 합니다.
# 문자열 변경 시도 후 가격: 60000
#endregion
#region
# print("=== 음수 가격 변경 시도 ===")

# try:
#     validated_product.price = -5000
# except ValueError as error:
#     print(error)

# print("음수 변경 시도 후 가격:", validated_product.price)
# 예상 결과:
# "가격은 0 이상이어야 합니다."가 출력된다.
# -5000은 저장되지 않고 기존 가격 60000이 유지된다.
#
# 실제 결과:
# === 음수 가격 변경 시도 ===
# 가격은 0 이상이어야 합니다.
# 음수 변경 시도 후 가격: 60000
#endregion
#region
# 문제 1
# 다음 조건이 먼저 실행되는 이유는 무엇인가?
# if type(new_price) is not int:
# 답: 이 if new_price < 0: 조건이 먼저 실행된다면 문자열은 바로 거를수가 없어서
#[보완]
#자료형 검사를 하지 않고 new_price < 0을 먼저 실행하면, new_price가 문자열일 떄 문자열과 정수를 비교하게 되어 TypeError가 발생하기 때문이다.
#따라서 먼저 정수인지 확인하고 정수인 값에 대해서만 0보다 작은지를 검사한다.

# 문제 2
# 문자열 가격에서 ValueError가 발생하면 다음 코드는 실행되는가?
# self._price = new_price
# 이유도 작성한다.
# 답: ValueError가 발생하면 그 함수의 ValueError code는 전부 중단되기 때문에 실행되지 않는다.
#[보완]
#ValueError가 발생하는 순간 setter의 실행이 중단되므로, 그 아래에 있는 self._price = new_price까지 도달하지 못한다. 발생한 ValueError는 setter를 호출한 바깥쪽 try-except에서 처리된다.

# 문제 3
# 잘못된 가격 변경을 시도한 뒤 기존 가격 60000이 유지되는 이유는 무엇인가?
# 답: 객체의 기존 내부의 가격을 변경하지 못 하였으므로 원래의 가격은 유지된다.

# 문제 4
# 생성자에서 다음 두 코드의 차이는 무엇인가?
# self._price = price
# self.price = price
# 답: 전자는 실제 객체의 속성에 값을 저장하는 것이고, 후자는 setter를 호출하여 객채를 처음 생성했을 때 전달한 가격도 검증한다.

# 문제 5
# 현재 코드에서 다음 객체는 정상적으로 생성되는가?
# ValidatedProduct("마우스", "삼만원")
# 어느 실행 과정에서 문제가 발생하는지도 작성한다.
#답: def price(self, new_price):를 실행하는 과정에서 type(new_price) is not int이기 때문에 ValueError가 발생한다.
#[보완]
#정상적으로 생성되지 않는다.
#ValidatedProduct("마우스", "삼만원")을 실행하면 __init__()의 self.price = price가 price setter를 호출한다.
#setter에서 type(new_price) is not int 조건이 참이므로 ValueError가 발생하고, self._price에는 값이 저장되지 않는다.
#따라서 객체 생성도 끝까지 완료되지 않는다.
#endregion
#endregion

# region 5단계: 객체 생성 시 최초 가격 검증

print("=== 문자열 최초 가격으로 생성 시도 ===")

try:
    invalid_product1 = ValidatedProduct("마우스", "삼만원")
    print("생성 성공:", invalid_product1.price)
except ValueError as error:
    print("생성 실패:", error)


print("=== 음수 최초 가격으로 생성 시도 ===")

try:
    invalid_product2 = ValidatedProduct("모니터", -10000)
    print("생성 성공:", invalid_product2.price)
except ValueError as error:
    print("생성 실패:", error)

# 예상 결과:
# 문자열 최초 가격에서는 "가격은 정수여야 합니다."가 출력된다.
# 음수 최초 가격에서는 "가격은 0 이상이어야 합니다."가 출력된다.
# 두 객체 모두 정상적으로 생성되지 않는다.
# 실제 결과:
# === 문자열 최초 가격으로 생성 시도 ===
# 생성 실패: 가격은 정수여야 합니다.
# === 음수 최초 가격으로 생성 시도 ===
# 생성 실패: 가격은 0 이상이어야 합니다.
#region
# 문제 1
# 객체 생성 중인데도 price setter가 실행되는 이유는 무엇인가?
# __init__ 생성자에 self.price = price를 넣어서 이것이 price setter를 호출하였기 때문이다.

# 문제 2
# invalid_product1 = ValidatedProduct(...)에서 ValueError가 발생하면 invalid_product1 변수에는 완성된 객체가 저장되는가?
# ValueError가 발생하면 그 이후의 코드는 전부 실행이 중단되고, 처리 문자열을 찾아가기 때문에 완성되지 저장되지 않는다.
#[보완]
#대입문의 오른쪽인 ValidatedProduct(...)의 객체 생성이 정상적으로 끝나야 그 결과가 왼쪽 변수에 저장된다.
#그러나 객체 생성 도중 ValueError가 발생했으므로 대입 자체가 완료되지 않는다.
#따라서 invalid_product1이 이전에 존재하지 않았다면 변수도 새로 만들어지지 않는다.

# 문제 3
# __init__()에서 self._price = price를 사용했다면 이번 두 잘못된 객체의 생성 결과는 어떻게 달라지는가?
# 객체를 처음 생성할 때 전달한 가격은 저장되므로 잘못된 두 객체가 생성되었다.
#endregion
#endregion






































