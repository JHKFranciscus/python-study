FILE_NAME = "review_memos.txt"

def add_memo(memo):
    # with open(FILE_NAME, "a", encoding="utf-8") as file:
    #     clean_memo = memo.strip()

    #     if clean_memo == "":
    #         print("공백은 저장할 수 없습니다.")
    #         return False

    #     file.write(clean_memo + "\n")
        
    #     return True
    clean_memo = memo.strip()

    if clean_memo == "":
        # print("공백은 저장할 수 없습니다.")
        return False

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(clean_memo + "\n")

    return True
#입력 정리 → 빈 값 검사 → 정상일 때만 파일 열기 → 저장
    
def load_memos():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            #memos = file.read()
            # memos = file.readlines()
            # return memos
            return file.readlines()

    except FileNotFoundError:
        # print("파일이 존재하지 않아 []로 시작합니다.")
        return []


def show_memo(memos):
    if len(memos) == 0:
        print("저장된 메모가 없습니다.")
        return False

    for memo_number, memo in enumerate(memos, start=1):
        clean_memo = memo.strip()

        if clean_memo == "":
            continue

        #print(f"{memo_number}. {memo}")
        print(f"{memo_number}. {clean_memo}")

    return True

def search_memos(memos, target_memo):
    # target_memo = target_memo.strip().lower()
    clean_target = target_memo.strip().lower()

    #if target_memo == "":
    if clean_target == "":
        print("공백은 검색되지 않습니다.")
        return False

    found = False

    for memo_number, memo in enumerate(memos, start=1):
        # memo = memo.strip().lower()
        clean_memo = memo.strip()

        #if target_memo in memo:
        if clean_target in clean_memo.lower():
            print(f"{memo_number}. {memo}")
            found = True

    if not found:
        print("검색 결과가 없습니다.")


memos = load_memos()

while True:
    print()
    print("1. 메모 추가")
    print("2. 전체 조회")
    print("3. 검색")
    print("4. 종료")

    menu = input("메뉴를 입력하세요: ")

    if menu == "1":
        memo = input("입력: ")

        added = add_memo(memo)

        if not added:
            print("공백은 저장할 수 없습니다.")
        else:
            print("메모 추가에 성공했습니다.")
            memos = load_memos()

    elif menu == "2":
        show_memo(memos)

    elif menu == "3":
        target_memo = input("검색어를 입력하세요: ")

        search_memos(memos, target_memo)

    elif menu == "4":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴를 입력해주세요.")
