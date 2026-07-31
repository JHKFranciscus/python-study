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


class DownloadProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def print_info(self):
        super().print_info()
        print(f"file_size: {self.file_size}")

#region
print("=== 정상 일반 상품 생성 ===")
product = Product("키보드", 50000)
product.print_info()

print("=== 정상 다운로드 상품 생성 ===")
download_product = DownloadProduct("게임", 30000, 40)
download_product.print_info()

# 예상 결과:
# 일반 상품은 가격 50000으로 생성된다.
# 다운로드 상품은 가격 30000, 파일 크기 40으로 생성된다.
# 실제 결과:
# === 정상 일반 상품 생성 ===
# name: 키보드, price: 50000
# === 정상 다운로드 상품 생성 ===
# name: 게임, price: 30000
# file_size: 40
#endregion
#region
print()
print("=== 다운로드 상품 문자열 가격 생성 시도 ===")

try:
    invalid_download1 = DownloadProduct("게임", "삼만원", 40)
except ValueError as error:
    print("생성 실패:", error)


print("=== 다운로드 상품 음수 가격 생성 시도 ===")

try:
    invalid_download2 = DownloadProduct("게임", -30000, 40)
except ValueError as error:
    print("생성 실패:", error)

# 예상 결과:
# 문자열 가격에서는 "가격은 정수여야 합니다."가 출력된다.
# 음수 가격에서는 "가격은 0 이상이어야 합니다."가 출력된다.
# DownloadProduct에 setter를 다시 작성하지 않았어도 부모 Product의 setter가 가격을 검증한다.
# 실제 결과:
# === 다운로드 상품 문자열 가격 생성 시도 ===
# 생성 실패: 가격은 정수여야 합니다.
# === 다운로드 상품 음수 가격 생성 시도 ===
# 생성 실패: 가격은 0 이상이어야 합니다.
#endregion
#region
print()
print("=== 상속받은 setter로 가격 변경 ===")

download_product.price = 35000
print("변경 후 가격:", download_product.price)

try:
    download_product.price = "삼만오천원"
except ValueError as error:
    print("변경 실패:", error)

print("문자열 변경 시도 후 가격:", download_product.price)

try:
    download_product.price = -35000
except ValueError as error:
    print("변경 실패:", error)

print("음수 변경 시도 후 가격:", download_product.price)

# 예상 결과:
# 정상 가격 35000으로 변경된다.
# 문자열과 음수 가격은 모두 거부된다.
# 잘못된 변경 이후에도 가격 35000이 유지된다.
# 실제 결과:
# === 상속받은 setter로 가격 변경 ===
# 변경 후 가격: 35000
# 변경 실패: 가격은 정수여야 합니다.
# 문자열 변경 시도 후 가격: 35000
# 변경 실패: 가격은 0 이상이어야 합니다.
# 음수 변경 시도 후 가격: 35000
#endregion
#region
# 문제 1
# DownloadProduct 클래스에 price getter와 setter를 다시 작성하지 않았는데도 download_product.price를 사용할 수 있는 이유는 무엇인가?
# DownloadProduct는 Product의 한 종류로 Product를 상속받았다. 이에 따라서 Product의 attribute와 method를 이어받는데 Product의 getter와 setter도 함께 이어받기 때문이다.
#[보완]
#DownloadProduct는 Product를 상속하므로 Product 클래스에 정의된 price getter와 stter를 물려받는다.
#따라서 DownloadProduct에 getter와 setter를 다시 작성하지 않아도 download_product.price로 조회하거나 변경할 수 있다.
# 단, _pirce 같은 instance attribute는 자동으로 생성되는 것이 아니라 super().__init__(name, price)를 통해 부보 생성자가 실행될 때 만들어진다. 

# 문제 2
# DownloadProduct("게임", "삼만원", 40)을 생성할 때 어떤 순서로 실행되어 ValueError가 발생하는가?
# class DownloadProduct(Product): 실행
# -> def __init__(self, name, price, file_size): 실행
# -> super().__init__(name, price)가 class Product의 __init__(self, name, price)를 호출
# -> __init__(self, name, price)실행
# -> self.price = price가 @price.setter를 통하여 def price(self, new_price):를 호출
# -> def price(self, new_price):를 실행
# -> if type(new_price) is not int: 조건에 걸려서 raise ValueError("가격은 정수여야 합니다.")가 발생

# 문제 3
# super().__init__(name, price)를 호출하지 않는다면 부모의 가격 초기화와 검증은 자동으로 실행되는가?
# DownloadProduct 클래스의 __init__() method는 Product 클래스의 __init__을 오버라이딩 한 것으로 super()가 없다면 부모 클래스의 __init__도 실행할 수 없기 때문에 부모의 가격 초기화와 검증은 자동으로 실행되지 않는다.

# 문제 4
# download_product.price = -35000에서 DownloadProduct의 메서드와 Product의 메서드 중 어느 setter가 실행되는가?
# Product 클래스에 setter를 가지고 있기 때문에 Product의 메서드 setter가 실행된다.

# 문제 5
# 잘못된 가격 변경 후에도 기존 가격 35000이 유지되는 이유는 무엇인가?
# 기존 내부 가격을 변경하지 않았기 때문이다.
#[보완]
#ValueError가 발생하여 self._price = new_price까지 도달하지 못했으므로 기존 내부 가격 35000이 유지된다.
#endregion