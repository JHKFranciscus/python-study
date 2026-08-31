from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://127.0.0.1.:27017/")
db = client["study_tracker"]
records = db["records"]

record_one = {
    "subject": "Python",
    "minutes": 60,
    "completed": True
}

record_two = {
    "subject": "Flask",
    "minutes": 90,
    "completed": True
}

record_three = {
    "subject": "MongoDB",
    "minutes": 120,
    "completed": False
}

result_one = records.insert_one(record_one)

result_many = records.insert_many([record_two, record_three])


print(records.find_one({'subject': "Python"}))
print(records.find_one({'subject': "Flask", 'minutes': 90}))


print()
print("==전체 조회==")
records_list = records.find()
for record in records_list:
    print(record)

print()
print("==아이디로 찾기==")
one_id = result_one.inserted_id
print(records.find_one({
    "_id": one_id
}))

print()
print(records.find_one({'subject': "Java"}))