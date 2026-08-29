from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

memos = []
memoId = 1

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/memo", methods=["GET", "POST"])
def addMemo():
    global memoId

    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        memo = {
            "id": memoId,
            "title": title,
            "content": content,
        }

        memoId += 1

        memos.append(memo)

        return jsonify({
            "result": "success",
        })

    elif request.method == "GET":
        return jsonify({
            "result": "success",
            "memos": memos,
        })

if __name__ == "__main__":
    app.run(debug=True)