# Program 7: Count characters, including spaces and newline characters
filename = input("Enter file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print("Total number of characters (including spaces):", len(content))
except FileNotFoundError:
    print("Error: File not found.")
