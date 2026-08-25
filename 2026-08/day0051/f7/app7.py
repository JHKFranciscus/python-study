from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("search_inquiry.html")

@app.route("/search")
def search():
    titleApp = request.args.get("titleSearch")
    return render_template("searchresult.html", titleResult=titleApp)

@app.route("/inquiry", methods=["POST"])
def inquiry():
    nameApp = request.form.get("nameInquiry")
    inquiryApp = request.form.get("inquiry")
    return render_template("inquiryresult.html", nameResult=nameApp, inquiryResult=inquiryApp)

if __name__ == "__main__":
    app.run(debug=True)
