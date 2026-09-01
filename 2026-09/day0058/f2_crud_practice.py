from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["study_tracker"]
records = db["records"]

#1 Create
print("==Create==")
created1 = records.insert_one(
    {
        "subject": "CRUDPractice",
        "minutes": 40,
        "completed": False
    }
)

task_id = created1.inserted_id
print(f"task_id: {task_id}")

print()
#2 Read
print("==Read==")
readed2 = records.find_one(
    {"_id": task_id}
)
print(f"readed_document: {readed2}")

print()
#3 Update
print("==Update==")
updated3 = records.update_one(
    {"_id": task_id},
    {"$set": {
        "minutes": 50,
        "completed": True
    }}
)

print(f"matched_count: {updated3.matched_count}")
print(f"modified_count: {updated3.modified_count}")

#4 수정 확인
result_updated3 = records.find_one(
    {"_id": task_id}
)
print(f"updated_document: {result_updated3}")

print()
#5 Delete
print("==Delete==")
deleted4 = records.delete_one(
    {"_id": task_id}
)

print(f"deleted_count: {deleted4.deleted_count}")

#6 삭제 확인
result_deleted4 = records.find_one(
    {"_id": task_id}
)

print(f"final_result: {result_deleted4}")





