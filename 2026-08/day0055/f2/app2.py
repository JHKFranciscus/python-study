from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

memos = []
memo_id = 1

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/memo", methods=["GET", "POST"])
def addMemo():
    global memo_id

    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        new_memo = {
            "id": memo_id,
            "title": title,
            "content": content,
        }

        memo_id += 1

        memos.append(new_memo)

        return jsonify("success")

    elif request.method == "GET":
        return jsonify(memos)

if __name__ == "__main__":
    app.run(debug=True)