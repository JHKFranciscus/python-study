from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {
    "2": {
        "title": "Flask 복습",
        "done": False
    },
    "6": {
        "title": "Ajax 정리",
        "done": True
    }
}



@app.route("/tasks/<task_id>/data")
def getTask(task_id):
    return jsonify(tasks[task_id])


@app.route("/tasks/<task_id>/title", methods=["POST"])
def postTask(task_id):
    new_title = request.form.get("title")

    if task_id in tasks:
        tasks[task_id]["title"] = new_title

        return jsonify(tasks[task_id])


