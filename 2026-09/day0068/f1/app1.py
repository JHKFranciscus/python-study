from flask import Flask, request, render_template,jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["test0910"]
books = db["books"]

allowed_category = ["programming", "novel", "essay"]
allowed_sort = ["latest", "oldest"]


@app.route("/")
def home():
    return render_template("app1.html")

@app.route("/books", methods=["GET", "POST"])
def find_add_books():
    if request.method == "POST":
        data = request.get_json()

        new_title = data.get("new_title")
        new_category = data.get("new_category")
        new_read_date = data.get("new_read_date")
        new_pages = data.get("new_pages")

        if new_category and new_category not in allowed_category:
            return jsonify(
                {"result": "invalid category"}
            ), 400

        books.insert_one(
            {"title": new_title,
             "category": new_category,
             "read_date": new_read_date,
             "pages": new_pages}
        )

        return jsonify(
            {"result": "add success"}
        )

    elif request.method == "GET":
        category = request.args.get("category")
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        sort = request.args.get("sort")

        query = {}

        if category:
            if category not in allowed_category:
                return jsonify(
                    {"result": "invalid category"}
                    ), 400
            query["category"] = category

        if sort and sort not in allowed_sort:
            return jsonify(
                {"result": "invalid sort"}
                ), 400

        query_date = {}

        if start_date and end_date and start_date > end_date:
            return jsonify(
                {"result": "invalid read_date"}
                ), 400

        if start_date:
            query_date["$gte"] = start_date

        if end_date:
            query_date["$lte"] = end_date

        if query_date:
            query["read_date"] = query_date

        sort_direction = -1

        if sort == "oldest":
            sort_direction = 1

        books_list = list(books.find(query).sort("read_date", sort_direction))

        for book in books_list:
            book["_id"] = str(book["_id"])

        return jsonify(
            {"books_list": books_list}
        )


@app.route("/books/<book_id>", methods=["PATCH"])
def update_book(book_id):
    update_datas = request.get_json()
    update_data = update_datas.get("update_data")

    update_title = update_data.get("update_title")
    update_category = update_data.get("update_category")
    update_read_date = update_data.get("update_read_date")
    update_pages = update_data.get("update_pages")

    update_query = {}

    if "update_title" in update_data:
            update_query["title"] = update_title

    if "update_category" in update_data:
            if update_category not in allowed_category:
                 return jsonify({
                    "error": "invalid category"
                })
            update_query["category"] = update_category

    if "update_read_date" in update_data:
            update_query["read_date"] = update_read_date
    
    if "update_pages" in update_data:
            update_query["pages"] = update_pages

    if not update_query:
        return jsonify({"error": "invalid query"}), 400

    try:
        book_id = ObjectId(book_id)
    except:
        return jsonify({
            "error": "잘못된 id 형식입니다."
        }), 400

    update_result = books.update_one(
        {"_id": book_id},
        {"$set": update_query}
    )

    if update_result.matched_count == 0:
        return jsonify({
            "error": "기록을 찾을 수 없습니다."
        }), 404

    return jsonify({
            "result": "update success"
        })

@app.route("/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    books.delete_one(
        {"_id": ObjectId(book_id)},
    )

    return jsonify(
            {"result": "delete success"}
        )



if __name__ == "__main__":
    app.run(debug=True)


