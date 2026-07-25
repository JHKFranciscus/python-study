import json

FILE_NAME = "rebuild_books.json"


#파일 처리
def load_books():
    try:  
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            books = json.load(file)
            return books
    except FileNotFoundError: 
        return []  

    except json.JSONDecodeError:
        print("저장 파일의 JSON 형식이 올바르지 않아 빈 목록으로 시작합니다.")
        return []

def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

    return

#도서처리
def add_book(books):
    title = input("새 제목: ").strip()
    input_price = input("새 가격: ").strip()

    if title == "":
        print("제목을 입력해주세요.")
        return

    if not input_price.isdigit():
        print("가격은 0 이상의 정수로 입력해주세요.")
        return False

    price = int(input_price)

    new_book = {"title": title, "price": price}

    books.append(new_book)

    save_books(books)

    return True

def show_books(books):
    if books == []:
        print("도서가 존재하지 않습니다.")
    else:
        for book_number, book in enumerate(books, start=1):
            title = book["title"]
            price = book["price"]
            print(f"{book_number}. title: {title}, price: {price}원")

def search_books(books):
    keyword = input("검색어를 입력하세요: ").strip().lower()

    found = []

    if keyword == "":
        print("빈 칸은 검색할 수 없습니다.")
        return None

    for book in books:
        cleaned_title = book["title"].strip().lower()

        if keyword in cleaned_title:
            found.append(book)

    return found

def update_book_price(books):
    target_title = input("가격을 수정할 도서 제목을 입력하세요: ").strip()
    new_price_text = input("새 가격을 입력하세요: ").strip()

    if target_title == "":
        print("도서 제목은 비워 둘 수 없습니다.")
        return
    if not new_price_text.isdigit():
        print("가격은 0 이상의 정수로 입력해주세요.")
        return

    new_price = int(new_price_text)

    for book in books:
        if book["title"].lower() == target_title.lower():
            book["price"] = new_price
            save_books(books)

            print("도서 가격을 수정하고 파일에 저장했습니다.")
            return

    print("일치하는 도서를 찾지 못했습니다.")

def delete_book(books):
    target_title = input("삭제할 도서 제목을 입력하세요:").strip()

    if target_title == "":
        print("도서 제목은 비워 둘 수 없습니다.")
        return
    for index in range(len(books)):
        book = books[index]

        if book["title"].lower() == target_title.lower():
            deleted_book = books.pop(index)
            save_books(books)

            print(f"{deleted_book['title']} 도서를 삭제했습니다.")
            return

    print("일치하는 도서를 찾지 못했습니다.")



#사용자 입출력
books = load_books()

while True:
    print("=== JSON 도서 관리 프로그램 독립 재현 ===")
    print("1. 도서 추가")
    print("2. 전체 도서 조회")
    print("3. 제목 키워드 검색")
    print("4. 도서 가격 수정")
    print("5. 도서 삭제")
    print("0. 종료")

    menu = input("메뉴를 선택하세요: ")

    if menu == "1":
        add_book(books)

    elif menu == "2":
        show_books(books)

    elif menu == "3":
        found = search_books(books)

        # if found == "":
        if found is None:
            continue

        elif found == []:
            print("검색 결과가 없습니다.")
        else:
            for book in found:
                print(f"{book["title"]} / {book["price"]}원")
                
    elif menu == "4":
        update_book_price(books)

    elif menu == "5":
        delete_book(books)

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 번호를 입력해주세요")


# load_books()                → 파일 처리
# save_books(books)           → 파일 처리
# add_book(books)             → 도서 처리
# show_books(books)           → 도서 처리
# update_book_price(books)    → 도서 처리
# delete_book(books)          → 도서 처리
# while 메뉴 부분              → 사용자 입출력

# 코드를 보면서 다음 질문에 답한다.

# JSON 파일을 직접 여는 함수는 무엇인가?
# def load_books()
#[수정 후]
# save_books(books)
# 파일을 열지 않고 books 리스트만 처리하는 함수는 무엇인가?
# show_books(books)
#[수정 후]
# add_book(books), show_books(books), update_book_price(books), delete_book(books)
# 도서 처리 기능이 중심이지만 사용자 입출력도 섞여 있다.
# input()과 print()가 들어 있는 부분은 어디인가?
# while 메뉴 부분
#[수정 후]
# while 메뉴 부분과 add_book(), show_books(),
# update_book_price(), delete_book() 내부
# JSON 파일 이름을 바꾸면 현재 코드의 몇 군데를 수정해야 하는가?
# 1군데
# 메뉴 코드가 없어도 도서 추가·검색·수정·삭제 함수만 따로 호출할 수 있는가?
# 가능하다