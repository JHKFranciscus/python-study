from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["test0914"]
reservations = db["reservations"]

allowed_field = ["name", "room", "date", "purpose"]
allowed_room = ["A", "B", "C"]



@app.route("/")
def home():
    return render_template("app1.html")

@app.route("/reservation", methods=["POST"])
def add_reservation():
    new_reservation = request.get_json()["new_reservation"]

    add_reservation = {}

    for field in allowed_field:
        if field not in new_reservation or new_reservation[field] == "":
            return jsonify(
                {"err": f"invalid {field}"}
            ), 400

    if new_reservation["room"] not in allowed_room:
        return jsonify(
            {"err": "invalid room"}
        ), 400

    for field in allowed_field:
        if field in new_reservation:
            add_reservation[field] = new_reservation[field]

    reservations.insert_one(add_reservation)

    return jsonify(
        {"result": "add success"}
    )

@app.route("/reservations", methods=["GET"])
def reserve_rooms():
    room = request.args.get("room")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    sort = request.args.get("sort")

    query = {}

    if room:
        query["room"] = room

    date_query= {}

    if start_date:
            date_query["$gte"] = start_date

    if end_date:
            date_query["$lte"] = end_date

    if date_query:
        query["date"] = date_query

    cursor = reservations.find(query)

    if sort == "nearest":
        cursor = cursor.sort("date", 1)
    elif sort == "latest":
        cursor = cursor.sort("date", -1)

    reservations_list = list(cursor)

    for reservation in reservations_list:
        reservation["_id"] = str(reservation["_id"])

    return jsonify(
        {"reservations": reservations_list}
    )


@app.route("/reservation/<reservation_id>", methods=["PATCH"])    
def edit_reservation(reservation_id):
    update_reservation = request.get_json()["editReservation"]

    edit_reservation = {}

    if "room" in update_reservation:
        if update_reservation["room"] not in allowed_room:
            return jsonify(
                {"err": "invalid room"}
            ), 400

    print(update_reservation)

    for field in allowed_field:
        if field in update_reservation:
            edit_reservation[field] = update_reservation[field]

    print()
    print(edit_reservation)

    update_result = reservations.update_one(
        {"_id": ObjectId(reservation_id)},
        {"$set": edit_reservation}
    )

    if update_result.matched_count == 0:
        return jsonify(
            {"err": "Not In Document"}
        ), 404

    return jsonify(
        {"result": "update success"}
    )


@app.route("/reservation/<reservation_id>", methods=["DELETE"])    
def del_reservation(reservation_id):    
    delete_result = reservations.delete_one(
        {"_id": ObjectId(reservation_id)}
    )

    if delete_result.deleted_count == 0:
        return jsonify(
            {"err": "Not In Document"}
        ), 404

    return jsonify(
        {"result": "delete success"}
    )




if __name__ == "__main__":
    app.run(debug=True)