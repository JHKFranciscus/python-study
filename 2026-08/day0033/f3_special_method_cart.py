#1
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}원"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price
#2
class Cart:
    # catalog = []
    def __init__(self):
        self.catalog = []

    # def __add__(cls, product):
    # def add(cls, product):
        # cls.catalog.append(product)
    def add(self, product):
        self.catalog.append(product)

    def __len__(self):
        return len(self.catalog)

    def __iter__(self):
        return iter(self.catalog)
#3
cart = Cart()

item1 = Product("키보드", 50000)
item2 = Product("마우스", 30000)
item3 = Product("모니터", 200000)
#4
cart.add(item1)
cart.add(item2)
cart.add(item3)
#5
print(f"상품 수: {len(cart)}")
#6
for product in cart:
    print(product)
#7
item4 = Product("키보드", 50000)

print(item1 == item4)










