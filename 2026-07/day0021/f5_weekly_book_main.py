import json
import f5_weekly_book_storage
import f5_weekly_book_service

# books = f5_weekly_book_storage.load()

# if books is True:
#     books = f5_weekly_book_storage.load()

# elif books is None:
#     print("파일이 존재하지 않습니다.")
#     books = []

# elif books is False:
#     print("잘못 된 값이 들어있습니다.")
#     books = []
try:
    books = f5_weekly_book_storage.load()

except FileNotFoundError:
    print("파일이 존재하지 않습니다. 빈 목록으로 시작합니다.")
    books = []

except json.JSONDecodeError:
    print("JSON 형식이 잘못되었습니다. 빈 목록으로 시작합니다.")
    books = []

while True:
    print()
    print("1. 전체 조회")
    print("2. 도서 추가")
    print("3. 제목 검색")
    print("4. 가격 수정")
    print("5. 도서 삭제")
    print("6. 종료")

    menu = input("메뉴: ")

    if menu == "1":
        all_books = f5_weekly_book_service.get_all_books(books)

        # if found:
        #     for book_number, book in enumerate(books, start=1):
        #         print(f"{book_number}. {book["title"]} / {book["price"]}원")
        # else:
        #     print("도서가 존재하지 않습니다.")
        if len(all_books) == 0:
            print("도서가 존재하지 않습니다.")
        else:
            for book_number, book in enumerate(all_books, start=1):
                print(f"{book_number}. {book['title']} / {book['price']}원")

    elif menu == "2":
        title = input("새 제목: ")
        price = input("새 가격: ")

        try:
            price = int(price)

        except ValueError:
            print("가격은 숫자로 입력해주세요.")
            continue

        added_book = f5_weekly_book_service.add_book(books, title, price)

        if added_book:
            f5_weekly_book_storage.save(books)
            print("도서 추가에 성공하였습니다.")
            # books = f5_weekly_book_storage.load()

        else:
            print("빈칸은 추가하지 않습니다.")



    elif menu == "3":
        target_title = input("검색할 도서를 입력하세요: ")

        found_books = f5_weekly_book_service.find_book(books, target_title)

        # if found:
        #     for book_number, book in enumerate(books, start=1):
        #         if target_title in book["title"]:
        #             print(f"{book_number}. {book["title"]}, {book["price"]}원")
        if len(found_books) == 0:
            print("검색 결과가 없습니다.")
        else:
            for book_number, book in enumerate(found_books, start=1):
                print(f"{book_number}. {book['title']}, {book['price']}원")

    elif menu == "4":
        target_title = input("바꿀 책 제목: ")
        # changed_price = input("새 가격: ")

        try:
            changed_price = int(input("새 가격: "))

        except ValueError:
            print("가격은 숫자로 입력해주세요.")
            continue


        update = f5_weekly_book_service.update_book_price(books, target_title, changed_price)

        if update:
            f5_weekly_book_storage.save(books)
            print("변경 성공")
            # books = f5_weekly_book_storage.load()
        else:
            print("변경 실패")


    elif menu == "5":
        target_title = input("삭제할 책 제목을 입력해주세요: ")

        deleted_book = f5_weekly_book_service.delete_book(books, target_title)

        if deleted_book:
            f5_weekly_book_storage.save(books)
            print("삭제 성공")
            # books = f5_weekly_book_storage.load()
        else:
            print("삭제 실패")

    elif menu == "6":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 번호를 입력하세요.")