from texttools.cleaning import remove_punctuation, normalize_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = input("Enter a sentence or paragraph: ")
cleaned = normalize_spaces(remove_punctuation(text))
print("Cleaned text:", cleaned)
print("Tokens:", tokenize(cleaned))
print("Word frequency:", word_frequency(text))
