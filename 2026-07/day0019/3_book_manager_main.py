import book_storage
import book_service


books = book_storage.load_books()

while True:
    print()
    print("1. 도서 추가")
    print("2. 전체 도서 조회")
    print("3. 도서 검색")
    print("4. 도서 가격 수정")
    print("5. 도서 삭제")
    print("6. 프로그램 종료")

    menu = input("번호를 입력하세요: ")

    if menu == "1":
        title = input("새 제목: ")
        input_price = input("새 가격: ")

        added = book_service.add_book(books, title, input_price)

        if added:
            book_storage.save_books(books)
            print("도서가 추가되었습니다.")

    elif menu == "2":
        book_service.show_books(books)

    elif menu == "3":
        keyword = input("검색어를 입력하세요: ")

        found_books = book_service.search_books(books, keyword)

        if found_books is None:
            print("빈칸은 검색할 수 없습니다.")
        elif found_books == []:
            print("검색 결과가 없습니다.")
        else:
            for book_number, book in enumerate(found_books, start=1):
                title = book["title"]
                price = book["price"]

                print(f"{book_number}. title: {title}, price: {price}원")

    elif menu == "4":
        target_title = input("가격을 수정할 도서 제목을 입력하세요: ")
        new_price_text = input("새 가격을 입력하세요: ")

        updated = book_service.update_book_price(books, target_title, new_price_text)

        if updated:
            book_storage.save_books(books)
            print("도서 가격이 수정되었습니다.")
            
    elif menu == "5":
        target_title = input("삭제할 도서 제목을 입력하세요:")

        deleted = book_service.delete_book(books, target_title)

        if deleted:
            book_storage.save_books(books)
            print("도서가 삭제되었습니다.")

    elif menu == "6":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 번호를 입력해주세요.")


    