def long_records(records, min_minutes):
    # if records.minutes >= min_minutes:
    #     yield records
    for record in records:
        if record.minutes >= min_minutes:
            yield record

# @trace
# def get_topics(records):
#     # mapped = map(records.topic, records)
#     mapped = map(lambda record: record.topic, records)
#     return list(mapped)

# def trace(func):
#     def wrapper():
#         print("처리 시작")
#         func()
#         print("처리 끝")

#     return wrapper                                                                                                           

def trace(func):
    def wrapper(*args, **kwargs):
        print("처리 시작")
        result = func(*args, **kwargs)
        print("처리 끝")
        return result

    return wrapper

@trace
def get_topics(records):
    # mapped = map(records.topic, records)
    mapped = map(lambda record: record.topic, records)
    return list(mapped)

# 1. records가 여러 StudyRecord라면, 각 StudyRecord 하나를 꺼내려면 무엇이 필요한가?
# 2. map() 첫 번째 인수에는 값이 와야 하나, 함수가 와야 하나?
# 3. @trace를 사용하는 시점보다 trace의 정의가 위에 있어야 하나 아래에 있어야 하나?
# 4. get_topics(records)를 감싸려면 wrapper도 records를 받을 수 있어야 하지 않는가?
