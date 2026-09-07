from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = ["test0907"]

@app.route("/api/records", methods=["GET"])
def get_records():
    received_value = request.args.get("filter")

    mongo_condition = {
        "subject": received_value
    }

    mongo_cursor = db.records.find(mongo_condition)

    result_list = list(mongo_cursor)

    for one_record in result_list:
        one_record["_id"] = str(one_record["_id"])

    return jsonify(result_list)