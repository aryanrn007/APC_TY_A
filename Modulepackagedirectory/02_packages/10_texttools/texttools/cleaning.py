import string

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def normalize_spaces(text):
    return " ".join(text.split())
