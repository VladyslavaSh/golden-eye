from app import app
from flask import render_template
import controllers


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/xrates")
def view_rates():
    return controllers.ViewAllRates().call()

@app.route("/api")
def api_page():
    return render_template("api.html")


@app.route("/api/xrates/<fmt>")
def api_rates(fmt):
    return controllers.GetApiRates().call(fmt)


@app.route('/update/<int:from_currency>/<int:to_currency>')
@app.route('/update/all')
def update_xrates(from_currency=None, to_currency=None):
    return f"update by api"
