class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

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


keyboard = Product("키보드", 50000)
ebook = DownloadProduct("파이썬 전자책", 15000, 30)
service = SubscriptionProduct("코딩 학습 서비스", 9900, 6)
products = [keyboard, ebook, service]

for product in products:
    print(f"{product.name} / {product.price}원 / {product.get_product_type()}")


# 문제 1
# 다음 반복문에서 product 변수가 차례로 가리키는 실제 객체의 클래스 이름을 쓰세요.

# for product in products:
#     print(product.get_product_type())

# 답:Product, DownloadProduct, SubscriptionProduct

# 문제 2
# 반복문에서는 항상 똑같이 다음 메서드를 호출했습니다.

# product.get_product_type()

# 그런데도 "일반 상품", "다운로드 상품", "구독 상품"으로 결과가 달라지는 이유를 설명하세요.

# 답: 메소드 오버라이딩을 하여 같은 메소드라도 실제 객체마다 다른 값을 가지게 만들었다.
#[보완]
#자식 클래스들이 get_product_type()을 각각 오버라이딩했으며, Python이 변수가 실제로 가리키는 객체의 클래스에 맞는 메서드를 실행하기 때문에 결과가 달라진다.

# 문제 3
# DownloadProduct 클래스에서 다음 메서드를 삭제한다면,

# def get_product_type(self):
#     return "다운로드 상품"

# 전자책 객체에 대해 아래 코드를 실행했을 때 무엇이 출력되는지 쓰고, 그 이유도 설명하세요.

# print(ebook.get_product_type())

# 답: DownloadProduct는 Product를 상속받았기 때문에 Product의 attribute와 method를 이어받아 사용할 수 있다. 따라서 DownloadProduct가 ebook.get_product_type()을 사용하면 Product의 get_product_type() method를 사용하게 되어 "일반 상품"이 출력된다.