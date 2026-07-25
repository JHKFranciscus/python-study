file_name = "not_created_memos.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        memo_lines = file.readlines()

except FileNotFoundError:
    memo_lines = []
    print("메모 파일이 없어 빈 목록으로 시작합니다.")

print(memo_lines)