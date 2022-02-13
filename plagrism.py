from difflib import SequenceMatcher

def check_plagrism(txt1, txt2):
    return f"The texts are {int(SequenceMatcher(None, txt1, txt2).ratio() * 100)}% similar"