from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["study_shop"]
movies = db["movies"]


@app.route("/")
def home():
    movies_list = list(movies.find())

    return render_template("f3_home.html", movies=movies_list)


@app.route("/movie", methods=["GET", "POST"])
def create_movie():
    if request.method == "GET":
        return render_template("f3_create.html")

    elif request.method == "POST":
        title = request.form["title"]
        year = int(request.form["year"])
        rating = int(request.form["rating"])

        new_movie = {
            "title": title,
            "year": year,
            "rating": rating
        }

        movies.insert_one(new_movie)

        return redirect(url_for("home"))


@app.route("/movie/<movie_id>/detail")
def detail_movie(movie_id):
    find_movie = movies.find_one(
        {"_id": ObjectId(movie_id)}
    )

    return render_template("f3_detail.html", movie=find_movie)


@app.route("/movie/<movie_id>/edit", methods=["GET", "POST"])
def edit_movie(movie_id):
    if request.method == "GET":
        find_movie = movies.find_one(
            {"_id": ObjectId(movie_id)}
        )

        return render_template("f3_edit.html", movie=find_movie)

    elif request.method == "POST":
        title = request.form["title"]
        year = int(request.form["year"])
        rating = int(request.form["rating"])

        movies.update_one(
            {"_id": ObjectId(movie_id)},
            {"$set": {
                "title": title,
                "year": year,
                "rating": rating
            }}
        )

        return redirect(url_for("home"))


@app.route("/movie/<movie_id>/delete", methods=["POST"])
def delete(movie_id):
    movies.delete_one(
        {"_id": ObjectId(movie_id)}
    )

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)