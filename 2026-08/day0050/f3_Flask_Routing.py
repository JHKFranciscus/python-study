from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home ():
    return  "Order Server"

@app.route("/orders", methods=["GET", "POST"])
def orders ():
    if request.method == "GET":
        return "Order List"

    if request.method == "POST":
        return "Order Created"

@app.route("/orders/<int:order_id>")
def orders_detail (order_id):
    return f"Order {order_id}"