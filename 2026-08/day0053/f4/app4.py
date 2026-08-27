from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)

tasks = {
    "python": {
        "title": "Python 복습",
        "done": False
    },
    "flask": {
        "title": "Flask form 복습",
        "done": False
    },
    "http": {
        "title": "HTTP 정리",
        "done": True
    }
}


@app.route("/")
def start():
    return render_template("start.html", tasks=tasks)


@app.route("/code/create", methods=["POST"])
def createC():
    new_code = request.form.get("code")
    new_title = request.form.get("title")

    tasks[new_code] = {
        'title': new_title,
        'done': False
    }

    return redirect(url_for("start"))


@app.route("/code/<task_id>/check", methods=["POST"])
def checkC(task_id):
    if task_id in tasks:
        tasks[task_id]["done"] = True
        return redirect(url_for("start"))

    return "할 일을 찾을 수 없습니다.", 404


@app.route("/code/<task_id>/delete", methods=["POST"])
def deleteC(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return redirect(url_for("start"))

    return "할 일을 찾을 수 없습니다.", 404


if __name__ == "__main__":
    app.run(debug=True)