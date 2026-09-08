from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["independent0908"]
books = db["books"]

category_array = ["novel", "essay", "science"]

@app.route("/")
def home():
    return render_template("app1.html")

@app.route("/books", methods=["GET"])
def load_books():
    borrow_date = request.args.get("borrow_date")
    category = request.args.get("category")

    if category and category not in category_array:
        return jsonify({"result": "invalid category"}), 400

    query = {}

    if borrow_date:
        query["borrow_date"] = borrow_date

    if category:
        query["category"] = category

    book_list = list(books.find(query))

    for book in book_list:
        book["_id"] = str(book["_id"])

    return jsonify(
        {"books": book_list}
    )

if __name__ == "__main__":
    app.run(debug=True)