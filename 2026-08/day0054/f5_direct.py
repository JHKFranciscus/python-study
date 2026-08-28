from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {
    "1": {
        "title": "Flask 복습",
        "done": False
    },
    "4": {
        "title": "Ajax 연결",
        "done": False
    }
}

@app.route("/tasks/<task_id>/complete", methods=["POST"])
def changeDone(task_id):
    if task_id in tasks:
        tasks[task_id]["done"] = True

        return jsonify(tasks[task_id])


















