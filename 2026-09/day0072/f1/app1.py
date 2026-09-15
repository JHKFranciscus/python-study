from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["test0915"]
items = db["items"]

all_field = ["company", "position", "deadline", 'stage', "memo"]
allowed_field = ["company", "position", "deadline", "stage"]
allowed_stage = ["planned", "submitted", "interview", "finished"]


@app.route("/")
def home():
    return render_template("app1.html")

@app.route("/application", methods=["POST"])
def add_item():
    item_status = request.get_json()["new_item"]

    for field in allowed_field:
        if item_status[field] == "":
            return jsonify(
                {"error": "invalid value"}
            ), 400
        
    new_item = {}

    stage = item_status["stage"]

    if stage not in allowed_stage:
        return jsonify(
            {"error": "invalid value"}
        ), 400

    for field in all_field:
        if field in item_status:
            new_item[field] = item_status[field]

    items.insert_one(new_item)

    return jsonify(
        {"result": "add success"}
    )

@app.route("/applications", methods=["GET"])
def show_items():
    stage = request.args.get("stage")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    sort = request.args.get("sort")

    query = {}

    if stage:
        query["stage"] = stage

    date_query = {}

    if start_date:
        date_query["$gte"] = start_date

    if end_date:
        date_query["$lte"] = end_date

    if date_query:
        query["deadline"] = date_query

    cursor = items.find(query)

    if sort == "nearest":
        cursor = cursor.sort("deadline", 1)
    elif sort == "latest":
        cursor = cursor.sort("deadline", -1)

    items_list = list(cursor)

    for result in items_list:
        result["_id"] = str(result["_id"])

    return jsonify(
        {"items_list": items_list}
    )

@app.route("/application/<application_id>", methods=["PATCH"])
def edit_item(application_id):
    try:
        application_id = ObjectId(application_id)
    except:
        return jsonify(
            {"error": "invalid Id"}
        ), 400
    
    item = request.get_json()["update_item"]

    for field in allowed_field:
        if item[field] == "":
            return jsonify(
                {"error": "invalid value"}
            ), 400

    stage = item["stage"]

    if stage not in allowed_stage:
        return jsonify(
            {"error": "invalid value"}
        ), 400

    update_item = {}

    for field in all_field:
        if field in item:
            update_item[field] = item[field]

    update_result = items.update_one(
        {"_id": application_id},
        {"$set": update_item}
    )

    if update_result.matched_count == 0:
        return jsonify(
            {"error": "Not In Document"}
        ), 404

    return jsonify(
        {"result": "update success"}
    )

@app.route("/application/<application_id>", methods=["DELETE"])
def del_item(application_id):
    try:
        application_id = ObjectId(application_id)
    except:
        return jsonify(
            {"error": "invalid Id"}
        ), 400

    delete_result = items.delete_one(
        {"_id": application_id}
    )

    if delete_result.deleted_count == 0:
        return jsonify(
            {"error": "Not In Document"}
        ), 404

    return jsonify(
        {"result": "delete success"}
    )


if __name__ == "__main__":
    app.run(debug=True)