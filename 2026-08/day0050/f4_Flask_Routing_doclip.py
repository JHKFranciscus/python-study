from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home ():
    return "Member Server"

@app.route("/status")
def member ():
    return "Server Running"


@app.route("/members/<int:member_id>", methods=["GET", "POST"])
def member_id (member_id):
    if request.method == "GET":
        return f"Member {member_id}"

    if request.method == "POST":
        return f"Member {member_id} Updated"