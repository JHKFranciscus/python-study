# 1. 파일 전체 읽기
target_title = input("삭제할 제목을 입력하세요: ")

with open("delete_test_memos.txt", "r", encoding="utf-8") as file:
    memo_lines = file.readlines()

remaining_lines = []
found = False

# 2. 삭제할 줄을 제외하고 저장하기
for line in memo_lines:
    clean_line = line.rstrip("\n")
    title, category, content = clean_line.split("|")

    if title == target_title and not found:
        # and not found를 붙인 이유: 
        # 같은 제목의 메모가 여러 개 있어도 처음 발견한 메모 하나만 삭제하기 위해서다.
        #첫 번째 메모를 삭제하면 found가 True가 되므로, 이후 같은 제목의 메모는 remaining_lines에 저장된다.

        found = True
        continue

    remaining_lines.append(line)

# 3. 찾았을 때만 다시 저장하기
if found:
    with open("delete_test_memos.txt", "w", encoding="utf-8") as file:
        file.writelines(remaining_lines)

    print(f"'{target_title}' 메모를 삭제했습니다.")
else:
    print(f"'{target_title}' 메모를 찾지 못했습니다.")