from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {
    "3": {
        "title": "Flask",
        "done": False
    }
}


@app.route("/tasks/<task_id>/title", methods=["POST"])
def changeTitle(task_id):
    title = request.form.get("title")

    if task_id in tasks:
        tasks[task_id]["title"] = title

        task = tasks[task_id]

        return jsonify(task)

