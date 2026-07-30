# 문제 1번

DownloadProduct는 Product와 어떤 관계인가?
DownloadProduct는 Product이다.
이 문장이 맞는지 판단하고, is-a를 사용해 이유를 한 문장으로 작성한다.

# 답:
DownloadProduct는 Product와 상속관계이며, DownloadProduct is Product는 True이다.
왜냐하면 DownloadProduct는 Product의 한 종류이기 때문이다.


# 문제 2번

ProductManager는 Product와 어떤 관계인가?
ProductManager는 Product이다.
이 문장이 맞는지 판단하고, has-a를 사용해 이유를 한 문장으로 작성한다.

# 답:
객체 구성관계로, ProductManager is Product는 False이다.
왜냐하면 ProductManager는 Product의 객체를 attribute로 list에 가지고 있을 뿐이지, Product의 attribute나 method를 이어받은 것이 아니기 때문이다.

# 문제 3번

다음 코드에서 super().__init__(name, price)가 없다면 어떤 문제가 생기는지 작성한다.

```python
class DownloadProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size
```

#답:
이 코드에서 super().__init__(name, price)가 없다면 name과 price를 DownloadProduct attribute에 집어 넣는 코드를 중복 작성해야하는 문제가 생긴다.
#[수정 후]
#super().__init__(name, price)가 없고 self.name과 self.price도 직접 대입하지 않으면 DownloadProduct 객체에 name과 price 속성이 생성되지 않는다.
#따라서 해당 속성을 사용하는 메서드를 실행하면 AttributeError가 발생할 수 있다.
#이를 피하려면 self.name과 self.price를 자식 클래스에서 다시 대입해야 하므로 부모 클래스와 같은 초기화 코드가 중복된다.


# 문제 4번

부모와 자식 클래스에 같은 이름의 메서드가 있을 때 아래 코드는 어느 클래스의 메서드를 실행하는지 예상한다.

```python
product = DownloadProduct("게임", 30000, 50)
product.print_info()
```

#답:
자식 클래스의 instance가 메소드를 실행한다면 자식 클래스에서 먼저 메소드 탐색해 존재하면 실행하고 없다면 부모 클래스로 넘어가 메소드를 탐색한다.
#[추가]
#부모와 자식 클래스 모두 print_info()를 가지고 있다면, DownloadProduct.print_info()가 실행된다.
#자식 클래스에 print_info()가 없을 때만 Product.print_info()를 실행한다.