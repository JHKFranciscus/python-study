def search_courses_by_keyword(courses, keyword):
    found_courses = []
    normalized_keyword = keyword.strip().lower()
    
    for course in courses:        
        normalized_course = course["title"].strip().lower()

        if normalized_keyword in normalized_course:
            found_courses.append(course)
    
    return found_courses




courses = [
    {"title": "Python Web Basic", "duration": 30},
    {"title": "Java Algorithm", "duration": 45},
    {"title": "Advanced Python", "duration": 50},
    {"title": "Database Basic", "duration": 40},
    {"title": "Web Programming", "duration": 35},
]

keyword = input("제목: ")

found_courses = search_courses_by_keyword(courses, keyword)

print("검색된 강의 수", len(found_courses))

if found_courses:
    for course in found_courses:
        print("제목:", course["title"])
        print(f"강의 시간: {course["duration"]}분")
              
else:
    print("검색 결과가 없습니다.")

# 1. 검색어와 강의 제목을 모두 lower()로 바꾸는 이유:
# 입력정규화를 하여 똑같은 문자열로 처리하여 비교하기 위해
# 2. 검색 결과가 여러 개일 수 있으므로 사용한 자료형:
# list 자료형
# 3. found_courses가 빈 리스트일 때 if found_courses의 결과:
# False
# 4. append(course)로 결과 리스트에 들어가는 것은 새 딕셔너리인가, 원본 딕셔너리를 가리키는 값인가:
# 원본 딕셔너리를 가리키는 값이다.
# 5. 이 검색 함수의 최악의 시간 복잡도:
# O(n)