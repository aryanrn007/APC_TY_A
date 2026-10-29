# APL Practical Programs: String

# 8. Anagram checker (simple version: ignores spaces and case)
a = input("Enter first string: ").lower().replace(" ", "")
b = input("Enter second string: ").lower().replace(" ", "")
if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")

# 21. Search and highlight text (case-insensitive count)
text = input("Enter text: ")
word = input("Search word: ")
print("Count:", text.lower().count(word.lower()))
if word:
    print(text.replace(word, "**" + word + "**"))

# 22. Remove common stopwords
text = input("Enter text: ").lower()
stopwords = {"is", "and", "the", "a"}
result = [word for word in text.split() if word not in stopwords]
print(" ".join(result))

# 24. Split paragraph into sentences
import re
text = input("Enter paragraph: ")
sentences = re.split(r'(?<=[.!?])\\s+', text)
print(sentences)

# 25. Simple summary: display first two sentences
text = input("Enter paragraph: ")
sentences = re.split(r'(?<=[.!?])\\s+', text)
print("Summary:", " ".join(sentences[:2]))

# 26. Normalize text for NLP: lowercase and remove punctuation/numbers
text = input("Enter text: ").lower()
text = re.sub(r'[^a-z\\s]', '', text)
print(text)

# 27. Palindrome checker
s = input("Enter word or phrase: ").lower()
s = "".join(ch for ch in s if ch.isalnum())
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 28. Top 5 keywords by frequency
text = input("Enter text: ").lower()
stopwords = {"the", "is", "a", "and", "of"}
frequency = {}
for word in text.split():
    word = word.strip(".,!?;:")
    if word and word not in stopwords:
        frequency[word] = frequency.get(word, 0) + 1
print(sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:5])

# 29. Simple spell checker with a small sample dictionary
dictionary = {"hello", "world", "python", "student"}
words = input("Enter text: ").lower().split()
wrong = [word.strip(".,!?") for word in words if word.strip(".,!?") not in dictionary]
print("Misspelled words:", wrong)
