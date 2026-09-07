from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["test0907"]
studies = db["studies"]

@app.route("/")
def home():
    return render_template("app5.html")

@app.route("/api/lectures")
def view_lectures():
    level_filter = request.args.get("level_filter")
    sort_by = request.args.get("sort_by")

    search_condition = {}

    if level_filter:
        search_condition["level"] = level_filter

    studies_list = studies.find(search_condition)

    if sort_by:
        studies_list = studies_list.sort("duration", 1)

    studies_list = list(studies_list)

    for study in studies_list:
        study["_id"] = str(study["_id"])

    return jsonify(studies_list)

if __name__ == "__main__":
    app.run(debug=True)

