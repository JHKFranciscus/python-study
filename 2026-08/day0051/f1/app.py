from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def firstMake ():
    user_name = "minsu"
    user_age = 29
    return render_template("index.html", name=user_name, age=user_age)

if __name__ == "__main__":
    app.run(debug=True)
    