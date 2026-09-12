from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["test0912"]
records = db["records"]

allowed_subject = ["Python", "JavaScript", "CS", "SSAFY"]
allowed_sort = ["latest", "oldest"]

@app.route("/")
def home():
    return render_template("app1.html")


@app.route("/record", methods=["POST"])
def add_record():
    new_record = request.get_json().get("new_record")

    new_subject = new_record["subject"]
    new_study_date = str(new_record["study_date"])
    new_minutes = int(new_record["minutes"])
    new_memo = new_record["memo"]

    if new_subject and new_subject not in allowed_subject:
        return jsonify(
            {"error": "invalid subject"}
        ), 400

    result = records.insert_one({
        "subject": new_subject,
        "study_date": new_study_date,
        "minutes": new_minutes,
        "memo": new_memo
    })

    return jsonify(
        {"result": "create success"}
    ), 201


@app.route("/records")
def find_records():
    subject = request.args.get("subject")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    sort = request.args.get("sort")

    if subject and subject not in allowed_subject:
        return jsonify(
            {"error": "invalid subject"}
        ), 400

    query = {}

    if subject:
        query["subject"] = subject

    if start_date and end_date and start_date > end_date:
        return jsonify(
            {"error": "start_date > end_date"}
        ), 400

    date_query = {}

    if start_date:
        date_query["$gte"] = start_date

    if end_date:
        date_query["$lte"] = end_date

    if date_query:
        query["study_date"] = date_query

    if sort and sort not in allowed_sort:
        return jsonify(
            {"error": "invalid sort"}
        ), 400

    sort_directrion = -1

    if sort == "oldest":
        sort_directrion = 1

    records_list = list(records.find(query).sort("study_date", sort_directrion))

    for record in records_list:
        record["_id"] = str(record["_id"])

    return jsonify(
        {"result": records_list}
    )


@app.route("/records/<record_id>", methods=["PATCH"])
def edit_record(record_id):
    update_record = request.get_json()["update_record"]

    if update_record["subject"] and update_record["subject"] not in allowed_subject:
        return jsonify(
            {"error": "invalid subject"}
        ), 400

    query = {}

    if "subject" in update_record:
        query["subject"] = update_record["subject"]

    if "subject" in update_record:
        query["subject"] = update_record["subject"]

    if "subject" in update_record:
        query["subject"] = update_record["subject"]

    if "subject" in update_record:
        query["subject"] = update_record["subject"]

    if "subject" in update_record:
        query["subject"] = update_record["subject"]

    if not query:
        return jsonify(
            {"error": "수정 field 없음"}
        ), 400

    try:
        record_id = ObjectId(record_id)
    except:
        return jsonify(
            {"error": "invalid ObjectId"}
        ), 400

    update_result = records.update_one(
        {"_id": record_id},
        {"$set": query}
    )

    if update_result.matched_count == 0:
        return jsonify(
            {"error": "document 없음"}
        ), 404

    return jsonify(
        {"result": "update success"}
    )


@app.route("/record/<record_id>")
def del_record(record_id):
    try:
        record_id = ObjectId(record_id)
    except:
        return jsonify(
            {"error": "invalid ObjectId"}
        ), 400

    delete_result = records.delete_one(
        {"_id": record_id}
    )

    if delete_result.deleted_count == 0:
        return jsonify(
            {"error": "document없음"}
        ), 404

    return jsonify(
        {"result": "delete success"}
    )




if __name__ == "__main__":
    app.run(debug=True)