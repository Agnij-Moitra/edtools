#!/bin/python3
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from operator import le
from flask import Flask, render_template, request
import nltk
from rake_nltk import Rake
from re import sub
rake_nltk_var = Rake()
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
        summary = summarize(request.form.get("text"))
        if summary[0] == "":
            return apology("Too short to summerize")
        return render_template("text-out.html", summary=summary[0], keywords=summary[1])
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


def summarize(text):
    """Summerize text and extract keywords"""
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    average = int(sumValues / len(sentenceValue))

    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence

    rake_nltk_var.extract_keywords_from_text(text)
    keywords = rake_nltk_var.get_ranked_phrases()[:5]

    return [summary, keywords]


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
