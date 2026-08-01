from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_product_type(self):
        pass


class PhysicalProduct(Product):
    def get_product_type(self):
        return f"일반 상품"


class DownloadProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def get_product_type(self):
        return f"다운로드 상품"


class SubscriptionProduct(Product):
    def __init__(self, name, price, subscription_months):
        super().__init__(name, price)
        self.subscription_months = subscription_months

    def get_product_type(self):
        return f"구독 상품"


keyboard = PhysicalProduct("키보드", 50000)
ebook = DownloadProduct("파이썬 전자책", 15000, 30)
service = SubscriptionProduct("코딩 학습 서비스", 9900, 6)
products = [keyboard, ebook, service]

for product in products:
    print(f"{product.name} / {product.price}원 / {product.get_product_type()}")

# product = Product("테스트 상품", 1000)