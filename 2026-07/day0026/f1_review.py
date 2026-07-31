import json

FILE = "managed_products_review.json"

#1. Product: name, price / print_info(), to_dict()
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(f"name: {self.name}, price: {self.price}")

    def to_dict(self):
        return {"type" : "product", "name" : self.name, "price" : self.price}
        
#2. DownloadProduct(product): + file_size / print_info(), to_dict() 오버라이딩
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

#3. create_product_from_dict(data) -> Product / DownloadProduct / None
def create_product_from_dict(data):
    ##5. 복원할 클래스 종류를 구분하는 기준
    ## dictionary 상품의 종류를 구분
    if data["type"] == "product":
        return Product(data["name"], data["price"])
    
    elif data["type"] == "download_product":
        return DownloadProduct(data["name"], data["price"], data["file_size"])
    
    else:
        return None

#4. save_products(products, filename)
def save_products(products, filename):
    products_dict = []

    for product in products:
        product_dict = product.to_dict()
        products_dict.append(product_dict)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(products_dict, file, ensure_ascii=False, indent=4)

#5. load_products(filename)
def load_products(filename):
    products = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = json.load(file)

            for line in lines:
                one_line = create_product_from_dict(line)

                if one_line is not None:
                    products.append(one_line)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

    return products

#6. ProductManager: filename, products / add_product(product), show_all_products(), search_product(name), update_product_price(name, new_price), delete_product(name), save()
#12테스트
class ProductManager:
    def __init__(self, filename):
        self.filename = filename
        self.products = load_products(filename)

    def add_product(self, product):
        self.products.append(product)

    def show_all_products(self):
        for product in self.products:
            product.print_info()

    def search_product(self, name):
        clean_name = name.strip()
        for product in self.products:
            if clean_name == product.name.strip():
                return product

        return None

    def update_product_price(self, name, new_price):
        try:
            int_new_price = int(new_price)

        except (ValueError, TypeError):
            return False

        if int_new_price < 0:
            return False

        clean_name = name.strip()
        for product in self.products:
            if clean_name == product.name.strip():
                product.price = int_new_price
                return True

        return False

    def delete_product(self, name):
        clean_name = name.strip()
        for product in self.products:
            if clean_name == product.name.strip():
                self.products.remove(product)
                return product

        return None

    def save(self):
        save_products(self.products, self.filename)

p = Product("키보드", 50000)

d = DownloadProduct("게임", 30000, 40)

m = ProductManager(FILE)

if len(m.products) == 0:
    m.add_product(
        Product("키보드", 50000)
    )
    m.add_product(
        DownloadProduct("게임", 30000, 40)
    )
    m.add_product(
        Product("마우스", 10000)
    )
    m.add_product(
        DownloadProduct("자료", 50000, 5)
    )
    
print("=== 1. 전체 조회 ===")
m.show_all_products()

print("=== 2. '게임' 검색 ===")
print(m.search_product("게임"))

print("=== 3. ' 게임 ' 검색 ===")
print(m.search_product("  게임  "))

print("=== 4~5. '35000'으로 변경 + 타입 ===")
print(m.update_product_price("게임", "35000"))
g = m.search_product("게임")
print(g.price, type(g.price))                    # 35000 <class 'int'>

print("=== 6. '삼만원' 거부 ===")
print(m.update_product_price("게임", "삼만원"))  # False

print("=== 7. 음수 거부 ===")
print(m.update_product_price("게임", -5000))     # False

print("=== 8. 키보드 삭제 ===")
print(m.delete_product("키보드"))
print(len(m.products))                            # 1

print("=== 9. 저장 ===")
m.save()

print("=== 10~12. 새 매니저로 복원 ===")
m2 = ProductManager(FILE)
print(len(m2.products))                           # 1
print(type(m2.products[0]))                       # DownloadProduct
print(m2.products[0].price)                       # 35000
m2.show_all_products()
print(m2.search_product("게임"))
print(m2.update_product_price("게임", 40000))     # True
print(m2.delete_product("게임"))
