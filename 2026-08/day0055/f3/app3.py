from flask import Flask, request, render_template, jsonify

app = Flask("__name__")



do_works = [
    {"id": 1, "text": "Flask 복습", "done": False},
    {"id": 2, "text": "Ajax 복습", "done": True},
    {"id": 3, "text": "DOM 복습", "done": False},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/do_works")
def loadAll():
    return (do_works)

@app.route("/change-status/<int:statusId>", methods=["POST"])
def changeDone(statusId):
    for work in do_works:
        if work["id"] == statusId:
            if work["done"] == False:
                work["done"] = True
                return jsonify("success")

            elif work["done"] == True:
                work["done"] = False
                return jsonify("success")


if __name__ == "__main__":
    app.run(debug=True)