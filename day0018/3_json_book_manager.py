import json

FILE_NAME = "managed_books.json"

# 시간 복잡도: O(n)
# JSON 파일 전체를 읽고 모든 도서를 복원한다.
def load_books():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            books = json.load(file)
            return books
    except FileNotFoundError:
        return[]

# 시간 복잡도: O(n)
# 현재 도서 목록 전체를 JSON 파일에 다시 기록한다.
def save_books(books):
    with open (FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
#region
# 파일 작동 확인
# books = load_books()

# print("불러온 도서 목록:", books)
# test_book = {
#     "title": "알고리즘 첫걸음",
#     "price": 18000
# }

# books.append(test_book)
# save_books(books)

# print("시험 도서를 저장했습니다.")
#endregion
# 시간 복잡도: O(n)
# append는 평균 O(1)이지만 save_books()가 O(n)이다.
def add_book(books):
    #제목과 가격 입력
    title = input("도서 제목을 입력하세요: ").strip()
    price_text = input("도서 가격을 입력하세요: ").strip()

    #입력값 검사
    if title == "":
        print("도서 제목은 비워 둘 수 없습니다.")
        return
    
    if not price_text.isdigit():
        print("가격은 0 이상의 정수로 입력해야 합니다.")
        return

    #new dictionary 생성
    price = int(price_text)

    new_book ={
        "title": title,
        "price": price
    }

    #메모리의 books에 추가
    books.append(new_book)
    #수정된 books 전체를 JSON 파일에 저장
    save_books(books)

    print("도서를 추가하고 파일에 저장했습니다.")

# 시간 복잡도: O(n)
# 모든 도서를 한 번씩 출력한다.
def show_books(books):
    if len(books) == 0 :
        print("저장된 도서가 없습니다.")
        return

    print()
    print("[전체 도서 목록]")

    for index in range(len(books)):
        book = books[index]

        print(
            f"{index + 1}. "
            f"제목: {book['title']}, "
            f"가격: {book['price']}원"
        )

# 시간 복잡도: O(n)
# 검색 결과를 모두 찾기 위해 모든 도서를 확인한다.
def search_books(books):
    #검색어 입력 및 정규화
    keyword = input("검색할 제목 키워드를 입력하세요: ").strip().lower()

    #빈 검사어 검색    
    if keyword == "":
        print("검색어는 비워 둘 수 없습니다.")
        return

    # 빈 검색 결과 리스트 생성
    matched_books = []

    #모든 도서 제목 순차 확인
    for book in books:
        normalized_title = book["title"].lower()

        #일치하는 도서를 결과 리스트에 추가
        if keyword in normalized_title:
            matched_books.append(book)

    #결과 없음 또는 검색 결과 출력
    if len(matched_books) == 0:
        print("검색 결과가 없습니다.")
        return

    print()
    print("[검색 결과]")

    for index in range(len(matched_books)):
        book = matched_books[index]

        print(
            f"{index + 1}."
            f"제목: {book['title']}, "
            f"가격: {book['price']}원"
        )








books = load_books()

while True:
    print()
    print("=== JSON 도서 관리 프로그램 ===")
    print("1. 도서 추가")
    print("2. 전체 도서 조회")
    print("3. 제목 키워드 검색")
    print("0. 종료")

    menu = input("메뉴를 선택하세요: ").strip()

    if menu == "1":
        add_book(books)

    elif menu == "2":
        show_books(books)

    elif menu == "3":
        search_books(books)

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴 번호를 입력하세요.")

    
