# import f3_score_utils


# scores = [70, 80, 90]

# print(f3_score_utils.get_average(scores))
# print(f3_score_utils.get_max_score(scores))
#region
# 1. 첫 번째 print의 예상 결과:
# 80.0
# 2. 두 번째 print의 예상 결과:
# 90
# 3. import f3_score_utils는 무엇을 가져오는 것인가?
# f3_score_utils.py 모듈을 가져온다.
# 4. 왜 get_average(scores)라고 바로 쓰지 않고 f3_score_utils.get_average(scores)라고 쓰는가?
# f3_score_utils 모듈 속의 get_average(scores)라는 것을 나타내기 위하여
#[보완]
#imptort f3_score_utils로 모듈 자체를 가져왔기 때문에 그 모듈 안의 함수는 f3_score_utils.get_average처럼 모듈 이름을 통해 접근해야 한다.
#endregion
# from f3_score_utils import get_average, get_max_score


# scores = [70, 80, 90]

# print(get_average(scores))
# print(get_max_score(scores))
#region
# 1. 첫 번째 print의 예상 결과:
# 80.0
# 2. 두 번째 print의 예상 결과:
# 90
# 3. from f3_score_utils import get_average는 무엇을 가져오는 것인가?
# f3_score_utils 모듈을 가져오는데 그 중에서 get_average를 선별적으로 사용할 수 있게 만들어 준다.
#[수정 후]
#f3_score_utils 모듈 안의 get_average 함수 객체를 현재 파일의 get_average 이름으로 사용할 수 있게 가져온다.
# 4. 이번에는 왜 f3_score_utils.get_average(scores)가 아니라 get_average(scores)라고 바로 쓸 수 있는가?
# from f3_score_utils import get_average는 get_average(scores)가 f3_score_utils.get_average(scores)라는 것을 나타내기 때문이다.
#[수정 후]
#현재 파일의 get_average 이름이 그 함수 객체를 직접 가리키므로 모듈 이름을 붙이지 않고 바로 호출 할 수 있다.
#endregion
import f3_score_utils


scores = [70, 80, 90]

print(f3_score_utils.get_average(scores))
#region
# 1. f3_module_main.py를 실행하면 "score_utils 실행됨"은 출력될 것 같은가?
# yes
# 2. 출력된다면 왜 f3_score_utils.py를 직접 실행하지 않았는데도 그 안의 print가 실행될 것이라고 생각하는가?
# import시 함수 객체를 만들고, 그 .py 파일의 코드를 실행하면서 만들어진 함수, 변수 등을 그 모듈 객체의 namespace에 등록한다고 했기 때문이다.
#[수정]
#import할 때 해당 .py 파일의 코드를 위에서 아래로 실행하고, 그 과정에서 만들어진 함수, 변수 등의 이름을 모듈 객체의 namespace에 등록하기 때문이다.
#따라서 모듈 안의 print도 실행된다.
# 3. 전체 출력 순서를 예상하면?
# score_utils 실행됨
# 80.0
#endregion
#region
# 1. f3_score_utils.py를 직접 실행했을 때 __name__에는 어떤 값이 들어갈 것 같은가?
# <__main__.f3_score_utils.py at 0x....>
#[수정 후]
#__main__
# 2. f3_module_main.py에서 f3_score_utils를 import했을 때 f3_score_utils.py 내부의 __name__에는 어떤 값이 들어갈 것 같은가?
# <__main__.f3_score_utils.py at 0x....>
#[수정 후]
#f3_score_utils
# 3. 직접 실행했을 때와 import됐을 때 __name__ 값이 같을 것 같은가, 다를 것 같은가?
# 같을 것 같다.
#[수정 후]
#다르다
# 4. 왜 파이썬이 이런 값을 구분할 필요가 있을 것 같은가?
# 객체로 생성되어져있는 곳에서 사용하는 것과 실행중인 프로그램에서 사용하는 함수를 구분하기 위해서
#[수정 후]
#현재 파일이 직접 실행된 프로그램의 시작파일인지, 다른 파일에서 import된 모듈인지 구분하기 위해서이다.
#endregion
# 1. python3 f3_score_utils.py로 직접 실행했을 때 예상 출력은?
# score_utils 실행됨
# 80.0
# 2. 왜 if문 안의 코드가 실행되는가?
# 이 파이썬의 파일이 __main__이라는 이름으로 실행되고 있기 때문이다.
#[수정 후]
#f3_score_utils.py를 직접 실행했기 때문에 이 파일의 __name__값이 "__main__"이 되고, 조건식이 True가 되기 때문이다.
# 3. python3 f3_module_main.py를 실행했을 때 f3_score_utils.py 안의 "score_utils 직접 실행됨"은 출력될 것 같은가?
# 실행되지 않는다.
# 4. 3번처럼 예상한 이유는?
# 모듈이 메인 프로그램이 아닌 다른 파일에서 모듈로 실행될 때는 __main__이라는 이름으로 실행되지 않는다.
#[수정 후]
#f3_score_utils가 다른 파일에서 import되면 __name__의 값은 "__main__"이 아니라 "f3_score_utils"가 된다.
#따라서 조건식이 False가 되어 if문 안의 코드는 실행되지 않는다.
# 5. if __name__ == "__main__":을 사용하는 목적은 무엇인가?
# 아래의 코드가 현재 모듈을 메인 프로그램으로 작동시킬 때만 작동하게 하기 위해서
#endregion















