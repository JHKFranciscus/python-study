from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["test0911"]
records = db["records"]

allowed_subject = ["Python", "JavaScript", "CS", "SSAFY"]
allowed_sort = ["latest", "oldest"]

@app.route("/")
def home():
    return render_template("app2.html")

@app.route("/record", methods=["GET", "POST"])
def find_add_record():
    if request.method == "POST":
        new_record = request.get_json().get("new_record")

        new_subject = new_record.get("new_subject")
        new_study_date = new_record.get("new_study_date")
        new_minutes = new_record.get("new_minutes")
        new_memo = new_record.get("new_memo")

        if new_subject not in allowed_subject:
            return jsonify(
                {"err": "invalid subject"}
            ), 400

        add_record = {
            "subject": new_subject,
            "study_date": new_study_date,
            "minutes": new_minutes,
            "memo": new_memo
        }

        records.insert_one(add_record)

        return jsonify(
            {"result": "add success"}
        )


    if request.method == "GET":
        subject = request.args.get("subject")
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        sort = request.args.get("sort")

        query = {}

        if subject and subject not in allowed_subject:
            return jsonify(
                {"err": "invalid subject"}
            ), 400

        if subject:
            query["subject"] = subject

        if start_date and end_date and start_date > end_date:
            return jsonify(
                {"err": "invalid date"}
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
                {"err": "invalid sort"}
            ), 400

        sort_direction = -1

        if sort == "oldest":
            sort_direction = 1

        records_list = list(records.find(query).sort("study_date", sort_direction))

        for record in records_list:
            record["_id"] = str(record["_id"])

        return jsonify(
            {"records": records_list}
        )

@app.route("/record/<record_id>", methods=["PATCH"])
def update_record(record_id):
        try:
            record_id = ObjectId(record_id)
        except:
            return jsonify({
                "err": "invalid id type"
            }), 400
        
        u_record = request.get_json().get("update_record")

        u_data = {}

        if "subject" in u_record:
            if u_record["subject"] not in allowed_subject:
                return jsonify(
                    {"err": "Winvalid subject"}
                ), 400
            u_data["subject"] = u_record["subject"]

        if "study_date" in u_record:
            u_data["study_date"] = u_record["study_date"]

        if "minutes" in u_record:
            u_data["minutes"] = u_record["minutes"]

        if "memo" in u_record:
            u_data["memo"] = u_record["memo"]

        update_result = records.update_one(
            {"_id": record_id},
            {"$set": u_data
        )

        if update_result.matched_count == 0:
            return jsonify(
                {"err": "Not In Record"}
            ), 404

        return jsonify(
            {"result": "update success"}
        )

@app.route("/record/<record_id>", methods=["DELETE"])
def delete_record(record_id):
        try:
            record_id = ObjectId(record_id)
        except:
            return jsonify({
                "err": "invalid id type"
            }), 400

        delete_result = records.delete_one(
            {"_id": record_id}
        )

        return jsonify(
            {"result": "delete success"}
        )

if __name__ == "__main__":
    app.run(debug=True)