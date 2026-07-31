# 방식 1: 직접 속성 변경
class DirectProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# 방식 2: 가격 변경 메서드에서 검증
class MethodProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def change_price(self, new_price):
        if type(new_price) is not int:
            return False

        if new_price < 0:
            return False

        self.price = new_price
        return True


# 방식 3: property setter에서 검증
class PropertyProduct:
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


print("=== 방식 1: 직접 속성 변경 ===")

direct_product = DirectProduct("키보드", 50000)
direct_product.price = -5000

print("변경 후 가격:", direct_product.price)


print("=== 방식 2: 변경 메서드 사용 ===")

method_product = MethodProduct("키보드", 50000)

print("메서드 사용 결과:", method_product.change_price(-5000))
print("메서드 사용 후 가격:", method_product.price)

method_product.price = -5000
print("메서드를 우회한 뒤 가격:", method_product.price)


print("=== 방식 3: property setter 사용 ===")

property_product = PropertyProduct("키보드", 50000)

try:
    property_product.price = -5000
except ValueError as error:
    print(error)

print("setter 실행 후 가격:", property_product.price)


# 예상 결과:
# 방식 1에서는 -5000이 그대로 저장된다.
# 방식 2에서는 change_price(-5000)가 False를 반환하고 기존 가격 50000이 유지된다.
# 그러나 method_product.price = -5000으로 직접 대입하면 검사를 우회하여 -5000이 저장된다.
# 방식 3에서는 product.price = -5000 자체가 setter를 호출하므로 음수가 거부되고 기존 가격 50000이 유지된다.

# 실제 결과:
# python3 f8_validation_comparison.py 
# === 방식 1: 직접 속성 변경 ===
# 변경 후 가격: -5000
# === 방식 2: 변경 메서드 사용 ===
# 메서드 사용 결과: False
# 메서드 사용 후 가격: 50000
# 메서드를 우회한 뒤 가격: -5000
# === 방식 3: property setter 사용 ===
# 가격은 0 이상이어야 합니다.
# setter 실행 후 가격: 50000



# 문제 1
# 세 방식 중 잘못된 값을 전혀 검사하지 않는 방식은 무엇인가?
# 답: 방식 1: 직접 속성 변경

# 문제 2
# change_price() 메서드에 검증이 있어도 다음 코드가 잘못된 값을 저장할 수 있는 이유는 무엇인가?

# method_product.price = -5000

# 답: method를 우회하여 직접 속성 변경으로 바꿨기 때문이다.
#[보완]
#change_price()를 호출하지 않고 price 속성에 직접 값을 대입했기 때문에 change_price() 내부의 검증 코드가 실행되지 않는다.

# 문제 3
# property setter 방식에서 외부 코드가 내부 저장 속성 이름인 _price를 알아야 하는가?
# 답: 몰라도 된다.
#[보완]
#외부 코드는 product.price로 조회하거나 값을 대입하면 된다.
#실제 저장 속성이 _price라는 사실은 클래스 내부 구현에 해당하므로 외부 코드가 알 필요가 없다.

# 문제 4
# 가격 검증 규칙을 수정해야 할 때 setter 방식이 유리한 이유는 무엇인가?
# 답: 겉으로는 속성에 직접대입하는 것 같기 때문이다.
# [수정 후]
# 가격 생성과 변경이 모두 같은 setter를 거치므로 가격 검증 규칙을 setter 한 곳에서 관리할 수 있기 때문이다.
# 검증 규칙이 바뀌어도 가격을 변경하는 여러 코드마다 수정할 필요 없이 setter의 검증 코드만 수정하면 된다.

