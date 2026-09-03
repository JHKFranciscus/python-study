from pymongo import MongoClient
from flask import Flask, request, render_template, redirect, url_for
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["study_shop"]
games = db["games"]

@app.route("/")
def home():
    games_list = list(games.find())

    return render_template("f2_start_point.html", games=games_list)

@app.route("/game", methods=["POST"])
def add_game():
    name = request.form["name"]
    price = int(request.form["price"])

    new_game = {
        "name": name,
        "price": price
    }

    games.insert_one(new_game)

    return redirect(url_for("home"))

@app.route("/game/<game_id>/edit", methods=["GET", "POST"])
def update_game(game_id):
    if request.method == "GET":
        find_game = games.find_one(
            {"_id": ObjectId(game_id)}
        )

        return render_template("f2_edit.html", game=find_game)

    elif request.method == "POST":
        name = request.form["name"]
        price = int(request.form["price"])

        games.update_one(
            {"_id": ObjectId(game_id)},
            {"$set": {
                "name": name,
                "price": price
            }}
        )

        return redirect(url_for("home"))

@app.route("/game/<game_id>/delete", methods=["POST"])
def delete_game(game_id):
    games.delete_one(
        {"_id": ObjectId(game_id)}
    )

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)