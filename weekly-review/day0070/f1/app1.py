from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["test0913"]
tasks = db["tasks"]

allowed_priority = ["low", "normal", "high"]
allowed_status = ["todo", "doing", "done"]



@app.route("/")
def home():
    return render_template("app1.html")

@app.route("/task", methods=["GET", "POST"])
def task_function():
    if request.method == "POST":
        new_task = request.get_json()["new_task"]

        new_task_dict = {}

        new_task_dict["title"] = new_task["title"]

        if new_task["priority"] not in allowed_priority:
            return jsonify(
                {"result": "invalid priority"}
            ), 400

        new_task_dict["priority"] = new_task["priority"]

        new_task_dict["status"] = "todo"

        tasks.insert_one(new_task_dict)

        return jsonify(
            {"result": "add success"}
            )

    elif request.method == "GET":
        status = request.args.get("status")
        priority = request.args.get("priority")
        sort = request.args.get("sort")

        find_data = {}

        if status:
            find_data["status"] = status

        if priority:
            find_data["priority"] = priority

        sort_direction = -1

        if sort == "oldest":
            sort_direction = 1

        tasks_list = list(tasks.find(find_data).sort("_id", sort_direction))

        for task in tasks_list:
            task["_id"] = str(task["_id"])

        return jsonify(
            {"tasks": tasks_list}
        )

@app.route("/task/<task_id>", methods=["PATCH"])
def update_task(task_id):
    try:
        task_id = ObjectId(task_id)
    except:
        return jsonify(
            {"result": "invalid id"}
        ), 400

    update_status = request.get_json()["update_status"]

    if update_status not in allowed_status:
        return jsonify(
            {"result": "invalid status"}
        ), 400

    update_result = tasks.update_one(
        {"_id": task_id},
        {"$set": {"status": update_status}}
    )

    if update_result.matched_count == 0:
        return jsonify(
            {"result": "Not in collections"}
        ), 404

    return jsonify(
        {"result": "update success"}
    )

@app.route("/task/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        task_id = ObjectId(task_id)
    except:
        return jsonify(
            {"result": "invalid id"}
        ), 400
    
    delete_result = tasks.delete_one(
        {"_id": task_id},
    )

    if delete_result.deleted_count == 0:
        return jsonify(
            {"result": "Not in collections"}
        ), 404

    return jsonify(
        {"result": "delete success"}
    )

        


if __name__ == "__main__":
    app.run(debug=True)