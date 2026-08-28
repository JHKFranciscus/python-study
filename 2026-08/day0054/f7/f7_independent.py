from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

books = [
    {
        "id": "1",
        "title": "Python",
        "favorite": False
    },
    {
        "id": "5",
        "title": "Flask",
        "favorite": True
    }
]



@app.route("/")
def home():
    return render_template("f7_independent.html", books=books)


@app.route("/books/favorite", methods=["POST"])
def changeFavorite():
    book_id = request.form.get("book_id")

    for book in books:
        if book_id == book["id"]:
            if book["favorite"] == False:
                book["favorite"] = True
                return jsonify(book)
            else:
                book["favorite"] = False
                return jsonify(book)

if __name__ == "__main__":
    app.run(debug=True)
    

