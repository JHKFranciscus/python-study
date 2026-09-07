from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = ("mongodb://localhost:27017/")
db = client["records0907"]
records = db["records"]


#1.
@app.route("/api/records", methods=["GET"])
def get_records1():
    selected_value = request.args.get("filter")

    search_condition = {}

    if selected_value:
        search_condition["subject"] = selected_value

    result_cusor = db.records.find(search_condition)

    record_list = list(result_cusor)

    for record in record_list:
        record["_id"] = str(record["_id"])

    return jsonify(record_list)


# 2. /api/records?filter=JavaScript&order=minutes&direction=desc
@app.route("/api/records", methods=["GET"])
def get_records2():
    selected_subject = request.args.get("filter")
    selected_order = request.args.get("order")
    selected_direction = request.args.get("direction")
    search_condition = {}

    if selected_subject:
        search_condition["subject"] = selected_subject

    result_cursor = db.records.find(search_condition)

    sort_direction = 1

    if selected_direction == "desc":
        sort_direction = -1

    if selected_order == "minutes":
        result_cursor = result_cursor.sort(
            selected_order,
            sort_direction
        )

    record_list = list(result_cursor)

    for record in record_list:
        record["_id"] = str(record["_id"])

    return jsonify(record_list)