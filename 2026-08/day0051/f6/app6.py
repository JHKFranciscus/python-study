from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("profile_form.html")

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "GET":
        return render_template("profile_form.html")

    if request.method == "POST":
        nicknameApp = request.form.get("nicknameForm")
        languageApp = request.form.get("languageForm")

        return render_template("profile_result.html", nicknameResult=nicknameApp, languageResult=languageApp)

if __name__ == "__main__":
    app.run(debug=True)