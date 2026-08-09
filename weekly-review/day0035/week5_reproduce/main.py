from study import StudyRecord, long_records, get_topics, trace


obj_1 = StudyRecord("Python 자료처리", 50)
obj_2 = StudyRecord("Generator", 5)
obj_3 = StudyRecord("Decorator", 45)
obj_4 = StudyRecord("Pathlib", 20)

obj_1.notes.append("enumerate 복습")

objs = list[obj_1, obj_2, obj_3, obj_4]

for num, obj in enumerate(objs, start=1):
    print(f"{num}. {obj}")