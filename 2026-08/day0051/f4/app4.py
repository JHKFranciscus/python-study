from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    nickname = request.form.get("nickname")
    return render_template("result.html", nickname=nickname)

if __name__ == "__main__":
    app.run(debug=True)