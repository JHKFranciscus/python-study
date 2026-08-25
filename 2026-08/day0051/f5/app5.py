from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def first():
    return render_template("form.html")

@app.route("/results", methods=["POST"])
def second():
    username = request.form.get("username")
    usergame = request.form.get("usergame")
    return render_template("result.html", username=username, usergame=usergame)

if __name__ == "__main__":
    app.run(debug=True)