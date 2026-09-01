from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["practice_db"]
records = db["records"]

create1 = records.insert_many([
    {
        "title": "Python",
        "pages": 300,
        "finished": False,

    },
    {
        "title": "Flask",
        "pages": 220,
        "finished": False,
    },
    {
        "title": "MongoDB",
        "pages": 250,
        "finished": False,
    }
])

print("==Create==")
task_ids = create1.inserted_ids
for task_id in task_ids:
    print(task_id)

print()
print("==Read==")
read2 = records.find(
    {"finished": False}
)
for read in read2:
    print(read)

print()
print("==Update==")
update3 = records.update_one(
    {"_id": task_ids[1]},
    {"$set": {
        "pages": 240,
        "finished": True
    }}
)
updated_flask = records.find_one({"_id": task_ids[1]})
print(updated_flask)

print()
print("==Delete==")
delete4 = records.delete_many(
    {"finished": False}
)

print()
print("==Rest==")
for task_id in task_ids:
    record = records.find_one({"_id": task_id})
    if record is not None:
        print(record)

