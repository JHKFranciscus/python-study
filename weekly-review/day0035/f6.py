from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int
#region
# products에는 Product 객체 여러 개가 들어 있다고 가정한다.

# products에는 무엇이 들어 있는가?
# Product 객체 여러 개
# product에는 무엇이 들어 있는가?
# product가 Product 객체 1개라면 product에는 field가 들어있다.
# 가격을 확인할 때 products.price와 product.price 중 무엇을 써야 하는가?
# product.price를 써야한다.
#endregion
#region
#--------------------------------------------------------------------------
# products에서 price >= min_price인 Product를 하나씩 yield하는
# expensive_products(products, min_price) generator 함수를 직접 작성한다.
#endregion
def expensive_products(products, min_price):
    for product in products:
        if product.price >= min_price:
            yield product
#region
#---------------------------------------------------------
# 1. map()의 두 번째 인수 products에는 무엇이 들어 있는가?
# Product 객체 여러 개
# 2. map()의 첫 번째 인수에는 값과 함수 중 무엇이 들어가야 하는가?
# 함수
# 3. lambda가 Product 객체 하나를 product라는 이름으로 받는다면,
#    product에서 name을 꺼내 반환하는 식은 무엇인가?
#lambda product: product.name

# def get_names(products):
#     return list(map(lambda product: product.name, products))
#endregion
#region
#-----------------------------------------------------------------
# 1. get_names는 호출할 때 어떤 값을 인수로 받는가?
# product
#수정: products
# 2. wrapper가 get_names를 대신하게 된다면
#    wrapper도 무엇을 매개변수로 받아야 하는가?
# 이것만 주고 무슨 소리인지 알라고 하라고?
#products
# 3. func(products)를 실행한 결과를
#    나중에 다시 반환하려면 무엇에 저장해야 하는가?
# 모른다.
#result = func(products)처럼 변수에 저장한다.
#endregion
def trace(func):
    def wrapper(products):
        print("처리 시작")
        result = func(products)
        print("처리 끝")
        return result

    return wrapper

@trace
def get_names(products):
    return list(map(lambda product: product.name, products))


products = [
    Product("키보드", 50000),
    Product("마우스", 30000),
    Product("모니터", 200000)
]

print(get_names(products))
# 예상 결과:
# [키보드, 마우스, 모니터]
# 수정 후 예상:
# 처리 시작
# 처리 끝
# ['키보드', '마우스', '모니터']











