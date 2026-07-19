# 복습 1
books = [
    {"title": "파이썬 기초", "price": 15000},
    {"title": "자료구조 입문", "price": 20000}
]


def find_book(books, target_title):
    for book in books:
        if book["title"] == target_title:
            return book

    return None

# 질문
# 1. find_book(books, "파이썬 기초")가 반환하는 것은 제목 문자열인가, 딕셔너리인가?
# dicdtionary
# 2. 반환된 dictionary는 books 안의 원본 dictionary와 별개의 새로운 dictionary인가?
# books 안에 들어 있는 원본 dictionary와 같은 dictionary 객체이다.
# 3. 다음 코드를 실행하면 원본 books의 가격도 바뀌는가?
# 원본 books의 가격도 바뀐다.
# find_book()이 books 안의 원본 딕셔너리를 그대로 반환했고,
# found_book은 그 딕셔너리를 가리키기 때문이다.

found_book = find_book(books, "파이썬 기초")
found_book["price"] = 18000

# 4. 3번의 변경이 함수 호출이 끝난 뒤에도 유지되는 이유를 현재 이해한 방식으로 설명해라.
# find_book이 books안에 있는 원본 dictionary를 반환했다. found_book도 그 dictionary를 가리킨다. 함수호출이 끝나도 원본 dictionary는 books 안에 계속 존재하므로 found_book을 통해 변경한 내용도 원본에 남는다.
# 5. 다음처럼 작성하면 원본 books의 가격도 바뀌는가?
# books 안에 들어 있는 원본 dictionary와 다른 dictionary 객체이다.

found_book = find_book(books, "파이썬 기초").copy()
found_book["price"] = 18000

# 6. find_book()이 도서를 찾지 못했을 때 None을 반환하도록 한 이유는 무엇인가?
# 찾지 못했다는 것을 알리기 위해서


# 복습 2
book = {
    "title": "파이썬 기초",
    "price": 15000,
    "stock": 3
}

# 1. book["author"]를 실행하면 어떤 일이 발생하는가?
# KeyError가 발생한다.
# 2. book.get("author")를 실행하면 무엇이 반환되는가?
# None
# 3. book.get("author", "저자 정보 없음")을 실행하면 무엇이 반환되는가?
# None 저자 정보 없음
#[수정 후]
# 저자 정보 없음
# 4. 다음 반복문에서 key와 value에는 각각 무엇이 들어가는가?
for key, value in book.items():
    print(key, value)
# title 파이썬 기초
# price 15000
# stock 3
# 5. items()를 사용하지 않고 다음처럼 작성하면 book_info에는 무엇이 들어가는가?
for book_info in book:
    print(book_info)
# key 값만 들어간다.


# 복습 3 리스트 안 딕셔너리 CRUD 복습

# 1. 새로운 도서를 books의 마지막에 추가한다.
new_book = {
    "title": "알고리즘 첫걸음",
    "price": 18000
}

books.append(new_book)


# 2. books의 모든 도서 제목과 가격을 출력한다.
for book in books:
    print(book["title"], book["price"])


# 3. 제목이 "자료구조 입문"인 도서를 찾아 가격을 23000으로 수정한다.
for book in books:
    if book["title"] == "자료구조 입문":
        book["price"] = 23000
        break


# 4. 제목이 "파이썬 기초"인 도서를 찾아 삭제한다.
for book in books:
    if book["title"] == "파이썬 기초":
        books.remove(book)
        break

# 5. 3번에서 break를 사용한 이유는 무엇인가?
# 반복문을 종료하기 위해서
# 원하는 조건을 충족했으니 더 비교할 필요가 없어서
# 6. 4번에서는 딕셔너리 자체를 삭제하는가, 딕셔너리 안의 title 키만 삭제하는가?
# dictionary 자체를 삭제한다.
# 7. books.remove(book)는 무엇을 기준으로 삭제할 대상을 정하는가?
# books 리스트에서 book과 값이 같은 첫 번째 원소를 찾아 삭제한다.

#------------------------------------------------------------
# CS복습

# 복습 1. 순차 탐색과 비교 횟수
numbers = [12, 5, 27, 8, 19]


def find_number(numbers, target):
    comparison_count = 0

    for number in numbers:
        comparison_count += 1

        if number == target:
            return True, comparison_count

    return False, comparison_count

print(find_number(numbers, 12))
print(find_number(numbers, 8))
print(find_number(numbers, 19))
print(find_number(numbers, 100))
#region
# 1. 12를 찾을 때 비교 횟수: 1회
# 2. 8을 찾을 때 비교 횟수: 4회
# 3. 19를 찾을 때 비교 횟수: 5회
# 4. 100을 찾을 때 비교 횟수: 5회
# 5. 순차 탐색은 어떤 순서로 값을 확인하는가?
# iterable에 들어있는 순서대로 앞에서부터 확인한다.
#[수정 후]
# iterable 안의 첫 번째 원소부터 마지막 원소까지 차례대로 확인
# 6. 찾는 값이 리스트 첫 번째에 있으면 비교 횟수는 몇 번인가?
# 1회
# 7. 찾는 값이 리스트 마지막에 있으면 비교 횟수는 몇 번인가?
# 마지막 값의 순서만큼 횟수를 비교한다.
# 8. 찾는 값이 리스트에 없으면 비교 횟수는 몇 번인가?
# 리스트 안에 들어있는 값의 갯수만큼 비교한다.
# 9. 리스트 원소가 n개일 때 최악의 경우 시간복잡도가 O(n)인 이유는 무엇인가?
# 실행시간이 리스트 원소와 비교한 횟수에 비례하기 때문에 최악의 경우 n회를 비교해야하기 때문이다.
# 10. O(n)은 반드시 정확히 n번 실행된다는 뜻인가?
# 아니다. 데이터양(n)에 비례하여 실행시간이 길어진다는 이야기이다
#[수정 후]
# 반드시 n번 실행된다는 뜻은 아니다.
# 데이터 수(n)이 증가할 때 작업량이 대체로 n에 비례하여 증가한다는 뜻


# 복습 2 Git 작업 흐름
# 1. 현재 변경 파일과 저장소 상태 확인
# git status
# 2. 변경된 파일과 새 파일을 스테이징 영역에 추가
# git add -A
# 3. 스테이징된 변경 내용을 하나의 기록으로 저장
# git commit -m "메세지"
# 4. 로컬 저장소의 commit을 원격 저장소에 전송
# git push
# 5. git status와 git add -A는 같은 작업인가?
# 다른 작업이다
# 6. git add -A를 했다고 GitHub에 변경 내용이 올라가는가?
# 올라가지 않는다.
# 7. commit 메시지는 프로그램 실행 결과에 영향을 주는가?
# 영향을 주지 않는다.
# 8. git commit을 했지만 git push를 하지 않았다면 변경 내용은 어디까지 저장되어 있는가?
# git에 까지만 저장이 된다.
#[수정 후]
# 로컬 저장소의 commit 기록까지 저장되고, 
# 원격저장소인 GitHub에는 전송되지 않는다.
# 9. 마지막에 git status를 다시 확인하는 이유는 무엇인가?
# gitHub에 제대로 파일들이 전송되었는지 확인하기 위하여
#[수정 후]
# 아직 commit하지 않은 변경이나 스테이징되지 않은 파일이 남아 있는지,
# 현재 작업 폴더가 깨끗한 상태인지 확인하기 위해서다.
