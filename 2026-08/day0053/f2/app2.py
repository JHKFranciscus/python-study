from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)

books = [
    {"id": 1, "title": "Python 기초", "author": "김철수"},
    {"id": 3, "title": "Flask 입문", "author": "이영희"},
    {"id": 8, "title": "JavaScript 기초", "author": "박민수"},
]

@app.route("/")
def home():
    return redirect(url_for("startpoint"))


@app.route("/books/all")
def startpoint():
    return render_template("all.html", books=books)


@app.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
def edit(book_id):
    for book in books:
        if book["id"] == book_id:

            if request.method == "GET":
                return render_template("edit.html", book=book)

            elif request.method == "POST":
                new_title = request.form.get("title")
                new_author = request.form.get("author")

                book["title"] = new_title
                book["author"] = new_author

                return redirect(url_for("detail", book_id=book["id"]))


@app.route("/books/<int:book_id>/detail")
def detail(book_id):
    for book in books:
        if book["id"] == book_id:
            return render_template("deep.html", book=book)

    return "책을 찾을 수 없습니다.", 404


@app.route("/books/<int:book_id>/delete", methods=["POST"])
def delBook(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            break

    return redirect(url_for("startpoint"))


if __name__ == "__main__":
    app.run(debug=True)