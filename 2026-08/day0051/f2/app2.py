from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def first():
    return render_template("index2.html")

@app.route("/search")
def second():
    search = request.args.get("keyword")
    return search 

if __name__ == "__main__":
    app.run(debug=True)