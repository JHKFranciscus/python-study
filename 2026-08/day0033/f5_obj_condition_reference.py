class Box:
    def __init__(self):
        self.items = []


box1 = Box()
box2 = box1

box2.items.append("키보드")

print(box1.items)    #box1.items = list
print(box2.items)    #box2.items = list
print(box1 is box2)  #box1 & box2 = object
#region
# 예상 결과:
# 키보드
# 키보드
# True
# 실제 결과:
# ['키보드']
# ['키보드']
# True

# 판단:
# - box1이 가리키는 것은: Box 클래스의 instance
# - box2가 가리키는 것은: box1이 가리키는 instance
# - Box 객체는 총 몇 개 생성됐는가: 1개
# - box2.items를 수정하면 box1.items에도 영향을 주는가: yes 
# - 그 이유는: box2가 가리키는 객체와 box1이 가리키는 객체가 같기 때문에 box2가 가리키는 객체의 속성과 box1이 가리키는 객체의 속성 또한 동일하다. 그러므로 box2의 속성을 수정하면 box1속성에도 영향을 준다.
#endregion
print()
class Box:
    def __init__(self):
        self.items = []


box1 = Box()
box2 = Box()

box1.items.append("키보드")

print(box1.items)
print(box2.items)
print(box1 is box2)
#region
# 예상 결과:
# ['키보드']
# []
# False

# 판단:
# - Box 객체는 총 몇 개 생성되는가: 2개
# - box1.items와 box2.items는 같은 리스트인가: 서로 다른 객체이므로 서로 다른 속성을 가지므로 서로 다른 리스트이다.
# - box1.items를 수정하면 box2.items에도 영향을 주는가: 주지 않는다. 
# - 그 이유는: box1과 box2는 서로 다른 객체이므로 서로 다른 속성을 가지므로 box1.items라는 box1의 속성인 list를 수정하여도 box2의 속성인 list에 영향을 주지 않는다.
#endregion
print()
class Box:
    def __init__(self):
        self.items = []


box1 = Box()
box2 = Box()

box2.items = box1.items

box1.items.append("키보드")

print(box1.items)
print(box2.items)

print(box1 is box2)
print(box1.items is box2.items)
#region
# 예상 결과:
['키보드']
[]
False
True

# 판단:
# - box1과 box2는 같은 Box 객체인가: False
# - box1.items와 box2.items는 같은 list 객체인가: True
# - Box 객체는 몇 개인가: 2개
# - items list 객체는 최종적으로 몇 개인가: 1개
# - box1.items를 수정했는데 box2.items에서도 보이는 이유는: box1.items와 box2.items가 같은 리스트 객체를 속성으로 참조하고 있기 때문이다.
#endregion


