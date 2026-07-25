# 1. 필요한 값 준비
target_title = input("타이틀을 입력하세요: ")
new_content = "우유와 휴지와 물을 산다"

with open("structured_memos.txt", "r", encoding="utf-8") as file:
    memo_lines = file.readlines()

found = False

# 2. 모든 줄을 순서대로 확인하기
for index in range(len(memo_lines)):
    clean_line = memo_lines[index].rstrip("\n")
    title, category, content = clean_line.split("|")

    if title == target_title:
        changed_line = "|".join([title, category, new_content]) + "\n"
        memo_lines[index] = changed_line
        found = True
        break

# 3. 찾았을 때만 파일에 저장하기
if found:
    with open("structured_memos.txt", "w", encoding="utf-8") as file:
        file.writelines(memo_lines)

    print(f"'{target_title}' 메모를 수정했습니다.")
else:
    print(f"'{target_title}' 메모를 찾지 못했습니다.")