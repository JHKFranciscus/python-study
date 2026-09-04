from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['movie_db']
movies = db['movies']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/movies", methods=["GET", "POST"])
def get_Movies():
    if request.method == "GET":
        movie_list = list(movies.find())

        for movie in movie_list:
            movie['_id'] = str(movie['_id'])

        return jsonify(
            {
                "movies": movie_list
            }
        )

    elif request.method == "POST":
        data = request.get_json()

        title = data['title']

        movies.insert_one({
            "title": title
        })

        return jsonify({"message": "등록완료"})

@app.route('/api/movies/<movie_id>', methods=['PATCH'])
def update_movie(movie_id):
    data = request.get_json()
    new_title = data['title']

    movies.update_one(
        {'_id': ObjectId(movie_id)},
        {'$set': {'title': new_title}}
    )

    return jsonify({
        'message': '수정완료'
    })

@app.route('/api/movies/<movie_id>', methods=["DELETE"])
def delete_movie(movie_id):
    movie_id = ObjectId(movie_id)

    movies.delete_one(
        {'_id': movie_id}
    )

    return jsonify({
        "message": "삭제완료"
    })


if __name__ == "__main__":
    app.run(debug=True)