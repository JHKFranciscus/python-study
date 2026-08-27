from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


materials = [
    {"id": 10, "name": "Flask 기본", "memo": "route 복습"},
    {"id": 25, "name": "Jinja 연습", "memo": "if와 for 연습"},
    {"id": 40, "name": "HTTP 정리", "memo": "status code 복습"},
]

@app.route("/")
def startAll():
    return render_template("start.html", materials=materials)


@app.route("/material/<int:m_id>/detail")
def mDetail(m_id):
    for material in materials:
        if material["id"] == m_id:
            return render_template("detail.html", material=material)

    return "자료를 찾을 수 없습니다.", 404


@app.route("/material/<int:m_id>/goupdate")
def mGoUpdate(m_id):
    for material in materials:
        if material["id"] == m_id:
            return render_template("update_h.html", material=material)



@app.route("/material/<int:m_id>/update", methods=["POST"])
def mUpdate(m_id):
    new_name = request.form.get("name")
    new_memo = request.form.get("memo")

    for material in materials:
        if material["id"] == m_id:
            material["name"] = new_name
            material["memo"] = new_memo

            return redirect(url_for("mDetail", m_id=m_id))



@app.route("/material/<int:m_id>/delete", methods=["POST"])
def mDelete(m_id):
    for material in materials:
        if material["id"] == m_id:
            materials.remove(material)
            break

    return redirect(url_for("startAll"))


if __name__ == "__main__":
    app.run(debug=True)