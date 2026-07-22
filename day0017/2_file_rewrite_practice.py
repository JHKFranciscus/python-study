# 1.파일 전체를 리스트로 읽기
with open("structured_memos.txt", "r", encoding="utf-8") as file:
    memo_lines = file.readlines()

print(memo_lines)
print(memo_lines[0])
print(memo_lines[1])

# 2. 리스트의 두 번째 줄 수정하기
print()
memo_lines[1] = "장보기|생활|우유와 휴지를 산다\n"

print("수정된 리스트")
print(memo_lines)

# 3. 수정된 리스트를 파일에 다시 저장하기
print("\n3. 파일에 다시 저장")
with open("structured_memos.txt", "w", encoding="utf-8") as file:
    file.writelines(memo_lines)

# 4. 실제 수정 결화 확인하기
print()
print("파일 수정 후")

with open("structured_memos.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip("\n"))