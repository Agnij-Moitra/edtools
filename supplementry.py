#!/usr/bin/env python
# coding: utf-8

from difflib import SequenceMatcher
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import resolve1
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdftypes import PDFNotImplementedError
from io import StringIO
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
from rake_nltk import Rake
rake_nltk_var = Rake()


def read_article(text):
    article = text.split(". ")
    sentences = []

    for sentence in article:
        print(sentence)
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences


def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(
                sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


def generate_summary(text, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []

    sentences = read_article(text)

    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    ranked_sentence = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))

    rake_nltk_var.extract_keywords_from_text(text)
    keywords = rake_nltk_var.get_ranked_phrases()[:5]

    return summarize_text[0], keywords


def get_txt(file_path):
    with open(file_path, 'r') as txtf:
        text = txtf.read().replace("\n", " ")
        return text


def get_pdf(file_path):
    output_string = StringIO()
    with open(file_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(
            rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

        return (output_string.getvalue())


def get_readability(intxt):

    letterno = float(letters(intxt))
    wordsno = float(words(intxt))
    sentenceno = float(sentences(intxt))

    avgl = float((letterno / wordsno)) * 100
    s = float((sentenceno / wordsno)) * 100

    # https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index

    index = int(round((0.0588 * avgl) - (0.296 * s) - 15.8))

    if index < 1:
        return "Readability Index: Before Grade 1"
    elif index >= 13 and index < 16:
        return "Readability Index: College Level"
    elif index >= 16:
        return "Expert"
    else:
        return f"Readability Index: Grade {index}"


def letters(string):

    lettercount = 0
    string = string.upper()

    for char in string:
        # using ord to convert from str to int of ascii
        word_ascii = ord(char) - 65
        if word_ascii < 0 or word_ascii > 25:
            pass
        else:
            lettercount += 1
    return lettercount


def words(string):
    wordcount = 1

    for char in string:
        # using ord to convert from str to int of ascii
        char_ascii = ord(char)

        if char_ascii == 32:
            wordcount += 1

    return wordcount


def sentences(string):
    sentencecount = 0

    for char in string:
        # using ord to convert from str to int of ascii
        char = ord(char)

        if char == 33 or char == 63 or char == 46:
            sentencecount += 1

    return sentencecount


def check_plagrism(txt1, txt2):
    return f"The texts are {int(SequenceMatcher(None, txt1, txt2).ratio() * 100)}% similar"


# from youtube_transcript_api import YouTubeTranscriptApi

# def get_captions(lnk):
#     if "youtube.com/watch?v" in lnk:
#         lnk = lnk.split("https://www.youtube.com/watch?v=")[1]
#     elif "https://youtu.be/" in lnk:
#         lnk = lnk.split("https://youtu.be/")[1]
#     else:
#         return "Invalid link"

#     try:
#         srt = YouTubeTranscriptApi.get_transcript(lnk,
#                                             languages=['en'])
#     except:
#         return "Couldn't find caption"
#     captions = ""
#     for i in srt:
#         captions += i["text"] + " "

#     return captions
