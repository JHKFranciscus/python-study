file_path = "study_notes.txt"

with open(file_path, "r", encoding = "utf-8") as file:
    content = file.read()

print(content)

# 1. file.read()가 반환한 값의 자료형은 무엇인가?
# 문자열 자료형

# 2. with 블록이 종료되었는데도 content를 출력할 수 있는 이유는 무엇인가?
# with 블록이 종료되면서 file이 가리키는 파일 객체는 닫힌 상태가 되지만, file.read()가 반환한 문자열 객체는 content가 따로 가리키고 있으므로 with 블록 밖에서도 content를 사용할 수 있다.

# 3. r 모드로 파일을 열었을 때 study_notes.txt의 기존 내용은 지워지는가?
# r 모드는 기존 파일의 내용을 변경하지 않는다.