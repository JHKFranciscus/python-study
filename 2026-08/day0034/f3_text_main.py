from f3_text_utils import normalize_name, contains_keyword

name = "  Alice  "
text = "python module study"

print(normalize_name(name))
print(contains_keyword(text, "module"))


# 1. python3 f3_text_utils.py를 직접 실행했을 때 예상 출력은?
# text_utils 직접 실행
# 2. python3 f3_text_main.py를 실행했을 때 예상 출력은?
# alice
# True
# 3. f3_text_main.py를 실행할 때 "text_utils 직접 실행"도 출력되는가?
# 출력되지 않는다.
# 4. 3번 결과가 그렇게 되는 이유는?
# f3_text_utils를 import할 때 __name__의 값이 파일명으로 돌아오기 때문이다.
#[수정 후]
#f3_text_utils가 import되면 __name__의 값은 "__main__"이 아니라 "f3_text_utils"이 된다. 따라서 if __name__ == "__main__": 조건이 False가 되어 그 안의 코드는 실행되지 않는다.
# 5. from f3_text_utils import normalize_name을 사용했기 때문에 normalize_name()을 모듈 이름 없이 바로 호출할 수 있는 이유는?
# normalize_name이 import를 실행할 때 생성된 f3_text_utils의 normalize_name 함수 객체에 이름이 연결되었기 때문이다.
#[수정 후]
#from f3_text_utils import normalize_name으로 f3_text_utils의 normalize_name 함수 객체를 현재 파일의 normalize_name이라는 이름에도 연결했기 때문이다.