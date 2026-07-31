import json

FILE = "rebuild_validated_products.json"

#1. Product: name, _price / print_info(), to_dict()
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(f"name: {self.name}, price: {self.price}")

    def to_dict(self):
        return {"type" : "product", "name" : self.name, "price" : self.price}

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if type(new_price) is not int:
            raise ValueError ("숫자를 입력해주세요.")

        if new_price < 0:
            raise ValueError ("0 이상의 숫자를 입력해주세요.")

        self._price = new_price

#2. DownloadProduct: + file_size / print_info(), to_dict() 오버라이딩
class DownloadProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def print_info(self):
        super().print_info()
        print(f"file_size: {self.file_size}")

    def to_dict(self):
        product_dict = super().to_dict()
        product_dict["type"] = "download_product"
        product_dict["file_size"] = self.file_size
        return product_dict

#3. create_product_from_dict: data -> Product, DownloadProduct, None
def create_product_from_dict(data):
    if data["type"] == "product":
        return Product(data["name"], data["price"])

    elif data["type"] == "download_product":    
        return DownloadProduct(data["name"], data["price"], data["file_size"])

    else:
        return None

#4. save_products(), load_products()
def save_products(products, filename):
    products_dict = []
    for product in products:
        product_dict = product.to_dict()
        products_dict.append(product_dict)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(products_dict, file, ensure_ascii=False, indent=4)

def load_products(filename):
    ref_products = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            products_dict = json.load(file)
                
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

    for product in products_dict:
        ref_product = create_product_from_dict(product)

        if ref_product is not None:
            ref_products.append(ref_product)
                
    return ref_products

#5. ProductManager: filename, products / add_product(product), show_all_products(), search_product(name), update_product_price(name, new_price), delete_product(name), save()
class ProductManager:
    def __init__(self, filename):
        self.filename = filename
        # self.products = products
        self.products = load_products(filename)
    
    def add_product(self, product):
        self.products.append(product)

    def show_all_products(self):
        for product in self.products:
            product.print_info()

    def search_product(self, name):
        for product in self.products:
            if name == product.name:
                return product

        return None

    def update_product_price(self, name, new_price):
        for product in self.products:
            if name == product.name:
                try:
                    product.price = new_price
                    return True

                except ValueError as err:
                    print(err)

        return False

    def delete_product(self, name):
        for product in self.products:
            if name == product.name:
                self.products.remove(product)
                return product

        return None

    def save(self):
        save_products(self.products, self.filename)

#1
print("#1")
manager = ProductManager(FILE)
print(f"파일이 없을 때 상품 수: {len(manager.products)}")
print()


#2
print("#2")
monitor = Product("모니터", 20000)
cut_pro = DownloadProduct("편집 프로그램", 70000, 15)
manager.add_product(monitor)
manager.add_product(cut_pro)
print()

#3
print("#3")
manager.show_all_products()
print()

#4
print("#4")
search1 = manager.search_product("편집 프로그램")
print(type(search1))
search1.print_info()
print()

#5
print("#5")
cut_pro_check = manager.update_product_price("편집 프로그램", 80000)
print(f"정상가격변경 성공여부: {cut_pro_check}")
print(type(cut_pro.price))

#6
print("#6")
cut_pro_check = manager.update_product_price("편집 프로그램", "팔만원")
print(f"가격변경 성공여부: {cut_pro_check}")
cut_pro_check = manager.update_product_price("편집 프로그램", -80000)
print(f"가격변경 성공여부: {cut_pro_check}")
print(cut_pro.price)
print()

#7
print("#7")
manager.save()
print()

#8
print("#8")
new_manager = ProductManager(FILE)

print(f"복원된 상품 수: {len(new_manager.products)}")

for product in new_manager.products:
    print(type(product))
    product.print_info()

print()

#9
# 9. 복원된 객체에서 setter 확인
print("#9")

restored_download = new_manager.search_product("편집 프로그램")

print(new_manager.update_product_price("편집 프로그램", 90000))
print(new_manager.update_product_price("편집 프로그램", "구만원"))
print(new_manager.update_product_price("편집 프로그램", -90000))

print("최종 가격:", restored_download.price)
print()

#10
print("#10")

deleted_product = new_manager.delete_product("모니터")

deleted_product.print_info()
print("남은 상품 수:", len(new_manager.products))

new_manager.save()


# 예상 결과:

# 1. 처음에는 상품 수가 0이다.
# 2. 일반 상품과 다운로드 상품을 등록하면 상품 수가 2가 된다.
# 3. 편집 프로그램 검색 결과는 DownloadProduct 객체다.
# 4. 가격 80000은 정상적으로 반영되고 int로 유지된다.
# 5. "팔만원"과 -80000은 거부되고 기존 가격 80000이 유지된다.
# 6. 저장 후 새 관리자로 두 상품이 복원된다.
# 7. 복원된 객체에서도 setter가 정상 작동한다.
# 8. 모니터 삭제 후 남은 상품 수는 1이다.

# 실제 결과:
# #1
# 파일이 없을 때 상품 수: 0

# #2

# #3
# name: 모니터, price: 20000
# name: 편집 프로그램, price: 70000
# file_size: 15
# None

# #4
# 검색 하면: search1

# #5
# 정상가격변경 성공여부: True
# <class 'int'>
# #6
# 숫자를 입력해주세요.
# 가격변경 성공여부: False
# 0 이상의 숫자를 입력해주세요.
# 가격변경 성공여부: False
# 80000

# #7

# #8
# 복원된 상품 수: 2
# name: 모니터, price: 20000
# name: 편집 프로그램, price: 80000
# file_size: 15
# None

# #9
# True
# 숫자를 입력해주세요.
# False
# 0 이상의 숫자를 입력해주세요.
# False
# 90000

# #10
# name: 모니터, price: 20000
# 1


