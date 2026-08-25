from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def first():
    return render_template("input.html")

@app.route("/search")
def second():
    search1 = request.args.get("name1")
    search2 = request.args.get("name2")

    return render_template("result.html", name1=search1, name2=search2)

if __name__ == "__main__":
    app.run(debug=True)