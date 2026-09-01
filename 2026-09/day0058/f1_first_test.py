from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["study_tracker"]
records = db["records"]


#region
# print("==update_one()==")
# result1 = records.update_one(
#     {"subject": "Flask"},
#     {"$set": {"completed": False}}
# )

# print(f"맞는 것: {result1.matched_count}")
# print(f"고친 것: {result1.modified_count}")

# record = records.find_one({"subject": "Flask"})
# print(record)
# print()
#endregion

#region
# print("==update_many()==")
# result2 = records.update_many(
#     {"subject": "MongoDB"},
#     {"$set": {"minutes": 130}}
# )

# print(f"맞는 것: {result2.matched_count}")
# print(f"고친 것: {result2.modified_count}")

# records2 = records.find(
#     {"subject": "MongoDB"},
# )

# for record in records2:
#     print(record)
#endregion

#region
# result3 = records.insert_one(
#     {
#         "subject": "PyDeleteTest",
#         "minutes": 15,
#         "completed": False
#     }
# )

# result = records.delete_one(
#     {"subject": "PyDeleteTest"}
# )

# print(f"삭제한 수: {result.deleted_count}")

# record = records.find_one({"subject": "PyDeleteTest"})
# print(record)
#endregion

#region
result4 = records.insert_many([
    {"subject": "PyDeleteManyTest", "minutes": 10, "completed": False},
    {"subject": "PyDeleteManyTest", "minutes": 20, "completed": False},
    {"subject": "PyDeleteManyTest", "minutes": 30, "completed": False}
])

result = records.delete_many(
    {"subject": "PyDeleteManyTest"}
)

print(f"삭제한 수: {result.deleted_count}")

print()
record = records.find_one(
    {"subject": "PyDeleteManyTest"}
)
print(record)
















