def update_memo(file_name, target_title, new_content):
    with open(file_name, "r", encoding="utf-8") as file:
        memos = file.readlines()

        found = False

        for index in range(len(memos)):
            cleaned_line = memos[index].strip("\n")
            title, category, content = cleaned_line.split("|")

            if title == target_title:
                # changed_line = "|".join(title, category, new_content) + "\n"
                changed_line = "|".join([title, category, new_content]) + "\n"
                memos[index] = changed_line
                found = True
                break

    # if found:
    #     with open(file_name, "r", encoding="utf-8") as file:
    #         file.writelines(changed_line)
    #         return True
    # else:
    #     print("검색어를 찾지 못함")
    #     return False
        if not found:
            return False

        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(memos)

        return True


def delete_memo(file_name, target_title):
    with open(file_name, "r", encoding="utf-8") as file:
        memos = file.readlines()

        found = False
        remaining_memo = []

        for line in memos:
            cleaned_line = line.strip("\n")
            title, category, content = cleaned_line.split("|")

            # if title == target_title:
            if title == target_title and not found:
                found = True
                continue

            # remaining_memo.append(cleaned_line + "\n")
            remaining_memo.append(line)

        # if found:
        #     with open(file_name, "r", encoding="utf-8") as file:
        #         file.writelines(remaining_memo)
        #         return True
        # else:
        #     print("검색어를 찾지 못함")
        if not found:
            return False
        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(remaining_memo)

        return True


file_name = "reproduction_memos.txt"

with open(file_name, "a", encoding="utf-8") as file:
    pass

while True:
    print("===전체목록===")
    print("1. 수정")
    print("2. 삭제")
    print("0. 종료")

    menu = input("메뉴를 입력해주세요: ")

    if menu == "1":
        target_title = input("제목: ")
        new_content = input("새 내용: ")
        # update_memo(file_name, target_title, new_content)
        result = update_memo(file_name, target_title, new_content)
        #아래 내용을 떠올리지 못함
        if result:
            print(f"'{target_title}' 메모를 수정했습니다.")
        else:
            print(f"'{target_title}' 메모를 찾지 못했습니다.")

    elif menu == "2":
        target_title = input("삭제 제목: ")
        #delete_memo(file_name, target_title)
        result = delete_memo(file_name, target_title)
        #아래 내용을 떠올리지 못함
        if result:
            print(f"'{target_title}' 메모를 삭제했습니다.")
        else:
            print(f"'{target_title}' 메모를 찾지 못했습니다.")

    elif menu == "0":
        print("프로그램을 종료합니다")
        break

    else:
        print("올바른 메뉴를 입력해주세요")






