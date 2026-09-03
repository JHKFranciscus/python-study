from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["alone_test"]
test1 = db["test1"]

print("A 실행됨")


@app.route("/")
def home():
    print("B 실행됨")
    tests_list = list(test1.find())
    
    print("현재 개수:", len(tests_list))
    return render_template("testb.html", test=tests_list)

if __name__ == "__main__":
    app.run(debug=True)