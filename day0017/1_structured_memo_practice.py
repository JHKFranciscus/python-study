# 1번

memo_line = "파이썬 복습|공부|파일 읽기와 쓰기를 다시 확인한다"

memo_data = memo_line.split("|")

print(memo_data)
print(memo_data[0])
print(memo_data[1])
print(memo_data[2])


# 2번
print()
memo_data = [
    "파이썬 복습",
    "공부",
    "파일 읽기와 쓰기를 다시 확인한다"
]

memo_line = "|".join(memo_data)

print(memo_line)


# 3번
print()
# title = "파이썬 복습"
# category = "공부"
# content = "파일 읽기와 쓰기를 다시 확인한다"

title = "장보기"
category = "생활"
content = "우유와 계란을 산다"

memo_line = "|".join([title, category, content])

# with open("structured_memos.txt", "a", encoding="utf-8") as file:
#     file.write(memo_line + "\n")


# 4번
print()
with open("structured_memos.txt", "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.rstrip("\n")
        title, category, content = clean_line.split("|")

        print("제목:", title)
        print("분류:", category)
        print("내용:", content)
        print("-" * 20)