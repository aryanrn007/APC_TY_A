# Program 9: Count vowels and consonants in a text file
filename = input("Enter file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read().lower()

    vowels = sum(1 for char in content if char in "aeiou")
    consonants = sum(1 for char in content if char.isalpha() and char not in "aeiou")

    print("Number of vowels:", vowels)
    print("Number of consonants:", consonants)
except FileNotFoundError:
    print("Error: File not found.")
