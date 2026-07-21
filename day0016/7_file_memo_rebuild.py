def add_memo(file_path):
    # new_memo = input("새 메모: ")
    new_memo = input("새 메모: ").strip()

    if new_memo == "":
        print("공백은 저장되지 않습니다.")
    else:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{new_memo}\n")
            print("메모를 저장했습니다.")

def show_all_memos(file_path):
    # has_memo = 0
    has_memo = False

    with open(file_path, "r", encoding="utf-8") as file:
        for memo_number, line in enumerate(file, start=1):
            cleaned_line = line.strip()

            # if line != "":
            if cleaned_line != "":
                print(f"{memo_number}. {cleaned_line}")
                # has_memo += 1
                has_memo = True
        
    # if has_memo == 0:
    if has_memo == False:
        print("저장된 메모가 없습니다.")

def search_memos(file_path):
    keyword = input("검색할 단어를 입력하세요: ").strip().lower()
    
    # found_count = False
    found_count = 0

    if keyword == "":
        print("검색어를 입력해주세요")
        # return을 안 넣으면 일치하는 항목이 없습니다가 계속 뜬다.
        return

    else:
        with open(file_path, "r", encoding="utf-8") as file:
            # for memo_number, file in enumerate(file, start=1):
            for memo_number, line in enumerate(file, start=1):
                # cleaned_line = line.strip().lower()
                #line에는 이미 \n이 들어 있고 print()도 줄바꿈을 추가하므로 출력 줄 사이가 벌어질 수 있습니다.
                original_memo = line.strip()
                normalized_memo = original_memo.lower()

                # if cleaned_line == keyword:
                # if keyword in cleaned_line:
                if keyword in normalized_memo:
                    print(f"{memo_number}. {original_memo}")
                    # found_count = True
                    found_count +=1
    
    # if found_count == False:
    if found_count == 0:
        print("일치하는 항목이 없습니다.")


file_path = "rebuild_memos.txt"
    
with open(file_path, "a", encoding="utf-8"):
    pass

while True:
    print()
    print("전체메뉴")
    print("1. 메모 추가")
    print("2. 전체 메모 보기")
    print("3. 키워드 검색")
    print("4. 종료")
    
    # menu = int(input("번호를 선택해주세요: "))
    menu = input("번호를 선택해주세요: ")

    # if menu == 1:
    if menu == "1":
        add_memo(file_path)

    # elif menu == 2:
    elif menu == "2":
        show_all_memos(file_path)
    
    # elif menu == 3:
    elif menu == "3":
        search_memos(file_path)
    
    # elif menu == 4:
    elif menu == "4":
        print("종료합니다.")
        break

    else:
        print("번호에 있는 메뉴를 입력해주세요")