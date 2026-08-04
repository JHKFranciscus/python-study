server_checks = [
    {"server": "인증 서버", "response_time": 120},
    {"server": "결제 서버", "response_time": 350},
    {"server": "검색 서버", "response_time": 280},
    {"server": "로그 서버", "response_time": 500},
]

#1단계 — iterator로 점검 기록 한 건씩 꺼내기
def process_next_server_check(check_iterator):
    try:
        check = next(check_iterator)
        print(f"{check["server"]}의 응답 시간은 {check["response_time"]}ms입니다.")
        return check

    except StopIteration:
        print("남아 있는 서버 점검 기록이 없습니다.")
        return None


check_iterator = iter(server_checks)

first = process_next_server_check(check_iterator)
second = process_next_server_check(check_iterator)
third = process_next_server_check(check_iterator)
forth = process_next_server_check(check_iterator)
fifth = process_next_server_check(check_iterator)

#2단계 — 느린 서버만 생성하는 generator
def generate_slow_servers(checks, standard):
    print("서버 응답 시간 검사를 시작합니다.")

    for check in checks:
        # print("인증 서버를 확인합니다.")
        print(f"{check["server"]}를 확인합니다.")
        # a = next(check)
        # if standard >= 300:
        if check["response_time"] >= standard:
            # yeild a
            yield check

    print("서버 응답 시간 검사가 끝났습니다.")

#3단계 — next()로 첫 번째 느린 서버 꺼내기
slow_server_generator = generate_slow_servers(server_checks, 300)

first_slow_server = next(slow_server_generator)
print("첫 번째 느린 서버:", first_slow_server)
#4단계 — 남은 값을 for문으로 처리하기
for server in slow_server_generator:
    print("추가 느린 서버:", server)

print("느린 서버 처리가 끝났습니다.")

# 문제 1:
# server_checks는 iterable인가, iterator인가?
# 답: iterable

# 문제 2:
# check_iterator는 iterable인가, iterator인가?
# 답: iterator
#[보완]
# check_iterator의 주된 분류: iterator
# 동시에 for문에 넣을 수 있으므로 iterable이기도 함

# 문제 3:
# slow_server_generator를 생성한 직후 아직 검사된 서버가 없는 이유는 무엇인가?
# 답: 처음 함수를 실행하면 generator만 생성될 뿐 함수 본문은 실행하지 않기 때문이다.
#[수정]
#generator 함수를 호출하면 generator 객체만 생성되고, next()나 for문이 값을 요청하기 전까지 함수 본문은 실행되지 않는다.


# 문제 4:
# 첫 번째 값을 next()로 꺼낸 뒤 같은 generator를 for문에 넣으면 처음부터 다시 검사하지 않는 이유는 무엇인가?
# 답: generator는 yield로 일시중지한 부분부터 실행을 재개하는데 yield로 일시중지한 이후부터 검사를 실시하기 때문이다. 
#[보완]
# yield에서 멈춘 실행 상태를 기억한다. next()나 for문이 값을 요청하면 그 yield에서 실행을 재개한 뒤, 이후 코드와 for문의 다음 반복을 계속한다.

# 문제 5:
# yield와 return은 함수 실행을 끝내는 방식에서 무엇이 다른가?
# 답: return은 값을 반환하며 함수 실행을 끝내지만 yield는 값을 반환하며 함수 실행을 끝내지 않고 일시중지를 할 뿐이다.