from study_tools import StudyRecord, save_record


# record = StudyRecord()

# record.topic = "pathlib"
# record.minutes = 45
record = StudyRecord("pathlib", 45)
# record.tags.append("python", "file")
record.tags.append("python")
record.tags.append("file")

save_record(record)

print(record)

# 1. print(record)의 예상 결과:
# StudyRecord(topic='pathlib', minutes='45, tags='python', 'file')
#[수정 후]
#StudyRecord(topic='pathlib', minutes='45, tags=['python', 'file'])
# 2. study_records/record.txt의 예상 내용:
# 주제: pathlib
# 시간: 45분
# 태크: pythonfile
#[수정 후]
# 주제: pathlib
# 시간: 45분
# 태크: python, file