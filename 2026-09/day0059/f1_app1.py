from flask import Flask, redirect, url_for, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["study_db"]
tasks = db["tasks"]



@app.route("/")
def home():
    return """
    <form action="/tasks" method="POST">
        <input type="text" name="title">
        <button type="submit">task 추가</button>
    </form>
    <a href="/tasks">task 조회</a>
    """

@app.route("/tasks", methods=["GET", "POST"])
def get_tasks():
    title = request.form.get("title")

    if request.method == "POST":
        result = tasks.insert_one({
            "title": title,
            "done": False
        })

        return str(result.inserted_id)

    result = list(tasks.find())
    return str(result)

@app.route("/tasks/<task_id>/done", methods=["POST"])
def complete_task(task_id):
    result = tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"done": True}}
    )

    return str(result.modified_count)

@app.route("/tasks/<task_id>/delete", methods=["POST"])
def delete_task(task_id):
    result = tasks.delete_one(
        {"_id": ObjectId(task_id)},
    )

    return str(result.deleted_count)


















if __name__ == "__main__":
    app.run(debug=True)


