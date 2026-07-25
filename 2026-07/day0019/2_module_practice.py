import message_tools

user_name = input("이름을 입력하세요: ")

welcome_message = message_tools.make_welcome_message(user_name)
print(welcome_message)

goodbye_message = message_tools.make_goodbye_message(user_name)
print(goodbye_message)

# 1. 모듈이란 무엇인가?
# 파이썬에서 .py같은 하나의 파일
#[수정 후]
# 파이썬 코드가 작성된 하나의 .py 파일을 모듈로 사용할 수 있다.
# 2. import message_tools는 어떤 파일을 불러오는가?
# 같은 폴더 내의 message_tools라는 이름을 가지 파일
#[수정 후]
# 현재 폴더에 있는 message_tools.py 파일을 모듈로 불러온다.
# 3. message_tools.make_welcome_message에서 점(.)은 어떤 관계를 나타내는가?
# 모듈명.모듈 내 함수로 모듈명을 가진 모듈 내의 함수를 사용하게 해준다는 의미이다.
#[수정 후]
# message_tools 모듈 안에 있는 make_welcome_message 함수를 사용한다는 의미이다.
# 4. input()은 어느 파일에 있는가?
# 2_module_practice.py
# 5. 실제 메시지를 만드는 코드는 어느 파일에 있는가?
# message_tools.py
# 6. message_tools.py를 수정하면 2_module_practice.py에서 사용하는 결과도 바뀌는가?
# message_tools.py에서 결과값을 불러오기 떄문에 그렇다.
#[수정 후]
# message_tools.py의 함수를 불러와 호출하므로, 함수를 수정한 뒤 프로그램을 다시 실행하면 결과도 바뀐다.