from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["test0906"]
items = db["items"]


@app.route("/")
def home():

    return render_template("app.html")


@app.route("/item", methods=["POST", "GET"])
def add_find_item():
    if request.method == "POST":
        item = request.get_json()

        new_item = {
            "name": item["name"],
            "quantity": int(item["quantity"])
        }

        items.insert_one(new_item)

        return jsonify({
            "result": "add success"
        })

    elif request.method == "GET":
        items_list = list(items.find())

        for item in items_list:
            item["_id"] = str(item["_id"])

        return jsonify({
            "items": items_list
        })


@app.route("/item/<item_id>", methods=["PATCH"])
def update_item(item_id):
    update_data = request.get_json()

    items.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {"quantity": int(update_data["quantity"])}}
    )

    return jsonify({
        "result": "update success"
    })


@app.route("/item/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    items.delete_one(
        {"_id": ObjectId(item_id)}
    )

    return jsonify({
        "result": "delete success"
    })


if __name__ == "__main__":
    app.run(debug=True)