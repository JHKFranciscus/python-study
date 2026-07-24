def add_book(books, title, input_price):
    title = title.strip()
    input_price = input_price.strip()
    
    if title == "":
        print("제목을 입력해주세요.")
        return False

    if not input_price.isdigit():
        print("가격은 0 이상의 정수로 입력해주세요.")
        return False

    price = int(input_price)

    new_book = {"title": title, "price": price}

    books.append(new_book)

    return True

def show_books(books):
    if books == []:
        print("도서가 존재하지 않습니다.")
    else:
        for book_number, book in enumerate(books, start=1):
            title = book["title"]
            price = book["price"]
            print(f"{book_number}. title: {title}, price: {price}원")

def search_books(books, keyword):
    keyword = keyword.strip().lower()

    if keyword == "":
        return None

    found = []

    for book in books:
        cleaned_title = book["title"].strip().lower()

        if keyword in cleaned_title:
            found.append(book)

    return found

def update_book_price(books, target_title, new_price_text):
    target_title = target_title.strip()
    new_price_text = new_price_text.strip()

    if target_title == "":
        print("도서 제목은 비워 둘 수 없습니다.")
        return False
    
    if not new_price_text.isdigit():
        print("가격은 0 이상의 정수로 입력해주세요.")
        return False

    new_price = int(new_price_text)

    for book in books:
        if book["title"].lower() == target_title.lower():
            book["price"] = new_price
            return True

    print("일치하는 도서를 찾지 못했습니다.")
    return False

def delete_book(books, target_title):
    target_title = target_title.strip()

    if target_title == "":
        print("도서 제목은 비워 둘 수 없습니다.")
        return False
    
    for index in range(len(books)):
        book = books[index]

        if book["title"].lower() == target_title.lower():
            books.pop(index)
            return True

    print("일치하는 도서를 찾지 못했습니다.")
    return False