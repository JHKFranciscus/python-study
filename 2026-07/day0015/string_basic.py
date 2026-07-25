#문자열 기본 연습
book_title = "Python Basic"

#문자열 인덱스 확인
print("첫 번째 문자:", book_title[0])
print("두 번째 문자:", book_title[1])
print("마지막 문자:", book_title[-1])

#문자열 슬라이싱 확인
print("앞부분:",book_title[:6])
print("뒷부분:",book_title[7:])
print("중간 부분:", book_title[1:5])

#문자열의 길이 확인
print("문자열 길이:", len(book_title))

#새로운 문자열 생성
changed_title = "J"  + book_title[1:]

print("원본 문자열:", book_title)
print("새로운 문자열:", changed_title)