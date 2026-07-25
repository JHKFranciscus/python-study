original_book = {"title": "자료구조 입문", "price": 22000}

same_book = original_book

same_book["price"] = 24000

print("original_book:", original_book)
print("same_book:", same_book)


print()
original_book = {"title": "자료구조 입문", "price": 22000}

copied_book = original_book.copy()

copied_book["price"] = 24000

print("original_book:", original_book)
print("copied_book:", copied_book)

# 1. same_book의 가격을 바꿨을 때 original_book도 바뀐 이유는 무엇인가?
# same_book과 original_book이 같은 객체를 가리키고 있기 때문에 same_book을 통해 그 객체를 수정해도 original_book에서도 변경이 된다.
# 2. copied_book의 가격을 바꿨을 때 original_book은 바뀌지 않은 이유는 무엇인가?
# .copy()는 복사하는 변수가 가리키는 객체와 동일한 내용을 가진 새로운 dictionary객체를 생성하는 method이기 때문에 copied_book이랑 original_book은 서로 다른 객체를 가리킵니다. 따라서 copied_book를 통해 객체를 수정해도 original_book의 객체는 변경되지 않습니다.