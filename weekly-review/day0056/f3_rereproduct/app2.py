from flask import Flask, request, render_template

app = Flask(__name__)

scores = {
    "minsu": 70,
    "jisu": 85
}

@app.route("/")
def home():
    return render_template("index2.html", scores=scores)

@app.route("/add", methods=["POST"])
def addScores():
    addName = request.form.get("name")
    addScore = request.form.get("score")

    scores[f"{addName}"] = addScore

    return render_template("index2.html", scores=scores)

@app.route("/search")
def searchScores():
    searchName = f"{request.args.get("searchName")}"

    if searchName in scores:
        return render_template("index2.html", scores=scores, searchName=searchName, searchScore=scores[searchName])

    else:
        missName = "존재하지 않는 이름입니다."
        return render_template("index2.html", scores=scores, missName=missName)


if __name__ == "__main__":
    app.run(debug=True)