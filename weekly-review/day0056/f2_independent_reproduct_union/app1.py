from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

tasks =[
    {"title": "Python 공부", "done": False},
    {"title": "Flask 복습", "done": True}
]



@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/loadTasks")
def loadTasks():
    return jsonify(tasks)


@app.route("/addTask", methods=["POST"])
def addTasks():
    title = request.form.get("title")

    new_task = {
        "title": title,
        "done": False,
    }

    tasks.append(new_task)

    return jsonify({
        "result": "success"
    })


@app.route("/changeTaskDone/<int:task_id>", methods=["POST"])
def changeTaskDone(task_id):
    for i in range(len(tasks)):
        task = tasks[i]
        if task_id == i:
            if task["done"] == True:
                task["done"] = False
                return jsonify({
                    "result": "success"
                    })

            else:
                task["done"] = True
                return jsonify({
                    "result": "success"
                    })


if __name__ == "__main__":
    app.run(debug=True)