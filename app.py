#!/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/text-summerizer", methods=["GET"])
def text():
    return render_template("text-summerizer.html")


if __name__ == "__main__":
    app.run(debug=True)