books = [{"title": "파이썬 기초", "price": 18000}, {"title": "자료구조 입문", "price": 22000}]

found_book = books[1]

print("수정 전 found_book:", found_book)
print("수정 전 books:", books)

found_book["price"] = 24000
print()

print("수정 후 found_book:", found_book)
print("수정 후 books:", books)

# found_book의 가격만 수정했는데 books 안의 가격도 바뀐 이유는 무엇인가?
# found_book에 books[1]을 삽입했으니까 found_book["price"]는 books[1]["price"]가 되기 때문이다.
# [수정]
# found_book = books[1]은 딕셔너리를 새로 복사한 것이 아니다.
# found_book와 books[1]이 같은 딕셔너리 객체를 가리키므로,
# found_book["price"]로 그 객체를 수정하면 books[1]에서도 변경된 값이 보인다.
# 부정확: found_book 안에 books[1]을 삽입했다.
# 정확: found_book가 books[1]과 같은 딕셔너리 객체를 가리키게 했다.