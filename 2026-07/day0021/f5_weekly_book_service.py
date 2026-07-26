def add_book(books, title, price):
    title = title.strip()

    if title == "":
        return False
    # try:
    #     price = int(price)

    # except ValueError:
    #     return None

    new_book ={"title": title, "price": price}

    books.append(new_book)
    return True

def get_all_books(books):
    # if len(books) == 0:
    #     return False

    # return True
    return books

def find_book(books, target_title):
    # target_title = target_title.strip()

    # found = False

    # for index in range(len(books)):
    #     book = books[index]

    #     if target_title in book["title"]:
    #         found = True

    # return found
    clean_target = target_title.strip().lower()

    if clean_target == "":
        return []

    found_books = []

    for book in books:
        clean_book_title = book["title"].strip().lower()

        if clean_target in clean_book_title:
            found_books.append(book)

    return found_books


def update_book_price(books, target_title, changed_price):
    # target_title = target_title.strip()
    # changed_price = changed_price.strip()

    # for index in range(len(books)):
    #     book = books[index]

    #     try:
    #         changed_price = int(changed_price)
    #     except ValueError:
    #         return None

    #     if target_title == book["title"]:
    #         book["price"] = changed_price
    #         return True

    # return False
    clean_target = target_title.strip().lower()

    for book in books:
        clean_book_title = book["title"].strip().lower()

        if clean_target == clean_book_title:
            book["price"] = changed_price
            return True

    return False

def delete_book(books, target_title):
    # target_title = target_title.strip()

    # for index in range(len(books)):
    #     book = books[index]

    #     if target_title == book["title"]:
    #         # books.pop(book)
    #         books.pop(index)
    #         return True

    # return False
    clean_target = target_title.strip().lower()

    for index in range(len(books)):
        clean_book_title = books[index]["title"].strip().lower()

        if clean_target == clean_book_title:
            books.pop(index)
            return True

    return False