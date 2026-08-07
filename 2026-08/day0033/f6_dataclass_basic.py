# from dataclasses import dataclass


# @dataclass
# class Product:
#     name: str
#     price: int


# p1 = Product("키보드", 50000)
# p2 = Product("키보드", 50000)

# print(p1)
# print(p1 == p2)
#region
# 예상 결과:
# <class 'Product' at fx0.....>
# False
# 실제 결과:
# Product(name='키보드', price=50000)
# True

# 판단:
# - Product에 직접 __init__을 작성했는가: 작성하지 않았다.
# - 그런데 Product("키보드", 50000)가 가능한 이유는: @dataclass를 사용했기 때문이다.
# - 직접 __eq__을 작성하지 않았는데 p1 == p2는 어떻게 될 것으로 예상하는가: 두 개는 다른 객체이기 때문에 속성 또한 다르므로 Fasle가 뜰 것을 예상한다.
#[수정 후]
#@dataclass가 __eq__()도 자동 생성하므로 각 필드 값이 같으면 True가 된다.
#endregion
from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: int
    stock: int = 0


item1 = Item("키보드", 50000)
item2 = Item("마우스", 30000, 5)

print(item1)
print(item1.stock)
print(item2.stock)
#region
# 예상 결과:
# Item("name": 키보드, "price": 50000)
# 0
# 5
# 실제 결과
# Item(name='키보드', price=50000, stock=0)
# 0
# 5

# 판단:
# - item1의 stock은: 0
# - 그 값이 들어가는 이유는: Item class를 생성할 stock 속성이 자동으로 생성되는데 그 기본값을 0으로 해두었기 때문이다.
# - item2의 stock은: 5
#endregion




