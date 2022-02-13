#!/usr/bin/env python
# coding: utf-8

from youtube_transcript_api import YouTubeTranscriptApi

def get_captions(lnk):
    if "youtube.com/watch?v" in lnk:
        lnk = lnk.split("https://www.youtube.com/watch?v=")[1]
    elif "https://youtu.be/" in lnk:
        lnk = lnk.split("https://youtu.be/")[1]
    else:
        return "Invalid link"

    try:
        srt = YouTubeTranscriptApi.get_transcript(lnk,
                                            languages=['en'])
    except:
        return "Couldn't find caption"
    captions = ""
    for i in srt:
        captions += i["text"] + " "

    return captions
    