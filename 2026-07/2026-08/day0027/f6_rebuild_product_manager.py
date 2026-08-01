#1. 
import json
from abc import ABC, abstractmethod

#2. Product: name, _price / price getter, price setter / get_product_info(), to_dict() 추상메서드
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        # if isinstance(new_price, int):
        if not isinstance(new_price, int):
            raise ValueError ("가격은 정수로 입력해주세요.")

        if new_price < 0:
            raise ValueError ("가격은 0 이상이어야 합니다.")

        self._price = new_price       #빼먹음

    @abstractmethod
    def get_product_info(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

#3. PhysicalProduct / physical
class PhysicalProduct(Product):
    def get_product_info(self):
        return f"{self.name} / {self.price}원 / 일반 상품"

    def to_dict(self):
        return {"type" : "physical", "name" : self.name, "price" : self.price}

#4. DownloadProduct: file_size / download
class DownloadProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def get_product_info(self):
        return f"{self.name} / {self.price}원 / 다운로드 상품 / {self.file_size}MB"

    def to_dict(self):
        return {"type" : "download", "name" : self.name, "price" : self.price, "file_size" : self.file_size}

#5. SubscriptionProduct: subscription_months / subscription
class SubscriptionProduct(Product):
    def __init__(self, name, price, subscription_months):
        super().__init__(name, price)
        self.subscription_months = subscription_months

    def get_product_info(self):
        return f"{self.name} / {self.price}원 / 구독 상품  / {self.subscription_months}개월"

    def to_dict(self):
        return {"type" : "subscription", "name" : self.name, "price" : self.price, "subscription_months" : self.subscription_months}

#6. ProductManager: register_product(product), show_products(), search_product(name), change_product_price(name, new_price), delete_product(name), save_to_file(filename), load_from_file(filename)
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

        # for product in self.products:
        #     if clean_name == product.name:
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

        # for product in self.products:
        #     if clean_name == product.name:
        product = self.search_product(clean_name)

        if product is None:
                return False
        
        self.products.remove(product)
        return True

        # return False

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
                for product in products:
                    if product["type"] == "physical":
                        p = PhysicalProduct(product["name"], product["price"])
                        self.register_product(p)

                    elif product["type"] == "download":
                        d = DownloadProduct(product["name"], product["price"], product["file_size"])
                        self.register_product(d)

                    elif product["type"] == "subscription":
                        s = SubscriptionProduct(product["name"], product["price"], product["subscription_months"])
                        self.register_product(s)

                    else:
                        return None

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []

#region
#테스트 5개
FILE_NAME = "rebuild_products.json"

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
#endregion
#region
# CS 기초 — 다형성과 동적 디스패치

# 문제 1
# product.get_product_info()라는 같은 코드를 호출해도 객체마다 다른 결과가 나오는 이유는 무엇인가?
# 답: prduct에 들어가는 값은 반복문이 반복될 때 마다 달라지고, 그 실제 객체의 클래스에 따라 실행되는 메소드가 달라지기 때문이다.

# 문제 2
# 동적 디스패치에서 실제로 실행할 메서드는 무엇을 기준으로 선택되는가?
# 답: 실제 객체의 class를 기준으로 선택된다.
#[좀 더 정확하게]
#프로그램 실행 시점에 변수가 가리키는 실제 객체의 클래스를 기준으로 선택된다.

# 문제 3
# DownloadProduct에 get_product_info()가 없다면 Python은 다음으로 어디에서 메서드를 찾는가?
# 답: 부모 class에서 같은 이름의 method가 있는지 찾는다.
#endregion