# import my_utils.text_utils
# import my_utils.score_utils


# name = "  Alice  "
# scores = [70, 80, 90]

# print(my_utils.text_utils.normalize_name(name))
# print(my_utils.score_utils.get_average(scores))
#region
# 1. 첫 번째 print의 예상 결과:
# alice
# 2. 두 번째 print의 예상 결과:
# 80.0
# 3. import my_utils.text_utils에서 my_utils와 text_utils는 각각 무엇인가?
# my_utils는 패키지이고 text_utils는 모듈이다.
# 4. 왜 text_utils.normalize_name(name)이 아니라 my_utils.text_utils.normalize_name(name)이라고 쓰는가?
# text_utils가 같은 폴더 내에 존재하지 않아 어디 존재하는지 확인하지 못하므로 my_utils폴더 안의 text_utils이라는 것을 알려주기 위해서이다.
#[수정 후]
#import 방식으로 가져왔기 때문에 현재 파일에서는 my_utils를 통해 그 안의 text_utils 모듈에 접근해야 한다.
#따라서 my_utils.text_utils.normalize_name(name)이라고 쓴다.
# 5. my_utils.text_utils라는 점(.)으로 이어진 표현은 무엇을 나타낸다고 생각하는가?
# 앞의 것 안의 뒤의 것이라는 것을 나타낸다
#[수정 후]
#패키지 안의 모듈이라는 import 경로를 나타낸다.
#endregion
# from my_utils.text_utils import normalize_name
# from my_utils.score_utils import get_average


# name = "  Alice  "
# scores = [70, 80, 90]

# print(normalize_name(name))
# print(get_average(scores))
#region
# 1. 첫 번째 print의 예상 결과:
# alice
# 2. 두 번째 print의 예상 결과:
# 80.0
# 3. from my_utils.text_utils import normalize_name에서 my_utils는 무엇인가?
# 패키지
# 4. text_utils는 무엇인가?
# 모듈
# 5. normalize_name은 무엇인가?
# 함수 객체
# 6. 왜 이번에는 my_utils.text_utils.normalize_name(name)이 아니라 normalize_name(name)이라고 바로 쓸 수 있는가?
# import 해서 실행되어 만들어진 my_utils.text_utils.normalize_name함수객체를 현재 파일에 있는 normalize_name이름에 바로 연결했기 때문이다.
# 7. import my_utils.text_utils 방식과 from my_utils.text_utils import normalize_name 방식의 가장 큰 차이는 무엇이라고 생각하는가?
# 함수를 실행할 때 마다 일일이 찾는 경로를 붙이지 않아도 된다는 것이다.
#[수정 후]
#import my_utils.text_utils는 패키지와 모듈 경로를 통해 함수에 접근하고, from my_utils.text_utils import normalize_name은 normalize_name이라는 이름을 현재 파일에서 직접 사용할 수 있게 한다.
#endregion
from my_utils import normalize_name, get_average


name = "  Alice  "
scores = [70, 80, 90]

print(normalize_name(name))
print(get_average(scores))





