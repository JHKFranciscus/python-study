from pathlib import Path


file_path = Path("data/users.json")

print(file_path)
print(type(file_path))
#region
# 1. print(file_path)의 예상 결과는?
# Path('data/users.json')
#[수정 후]
#data/users.json
# 2. type(file_path)는 str일 것 같은가, Path와 관련된 객체 타입일 것 같은가?
# Path와 관련된 객체 타입
#[정확히 하면]
#<class 'pathlib.PosixPath'>
# 3. Path("data/users.json")을 실행한 것만으로 실제 data 폴더와 users.json 파일이 생성될 것 같은가?
# 아니다 file_path라는 객체가 생성될 뿐 폴더와 파일이 생성되지는 않는다.
# 4. 문자열 "data/users.json"을 그냥 저장하는 것과 Path("data/users.json")을 만드는 것은 어떤 차이가 있을 것 같다고 예상하는가?
# 문자열을 그냥 저장하는 것은 말 그대로 문자열을 변수에 저장하는 것이지만 객체를 만드는 것은 모르겠다.
#[수정 후]
#문자열은 경로 내용을 단순한 문자로 저장하지만, Path 객체는 경로를 나타내면서 경로를 확인하거나 파일명, 부모 경로, 확장자 등을 다루는 기능도 제공한다.
#endregion
print()
print(file_path.name)
print(file_path.parent)
print(file_path.suffix)
print(file_path.exists())
#region
# 1. file_path.name의 예상 결과는?
# data/users.json
#[수정 후]
#users.json
# 2. file_path.parent의 예상 결과는?
# data
# 3. file_path.suffix의 예상 결과는?
# users
#[수정 후]
#.json
# 4. file_path.exists()의 예상 결과는?
# False
# 5. exists()가 False라면, Path 객체 자체가 존재하지 않는다는 뜻일까 실제 파일이 존재하지 않는다는 뜻일까?
# 실제 파일이 존재하지 않는다는 뜻이다.
#endregion
print()
base_dir = Path("data")
json_path = base_dir / "users.json"

print(base_dir)
print(json_path)
print(json_path == Path("data/users.json"))
#region
# 1. print(base_dir)의 예상 결과는?
# data
# 2. print(json_path)의 예상 결과는?
# data/users.json
# 3. json_path == Path("data/users.json")의 예상 결과는?
# False
#[수정 후]
#True
# 4. 문자열끼리 "/"를 쓰는 것과 달리 Path 객체에서 "/"를 사용할 수 있는 이유는 무엇일 것 같은가?
# Python에서 그렇게 문법을 정해두었기 때문이다.
#Path 객체는 / 연산자가 경로를 이어 붙이도록 동작하게 구현되어 있기 때문이다.
#endregion
print()
base_dir.mkdir(exist_ok=True)

print(base_dir.exists())
print(base_dir.is_dir())
#region
# 1. mkdir() 실행 후 실제 day0034 폴더 안에 data 폴더가 생길 것 같은가?
# yes
# 2. print(base_dir.exists()) 예상 결과는?
# True
# 3. print(base_dir.is_dir()) 예상 결과는?
# True
# 4. Path("data")와 Path("data").mkdir()의 가장 큰 차이는 무엇인가?
# 전자는 "data"라는 이름을 가진 경로 객체를 만드는 것이라면 후자는 "data"라는 폴더를 경로에 만드는 것이다.
#[보완]
#Path("data")는 "data"라는 경로를 나타내는 Path 객체만 만든다. Path("data").mkdir()는 그 Path 객체가 가리키는 위치에 실제 data 디렉터리를 생성한다.
# 5. exist_ok=True는 왜 필요할 것 같은가?
# 이미 같은 이름의 파일이 존재한다면 그냥 그대로 두어라는 명령이다.
#[수정 후]
#같은 경로의 디렉터리가 이미 존재하더라도 FileExistsError를 발생시키지 않고 그대로 진행하도록 한다.
#endregion
print()
json_path.write_text("hello pathlib", encoding="utf-8")

print(json_path.exists())
print(json_path.is_file())
print(json_path.read_text(encoding="utf-8"))
#region
# 1. write_text() 실행 후 data/users.json 파일이 실제로 생성될 것 같은가?
# yes
# 2. print(json_path.exists()) 예상 결과는?
# True
# 3. print(json_path.is_file()) 예상 결과는?
# True
# 4. print(json_path.read_text(...)) 예상 결과는?
# hello pathlib
# 5. write_text()가 반환하는 것과 read_text()가 반환하는 것은 각각 무엇일 것 같은가?
# write_text()는 파일에 쓰는 것이 때문에 반환하는 것이 없지만, read_text()는 파일에서 불러오는 것이기 떄문에 파일의 문자열을 파이썬 문자열로 반환한다.
#[확인 후]
#write_text()는 파일에 쓴 문자 수를 int로 반환하고,
#read_text()는 파일으이 내용을 str로 반환한다.
#endregion