#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, request
import nltk
from summerizer import generate_summary
from ytcaptions import get_captions
nltk.download('stopwords')
nltk.download('punkt')
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Render index.html"""
    return render_template("index.html")


@app.route("/Text-Summerizer", methods=["GET", "POST"])
def text_summerizer():
    if request.method == "POST":
        if request.form.get("text") != "":
            try:
                summary = generate_summary(request.form.get("text"))
            except IndexError:
                return apology("Too short to summerize")
            return render_template("text-out.html", summary=summary[0], keywords=summary[1])
        if request.form.get("ytlnk") != "":
            captions = get_captions(request.form.get("ytlnk"))
            if captions == "Invalid link" or captions == "Couldn't find transcript":
                return apology(captions)
            else:
                # try:
                summary = generate_summary(captions)
                # except IndexError:
                #     return apology("Too short to summerize")
                return render_template("text-out.html", summary=summary[0], keywords=summary[1])
        else:
            return apology("Please enter text or youtube link.")
    return render_template("Text-Summerizer.html")


@app.route("/Plagrism-Checker", methods=["GET"])
def plagrism():
    return render_template("Plagrism-Checker.html")


@app.route("/Citation-Generator", methods=["GET"])
def citation():
    return render_template("Citation-Generator.html")


@app.route("/Readability-Checker", methods=["GET"])
def readablility():
    return render_template("Readability-Checker.html")


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.
        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("error.html", top=code, bottom=escape(message)), code


if __name__ == "__main__":
    app.run(debug=True)
