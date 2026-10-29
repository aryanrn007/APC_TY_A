# Program 10: Count alphabets, digits, spaces, and special characters
filename = input("Enter file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    alphabets = sum(1 for char in content if char.isalpha())
    digits = sum(1 for char in content if char.isdigit())
    spaces = sum(1 for char in content if char == " ")
    special_characters = sum(
        1 for char in content
        if not char.isalnum() and not char.isspace()
    )

    print("Alphabets:", alphabets)
    print("Digits:", digits)
    print("Spaces:", spaces)
    print("Special characters:", special_characters)
except FileNotFoundError:
    print("Error: File not found.")
