class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}원"


class Catalog:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def __iter__(self):
        return iter(self.products)


catalog = Catalog()

catalog.add(Product("키보드", 50000))    #Product("키보드", 50000)  =  객체
catalog.add(Product("마우스", 30000))
catalog.add(Product("모니터", 200000))

for product in catalog:            #product = 객체, catalog는 객체를 모아둔 객체
    print(product)
#region
# 예상 결과:
# 키보드 - 50000원
# 마우스 - 30000원
# 모니터 - 200000원

# 판단:
# - for문이 처음 catalog에 대해 사용하는 것은: def __iter__(self)
#iter(catalog)를 호출 -> catalog.__iter__()가 실행된다.
# - Catalog.__iter__()이 반환하는 것은: iter(catalog.products)
#list의 iterator 객체
# - 그 iterator가 실제로 반복하는 대상은: catalog.products
# - for문의 product에 차례대로 들어오는 것은 문자열인가 Product 객체인가: 모르겠다.
#Product 객체
# - print(product)에서는 Product의 어떤 특수 메서드가 사용되는가: __str__
#Product.__str__()
#endregion
print()
iterator = iter(catalog)

print(next(iterator))
print(next(iterator))
print(next(iterator))
#region
# 예상 결과:
# 키보드 - 50000원
# 마우스 - 30000원
# 모니터 - 200000원

# 판단:
# - iter(catalog)가 반환하는 것은: catalog 객체 iterator로 만든 것
#[수정]
#catalog.products의 list_iterator 객체
# - next(iterator)가 첫 번째로 반환하는 것은: catalog 객체 list의 첫번째 요소
#[수정]
#catalog.products의 첫 번째 Product 객체
# - next(iterator)가 반환한 값은 문자열인가 Product 객체인가: Product 객체
# - 그런데 화면에는 왜 "키보드 - 50000원"처럼 보일 것으로 예상하는가: Product 객체의 __str__이 실행되기 때문에
# - next(iterator)를 한 번 더, 총 4번째 호출하면 어떤 일이 생길 것으로 예상하는가: StopIteration이 작동하여 프로그램이 종료된다.
#[수정]
#StopIteration 예외가 발생하고, 현재 코드에서는 처리하지 않으므로 프로그램이 종료됨.
#endregion








