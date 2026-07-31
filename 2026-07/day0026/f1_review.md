```python
import json

FILE = "managed_products.json"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(f"name: {self.name}, price: {self.price}")

    ##1. Product 객체를 딕셔너리로 바꾸는 부분
    ## 객체를 JSON 저장용 딕셔너리로 변환
    def to_dict(self):
        return {"type" : "product", "name" : self.name, "price" : self.price}
        
class DownloadProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def print_info(self):
        super().print_info()
        print(f"file_size: {self.file_size}")
    
    ##2. DownloadProduct 객체를 딕셔너리로 바꾸는 부분
    ## 객체를 JSON 저장용 딕셔너리로 변환

    def to_dict(self):
        product_dict = super().to_dict()
        product_dict["type"] = "download_product"
        product_dict["file_size"] = self.file_size
        return product_dict

##3. 딕셔너리를 Product 객체로 복원하는 부분
##4. 딕셔너리를 DownloadProduct 객체로 복원하는 부분
## 딕셔너리의 상품 종류를 확인해 객체로 복원
def create_product_from_dict(data):
    ##5. 복원할 클래스 종류를 구분하는 기준
    ## dictionary 상품의 종류를 구분
    if data["type"] == "product":
        return Product(data["name"], data["price"])
    
    elif data["type"] == "download_product":
        return DownloadProduct(data["name"], data["price"], data["file_size"])
    
    else:
        return None

def save_products(products, filename):
    products_dict = []

    for product in products:
        product_dict = product.to_dict()
        products_dict.append(product_dict)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(products_dict, file, ensure_ascii=False, indent=4)

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
```
#-------------------------------------------------------------------------------------------
어제 완성한 Product, DownloadProduct, ProductManager와 JSON 파일을 열어 놓는다.

# 1단계: 코드에서 위치 찾기

다음 다섯 부분을 직접 찾아라.

1. Product 객체를 딕셔너리로 바꾸는 부분
2. DownloadProduct 객체를 딕셔너리로 바꾸는 부분
3. 딕셔너리를 Product 객체로 복원하는 부분
4. 딕셔너리를 DownloadProduct 객체로 복원하는 부분
5. 복원할 클래스 종류를 구분하는 기준

찾은 코드에 이미 주석이 있다면 그대로 둔다. 새 주석을 추가한다면 다음처럼 짧게 표시한다.

# 객체를 JSON 저장용 딕셔너리로 변환
# 딕셔너리의 상품 종류를 확인해 객체로 복원

#---------------------------------------------------------------------------------------------
# 2단계: 복습 문제

다음 답안을 코드 아래 또는 별도 복습 기록에 작성한다.

문제 1
객체를 그대로 JSON 파일에 저장하지 않고 딕셔너리로 변환한 이유는 무엇인가?
답: JSON파일로 변환하는 직렬화는 문자열, 숫자, 불, null, 배열, 객체라는 기본 자료형은 읽어서 변형할 수 있지만, 사용자 지정 타입인 클래스는 직렬화를 할 수 없기 때문이다.
[수정]
JSON은 문자열, 숫자, 불리언, null, 배열, 객체와 같은 기본 JSON 자료형은 저장할 수 있지만, Product와 같은 사용자 정의 클래스 객체를 직접 저장할 수 없기 때문이다.
따라서 객체의 속성을 딕셔너리로 변환한 뒤 JSON으로 저장한다.

문제 2
JSON 파일을 json.load()로 읽었을 때 바로 Product 객체가 나오는가? 아니라면 어떤 형태의 값이 나오는가?
답: 특별한 설정을 하지 않는 한 Product 객첵 나오지 않고, 내용이 dictionary로 담긴 list 자료형으로 나온다.

문제 3
Product와 DownloadProduct를 복원할 때 상품 종류를 구분하기 위해 어떤 정보가 필요한가?
답: data["type"]

문제 4
프로그램 실행 중 메모리의 상품 목록에 상품을 추가했지만 JSON 파일에 저장하지 않았다. 프로그램을 종료하면 추가한 상품은 어떻게 되는가?
답: 메모리 상에서만 존재하던 상품은 프로그램 종료시 JSON 파일에 추가되지 않고 삭제된다.
[수정]
파일에 저장하지 않은 상품은 프로그램이 종료될 때 메모리에서 사라진다.
JSON 파일에는 해당 상품이 추가되지 않는다.

문제 5
JSON 파일에는 상품이 저장되어 있지만 프로그램 시작 시 파일을 읽지 않았다. 이때 메모리의 상품 목록은 어떤 상태인가?
답: 비어있다.

#---------------------------------------------------------------------------------------------
# 3단계: 실행 확인

다음 순서대로 실제로 실행한다.

일반 상품 한 개 등록
다운로드 상품 한 개 등록
JSON 파일 저장
프로그램 종료
프로그램 다시 실행
JSON 파일 복원
전체 상품 조회

예시는 그대로 복사하지 말고 본인이 값을 정한다.

일반 상품
이름: 마우스
가격: 10000

다운로드 상품
이름: 자료
가격: 50000
파일 크기: 5

#----------------------------------------------------------------------------------------------
# 4단계: 예상 결과와 실제 결과 기록

예상 결과는 지우지 않고 실제 결과 옆에 남긴다.

예상 결과:
일반 상품과 다운로드 상품이 각각 두 개씩 조회된다.

실제 결과:
실제 실행 후 확인한 내용을 작성한다.

=== 1. 전체 조회 ===
name: 키보드, price: 50000
name: 게임, price: 30000
file_size: 40
name: 마우스, price: 10000
name: 자료, price: 50000
file_size: 5
=== 2. '게임' 검색 ===
<__main__.DownloadProduct object at 0x7d41dbf79090>
=== 3. ' 게임 ' 검색 ===
<__main__.DownloadProduct object at 0x7d41dbf79090>
=== 4~5. '35000'으로 변경 + 타입 ===
True
35000 <class 'int'>
=== 6. '삼만원' 거부 ===
False
=== 7. 음수 거부 ===
False
=== 8. 키보드 삭제 ===
<__main__.Product object at 0x7d41dbf78f50>
3
=== 9. 저장 ===
=== 10~12. 새 매니저로 복원 ===
3
<class '__main__.DownloadProduct'>
35000
name: 게임, price: 35000
file_size: 40
name: 마우스, price: 10000
name: 자료, price: 50000
file_size: 5
<__main__.DownloadProduct object at 0x7d41dbfe1220>
True
<__main__.DownloadProduct object at 0x7d41dbfe1220>