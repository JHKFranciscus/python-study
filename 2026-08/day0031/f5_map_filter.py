def double(number):
    print("double 실행:", number)
    return number * 2


def is_even(number):
    print("is_even 실행:", number)
    return number % 2 == 0


numbers = [1, 2, 3, 4]

mapped = map(double, numbers)
filtered = filter(is_even, numbers)

print("map 객체 생성 완료")
print("filter 객체 생성 완료")

print("mapped 자료형:", type(mapped))
print("filtered 자료형:", type(filtered))

print("mapped 첫 번째 변환:", list(mapped))
print("mapped 두 번째 변환:", list(mapped))

print("filtered 첫 번째 변환:", list(filtered))
print("filtered 두 번째 변환:", list(filtered))
#region
# 예상
# 1. mapped에는 리스트가 저장되는가, map 객체가 저장되는가?
# 답: map 객체가 저장된다.
# 2. filtered에는 리스트가 저장되는가, filter 객체가 저장되는가?
# 답: filter 객체가 저장된다.
# 3. mapped와 filtered를 만드는 시점에 double과 is_even 함수가 바로 실행되는가?
# 답: 둘 다 지연 계산되는 1회성 iterator이다.
# 4. type(mapped)의 결과는 무엇인가?
# 답: <class 'map'>
# 5. type(filtered)의 결과는 무엇인가?
# 답: <class 'filter'>
# 6. list(mapped)의 첫 번째 결과는 무엇인가?
# 답: [2, 4, 6, 8]
# 7. list(mapped)의 두 번째 결과는 무엇인가?
# 답: []
# 8. list(filtered)의 첫 번째 결과는 무엇인가?
# 답: [2, 4]
# 9. list(filtered)의 두 번째 결과는 무엇인가?
# 답: []
# 10. map 객체와 filter 객체가 두 번째에는 빈 리스트가 되는 이유는?
# 답: 둘 다 1회성 iterator이기 떄문이다.
# 예상 출력 순서:
# map 객체 생성 완료
# filter 객체 생성 완료
# mapped 자료형: <class 'map'>
# filtered 자료형: <class 'filter'>
# mapped 첫 번째 변환: [2, 4, 6, 8]
# mapped 두 번째 변환: []
# filtered 첫 번째 변환: [2, 4]
# filtered 두 번째 변환:[]
# [확인 후 정정]
# list(mapped)를 계산하는 동안 double이 먼저 네 번 실행된다.
# list(filtered)를 계산하는 동안 is_even이 먼저 네 번 실행된다.
# 실제 출력:
# map 객체 생성 완료
# filter 객체 생성 완료
# mapped 자료형: <class 'map'>
# filtered 자료형: <class 'filter'>
# double 실행: 1
# double 실행: 2
# double 실행: 3
# double 실행: 4
# mapped 첫 번째 변환: [2, 4, 6, 8]
# mapped 두 번째 변환: []
# is_even 실행: 1
# is_even 실행: 2
# is_even 실행: 3
# is_even 실행: 4
# filtered 첫 번째 변환: [2, 4]
# filtered 두 번째 변환: []
#endregion
print("\n--- filter 후 map 연결 ---")

scores = [35, 80, 62, 95, 40]

passed = filter(lambda score: score >= 60, scores)
bonus_scores = map(lambda score: score + 5, passed)

print("passed 자료형:", type(passed))
print("bonus_scores 자료형:", type(bonus_scores))
print("최종 결과:", list(bonus_scores))
print("passed 재사용:", list(passed))
print("bonus_scores 재사용:", list(bonus_scores))
#region
# 실습 2 예상
# 1. filter에 전달된 lambda의 역할은 무엇인가?
# 답: 조건을 반환할 함수 객체
# 2. map에 전달된 lambda의 역할은 무엇인가?
# 답: 적용할 함수 객체
# 3. passed에는 어떤 종류의 객체가 저장되는가?
# 답: <class 'filter'>
# 4. bonus_scores에는 어떤 종류의 객체가 저장되는가?
# 답: <class 'map'>
# 5. 객체를 만드는 시점에 점수 비교와 5점 추가가 모두 즉시 실행되는가?
# 답: 지연 계산을 하는 객체로 객체를 만드는 시점에서는 함수가 실행되지 않는다.
# 6. 최종 결과는 무엇인가?
# 답: 최종 결과: [85, 67, 100]
# 7. 35와 40에도 5를 더하는 lambda가 실행되는가?
# 답과 이유: passed 객체가 원본 원소 중 35와 40을 제외하기 때문에 35와 40에는 passed를 사용하는 5를 더하는 lambda는 실행되지 않는다.
# 8. list(bonus_scores)를 실행할 때 filter와 map 중 어느 것이 먼저 각 값을 처리하는가?
# 답: map을 실행하면 그 안의 passed가 filter를 호출하기 때문에 filter가 먼저 각 값을 처리한 후 map이 처리한다.
# [보완]
# filter가 전체 처리를 끝낸 뒤 map이 시작되는 것은 아니다.
# list(bonus_scores)가 값을 하나 요청할 때마다 map이 filter에 값을 요청하고, filter를 통과한 값에만 map의 lambda가 실행된다.
# 9. passed 재사용의 결과는 무엇인가?
# 답: []
# 10. bonus_scores 재사용의 결과는 무엇인가?
# 답: []
# 예상 출력 순서:
#이전 계산은 제외한다
#
# --- filter 후 map 연결 ---
# passed 자료형: <class 'filter'>
# bonus_scores 자료형: <class 'map'>
# 최종 결과: [85, 67, 100]
# passed 재사용: []
# bonus_scores 재사용: []
#endregion



































