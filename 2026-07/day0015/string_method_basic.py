# 문자열 메서드 기본 연습

original_title = "   Python Basic   "

#양쪽 공백 제거
cleaned_title = original_title.strip()

#대소문자 변경
lower_title = cleaned_title.lower()
upper_title = cleaned_title.upper()

#문자열 일부 교체
changed_title = cleaned_title.replace("Basic", "Programming")

print("원본 문자열:", original_title)
print("공백 제거:", cleaned_title)
print("소문자 변환:", lower_title)
print("대문자 변환:", upper_title)
print("문자열 교체:", changed_title)

#원본이 직접 변경되었는지 확인
print("처리 후 원본 문자열:", original_title)

#문자열 분리
book_data = "Python Basic,15000,홍길동"
book_parts = book_data.split(",")

print("분리 결과:", book_parts)
print("도서 제목:", book_parts[0])
print("가격:", book_parts[1])
print("저자:", book_parts[2])


# strip()을 사용했는데도 original_title에 공백이 남아 있는 이유는 무엇인가?
# original_title.strip()은 양쪽 공백이 제거된 새로운 문자열을 반환하는 메서드이다. 그 반환값을 clean_title에 저장햇으므로 original_title은 계속 기존 문자열을 가리킨다.
# cleaned_title.lower()의 결과 자료형은 무엇인가? 문자열 자료형 str
# book_data.split(",")의 결과 자료형은 무엇인가? 리스트 자료형 list

print("분리 결과의 자료형:", type(book_parts))
print("가격 원소의 자료형:", type(book_parts[1]))