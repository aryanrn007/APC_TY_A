# Program 8: Display lines of a text file in reverse order
filename = input("Enter file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in reversed(lines):
        print(line.rstrip())
except FileNotFoundError:
    print("Error: File not found.")
