import json
from abc import ABC, abstractmethod

FILE_NAME = "rebuild_products.json"

#1 Product 추상 클래스
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError ("잘못된 가격입니다.")

        self._price = new_price

    @abstractmethod
    def show_info(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

#2 NormalProduct
class NormalProduct(Product):
    def __init__(self, name, price, stock):
        super().__init__(name, price)
        self.stock = stock

    def show_info(self):
        print(f"[일반] {self.name} / {self.price}원 / 재고 {self.stock}개")

    def to_dict(self):
        return {"type": "normal", "name": self.name, "price": self.price, "stock": self.stock}

#3 DownloadProduct
class DownloadProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def show_info(self):
        print(f"[다운로드] {self.name} / {self.price}원 / {self.file_size}MB")

    def to_dict(self):
        return {"type": "download", "name": self.name, "price": self.price, "file_size": self.file_size}

#4 def create_product(data):
def create_product(data):
    if data["type"] == "normal":
        return NormalProduct(data["name"], data["price"], data["stock"])

    elif data["type"] == "download":
        return DownloadProduct(data["name"], data["price"], data["file_size"])

    else:
        return None

#5 ProductManager
class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return True

    def show_all(self):
        if len(self.products) == 0:
            print("등록된 상품이 없습니다.")

        for product in self.products:
            product.show_info()

    def search_product(self, name):
        for product in self.products:
            if name == product.name:
                return product

        return None

    def update_price(self, name, new_price):
        product = self.search_product(name)

        if product is None:
            return False

        # try:
        #     product.price = new_price
        #     return True

        # except ValueError as err:
        #     print(err)
        #     return False

        product.price = new_price
        return True

    def delete_product(self, name):
        product = self.search_product(name)

        if product is None:
            return False

        self.products.remove(product)
        return True

    def save(self, filename):
        products_dict = []

        for product in self.products:
            product_dict = product.to_dict()
            products_dict.append(product_dict)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(products_dict, file, ensure_ascii=False, indent=2)

    def load(self, filename):
        self.products = []

        try:
            with open(filename, "r", encoding="utf-8") as file:
                products_dict = json.load(file)

        except FileNotFoundError:
                # return []
                return

        except json.JSONDecodeError:
                # return []
                return

        # products = []


        for product_dict in products_dict:
            product = create_product(product_dict)

            if product is None:
                continue

            # products.append(product)
            self.products.append(product)

        

manager = ProductManager()

manager.add_product(
    NormalProduct("키보드", 30000, 10)
)

manager.add_product(
    DownloadProduct("게임", 50000, 80)
)

print("=== 전체 조회 ===")
manager.show_all()

print()
print("=== 검색 ===")
product = manager.search_product("게임")
if product is not None:
    product.show_info()

print()
print("=== 가격 변경 ===")
manager.update_price("키보드", 35000)
manager.show_all()

print()
print("=== 저장 ===")
manager.save("rebuild_products.json")
print()


new_manager = ProductManager()
new_manager.load("rebuild_products.json")

print("=== 다시 불러온 결과 ===")
new_manager.show_all()


print()
print("=== 삭제 ===")
new_manager.delete_product("게임")
new_manager.show_all()

print()
print("=== 잘못된 가격 ===")

try:
    manager.update_price("키보드", -1)
except ValueError as error:
    print(type(error).__name__)
    print(error)

#-----------------------------------------------
print()
print("=== 없는 파일 불러오기 ===")

test_manager = ProductManager()
test_manager.add_product(
    NormalProduct("임시 상품", 1000, 1)
)
test_manager.load("not_found_products.json")
test_manager.show_all()

#-----------------------------------------------
print()
print("=== 잘못된 JSON 불러오기 ===")

test_manager.add_product(
    NormalProduct("임시 상품", 1000, 1)
)
test_manager.load("broken_products.json")
test_manager.show_all()

#----------------------------------------------------
print("=== 가격 변경 진단 ===")

result = manager.update_price("키보드", 35000)
print("반환값:", result)

product = manager.search_product("키보드")
print("검색 결과:", product)

if product is not None:
    print("현재 가격:", product.price)

















