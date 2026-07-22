def update_memo(file_name, target_title, new_content):
    with open(file_name, "r", encoding="utf-8") as file:
        memo_lines = file.readlines()

        found = False

        for index in range(len(memo_lines)):
            clean_line = memo_lines[index].rstrip("\n")
            title, category, content = clean_line.split("|")

            if target_title == title:
                # changed_line = "|".join(title, category, new_content)
                changed_line = "|".join([title, category, new_content]) + "\n"
                #
                memo_lines[index] = changed_line
                found = True
                break

    # if found:
    #     with open(file_name, "r", encoding="utf-8") as file:
    #         file.writelines(changed_line)

    #     print("변경을 완료했습니다.")
    # else:
    #     print(f"{target_title} 메모를 찾지 못했습니다.")
        if not found:
            return False

        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(memo_lines)

        return True


def delete_memo(file_name, target_title):
    # new_memo = []
    # found = False
    with open(file_name, "r", encoding="utf-8") as file:
        memo_lines = file.readlines()

        remaining_lines = []
        found = False

        for line in memo_lines:
            cleaned_line = line.rstrip("\n")
            title, category, content = cleaned_line.split("|")

            # if target_title == title:
            if title == target_title and not found:
                found = True
                continue

            # new_str = "|".join(title, category, content)
            # remaining_lines.append(new_str)
            remaining_lines.append(line)

    # if found:
    #     with open(file_name, "r", encoding="utf-8") as file:
    #         file.writelines(remaining_lines)
    #     print()
        if not found:
            return False
        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(remaining_lines)

        return True


file_name = "delete_test_memos.txt"

while True:
    print()
    print("1. 메모 수정")
    print("2. 메모 삭제")
    print("0. 종료")

    menu = input("메뉴를 선택하세요: ")

    if menu == "1":
        target_title = input("제목: ")
        new_content = input("새 내용: ")

        result = update_memo(file_name, target_title, new_content)

        if result:
            print(f"'{target_title}' 메모를 수정했습니다.")
        else:
            print(f"'{target_title}' 메모를 찾지 못했습니다.")

    elif menu == "2":
        target_title = input("삭제할 제목을 입력하세요: ")

        result = delete_memo(file_name, target_title)

        if result:
            print(f"'{target_title}' 메모를 삭제했습니다.")
        else:
            print(f"'{target_title}' 메모를 찾지 못했습니다.")

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴를 선택하세요.")