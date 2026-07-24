import memo_storage
import memo_service

# FILE_NAME = "memos.json"

memos = memo_storage.load_memos()

while True:
    print()
    print("1. 메모 추가")
    print("2. 전체 메모 조회")
    print("3. 메모 검색")
    print("4. 프로그램 종료")

    menu = input("메뉴를 골라주세요: ")

    if menu == "1":
        text = input("저장할 메모를 입력해주세요: ")

        added = memo_service.add_memo(memos, text)

        # if added != False:
        #     memo_storage.save_memos(memos)
        #     print("메모 추가를 완료했습니다.")
        if added:
            memo_storage.save_memos(memos)
            print("메모 추가를 완료했습니다.")

    elif menu == "2":
        if len(memos) == 0:
            print("저장해 둔 메모가 없습니다.")
        else:
            for number, memo in enumerate(memos, start=1):
                # print(f"{number}. {memo}")
                print(f"{number}. {memo['text']}")

    elif menu == "3":
        keyword = input("찾을 검색어를 입력해주세요: ")

        # if found:
        #     found = memo_service.search_memos(memos, keyword)
        # else:
        #     print("검색어를 포함하는 항목을 찾지 못했습니다.")
        found = memo_service.search_memos(memos, keyword)

        if found is None:
            print("빈칸은 검색할 수 없습니다.")

        elif found ==[]:
            print("검색어를 포함하는 항목을 찾지 못했습니다.")

        else:
            for number, memo in enumerate(found, start=1):
                print(f"{number}. {memo['text']}")
                
        
    elif menu == "4":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 숫자를 입력하세요")


