products = [
    {"name": "키보드", "price": 50000, "stock": 3},
    {"name": "마우스", "price": 30000, "stock": 0},
    {"name": "모니터", "price": 200000, "stock": 2},
    {"name": "USB", "price": 10000, "stock": 5},
    {"name": "헤드셋", "price": 80000, "stock": 1},
]

def discount_10(price):
    return price * 90 // 100


def discount_20(price):
   return price * 80 // 100

def select_discount(choice):
    if choice == "1":
        return discount_10

    elif choice == "2":
        return discount_20

    else:
        return None

def apply_discount(product, discount_function):
    return {
        "name": product["name"],
        "original_price": product["price"],
        "discounted_price": discount_function(product["price"]),
        }

selected_discount = select_discount("2")

sellable_products = filter(lambda product: product["stock"] > 0, products)

discounted_products = map(lambda product: apply_discount(product, selected_discount), sellable_products)

result = list(discounted_products)

print("선택된 할인 함수:", selected_discount.__name__)
print("결과 자료형:", type(result))

for product in result:
    print(
        product["name"],
        product["original_price"],
        "→",
        product["discounted_price"],
    )

print("원본 상품 목록:", products)
print("map 객체 재사용:", list(discounted_products))
#region
# 예상
# 1. selected_discount에는 무엇이 저장되는가?
# 답: discount_20이라는 이름을 가진 함수 객체
# 2. discount_20 함수가 실제로 실행되는 시점은 언제인가?
# 답: "discounted_price": discount_function(product["price"])에서 실행된다.
#[보완]
#discount_20dms selected_discount에 저장될 때 실행되지 않는다.
#result = list(discounted_products)가 map 객체의 값을 요청할 때, 재고가 있는 상품마다 apply_discount() 내부에서 실행된다.
# 3. sellable_products에는 어떤 객체가 저장되는가?
# 답: filter 객체가 저장된다.
# 4. discounted_products에는 어떤 객체가 저장되는가?
# 답: map 객체가 저장된다.
# 5. 결과에서 제외되는 상품은 무엇이며, 이유는 무엇인가?
# 답: 마우스는 filter 객체의 product["stock"] > 0라는 조건을 충족시키지 못하여 원본 객체에서 요소가 제외되었다.
#[수정]
#조건을 만족하지 못한 마우스를 다음 단계인 map으로 전달하지 않은 것이다.
# 6. 키보드의 할인 가격은 얼마인가?
# 답: 40000.0
# 7. 모니터의 할인 가격은 얼마인가?
# 답: 160000.0
# 8. USB의 할인 가격은 얼마인가?
# 답: 8000.0
# 9. 헤드셋의 할인 가격은 얼마인가?
# 답: 64000.0
# 10. 원본 products의 가격 값도 할인된 값으로 변경되는가?
# 답과 이유: map과 filter는 새로운 1회성 iterator 객체를 생성하기 때문에 원본의 가격은 변경되지 않는다.
#[수정]
#apply_discount()가 product[price"]에 새 값을 대입하지 않고, 할인 결과를 담은 새로운 distionary를 생성하여 반환하기 때문이다.
# 11. list(discounted_products)를 다시 실행한 결과는 무엇인가?
# 답: []
# 예상 출력 순서:
# 선택된 할인 함수: discount_20
# 결과 자료형: <class 'list>'
# 키보드 50000 → 40000.0
# 모니터 200000 → 160000.0
# USB 10000 → 8000.0
# 헤드셋 80000 →  64000.0
# 원본 상품 목록: [{"name": "키보드", "price": 50000, "stock": 3}, {"name": "마우스", "price": 30000, "stock": 0}, {"name": "모니터", "price": 200000, "stock": 2}, {"name": "USB", "price": 10000, "stock": 5}, {"name": "헤드셋", "price": 80000, "stock": 1}]
# map 객체 재사용: []
# 실제 출력:
# 선택된 할인 함수: discount_20
# 결과 자료형: <class 'list'>
# 키보드 50000 → 40000
# 모니터 200000 → 160000
# USB 10000 → 8000
# 헤드셋 80000 → 64000
# 원본 상품 목록: [{'name': '키보드', 'price': 50000, 'stock': 3}, {'name': '마우스', 'price': 30000, 'stock': 0}, {'name': '모니터', 'price': 200000, 'stock': 2}, {'name': 'USB', 'price': 10000, 'stock': 5}, {'name': '헤드셋', 'price': 80000, 'stock': 1}]
# map 객체 재사용: []
#endregion




















