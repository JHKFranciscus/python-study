from flask import Flask, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["study_db"]
tasks = db["tasks"]


@app.route("/")
def home():
    return """
    <form action="/task" method="post">
        <input type="text" name="title">
        <button type="submit">추가</button>
    </form>

    <a href="/task">전체 조회</a>

    <form action="/task/6a97eace4a2a1d914caffc82/update" method="post">
        <button type="submit">변경</button>
    </form>   

    <form action="/task/6a97eace4a2a1d914caffc82/delete" method="post">
        <button type="submit">삭제</button>
    </form>    
    """

@app.route("/task", methods=["GET", "POST"])
def createTask():
    if request.method == "POST":
        title = request.form.get("title")

        result_create = tasks.insert_one(
            {
                "title": title,
                "done": False
            }
        )

        return str(result_create.inserted_id)

    result_read = tasks.find()
    return str(list(result_read))

@app.route("/task/<task_id>/update", methods=["POST"])
def updateTask(task_id):    
    result_update = tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"done": True}}
    )

    return str(result_update.modified_count)

@app.route("/task/<task_id>/delete", methods=["POST"])
def deleteTask(task_id):
    result_delete = tasks.delete_one(
        {"_id": ObjectId(task_id)},
    )

    return str(result_delete.deleted_count)



if __name__ == "__main__":
    app.run(debug=True)