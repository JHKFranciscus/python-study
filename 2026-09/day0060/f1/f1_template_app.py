from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["study_shop"]
books = db["books"]

message = "Flask에서 보낸 값"

@app.route("/")
def home():
    books_list = list(books.find())
    
    return render_template(
        "f1_index.html",
        text=message, books=books_list
        )

@app.route("/books", methods=["POST"])
def create():
    title = request.form["title"]
    price = int(request.form["price"])

    new_book = {
        "title": title,
        "price": price
    }

    create_book = books.insert_one(new_book)

    return redirect(url_for("home"))

@app.route("/books/<book_id>/edit", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "GET":
        ubook = books.find_one(
        {"_id": ObjectId(book_id)}
    )

        return render_template("f1_edit.html", ubook=ubook)

    elif request.method == "POST":
        title = request.form["title"]
        price = int(request.form["price"])

        update_book = books.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": {"title": title, "price": price}}
        )

        return redirect(url_for("home"))

@app.route("/books/<book_id>/delete", methods=['POST'])
def delete_book(book_id):
    delete_book = books.delete_one(
        {"_id": ObjectId(book_id)}
    )

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)