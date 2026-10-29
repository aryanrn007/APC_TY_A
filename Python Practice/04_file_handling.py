# APL Practical Programs: File Handling

# Create data.txt in this folder before running these programs.

# 20. Count words and show top 10 words from data.txt
with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = text.split()
frequency = {}
for word in words:
    word = word.strip(".,!?;:'\\"()")
    if word:
        frequency[word] = frequency.get(word, 0) + 1

print("Total words:", len(words))
print("Top 10:", sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:10])

# 23. Find and replace text from data.txt, save to new.txt
with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()

old = input("Find word: ")
new = input("Replace with: ")
text = text.replace(old, new)

with open("new.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Saved to new.txt")
