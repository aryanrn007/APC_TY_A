from collections import Counter
import re

def word_frequency(text):
    words = re.findall(r"\b[\w']+\b", text.lower())
    return dict(Counter(words))
