class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        return f"[일반 상품] 상품명: {self.name}, 가격: {self.price}원"

    def change_price(self, new_price):
        if type(new_price) is int and new_price >= 0:
            self.price = new_price
            return True

        return False


class DownloadProduct(Product):
    def __init__(self, name, price, file_size, file_format):
        super().__init__(name, price)
        self.file_size = file_size
        self.file_format = file_format

    def show_info(self):
        return f"[다운로드 상품] 상품명: {self.name}, 가격: {self.price}원, 파일 크기: {self.file_size}MB, 형식: {self.file_format}"


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return True

    def show_all_products(self):
        products = []
        for product in self.products:
            product_info = product.show_info()
            products.append(product_info)
            # return products
        return products

    def find_product(self, target_name):
        for product in self.products:
            if product.name.lower() == target_name.lower():
                # return product.show_info() #막힌 부분
                return product

        return None

    def change_product_price(self, target_name, new_price):
        change_product = self.find_product(target_name)
        if change_product is not None:
            # return self.change_price(new_price)  #막힌 부분
            return change_product.change_price(new_price)

        return False

    def delete_product(self, target_name):
        # for product in self.products:   #막힌 부분
        #     if target_name.lower() == product.name.lower(): #막힌 부분
        del_product = self.find_product(target_name)
        if del_product is not None:
                self.products.remove(del_product)
                return True

        return False


product1 = Product("키보드", 50000)

download1 = DownloadProduct(
    "파이썬 강의",
    30000,
    1200,
    "MP4"
)

product2 = Product("마우스", 25000)

manager = ProductManager()  #막힌 부분


manager.add_product(product1)
manager.add_product(download1)
manager.add_product(product2)

print(manager.change_product_price("없는 상품", 40000))

print("1. 전체 조회")
print("2. 강의 검색")
print("3. 가격 변경")
print("4. 상품 삭제")
print("0. 종료")

while True:
    print()

    menu = input("메뉴를 고르세요: ")

    if menu == "1":
        print(manager.show_all_products())

    elif menu == "2":
        target_name = input("검색 제목: ")

        found = manager.find_product(target_name)

        if found is None:
            print("없는 상품")
        else:
            print(found.show_info())

    elif menu == "3":
        target_name = input("찾는 물품명: ")
        try:
            new_price = int(input("바꿀 금액: "))
        except ValueError:
            print("실패")
            continue

        changed = manager.change_product_price(target_name, new_price)

        if changed is False:
            print("실패")
        else:
            print("성공")

    elif menu == "4":
        target_name = input("찾는 물품명: ")

        deledted = manager.delete_product(target_name)

        if deledted == True:
            print("True")
        else:
            print("False")

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 번호를 입력해주세요")













