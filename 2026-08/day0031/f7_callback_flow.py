def is_passing(score):
    print("is_passing 시작")
    result = score >= 60
    print("is_passing 종료")
    return result


def save_result(score):
    print("save_result 시작")
    print("저장된 점수:", score)
    print("save_result 종료")


def process_score(score, checker, handler):
    print("process_score 시작")

    if checker(score):
        print("조건 통과")
        handler(score)
    else:
        print("조건 실패")

    print("process_score 종료")


print("전체 처리 시작")
process_score(80, is_passing, save_result)
print("전체 처리 종료")
#region
# 예상
# 1. process_score의 checker에는 무엇이 저장되는가?
# 답: is_passing
# 2. process_score의 handler에는 무엇이 저장되는가?
# 답: save_result
# 3. checker(score)는 실제로 어떤 호출과 같은가?
# 답: is_passing(80)
# 4. handler(score)는 실제로 어떤 호출과 같은가?
# 답: save_result(80)
# 5. is_passing이 끝난 뒤 제어권은 어디로 돌아오는가?
# 답: process_score()
#[보완]
#process_score()의 if checker(score): 호출 위치로 돌아온다.
#반환값 True를 이용해 if 조건을 판단한다.
# 6. save_result가 끝난 뒤 제어권은 어디로 돌아오는가?
# 답: process_score()
#[보완]
#process_score()의 handler(score) 호출 위치로 돌아온다.
#이후 print("process_score 종료")를 실행한다.
# 7. 이 코드에서 콜백을 호출할 시점을 결정하는 함수는 무엇인가?
# 답: process_score()
# 8. is_passing과 save_result 중 실제로 호출되는 콜백은 무엇인가?
# 답: 둘 다 실제로 호출되는 콜백이다
# 9. score를 40으로 바꾸면 save_result가 실행되는가?
# 답과 이유: checker(score)에 False가 반환되어 if False이므로 그 아래의 코드는 실행되지 못하고 바로 else: 로 넘어가게 되므로 save_result에 도달할 수 없으므로 실행되지 않는다.
# 예상 출력 순서:
# 전체 처리 시작
# process_score 시작
# is_passing 시작
# is_passing 종료
# 조건 통과
# save_result 시작
# 저장된 점수: 80
# save_result 종료
# process_score 종료
# 전체 처리 종료
#endregion
