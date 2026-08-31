from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["shop"]
products = db["products"]
print(client.admin.command("ping"))

new_product = {
    "name": "notebook",
    "price": 2500
}

result = products.insert_one(new_product)

print()
print(result.inserted_id)

print()
print("==객체 추적==")
print(new_product)

print()
print(type(result.inserted_id))

print()
print("==find_one()==")

found_product = products.find_one({
    "name": "notebook"
})

print(found_product)

print()
print("==조건에 없는 document 찾기==")
not_found = products.find_one({
    "name": "does-not-exist"
})

print(not_found)

print()
print("==순회==")

found_product = products.find_one({
    "name": "notebook"
})

print()
print(found_product)

not_found = products.find_one({
    "name": "does-not-exist"
})

print()
print(not_found)


product_id = "6a953b1578099f496aa16983"

object_id = ObjectId(product_id)

found_by_id = products.find_one({
    "_id": object_id
})

print()
print("==id 확인==")
print(type(product_id))
print(type(object_id))
print(found_by_id)