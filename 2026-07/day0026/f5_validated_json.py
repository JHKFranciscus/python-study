import json

FILE = "validated_products.json"

#1 Product
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if type(new_price) is not int:
            raise ValueError("가격은 정수여야 합니다.")

        if new_price < 0:
            raise ValueError("가격은 0 이상이어야 합니다.")

        self._price = new_price

    def print_info(self):
        print(f"name: {self.name}, price: {self.price}")

    def to_dict(self):
        return {
            "type": "product",
            "name": self.name,
            "price": self.price
        }

#2 DowloadProduct
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

#3 create_product_from_dict
def create_product_from_dict(data):
    if data["type"] == "product":
        return Product(data["name"], data["price"])

    if data["type"] == "download_product":
         return DownloadProduct(
            data["name"],
            data["price"],
            data["file_size"]
        )

    return None

#4 save_products, load_products
def save_products(products, filename):
    products_dict = []

    for product in products:
        products_dict.append(product.to_dict())

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            products_dict,
            file,
            ensure_ascii=False,
            indent=4
        )

def load_products(filename):
    products = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data_list = json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

    for data in data_list:
        product = create_product_from_dict(data)

        if product is not None:
            products.append(product)

    return products

#region 정상 객체 저장-------------------------------------
products = [
    Product("키보드", 50000),
    DownloadProduct("게임", 30000, 40)
]

print("=== 저장 전 객체 조회 ===")

for product in products:
    product.print_info()

save_products(products, FILE)

print("저장 완료")

# 예상 결과:
# 일반 상품과 다운로드 상품이 정상적으로 출력된다.
# validated_products.json 파일이 생성된다.
# 가격은 JSON에서 숫자로 저장된다.
# 실제 결과:
# === 저장 전 객체 조회 ===
# name: 키보드, price: 50000
# name: 게임, price: 30000
# file_size: 40
# 저장 완료
#endregion
#region 새 목록으로 복원------------------------------
print()
loaded_products = load_products(FILE)

print("=== JSON 파일에서 복원 ===")
print("복원된 상품 수:", len(loaded_products))

for product in loaded_products:
    print(type(product))
    product.print_info()

# 예상 결과:
# 상품 두 개가 복원된다.
# 첫 번째는 Product 객체이다.
# 두 번째는 DownloadProduct 객체이다.
# 가격과 파일 크기가 저장 전 값과 같다.
# 실제 결과:
# === JSON 파일에서 복원 ===
# 복원된 상품 수: 2
# <class '__main__.Product'>
# name: 키보드, price: 50000
# <class '__main__.DownloadProduct'>
# name: 게임, price: 30000
# file_size: 40
#endregion
#region 복원된 객체에도 setter가 작동하는지 확인(이 테스트는 복원 결과가 단순한 딕셔너리가 아니라, getter와 setter를 가진 실제 클래스 객체라는 것을 확인한다.)----------------------------
print()
print("=== 복원 후 가격 변경 ===")

loaded_download = loaded_products[1]

loaded_download.price = 35000
print("정상 변경 후:", loaded_download.price)

try:
    loaded_download.price = "삼만오천원"
except ValueError as error:
    print("문자열 변경 실패:", error)

print("문자열 시도 후:", loaded_download.price)

try:
    loaded_download.price = -35000
except ValueError as error:
    print("음수 변경 실패:", error)

print("음수 시도 후:", loaded_download.price)
# 예상 결과:
# 복원된 DownloadProduct의 가격이 35000으로 정상 변경된다.
# 문자열과 음수는 거부된다.
# 잘못된 변경 이후에도 35000이 유지된다.
# 실제 결과:
# === 복원 후 가격 변경 ===
# 정상 변경 후: 35000
# 문자열 변경 실패: 가격은 정수여야 합니다.
# 문자열 시도 후: 35000
# 음수 변경 실패: 가격은 0 이상이어야 합니다.
# 음수 시도 후: 35000
#endregion
#region---------------------------------------------
# 문제 1
# to_dict()에서 self._price 대신 self.price를 사용하면 어떤 기능을 거쳐 가격 값을 가져오는가?
# @price.setter를 거쳐 self._price를 가져온다.
#[수정 후]
#to_dict()에서 self.price를 사용하면 @property가 붙은 price getter가 실행된다.
#getter가 self._price에 저장된 실제 가격을 반환하고, 반환된 가격이 dictionary의 값으로 들어간다.

# 문제 2
# JSON 파일에 저장되는 키 이름은 _price여야 하는가, price여야 하는가? 이유도 작성한다.
# _price여야한다. price는 외부에서 _price에 접근하기 위한 이름이다. 객체 내부의 속성은 '_'를 붙여서 _price라고 저장하는 것이 관례이다.
#[수정 후]
#JSON 파일에는 "price"라는 키 이름으로 저장한다.
#_price는 Product 객체 내부에서 실제 가격을 저장하는 파이썬 인스턴스 속성의 이름이다.
#JSON의 키 이름은 객체 내부 속성 이름과 반드시 같을 필요가 없으며, 외무에 저장하는 상품 데이터에서는 "price"라는 이름을 사용한다.
#복원할 때도 data["price"]로 값을 꺼내도록 작성했으므로 저장과 복원에서 같은 "price" 키를 사용해야 한다.

# 문제 3
# JSON 딕셔너리를 Product 객체로 복원할 때 가격이 setter 검증을 거치는 이유는 무엇인가?
# __init__으로 초기화를 할 때 self._price = price가 아닌 self.price = price로 초기화를 하여 값을 price에 대입했으므로 @price.setter가 바로 아래의 함수를 호출하여 setter 검증을 거치기 때문이다.

# 문제 4
# JSON 파일에서 복원한 DownloadProduct도 price setter를 사용할 수 있는 이유는 무엇인가?
# DownloadProduct는 Product 클래스를 상속받았기 때문에, Product 클래스에 있는 getter와 setter도 상속받았기 때문에 price setter를 사용할 수 있다.

# 문제 5
# JSON 파일의 가격을 직접 "삼만원"으로 고친 뒤 복원하면 현재 프로그램에서는 어느 지점에서 어떤 오류가 발생할 것으로 예상하는가?
# '@price.setter'가 호출하는 'price()'함수의 'if type(new_price) is not int:' 조건에 걸려서 'ValueError'가 발생할 것으로 예상된다.
#[보완]
# JSON 파일의 가격을 "삼만원"으로 바꿔도 JSON 문법 자체는 올바르므로 JSONDecodeError는 발생하지 않는다.
#load_products()에서 create_product_form_dict(data)를 호출하고, Product 또는 DownloadProduct 객체를 생성하는 과정에서 Product.__init__()의 self.price = price가 실행된다.
#이 때 price setter에서 type(new_price) is not int 조건이 참이 되어 ValueError("가격은 정수여야 합니다.")가 발생한다.
#현재 load_products()는 ValueError를 처리하지 않으므로 이 오류는 함수 밖으로 전달되고 프로그램 실행이 중단된다.
#endregion


















