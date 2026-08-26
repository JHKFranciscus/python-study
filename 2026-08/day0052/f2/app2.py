from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

books = [
    {"id": 1, "title": "파이썬 기초", "price": 18000},
    {"id": 2, "title": "Flask 입문", "price": 22000}
]



@app.route("/")
def home():
    return redirect(url_for("queryAndAdd"))

@app.route("/start", methods=["GET", "POST"])
def queryAndAdd():
    if request.method == "GET":
        return render_template("start.html", books=books)

    if request.method == "POST":
        title = request.form.get("inputTitle")
        price = int(request.form.get("inputPrice"))

        book_id = len(books)+1

        new_book = {
            "id": book_id,
            "title": title,
            "price": price
        }

        books.append(new_book)

        return redirect("/start")


@app.route("/detail/<int:book_id>")
def book_detail(book_id):
    for book in books:
        if book_id == book["id"]:
            return render_template("detail.html", book=book)

if __name__ == "__main__":
    app.run(debug=True)

