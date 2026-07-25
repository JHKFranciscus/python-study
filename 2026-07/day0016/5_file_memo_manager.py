def add_memo(file_path):
    memo = input("추가할 메모: ").strip()

    if memo == "":
        print("빈 메모는 저장할 수 없습니다.")
        return
    
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(memo + "\n")
    
    print("메모를 저장했습니다.")

def show_all_memos(file_path):
    has_memo = False
    
    with open(file_path, "r", encoding="utf-8") as file:
        for memo_number, line in enumerate(file, start=1):
            cleaned_meno = line.strip()

            if cleaned_meno != "":
                print(f"{memo_number}. {cleaned_meno}")
                has_memo = True
    
    if has_memo == False:
        print("저장된 메모가 없습니다.")

def search_memos(file_path):
    keyword = input("검색할 키워드: ").strip().lower()

    if keyword == "":
        print("빈 검색어는 사용할 수 없습니다.")
        return
    
    found_count = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for memo_number, line in enumerate(file, start=1):
            cleaned_memo = line.strip()

            if keyword in cleaned_memo.lower():
                print(f"{memo_number}. {cleaned_memo}")
                found_count += 1

    if found_count == 0:
        print("검색 결과가 없습니다.")


file_path = "memos.txt"

with open(file_path, "a", encoding="utf-8"):
    pass

while True:
    print()
    print("1. 메모 추가")
    print("2. 전체 메모 보기")
    print("3. 키워드 검색")
    print("4. 종료")

    menu = input("메뉴 선택: ").strip()

    if menu == "1":
        add_memo(file_path)

    elif menu == "2":
        show_all_memos(file_path)

    elif menu == "3":
        search_memos(file_path)
    
    elif menu == "4":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴를 입력하세요.")
#region
# 1. 프로그램을 종료한 뒤 다시 실행해도 메모가 남아 있는 이유는 무엇인가?
# 메모를 프로그램 내부의 변수에만 저장한 것이 아니라 memos.txt 파일에 저장했기 때문이다. 프로그램이 종료되어 변수는 사라져도 저장장치에 기록된 파일은 남는다.

# 2. 메모 저장에 w가 아니라 a 모드를 사용한 이유는 무엇인가?
# w를 설정값으로 하면 open시 파일 안의 내용만 길이를 0으로 잘라내고 새로운 내용을 저장하기 때문에

# 3. add_memo()에서 빈 문자열일 때 return을 실행하면 그 아래의 파일 쓰기 코드는 실행되는가?
# 함수 자체가 종료하여 실행되지 않는다.

# 4. show_all_memos()의 has_memo는 파일 내용 자체를 저장하는 변수인가? 아니면 어떤 상태를 나타내는 변수인가?
# has_memo는 파일 내용 자체를 저장하지는 않는다. 이것은 출력할 수 있는 비어 있지 않은 메모를 하나라도 발견해서 출력했는지를 나타내는 불리언 상태 변수이다.

# 5. 프로그램 시작 부분에서 a 모드로 파일을 열고 pass만 실행한 이유는 무엇인가?
# 처음 실행했을 때 memos.txt가 없더라도 a모드로 빈 파일을 생성하여 이후 r 모드에서 오류가 발생하지 않게 했다. 이미 파일이 있다면 기존 내용을 변경하지 않는다. pass는 이 단계에서 실제로 기록할 내용이 없기 때문에 사용했다.
#endregion
#region
# 1. 검색어와 메모 양쪽에 lower()를 적용한 이유는 무엇인가?
# 입력 정규화를 하여 대소문자가 달라도 같은 문자열로 검색할 수 있다.
# 2. cleaned_memo.lower()를 실행하면 cleaned_memo 원본이 소문자로 직접 변경되는가?
# 아니다. cleaned_memo에 새로 만들어진 소문자로 바뀐 문자열이 반환된다.
# 3. 키워드를 발견했는데도 break를 사용하지 않은 이유는 무엇인가?
# 일치하는 메모가 여러 개 있을 수 있으므로 첫 번째 결과를 발견한 뒤에도 파일의 마지막 줄까지 확인하기 위해
# 4. 메모가 n개일 때 키워드 검색을 O(n)이라고 보는 이유는 무엇인가?
# 메모가 n개일 떄 최악의 경우 첫 번째 메모부터 n번째 메모까지 모두 순차적으로 확인하므로 O(n)이라고 본다.
# 5. found_count는 검색된 메모 자체를 저장하는가, 아니면 어떤 정보를 저장하는가?
# 검색된 메모 문자열 자체를 저장하지는 않는다. 키워드와 일치한 메모가 몇 개인지를 정수로 저장한다.
#endregion