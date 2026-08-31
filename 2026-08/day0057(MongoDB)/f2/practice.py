from pymongo import MongoClient
from bson import ObjectId

first_book = {
    "title": "Python Basic",
    "price": 18000
}

second_book = {
    "title": "Flask Basic",
    "price": 22000
}

third_book = {
    "title": "MongoDB Basic",
    "price": 25000
}

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["study_shop"]
books = db["books"]

books.insert_one(first_book)

books.insert_many([second_book, third_book])


print("==1==")
PythonBasic = books.find_one({"title": "Python Basic"})
print(PythonBasic)

print()
print("==2==")
print(books.find_one({"price": 25000}))

print()
print("==3==")
find_books = books.find()
for find_book in find_books:
    print(find_book)

print()
print("==4==")
PythonBasic_id = PythonBasic["_id"]

found_by_id = books.find_one({
    "_id": PythonBasic_id
})

print(found_by_id)