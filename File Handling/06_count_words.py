# Program 6: Count the total number of words in a text file
filename = input("Enter file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        word_count = len(file.read().split())
    print("Total number of words:", word_count)
except FileNotFoundError:
    print("Error: File not found.")
