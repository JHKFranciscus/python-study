from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["tasks0905"]
tasks = db["task"]


@app.route("/")
def home():
    return render_template("app1.html")

@app.route("/task", methods=["GET", "POST"])
def find_add_task():
    if request.method == "GET":
        task_list = list(tasks.find())

        for task in task_list:
            task["_id"] = str(task["_id"])

        return jsonify({
            "tasks": task_list
        })

    elif request.method == "POST":
        new_content = request.get_json()["content"]

        new_task = {
            "content": new_content,
            "important": False
        }

        tasks.insert_one(new_task)

        return jsonify({
            "result": "creat success"
        })

@app.route("/task/<task_id>", methods=["PATCH"])
def update_task(task_id):
    new_important = request.get_json()["important"]

    tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"important": new_important}}
    )

    return jsonify(
        {"result": "update success"}
    )

@app.route("/task/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks.delete_one(
        {"_id": ObjectId(task_id)}
    )

    return jsonify(
        {"result": "delete success"}
    )

if __name__ == "__main__":
    app.run(debug=True)



