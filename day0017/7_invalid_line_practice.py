file_name = "invalid_memos.txt"

valid_memos = []
invalid_count = 0
line_number = 0

with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        line_number += 1
        clean_line = line.rstrip("\n")

        # 빈 줄 또는 공백있는 줄 확인
        if clean_line.strip() == "":
            print(f"{line_number}번째 줄: 빈 줄을 건너뜁니다.")
            invalid_count += 1
            continue

        memo_data = clean_line.split("|")

        # 제목, 분류, 내용의 세 부분인지 확인
        if len(memo_data) != 3:
            print(f"{line_number}번째 줄: 형식이 잘못되어 건너뜁니다.")
            invalid_count += 1
            continue

        title, category, content = memo_data

        # 세 값 중 비어 있는 값이 있는지 확인
        if (title.strip() == "" or category.strip() == "" or content.strip() == ""):
            print(f"{line_number}번째 줄: 비어 있는 값이 있어 건너뜁니다.")
            invalid_count += 1
            continue

        valid_memos.append(memo_data)

print()
print("정상 메모")

for memo_data in valid_memos:
    title, category, content = memo_data

    print("제목:", title)
    print("분류:", category)
    print("내용:", content)
    print("-" * 20)

print("정상 메모 수:", len(valid_memos))
print("잘못된 줄 수:", invalid_count)