# # 문제 1. 클래스 속성과 인스턴스 속성
# class Product:
#     category = "상품"

#     def __init__(self, name):
#         self.name = name


# product1 = Product("키보드")
# product2 = Product("마우스")

# product1.category = "전자기기"

# print(Product.category)
# print(product1.category)
# print(product2.category)


# # 문제 2. 프로퍼티 setter와 생성자
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("가격은 0원 이상이어야 합니다.")

#         self._price = value


# try:
#     product = Product("키보드", -1000)
#     print(product.price)
# except ValueError as error:
#     print(error)


# # 문제 3. 상속·오버라이딩·동적 디스패치
# class Product:
#     def __init__(self, name):
#         self.name = name

#     def show_info(self):
#         print(f"일반 상품: {self.name}")


# class DownloadProduct(Product):
#     def __init__(self, name, file_size):
#         super().__init__(name)
#         self.file_size = file_size

#     def show_info(self):
#         print(f"다운로드 상품: {self.name}, {self.file_size}MB")


# products = [
#     Product("책상"),
#     DownloadProduct("게임", 50)
# ]

# for product in products:
#     product.show_info()


# # 문제 4. 추상 클래스의 객체 생성
# from abc import ABC, abstractmethod


# class Product(ABC):
#     @abstractmethod
#     def show_info(self):
#         pass


# class NormalProduct(Product):
#     def show_info(self):
#         print("일반 상품")


# try:
#     product1 = Product()
#     product1.show_info()
# except TypeError as error:
#     print("Product 생성 실패")
#     print(type(error).__name__)


# product2 = NormalProduct()
# product2.show_info()


# #문제 5. JSON 딕셔너리와 클래스 객체
# class DownloadProduct:
#     def __init__(self, name, price, file_size):
#         self.name = name
#         self.price = price
#         self.file_size = file_size

#     def show_info(self):
#         print(
#             f"{self.name} / {self.price}원 / "
#             f"{self.file_size}MB"
#         )


# data = {
#     "type": "download",
#     "name": "게임",
#     "price": 30000,
#     "file_size": 50
# }

# product = data
# product.show_info()

# product = DownloadProduct(
#     "게임",
#     30000,
#     50
# )
# product.show_info()
