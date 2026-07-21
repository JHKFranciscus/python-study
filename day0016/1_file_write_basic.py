file_path = "study_notes.txt"

with open(file_path, "w", encoding = "utf-8") as file:
    file.write("파일 내용을 다시 작성했다.\n")
    file.write("문자열은 파일에 저장할 수 있다.\n")
    file.write("프로그램이 종료되어도 파일 내용은 남는다.\n")

print("저장 완료")