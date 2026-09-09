from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["test0909"]
records = db["records"]

department_list = ["frontend", "backend", "infra"]
status_list = ["waiting", "working", "done"]

@app.route("/")
def home():
    records_list = list(records.find())

    return jsonify(
        {"records": records_list}
    )

@app.route("/record")
def selected_record():
    department = request.args.get("department")
    status = request.args.get("status")

    if department and department not in department_list:
        return jsonify(
            {"invalid dapartment"}
        ), 400

    if status and status not in status_list:
        return jsonify(
            {"invalid status"}
        ), 400

    records_list = list(records.find())

    for record in records_list:
        record["_id"] = str(record["_id"])

    return jsonify(
        {"records": records_list}
    )


@app.route("/record/<record_id>")
def update_record(record_id):
    record_status = request.form["status"]

    records.update_one(
        {"_id": ObjectId(record_id)},
        {"$set": {"status": record_status}}
    )

    return jsonify(
        {"result": "update success"}
    )

@app.route("/record/<record_id>")
def delete_record(record_id):
    records.delete_one(
        {"_id": ObjectId(record_id)}
    )

    return jsonify(
        {"result": "delete success"}
    )


if __name__ == "__main__":
    app.run(debug=True)