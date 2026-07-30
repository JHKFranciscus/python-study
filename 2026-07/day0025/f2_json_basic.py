import json


book = {
    "title": "파이썬 기초",
    "price": 20000,
    "available": True
}

json_text = json.dumps(
    book,
    ensure_ascii=False,
    indent=4
)

print(json_text)
print(type(json_text))

#region
# 1. json_text의 자료형은 dict인가, str인가?
# json.dumps를 사용하여 파이썬 객체를 JSON형태의 파이썬 문자열로 만들기 때문에 str이다.

# 2. 출력된 JSON에서 True는 True와 true 중 무엇으로 표시되는가?
# 직렬화를 했지만 역직렬화를 하지 않았으므로 JSON형식으로 출력되고, JSON형식에서는 True는 true로 표시된다.
#[수정 후]
# json.dumps()가 Python 데이터를 JSON 문자열로 직렬화하므로 Python의 True는 JSON의 true로 변환되어 표시된다.
#endregion
restored_book = json.loads(json_text)

print(restored_book)
print(type(restored_book))
print(restored_book["available"])
print(type(restored_book["available"]))
print()
#region
# 1. restored_book의 자료형은 무엇인가?
# JSON 문자열을 역직렬화하여 구조를 복구해서 dictionary 형태로 만들었다.
# 2. restored_book["available"]은 true와 True 중 무엇으로 출력되는가?
# json.loads()가 JSON 문자열을 Python 데이터로 바꿨으므로 True
# 3. restored_book["available"]의 자료형은 무엇인가?
# Boolena 자료형이다.
# 4. json_text와 restored_book은 모양이 비슷하지만 어떤 차이가 있는가?
# json_text는 JSON 문자열 형식, restored_book은 Python 자료 구조 형식을 하는 형식의 차이가 있다.
#[수정 후]
# json_text는 JSON 형식의 내용을 가진 str 자료형이고, restored_book은 Python에서 실제로 사용할 수 있는 dict 자료형이다.
# 따라서 restored_book은 키를 이용해 값을 조회하거나 변경할 수 있다.
#endregion
with open("book_data.json", "w", encoding="utf-8") as file:
    json.dump(
        book,
        file,
        ensure_ascii=False,
        indent=4
    )

with open("book_data.json", "r", encoding="utf-8") as file:
    loaded_book = json.load(file)

print(loaded_book)
print(type(loaded_book))
print(loaded_book["title"])
print(loaded_book["available"])
#region
# 1. book_data.json 파일은 어느 폴더에 생성되는가?
# 답: ~/projects/python-study/2026-07/day0025 ->경로를 따로 설정하지 않는다면 현재 위치한 폴더
#[수정 후]
#Python 파일이 있는 위치가 아니라, 명령을 실행한 터미널의 현재 위치를 기준으로 한다.
# 2. loaded_book의 자료형은 무엇인가?
# 답: dictionary형식이다.
# 3. book_data.json 안의 available 값은 True와 true 중 무엇으로 저장되는가?
# 답: true
# 4. json.dumps()와 json.dump()의 가장 큰 차이는 무엇인가?
# 답: json.dumps()는 파이썬 객체를 JSON 문자열로 변환만하고, json.dump()는 파이썬 객체를 JSON 문자열로 변환한 후에 file에 써 넣는다는 것이다.
#[보완]
# json.dumps()는 Python 객체를 JSON 형식의 str로 변환하여 반환한다.
# json.dump()는 Python 객체를 JSON 형식으로 변환하여 열린 파일에 직접 기록한다.
#endregion
