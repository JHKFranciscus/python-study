# 직렬화·역직렬화·메모리와 파일의 차이

## 문제 1. 직렬화와 역직렬화

### 1
직렬화란 무엇인가?
답: 파이썬 객체를 JSON 형식 파일로 바꾸는 과정
[수정]
답: 메모리에 있는 Python 데이터를 저장하거나 전송할 수 있는 JSON 등의 형식으로 변환하는 과정이다.

### 2
역직렬화란 무엇인가?
답: JSON 형식 파일을 파이썬 객체로 되돌리는 과정
[수정]
답: JSON 형식의 문자열이나 파일 데이터를 Python의 list, dict, str, int 등의 자료형으로 변환하는 과정이다.

### 3
Python의 `Product` 또는 `DownloadProduct` 객체를 `json.dump()`에 그대로 전달할 수 없는 이유는 무엇인가?
답: 그 객체의 형식이 class 형식이라서 직렬화를 할 수 없는 형식이었기 때문이다.
[수정]
답: json 모듈은 dict, list, str, int, float, bool, None과 같은 기본 자료형은 처리할 수 있지만, 사용자가 만든 Product 클래스의 인스턴스를 어떤 JSON 구조로 바꿔야 하는지는 알 수 없기 때문이다.

### 4
오늘 프로그램에서 객체를 JSON 파일에 저장하기 전에 `to_dict()`를 호출한 이유는 무엇인가?
답: 객체를 dict 자료형을 요소로 가지고 있는 list 자료형을 만들어 직렬화를 가능하게 하기 위해서
[수정]
답: json 모듈이 처리할 수 없는 Product 계열 객체를, 처리할 수 있는 dict로 변환하고 그 dict들을 list에 담아 저장하기 위해서이다.

## 문제 2. 메모리와 파일의 차이
다음 코드가 실행되었다.
```python
manager = ProductManager("managed_products.json")

product = manager.search_product("게임")
product.price = 40000
```
아직 다음 코드는 실행하지 않았다.
manager.save()

1. 변경된 product 객체는 현재 어디에 존재하는가?
답: 메모리 상에 있는 객체에 존재한다.

2. product.price = 40000을 실행하면 managed_products.json의 가격도 즉시 40000으로 변경되는가?
답: 아니다. manager.save()를 실행시켜야지만 managed_products.json의 가격도 변경된다.

3. 그렇지 않다면 메모리의 객체와 JSON 파일의 데이터가 자동으로 함께 변경되지 않는 이유는 무엇인가?
답: 메모리의 객체가 바뀌면 JSON 파일의 데이터가 자동으로 바뀌게 코드를 안 짜놔서 
[수정]
답: 메모리의 객체와 디스크의 JSON 파일은 서로 다른 저장 공간에 존재하는 별개의 데이터이기 때문이다. 메모리의 객체를 변경하는 것은 파일 입출력 작업이 아니므로, save()를 호출하여 파일을 다시 쓰기 전에는 JSON 파일이 변경되지 않는다.

4. 이 상태에서 프로그램을 종료하면 메모리에서 변경한 가격 40000은 유지되는가?
답: 유지되지 않는다. 파일에 다시 작성을 해야지만 유지가 되는데 이 상태에서 종료하면 파일에 다시 작성을 하지 않고 종료를 하는 것이기 때문이다.

5. 프로그램을 다시 실행하면 상품 가격은 메모리에서 변경했던 40000과 JSON 파일에 저장돼 있던 가격 중 무엇으로 복원되는가?
답: JSON 파일에 저장돼 있던 가격으로 복원이 된다.

6. 가격 40000을 프로그램 종료 후에도 유지하려면 어떤 작업을 해야 하는가?
답: json.dump(products)를 하여 JSON 파일에 가격을 저장해 줘야한다.
[수정]
답: manager.save()를 호출해야 한다. save() 내부에서 각 객체를 to_dict()로 변환한 뒤 json.dump()를 사용하여 JSON 파일을 다시 기록한다.

## 문제 3. 저장과 불러오기 흐름

다음 빈칸을 채운다.

저장 과정

Product 계열 객체 목록
→ 각 객체의 (to_dict()) 호출
→ dict들을 담은 list
→ (json.dump())로 직렬화
→ JSON 파일에 기록

불러오기 과정

JSON 파일의 텍스트
→ (json.load())로 역직렬화
→ dict들을 담은 list
→ (create_product_from_dict()) 함수 호출
→ Product·DownloadProduct 객체 목록

## 문제 4. 마지막 구분

다음 두 문장의 차이를 설명한다.

문장 A
json.load()가 JSON 파일의 텍스트를
Python의 list와 dict로 역직렬화했다.

문장 B
create_product_from_dict()가 딕셔너리를 이용해
새로운 Product 계열 객체를 생성했다.

답: 문장 A는 JSON 파일의 텍스트를 그냥 역직렬화하여 list 자료형으로 만들고 안에 dict 자료형의 요소를 담고 있는 파이썬 객체를 만들었다는 것이다. 문장 B는 그 dict 자료형을 클래스 인스턴스로 만들어서 list안에 Product 계열 instance를 요소로 담고 있는 파이썬 객체를 만들었다는 것이다.
[수정]
답: 문장 A의 json.load()는 JSON 파일의 데이터를 Python의 list와 dict로 역직렬화할 뿐이며 Product 인스턴스를 만들지는 않는다. 문장 B의 create_product_from_dict()는 dict에 들어 있는 type, name, price 등의 값을 사용하여 새로운 Product 또는 DownloadProduct 인스턴스를 생성한다. 따라서 역직렬화와 사용자 정의 클래스 객체 복원은 서로 다른 단계이다.