from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"


@app.route("/books", methods=["GET", "POST"])
def books():
    if request.method == "GET":
        return "Book List"

    if request.method == "POST":
        return "Book Created"

@app.route("/books/<int:book_id>")
def book_detail(book_id):
    return f"Book {book_id}"