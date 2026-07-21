file_path = "study_notes.txt"

with open(file_path, "r", encoding = "utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        cleaned_line = line.strip()
        print(f"{line_number}번째 줄: {cleaned_line}")

# 1. 반복문에서 line의 자료형은 무엇인가?
# 문자열 자료형

# 2. line에 이미 \n이 들어 있을 수 있는데 print(line)을 사용하면 줄 사이가 벌어지는 이유는 무엇인가?
# 줄바꿈 문자와 print()자체의 줄바꿈이 합쳐져서 줄바꿈이 2번 발생하기 때문이다.

# 3. line.strip()은 원본 line 문자열을 직접 변경하는가, 아니면 새로운 문자열을 반환하는가?
# 새로운 문자열을 반환한다.

# 4. read()와 파일 객체를 for문으로 순회하는 방식의 차이는 무엇인가?
# read()는 파일 객체 내용을 한번에 읽어서 하나의 문자열로 반환하지만, for문으로 순회하면 한 줄씩 문자열로 읽는다.