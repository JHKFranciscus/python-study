from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

books = [
    {"id": 1, "title": "파이썬 기초", "price": 18000},
    {"id": 2, "title": "Flask 입문", "price": 22000}
]

@app.route("/")
def start():
    return render_template("start.html")

@app.route("/all")
def all():
    return render_template("query.html", books=books)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    price = int(request.form.get("price"))

    new_book = {"id": 1, "title": title, "price": price}

    books.append(new_book)

    return redirect(url_for('all'))

if __name__ == "__main__":
    app.run(debug=True)