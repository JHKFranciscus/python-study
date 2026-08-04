delivery_tasks = [
    "서울 배송",
    "대전 배송",
    "부산 배송",
]

for task in delivery_tasks:
    print(task)

print()
task_iterator = iter(delivery_tasks)

print(delivery_tasks)
print(task_iterator)
#region
# 예상 1: delivery_tasks를 출력하면 무엇이 나오는가?
# 답: ["서울 배송", "대전 배송", "부산 배송",]

# 예상 2: task_iterator를 출력하면 배송 작업들이 그대로 나오는가?
# 답: 모른다 안 가르쳐줬는데 어떻게 아냐

# iterate = 회차마다 대상이나 상태가 한 칸씩 옮겨가는 반복(반복이 순회를 낳는 구조)(값을 하나씩 차례대로 순회하는 것)

# iterable
# 반복할 값들을 가지고 있으며 iterator를 만들 수 있는 객체

# iterator
# 현재 어디까지 값을 꺼냈는지 기억하면서 다음 값을 하나씩 꺼내는 객체
#endregion

print()

delivery_iterator = iter(delivery_tasks)
#region
# 예상 결과를 먼저 작성한다.
# 첫 번째 next(): 서울 배송
# 두 번째 next(): 대전 배송
# 세 번째 next(): 부산 배송
#endregion
print(next(delivery_iterator))
print(next(delivery_iterator))
print(next(delivery_iterator))
#region
# 예상: 서울 배송
# 세 값을 전부 꺼낸 뒤 next()를 한 번 더 호출하면 어떻게 되는가?
# 답: 처음부터 다시 시작된다.
#[수정]
#StopIteration이라는 오류가 발생한다.
#endregion
# print(next(delivery_iterator))
print()

new_delivery_iterator = iter(delivery_tasks)

print(next(new_delivery_iterator))
print(next(new_delivery_iterator))
#region
# 예상 1: 새 iterator의 첫 번째 next() 결과
# 답: 서울 배송

# 예상 2: 기존 delivery_iterator와 new_delivery_iterator는 같은 진행 위치를 사용하는가?
# 답: 그러하다
#[수정]
# 두 iterator는 같은 진행 위치를 사용하지 않는다. 새 iterator는 기존 iterator의 상태와 관계없이 처음부터 시작한다.
#endregion
print()

first_iterator = iter(delivery_tasks)
second_iterator = iter(delivery_tasks)

print(next(first_iterator))
print(next(first_iterator))
print(next(second_iterator))
print(next(first_iterator))
#region
# 실행 전에 예상한다.
# 1번째 출력: 서울 배송
# 2번째 출력: 대전 배송
# 3번째 출력: 서울 배송
# 4번째 출력: 부산 배송
#endregion
print()

original_tasks = ["포장", "검수", "출고"]
work_iterator = iter(original_tasks)

print(iter(original_tasks) is original_tasks)
print(iter(work_iterator) is work_iterator)
#region
# 예상 1:
# iter(original_tasks) is original_tasks 결과는?
# False

# 예상 2:
# iter(work_iterator) is work_iterator 결과는?
# True
#endregion
#----------------------------------------------------------
print()

processes = ["접수", "분류", "완료"]
process_iterator = iter(processes)

print(next(process_iterator))
print(next(process_iterator))
print(next(process_iterator))
print()
print("===for문 1차 실험===")
for process in process_iterator:
    print(process)
print("===for문 1차 실험 끝===")
#region
# 예상: 
# 모든 값을 next()로 꺼낸 process_iterator를 for문으로 순회하면 무엇이 출력되는가?
# 답: StopIteration이 뜬다.
#[수정] 
#오류도 안 뜨지만 아무것도 뜨지 않는다.

# 1. for문이 처음부터 "접수"를 다시 출력하는가?
# 2. 아니면 아무 값도 출력하지 않고 끝나는가?
#답: for문이어도 전부 소모 된 객체를 다시 출력하지는 않는다.
#endregion
print()

new_process_iterator = iter(processes)

for process in new_process_iterator:
    print(process)

print("반복 종료")
#region
# 예상 결과:
# 접수
# 분류
# 완료
# 반복 종료
#endregion
print()

manual_process_iterator = iter(processes)

while True:
    try:
        process = next(manual_process_iterator)
        print(process)
    except StopIteration:
        print("더 이상 처리할 작업이 없습니다.")
        break

print("수동 반복 종료")
#region
# 예상 결과:
# 접수
# 분류
# 완료
# 더 이상 처리할 작업이 없습니다.
# 수동 반복 종료

# 문제 1:
# 이 코드에서 break가 없다면 어떻게 되는가?
# 답: 계속 StopIteration예외 처리로 돌아가서 "더 이상 처리할 작업이 없습니다."라는 문구가 반복된다.

# 문제 2:
# for문과 위 while문이 공통으로 하는 핵심 동작은 무엇인가?
# 답: iterate(회차마다 대상이나 상태가 한 칸씩 옮겨가며 반복되는 행위)
#[수정]
#for문과 위 while문은 iterator에서 next()로 값을 하나씩 꺼내고, StopIteration이 발생하면 반복을 종료한다.
#endregion















