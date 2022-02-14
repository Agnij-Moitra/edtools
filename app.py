#!/usr/bin/env python
# coding: utf-8

import os
from flask import Flask, render_template, request, request_started
from supplementry import check_plagrism, get_summary, get_epub, get_pdf, get_readability, get_txt, get_docx, get_epub
from werkzeug.utils import secure_filename
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
                summary = get_summary(request.form.get("text"))
            except IndexError:
                return apology("Too short to summerize")
            return render_template("Text-Out.html", summary=summary[0], keywords=summary[1])
        # elif request.form.get("ytlnk") != "":
        #     captions = get_captions(request.form.get("ytlnk"))
        #     if captions == "Invalid link" or captions == "Couldn't find transcript":
        #         return apology(captions)
        #     else:
        #         # try:
        #         summary = generate_summary(captions)
        #         # except IndexError:
        #         #     return apology("Too short to summerize")
        #         return render_template("text-out.html", summary=summary[0], keywords=summary[1])
        else:
            f = request.files['summerizerfile']
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, secure_filename(f.filename))
            try:
                f.save(secure_filename(f.filename))
            except FileNotFoundError:
                return apology("Please upload a file or enter text!")
            ext = os.path.splitext(f"{file_path}")[1]
            if ext == ".txt":
                text = get_txt(file_path)
                try:
                    summary = get_summary(text)
                except IndexError:
                    os.remove(file_path)
                    return apology("Too short to summerize")
                os.remove(file_path)
                return render_template("Text-Out.html", summary=summary[0], keywords=summary[1])
            if ext == ".pdf":
                text = get_pdf(file_path)
        
                try:
                    summary = get_summary(text)
                except IndexError:
                    os.remove(file_path)
                    return apology("Too short to summerize")
                os.remove(file_path)
                return render_template("Text-Out.html", summary=summary[0], keywords=summary[1])
            if ext == ".docx":
                text = get_docx(file_path)
                
                try:
                    summary = get_summary(text)
                except IndexError:
                    os.remove(file_path)
                    return apology("Too short to summerize")
                os.remove(file_path)
                return render_template("Text-Out.html", summary=summary[0], keywords=summary[1])
            if ext == ".epub":
                text = get_epub(file_path)
                
                try:
                    summary = get_summary(text)
                except IndexError:
                    os.remove(file_path)
                    return apology("Too short to summerize")
                os.remove(file_path)
                return render_template("Text-Out.html", summary=summary[0], keywords=summary[1])
            return apology("Please upload a file or enter text!")
    return render_template("Text-Summerizer.html")


@app.route("/Plagrism-Checker", methods=["GET", "POST"])
def plagrism():
    if request.method == "POST":
        text1 = request.form.get("text1")
        text2 = request.form.get("text2")
        if text1 or text2 != "":
            return render_template("Plagrism-Out.html", plagrism_msg=check_plagrism(text1, text2))
        else:
            return apology("No text entered!")
    return render_template("Plagrism-Checker.html")


@app.route("/Citation-Generator", methods=["GET", "POST"])
def citation():
    if request.method == "POST":
        title = request.form.get("title").capitalize()
        publisher = request.form.get("publisher").capitalize()
        year = request.form.get("year")
        first = request.form.get("first").capitalize()
        last = request.form.get("last").capitalize()
        vol = request.form.get("volume")

        if first == "" and last == "" and vol == "":
            apa = f"({year}), {title}, {publisher}"
            mla = f'"{title}", {publisher}, {year}'
            return render_template("Citation-Out.html", apa=apa, mla=mla)

        if last == "" and vol == "":
            return apology("Please enter last name!")

        if first == "" and vol == "":
            apa = f"{last}, ({year}), {title}, {publisher}"
            mla = f'{last}, "{title}", {publisher}, {year}'
            return render_template("Citation-Out.html", apa=apa, mla=mla)

        if vol == "":
            apa = f"{last}, {first}, ({year}), {title}, {publisher}"
            mla = f'{last}, {first}, "{title}", {publisher}, {year}'
            return render_template("Citation-Out.html", apa=apa, mla=mla)

        else:
            apa = f"{last}, {first}, ({year}), {title}, {vol}, {publisher}"
            mla = f'{last}, {first}, "{title}", vol. {vol}, {publisher}, {year}'
            return render_template("Citation-Out.html", apa=apa, mla=mla)

    return render_template("Citation-Generator.html")


@app.route("/Readability-Checker", methods=["GET", "POST"])
def readablility():
    if request.method == "POST":
        txt = request.form.get("readalibity_text")
        if txt == "":
            f = request.files['readabilityfile']
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, secure_filename(f.filename))
            try:
                f.save(secure_filename(f.filename))
            except FileNotFoundError:
                return apology("Please upload a file or enter text!")
            ext = os.path.splitext(f"{file_path}")[1]
            if ext == ".txt":
                text = get_txt(file_path)
                os.remove(file_path)
                return render_template("Readability-Out.html", index=get_readability(text))
            if ext == ".pdf":
                text = get_pdf(file_path)
                os.remove(file_path)
                return render_template("Readability-Out.html", index=get_readability(text))
            if ext == ".docx":
                text = get_docx(file_path)
                os.remove(file_path)
                return render_template("Readability-Out.html", index=get_readability(text))
            if ext == ".epub":
                text = get_epub(file_path)
                os.remove(file_path)
                return render_template("Readability-Out.html", index=get_readability(text))
            os.remove(file_path)
            return apology("Please upload a file or enter text!")

        return render_template("Readability-Out.html", index=get_readability(txt))
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
