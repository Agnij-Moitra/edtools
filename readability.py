#!/usr/bin/env python
# coding: utf-8

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
