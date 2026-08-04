#1단계 — 작업 데이터와 iterator 생성
inspection_tasks = [
    {"task_id": 101, "item": "노트북", "status": "대기"},
    {"task_id": 102, "item": "키보드", "status": "대기"},
    {"task_id": 103, "item": "모니터", "status": "대기"},
]

# task_id : 검사 작업 번호
# item    : 검사 대상
# status  : 현재 검사 상태

inspection_iterator = iter(inspection_tasks)

# 2단계 — 한 건씩 검사 처리
def process_next_inspection(task_iterator):
    try:
        task = next(task_iterator)
        task["status"] = "완료"

        print(
            f'{task["task_id"]}번 '
            f'{task["item"]} 검사를 완료했습니다.'
        )

        return task

    except StopIteration:
        print("남아 있는 검사 작업이 없습니다.")
        return None
#region
# 1. iterator에서 다음 작업 한 건을 꺼낸다.
# 2. 꺼낸 작업의 status를 "완료"로 변경한다.
# 3. 완료 내용을 출력한다.
# 4. 처리한 작업 딕셔너리를 반환한다.
# 5. 작업이 없으면 None을 반환한다.
#endregion

#3단계 — 실행 결과 예상
process_next_inspection(inspection_iterator)
process_next_inspection(inspection_iterator)
process_next_inspection(inspection_iterator)
process_next_inspection(inspection_iterator)
#region
# 예상 결과:
# 101번 노트북 검사를 완료했습니다.
# 102번 키보드 검사를 완료했습니다.
# 103번 모니터 검사를 완료했습니다.
# 남아 있는 검사 작업이 없습니다.
#endregion

#4단계 — 원본 데이터 변경 여부 예상
print()
print(inspection_tasks)
#region
# 예상:
# [{"task_id": 101, "item": "노트북", "status": "대기"}, {"task_id": 102, "item": "키보드", "status": "대기"}, {"task_id": 103, "item": "모니터", "status": "대기"},]
# next()로 꺼낸 딕셔너리의 status를 변경하면 원본 inspection_tasks의 status도 변경되는가?
# 답: next()로 꺼낸 dictionary는 iter()를 이용해 새롭게 만든 inspection_iterator라는 객체에서 꺼낸 값이기 때문에 원본의 요소는 건드리지 않는다.
# [실제 결과]
# 원본 inspection_tasks 안의 status도 모두 "완료"로 변경되었다.
# [수정]
# iter()는 원본 요소를 복사하지 않는다.
# next()로 꺼낸 task는 원본 리스트 안의 딕셔너리 객체를 가리키므로, task의 내부 값을 변경하면 원본 딕셔너리도 변경된다.
#endregion














