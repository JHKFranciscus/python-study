# @app.patch("/schedule/<schedule_id>", methods=["PATCH"])
# def update_schedule(schedule_id):
#     item = request.get_json()

#     allowed_priority = ["low", "normal", "high"]

#     update_data = {}

#     if "title" in item:
#         update_data["title"] = item["title"]

#     if "deadline" in item:
#         update_data["deadline"] = item["deadline"]

#     if "priority" in item:
#         if item["priority"] not in allowed_priority:
#             return jsonify(
#                 {"error": "invalid priority"}
#             ), 400

#     if "memo" in item:
#         update_data["memo"] = item["memo"]


#     schedules.update_one(
#         {"_id": ObjectId(schedule_id)},
#         {"$set": update_data}
#     )

#     return jsonify({"result": "success"})