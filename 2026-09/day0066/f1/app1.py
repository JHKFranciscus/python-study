from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId


app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["test0909"]
studies = db["studies"]

@app.route("/api/studies/<study_id>", methods=["PATCH"])
def update_study(study_id):
    data = request.get_json()

    db.studies.update_one(
        {"_id": ObjectId(study_id)},
        {"$set": {"minutes": data["minutes"]}}
    )


    return jsonify(
        {"message": "수정 완료"}
    )