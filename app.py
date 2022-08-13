# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/13 16:35
@Auth ： YONGYAN ZHU
@File ：app.py.py
@IDE ：PyCharm
@Motto：YOU ARE WHAT YOU CHOOSE TO BE.
"""
from flask import Flask, render_template, request
import joblib
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    model1 = joblib.load("regression_DBS")
    model2 = joblib.load("tree_DBS")

    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)

        # model1 = joblib.load("regression_DBS")
        pred1 = model1.predict([[rates]])
        # model2 = joblib.load("tree_DBS")
        pred2 = model2.predict([[rates]])

        return (render_template("index.html", result1=pred1, result2=pred2))
    else:
        return (render_template("index.html", result1="waiting", result2="waiting"))

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = int("1205"))

