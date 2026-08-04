temperature_records = [
    {"time": "09:00", "temperature": 21},
    {"time": "10:00", "temperature": 27},
    {"time": "11:00", "temperature": 30},
    {"time": "12:00", "temperature": 24},
    {"time": "13:00", "temperature": 32},
]

def generate_high_temperature_records(records, standard):
    print("온도 기록 검사를 시작합니다.")

    for record in records:
        print(f'{record["time"]} 기록을 확인합니다.')

        if record["temperature"] >= standard:
            yield record

    print("모든 온도 기록 검사가 끝났습니다.")
#region
# 1. 기록을 한 건 확인한다.
# 2. 온도가 기준 이상인지 검사한다.
# 3. 조건을 만족한 경우에만 해당 기록을 yield한다.
# 4. 다음 next()가 호출될 때 나머지 검사를 이어서 진행한다.
#endregion
high_temperature_generator = generate_high_temperature_records(
    temperature_records,
    28,
)

print(high_temperature_generator)
#region
# 예상 1:
# 위 함수 호출만으로 "온도 기록 검사를 시작합니다."가 출력되는가?
# 답: generator가 생성될 뿐 즉시 함수 본문이 실행되지는 않는다.

# 예상 2:
# 아직 몇 시 기록까지 검사한 상태인가?
# 답: 아직 검사를 하지도 않았다.
#endregion
print()

first_record = next(high_temperature_generator)

print("첫 번째 고온 기록:", first_record)
#region
# 예상 출력:
# 온도 기록 검사를 시작합니다.
# 09:00 기록을 확인합니다.
# 10:00 기록을 확인합니다.
# 11:00 기록을 확인합니다.
# 첫 번째 고온 기록: {"time": "11:00", "temperature": 30}
# 실제 출력:
# 온도 기록 검사를 시작합니다.
# 09:00 기록을 확인합니다.
# 10:00 기록을 확인합니다.
# 11:00 기록을 확인합니다.
# 첫 번째 고온 기록: {'time': '11:00', 'temperature': 30}
#endregion
print()

second_record = next(high_temperature_generator)

print("두 번째 고온 기록:", second_record)
#region
# 예상 출력:
# 12:00 기록을 확인합니다.
# 13:00 기록을 확인합니다.
# 두 번째 고온 기록: {"time": "13:00", "temperature": 32}
# 실제 출력:
# 12:00 기록을 확인합니다.
# 13:00 기록을 확인합니다.
# 두 번째 고온 기록: {'time': '13:00', 'temperature': 32}
# 두 번째 next()를 호출하면 어느 시간의 기록부터 확인하는가? 어떤 문장들이 어떤 순서로 출력되는가?
# 답: 12:00의 기록부터 확인한다.
#[수정]
#generator는 11:00 기록의 yield에서 실행을 재개한 뒤, for문의 다음 반복으로 넘어가 12:00 기록부터 확인한다.

# 1. 09:00부터 다시 검사하는가?
# 답: yield는 반환한 값 이후부터 다시 검사를 시작한다.
# [보완]
# 09:00부터 다시 시작하지 않는다. 정지했던 11:00 기록의 yield에서 재개한 뒤 다음 반복으로 진행한다.
# 2. 12:00 기록은 출력만 하고 넘어가는가?
# 답: 그러하다
# 3. 어느 기록에서 두 번째 yield가 실행되는가?
# 답: records의 요소인 {"time": "12:00", "temperature": 24}부터 실행된다.
# [수정]
# 두 번째 next()는 12:00 기록부터 확인하지만, 12:00은 기준 미만이므로 yield하지 않는다.
# 두 번째 yield는 {"time": "13:00", "temperature": 32}에서 실행된다.
# 4. "모든 온도 기록 검사가 끝났습니다."까지 이번에 출력되는가?
# 답: {"time": "13:00", "temperature": 32}을 반환하고 일시정지 되었으므로 출력되지 않는다.
#endregion
print()

# third_record = next(high_temperature_generator)

# print("세 번째 고온 기록:", third_record)
#region
# 예상:
# 세 번째 next()를 호출하면 어떤 문장이 출력되고, 어떤 결과가 발생하는가?
# 답: "모든 온도 기록 검사가 끝났습니다." 출력 이후에 StopIteration이 발생한다.
# 실제 출력
# 모든 온도 기록 검사가 끝났습니다.
# StopIteration

# 1. "13:00 기록을 확인합니다."가 다시 출력되는가?
# 답: 13:00 기록의 yeild에서 재개하지만, 다음 iterable부터 확인한다.
# [보완]
# 13:00 기록의 yield에서 실행을 재개하지만, "13:00 기록을 확인합니다."는 다시 실행하지 않는다.
# 현재 반복을 마친 뒤 for문의 다음 반복을 시도한다.

# 2. "모든 온도 기록 검사가 끝났습니다."가 출력되는가?
# 답: 출력된다.

# 3. third_record에 저장되는 값이 있는가?
# 답: StopIteration 때문에 프로그램이 종료되어 값이 저장되지 못한다.
#[보완]
#StoopIteration이 발생했기 떄문에 대입문이 완성되지 않아 third_record에 None이 저장되는 것도 아니고, 그냥 아무 값도 저장되지 않는다.

# 4. "세 번째 고온 기록:" 출력문까지 실행되는가?
# 답: StopIteration 때문에 프로그램이 종료되어 print()에 도달하지 못하여 출력문이 실행되지 못한다.
#endregion
print()

for_temperature_generator = generate_high_temperature_records(
    temperature_records,
    28,
)

for record in for_temperature_generator:
    print("고온 기록 처리:", record)

print("for문 처리가 끝났습니다.")
#region
# 예상 결과:
# 온도 기록 검사를 시작합니다.
# 09:00 기록을 확인합니다.
# 10:00 기록을 확인합니다.
# 11:00 기록을 확인합니다.
# 고온 기록 처리: {'time': '11:00', 'temperature': 30}
# 12:00 기록을 확인합니다.
# 13:00 기록을 확인합니다.
# 고온 기록 처리: {'time': '13:00', 'temperature': 32}
# 모든 온도 기록 검사가 끝났습니다.
# for문 처리가 끝났습니다.

# 문제 1:
# 조건을 만족하지 않는 09:00, 10:00, 12:00 기록도
# "기록을 확인합니다." 문장은 출력되는가?
# 답: 출력된다.

# 문제 2:
# "고온 기록 처리:"가 출력되는 기록은 몇 시 기록인가?
# 답: 11시와 13시 기록이다.

# 문제 3:
# generator가 끝났을 때 StopIteration 오류 화면이 나타나는가?
# 답: for문이 자동으로 처리하여 나타나지 않는다.

# 문제 4:
# "모든 온도 기록 검사가 끝났습니다."와
# "for문 처리가 끝났습니다." 중 무엇이 먼저 출력되는가?
# 답: for문 내에 존재하는 "모든 온도 기록 검사가 끝났습니다."가 먼저 출력된다.
#endregion
















