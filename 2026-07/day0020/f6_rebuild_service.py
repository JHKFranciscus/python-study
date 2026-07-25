def add_book(books, title, input_price):
    title = title.strip()
    input_price = input_price.strip()

    if title == "":
        print("제목을 다시 입력해주십시오.")
        return False

    try:
        price = int(input_price)

    except ValueError:
        print("가격은 0 이상의 정수로 입력해주십시오.")
        return False

    if price < 0:
        print("가격은 0 이상의 정수로 입력해주세요")
        return False  #빼먹음

    new_book = {"title": title, "price": price}
    books.append(new_book)
    return True


def show_books(books):
    if len(books) == 0:
        print("도서가 존재하지 않습니다.")
    else:
        for book_number, book in enumerate(books, start=1):
            print(f"{book_number}. {book["title"]} / {book["price"]}원")


