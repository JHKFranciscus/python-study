import f6_rebuild_storage
import f6_rebuild_service

books = f6_rebuild_storage.load_books()

while True:
    print()
    print("1. 도서 추가")
    print("2. 전체 도서 조회")
    print("3. 프로그램 종료")

    menu = input("메뉴를 입력해주세요: ")

    if menu == "1":
        title = input("새 도서: ")
        input_price = input("새 가격: ")

        added_book = f6_rebuild_service.add_book(books, title, input_price)

        if added_book:
            #f6_rebuild_storage.save_books()
            f6_rebuild_storage.save_books(books)
            print("도서 추가에 성공하였습니다.")

    elif menu == "2":
        # if len(books) == 0:
        #     print("도서가 존재하지 않습니다.")
        # else:
            # for book_number, book in enumerate(books, start=1):
            #     print(f"{book_number}. {book["title"]} / {book["price"]}원")
        f6_rebuild_service.show_books(books)

    elif menu == "3":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 번호를 입력해주세요.")
