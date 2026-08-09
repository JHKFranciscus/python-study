# 문제 1 — module과 package
다음 구조가 있다고 하자.

project/
│
├── main.py
│
└── calculator/
    ├── __init__.py
    ├── add.py
    └── multiply.py

add.py:
```python
def add(a, b):
    return a + b
```
1. 여기서 module은 무엇인가?
main.py, __init__.py, add.py, multiply.py
2. package는 무엇인가?
calculator/
3. main.py에서 add.py의 add 함수를 가져오려면 다음 import 문은 각각 무엇을 가져오는가?
A. import calculator.add
project/calculator/add.py
#[보완]
calculator.add 모듈

B. from calculator import add
__init__에 from .add import add가 적혀 있다는 전제 하에서는 project/calculator/add.py의 add 함수
#[수정]
#calculator package 안의 add 모듈

C. from calculator.add import add
project/calculator/add.py의 add 함수


# 문제 2 — import 후 호출 방법
다음 세 경우 각각 10 + 20을 계산하는 호출 코드를 적어라.

A
```python
import calculator.add
```
result = calculator.add.add(10, 20)

B
```python
from calculator import add
```
result = add.add(10, 20)

C
```python
from calculator.add import add
```
result = add(10, 20)


# 문제 3 — 가상환경과 requirements.txt
프로젝트 A
requests 2.x 필요

프로젝트 B
requests 3.x 필요


1. 두 프로젝트에 각각 가상환경을 만드는 이유는?
프로젝트 별로 다른 Python 버전을 사용하기 위해서
#[수정]
프로젝트마다 패키지와 버전을 독립적으로 관리하여 서로 충돌하지 않도록 하기 위해서
2. 가상환경 자체를 GitHub에 올리는 대신 requirements.txt를 저장하는 이유는?
타인의 컴퓨터에서 가상환경을 생성하여 그 곳에 install하기 위애서
#[수정]
가상환경 폴더 자체를 공유하지 않고, 필요한 패키지 목록과 버전을 기록하여 다른 환경에서 다시 설치할 수 있게 한다.
3. 다음 명령은 각각 무엇을 하는가?

   pip freeze > requirements.txt
pip freeze를 사용하면 목록이 생성되는데 그 목록을 > 을 실행하면 우측에 있는 requirements.txt에 문자열로 생성이 된다는 뜻이다. 우측의 파일이 존재하지 않을 경우 우측파일을 생성해서 작성한다.
#[수정]
현재 환경에 설치된 패키지와 버전 목록을 requirements.txt에 기록한다.
   pip install -r requirements.txt
requirements.txt에 있는 목록을 컴퓨터에 설치하고 실행할 준비를 마쳐준다는 뜻이다.
#[수정]
requirements.txt.에 적힌 패키지들을 설치한다.

# 문제 4 — pathlib
```python
from pathlib import Path

base = Path("data")
file_path = base / "students" / "scores.json"

print(base)
print(file_path)
print(file_path.name)
print(file_path.suffix)
print(file_path.parent)
```
1. Linux/WSL 기준 예상 출력 5줄을 적어라.
data
data.students.scores.json
scores.json
.json
data
#[수정]
data
data/students/scores.json
scores.json
.json
data/students
2. Path를 사용해서 경로를 만들 때 "data/students/scores.json"이라는 문자열 하나를 직접 만드는 것과 비교해 / 연산자를 사용하는 장점은 무엇인가?
없는 것 같은데? data를 놔두고 뒤에 것만 계속 바꿔준다고 해도 어차피 변수 만들 때 마다 base/파일명/파일명.json 계속 써줘야되는데 그러면  data/파일명/파일명.json을 쓰는 것 하고 뭔 차이가 있냐?
#[수정]
경로의 각 부분을 나누어 조립할 수 있고, 운영체제에 맞는 경로 형식으로 처리해준다.
