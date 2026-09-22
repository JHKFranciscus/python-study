from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["test0922"]
issues = db["issues"]

allowed_category = ["network", "computer", "facility"]
allowed_priority = ["low", "normal", "high"]
allowed_status = ["reported", "processing", "done"]



@app.route("/")
def home():
    return render_template("app1.html")

@app.route("/issue", methods=["POST"])
def add_issue():
    issue = request.get_json()["new_issue"]     #dictionary

    allowed_list = ["title", "location", "category", "priority", "report_date"]


    for field in allowed_list:
        if field not in issue:
            return jsonify(
                {"error": f"Not in ${field}"}
            ), 400
        
        elif issue[field] == "":
            return jsonify(
                {"error": f"invalid ${field}"}
            ), 400

    if issue["category"] not in allowed_category:
        return jsonify(
            {"error": "invalid category"}
        ), 400

    if issue["priority"] not in allowed_priority:
        return jsonify(
            {"error": "invalid priority"}
        ), 400

    new_issue = {
        "title": issue.get("title"),
        "location": issue.get("location"),
        "category": issue.get("category"),
        "priority": issue.get("priority"),
        "report_date": issue.get("report_date"),
        "memo": issue.get("memo"),
        "status": "reported",
    }

    issues.insert_one(new_issue)

    return jsonify(
        {"result": "add success"}
    ), 201


@app.route("/issues", methods=["GET"])
def load_issues():
    category = request.args.get("category")
    priority = request.args.get("priority")
    status = request.args.get("status")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    sort = request.args.get("sort")

    allowed_sort = ["oldest", "latest"]

    query = {}
    date_query = {}

    if category and category not in allowed_category:
        return jsonify(
            {"error": "invalid category"}
        ), 400

    if priority and priority not in allowed_priority:
        return jsonify(
            {"error": "invalid priority"}
        ), 400

    if status and status not in allowed_status:
        return jsonify(
            {"error": "invalid status"}
        ), 400

    if sort and sort not in allowed_sort:
        return jsonify(
            {"error": "invalid sort"}
        ), 400

    if category:
        query["category"] = category

    if priority:
        query["priority"] = priority

    if status:
        query["status"] = status

    if start_date:
        date_query["$gte"] = start_date

    if end_date:
        date_query["$lte"] = end_date

    if date_query:
        query["report_date"] = date_query

    find_issues = issues.find(query)

    if sort:
        if sort == "oldest":
            find_issues = find_issues.sort("report_date", 1)
        else:
            find_issues = find_issues.sort("report_date", -1)

    issues_list = list(find_issues)

    for issue in issues_list:
        issue["_id"] = str(issue["_id"])

    return jsonify(
        {"issues_list": issues_list}
    )

@app.route("/issue/<issue_id>", methods=["PATCH"])
def edit_issue(issue_id):
    try:
        issue_id = ObjectId(issue_id)
    except:
        return jsonify(
            {"error": "invalid id"}
        ), 400
    
    update_status = request.get_json().get("update_status")

    if not update_status:
        return jsonify(
            {"error": "Not in status"}
        ), 400

    if update_status not in allowed_status:
        return jsonify(
            {"error": "invalid status"}
        ), 400

    update_result = issues.update_one(
        {"_id": issue_id},
        {"$set": {"status": update_status}}
    )

    if update_result.matched_count == 0:
        return jsonify(
            {"error": "Not in document"}
        ), 404

    return jsonify(
        {"result": "update success"}
    )

@app.route("/issue/<issue_id>", methods=["DELETE"])
def delete_issue(issue_id):
    try:
        issue_id = ObjectId(issue_id)
    except:
        return jsonify(
            {"error": "invalid id"}
        ), 400

    delete_result = issues.delete_one(
        {"_id": issue_id}
    )

    if delete_result.deleted_count == 0:
        return jsonify(
            {"error": "Not in document"}
        ), 404

    return jsonify(
        {"result": "delete success"}
    )



if __name__ == "__main__":
    app.run(debug=True)