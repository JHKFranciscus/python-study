import json
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, int):
            raise ValueError ("가격은 정수로 입력해주세요.")

        if new_price < 0:
            raise ValueError ("가격은 0 이상이어야 합니다.")

        self._price = new_price

    @abstractmethod
    def get_product_info(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

class PhysicalProduct(Product):
    def get_product_info(self):
        return f"{self.name} / {self.price}원 / 일반 상품"

    def to_dict(self):
        return {"type" : "physical", "name" : self.name, "price" : self.price}

class DownloadProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def get_product_info(self):
        return f"{self.name} / {self.price}원 / 다운로드 상품 / {self.file_size}MB"

    def to_dict(self):
        return {"type" : "download", "name" : self.name, "price" : self.price, "file_size" : self.file_size}

class SubscriptionProduct(Product):
    def __init__(self, name, price, subscription_months):
        super().__init__(name, price)
        self.subscription_months = subscription_months

    def get_product_info(self):
        return f"{self.name} / {self.price}원 / 구독 상품  / {self.subscription_months}개월"

    def to_dict(self):
        return {"type" : "subscription", "name" : self.name, "price" : self.price, "subscription_months" : self.subscription_months}


def create_product_from_dict(data):
    product_type = data["type"]
            
    if product_type == "physical":
        return PhysicalProduct(data["name"], data["price"])

    elif product_type == "download":
        return DownloadProduct(data["name"], data["price"], data["file_size"])

    elif product_type == "subscription":
        return SubscriptionProduct(data["name"], data["price"], data["subscription_months"])
            
    else:
        raise ValueError("알 수 없는 상품 종류입니다.")


class ProductManager:
    def __init__(self):
        self.products = []

    def register_product(self, product):
        self.products.append(product)

    def show_products(self):
        if len(self.products) == 0:
            print("품목이 비어있습니다.")
            return
        
        for product in self.products:
            print(product.get_product_info())

    def search_product(self, name):
        clean_name = name.strip()

        for product in self.products:
            if clean_name == product.name:
                return product

        return None

    def change_product_price(self, name, new_price):
        clean_name = name.strip()

        product = self.search_product(clean_name)

        if product is None:
                return False

        try:
            product.price = new_price
            return True

        except ValueError as err:
            print(err)
            return False

    def delete_product(self, name):
        clean_name = name.strip()

        product = self.search_product(clean_name)

        if product is None:
                return False
        
        self.products.remove(product)
        return True

    def save_to_file(self, filename):
        products_dict = []
        for product in self.products:
            product_dict = product.to_dict()
            products_dict.append(product_dict)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(products_dict, file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                products = json.load(file)

                for product_data in products:
                    product = create_product_from_dict(product_data)
                    self.register_product(product)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []


FILE_NAME = "add_rebuild_products.json"

manager = ProductManager()
manager.register_product(PhysicalProduct("키보드", 50000))
manager.register_product(DownloadProduct("파이썬 전자책", 15000, 30))
manager.register_product(SubscriptionProduct("코딩 학습 서비스", 9900, 6))

# 테스트 1 — 저장 전 전체 조회
print("[저장 전]")
manager.show_products()

# 테스트 2 — JSON 저장·복원
manager.save_to_file(FILE_NAME)

new_manager = ProductManager()

new_manager.load_from_file(FILE_NAME)

print("\n[복원 후]")
new_manager.show_products()

# 테스트 3 — 가격 변경
print("\n[가격 변경]")

result = new_manager.change_product_price("키보드", 55000)

print(result)
print(new_manager.search_product("키보드").get_product_info())

# 테스트 4 — 잘못된 가격 변경
print("\n[잘못된 가격 변경]")

result = new_manager.change_product_price("키보드", -1000)

print(result)
print(new_manager.search_product("키보드").price)

# 테스트 5 — 삭제
print("\n[삭제]")

result = new_manager.delete_product("코딩 학습 서비스")

print(result)
new_manager.show_products()

# 테스트 6 - 객체 생성 함수
print("[객체 생성 함수 테스트]")

test_data = {
    "type": "download",
    "name": "테스트 전자책",
    "price": 12000,
    "file_size": 25
}

test_product = create_product_from_dict(test_data)

print(type(test_product).__name__)
print(test_product.get_product_info())


