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
    def price(self,new_price):
        if not isinstance(new_price, int):
            raise ValueError("가격은 정수여야 합니다.")

        if new_price < 0:
            raise ValueError("가격은 0 이상이어야 합니다.")

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
        return {"type": "physical", "name": self.name, "price": self.price}


class DownloadProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def get_product_info(self):
        return f"{self.name} / {self.price}원 / 다운로드 상품 / {self.file_size}MB"

    def to_dict(self):
        return {"type": "download", "name": self.name, "price": self.price, "file_size": self.file_size}


class SubscriptionProduct(Product):
    def __init__(self, name, price, subscription_months):
        super().__init__(name, price)
        self.subscription_months = subscription_months

    def get_product_info(self):
        return f"{self.name} / {self.price}원 / 구독 상품 / {self.subscription_months}개월"

    def to_dict(self):
        return {"type": "subscription", "name": self.name, "price": self.price, "subscription_months": self.subscription_months}


class ProductManager:
    def __init__(self):
        self.products = []

    def register_product(self, product):
        self.products.append(product)

    def show_products(self):
        if len(self.products) == 0:
            print("등록된 상품이 없습니다.")
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
        product = self.search_product(name)

        if product is None:
            return False
        else:
            # try:
            #     self.price(self,new_price)

            # except ValueError as err:
            #     print(err)

            # product.price = new_price
            # return True
            try:
                product.price = new_price
                return True

            except ValueError as err:
                print(err)
                return False

    def delete_product(self, name):
        product = self.search_product(name)

        if product is None:
            return False

        else:
            self.products.remove(product)
            return True

    def save_to_file(self, filename):
        # data = [product.to_dict() for product in self.products]
        data = []

        for product in self.products:
            data.append(product.to_dict())

        with open(filename, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as fp:
            data = json.load(fp)

        loaded_products = []

        for item in data:
            product_type = item["type"]

            if product_type == "physical":
                product = PhysicalProduct(
                    item["name"],
                    item["price"]
                )

            elif product_type == "download":
                product = DownloadProduct(
                    item["name"],
                    item["price"],
                    item["file_size"]
                )

            elif product_type == "subscription":
                product = SubscriptionProduct(
                    item["name"],
                    item["price"],
                    item["subscription_months"]
                )

            else:
                raise ValueError("알 수 없는 상품 종류입니다.")

            loaded_products.append(product)

        self.products = loaded_products


#region
# manager = ProductManager()

# manager.register_product(
#     PhysicalProduct("키보드", 50000)
# )

# manager.register_product(
#     DownloadProduct("파이썬 전자책", 15000, 30)
# )

# manager.register_product(
#     SubscriptionProduct("코딩 학습 서비스", 9900, 6)
# )

# print("[전체 상품]")
# manager.show_products()

# print("\n[검색]")
# found_product = manager.search_product("파이썬 전자책")

# if found_product is not None:
#     print(found_product.get_product_info())

# print("\n[가격 변경]")
# print(manager.change_product_price("키보드", 50000))
# manager.show_products()

# print("\n[삭제]")
# print(manager.delete_product("코딩 학습 서비스"))
# manager.show_products()
#endregion
#region
FILE_NAME = "products.json"

manager = ProductManager()

manager.register_product(
    PhysicalProduct("키보드", 50000)
)

manager.register_product(
    DownloadProduct("파이썬 전자책", 15000, 30)
)

manager.register_product(
    SubscriptionProduct("코딩 학습 서비스", 9900, 6)
)

print("[저장 전]")
manager.show_products()

manager.save_to_file(FILE_NAME)

loaded_manager = ProductManager()
loaded_manager.load_from_file(FILE_NAME)

print("\n[복원 후]")
loaded_manager.show_products()

print("\n[복원된 클래스]")
for product in loaded_manager.products:
    print(type(product).__name__)

# 테스트 1 — 문자열 가격으로 객체 생성
print("\n[문자열 가격 생성 테스트]")

try:
    invalid_product = PhysicalProduct("잘못된 상품", "1000")
except ValueError as err:
    print(err)

# 테스트 2 — 음수로 가격 변경
print("\n[음수 가격 변경 테스트]")

result = loaded_manager.change_product_price("키보드", -1000)

print(result)
print(loaded_manager.search_product("키보드").price)

# 테스트 3 — 존재하지 않는 파일
print("\n[없는 파일 테스트]")

missing_manager = ProductManager()

try:
    missing_manager.load_from_file("missing_products.json")
except FileNotFoundError:
    print("상품 파일을 찾을 수 없습니다.")

# 테스트 4 — JSON 형식이 잘못된 파일
with open("invalid_products.json", "w", encoding="utf-8") as fp:
    fp.write("[잘못된 JSON")


print("\n[잘못된 JSON 테스트]")

invalid_json_manager = ProductManager()

try:
    invalid_json_manager.load_from_file("invalid_products.json")
except json.JSONDecodeError:
    print("JSON 형식이 올바르지 않습니다.")

# 테스트 5 — 알 수 없는 상품 종류
unknown_data = [
    {
        "type": "video",
        "name": "동영상 상품",
        "price": 10000
    }
]

with open("unknown_products.json", "w", encoding="utf-8") as fp:
    json.dump(
        unknown_data,
        fp,
        ensure_ascii=False,
        indent=4
    )

print("\n[알 수 없는 상품 종류 테스트]")

unknown_manager = ProductManager()

try:
    unknown_manager.load_from_file("unknown_products.json")
except ValueError as err:
    print(err)
