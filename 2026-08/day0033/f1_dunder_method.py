class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def __str__(self):
        return f"{self.customer}의 주문"

    def __len__(self):
        return len(self.items)


order = Order("민수")

order.items.append("커피")        #order = 객체
order.items.append("샌드위치")    #order.items = list

print(order)
print(len(order))
#region
# 예상 결과:
# 민수의 주문
# 2

# 판단:
# - print(order)가 무엇을 사용하는가: __str__(self) method를 사용한다.
# - len(order)가 무엇을 사용하는가: __len__(self) method를 사용한다.
#endregion

print()
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}원"

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"


p1 = Product("키보드", 50000)        #p1 = 객체
p2 = Product("마우스", 30000)        #p2 = 객체

products = [p1, p2]                 #products = list

print(p1)                          
print(repr(p1))
print(products)
#region
# 예상 결과:
# 키보드 - 50000원
# '키보드' - 50000원
# [<fx0.....><fx0....>]
# 실제 결과:
# 민수의 주문
# 2
# 키보드 - 50000원
# Product(name='키보드', price=50000)
# [Product(name='키보드', price=50000), Product(name='마우스', price=30000)]

# 판단:
# - print(p1)는 어떤 특수 메서드를 사용하는가: __str__ 특수 메서드를 사용한다.
# - repr(p1)는 어떤 특수 메서드를 사용하는가: __str__ 특수 메서드와 __repr__ 특수 메서드를 사용한다.
#[수정 후]
#Product 객체에 대해서는 __repr__()만 사용한다.
# - print(products)에서 리스트 안의 Product 객체들은 __str__과 __repr__ 중 어느 표현을 사용하는가: 둘 다 사용하지 않고 객체의 주소를 반환한다.
#[수정 수]
#리스트 안에 들어 있는 객체를 표현할 때 리스트는 각 원소의 repr 표현을 사용한다.
#endregion

print()
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


p1 = Product("키보드", 50000)    
p2 = Product("키보드", 50000)
p3 = p1

print(p1 == p2)
print(p1 == p3)

print(p1 is p2)
print(p1 is p3)
#region
# 예상 결과:
# True
# True
# False
# True
# 실제 결과:
# False
# True
# False
# True

# 판단:
# - p1과 p2는 같은 객체인가: 다른 객체이다.
# - p1과 p2의 속성 값은 같은가: 둘의 속성 값은 같다.
# - p3는 어떤 객체를 가리키는가: p3가 가리키는 객체와 p1이 가리키는 객체는 동일하다
# - 현재 Product에 __eq__이 없을 때 p1 == p2는 어떻게 판단될 것으로 예상하는가: p1과 p2의 attribute's value는 동일하기 때문에 True라고 예상된다.
#[수정 후]
#객체의 속성 값이 같다는 것과 객체가 ==로 같다고 판단된다는 것은 별개라는 것
#endregion

print()
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


p1 = Product("키보드", 50000)    
p2 = Product("키보드", 50000)
p3 = p1
p4 = Product("키보드", 60000)

print(p1 == p2)
print(p1 == p4)
print(p1 is p2)

# 예상 결과:
True
False
False

# 판단:
# - p1 == p2에서 __eq__의 self는: p1
# - p1 == p2에서 __eq__의 other는: p2
# - p1과 p4는 name은 같은가: True
# - p1과 p4는 price도 같은가: False
# - __eq__을 정의해도 is의 판단 기준이 바뀌는가: eq는 ==의 판단 기준을 설정하는 특수 method이지 is의 판단 기준을 설정하는 특수 method가 아니다
















