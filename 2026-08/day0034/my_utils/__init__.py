#region
# 1. __init__.py도 파이썬의 .py 파일인가?
# yes
# 2. __init__.py는 my_utils 폴더 안에 있으므로 my_utils 패키지와 관련된 파일일 것 같은가?
# yes
# 3. __init__.py는 어떤 역할을 할 것 같다고 예상하는가?
# package를 통해 처음 객체가 만들어질 때 초기 attribute 값을 지정한다.
#[수정 후]
#패키지가 import될 때 실행되는 초기화용 파일일 것 같다.
#endregion
print("my_utils 패키지 초기화")
#region
# 1. f4_package_main.py에서 my_utils 안의 모듈을 import하면 "my_utils 패키지 초기화"가 출력될 것 같은가?
# yes
# 2. 출력된다면 어느 시점에 출력될 것 같은가?
# 제일 먼저 실행된다
#[수정 후]
#my_utils 패키지가 처음 import되는 시점에 __init__.py가 실행된다. 따라서 패키지 안의 text_utils나 score_utils 모듈이 로드되기 전에 실행된다.
# 3. __init__.py가 빈 파일이었다면 화면에 특별히 출력되는 것이 있었을까?
# 없다
#endregion
from .text_utils import normalize_name
from .score_utils import get_average

# 1. 첫 번째 print 예상 결과:
# alice
# 2. 두 번째 print 예상 결과:
# 80.0
# 3. from .text_utils import normalize_name에서 앞의 .은 무엇을 뜻하는가?
# 현재 이 파일이 속해 있는 패키지
# 4. __init__.py에서 normalize_name을 import하면 왜 from my_utils import normalize_name이 가능해지는가?
# __init__.py에서 my_utils.text_utils.normalize_name를 연결시켰기 때문이다.
#[수정 후]
#__init__.py에서 text_utils의 normalize_name 함수 객체를 my_utils 패키지 namespace의 normalize_name이라는 이름에 연결했기 때문이다.
# 5. text_utils.py의 normalize_name 함수 객체와 my_utils.normalize_name이 가리키는 함수 객체는 같은 객체일 것 같은가, 다른 객체일 것 같은가?
# 같은 객체이다.







