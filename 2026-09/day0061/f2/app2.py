from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["task0905"]
tasks = db["tasks"]


@app.route("/")
def home():
    return render_template("app2.html")


@app.route("/tasks", methods=["GET", "POST"])
def tasks_find_add():
    if request.method == "GET":
        tasks_list = list(tasks.find())

        for task in tasks_list:
            task['_id'] = str(task['_id'])

        return jsonify({
            "tasks": tasks_list
        })

    elif request.method == "POST":
        new_task = request.get_json()

        tasks.insert_one({
            "task": new_task["task"],
            "status": False
        })

        return jsonify({
            "message": "추가 완료"
        })


@app.route("/tasks/update/<task_id>", methods=["PATCH"])
def tasks_update(task_id):
    task = tasks.find_one(
        {'_id': ObjectId(task_id)}
    )

    if task['status'] == True:
        tasks.update_one(
            {'_id': ObjectId(task_id)},
            {"$set": {'status': False}}
        )
    else:
        tasks.update_one(
            {'_id': ObjectId(task_id)},
            {"$set": {'status': True}}
        )

    return jsonify({
        "message": "변경 완료"
    })


@app.route("/tasks/delete/<task_id>", methods=["DELETE"])
def tasks_delete(task_id):
    tasks.delete_one(
        {'_id': ObjectId(task_id)}
    )

    return jsonify({
        "message": "삭제 완료"
    })




if __name__ == "__main__":
    app.run(debug=True)