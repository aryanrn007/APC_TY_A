# Program 2: Display the complete contents of a text file
filename = input("Enter file name (e.g., student.txt): ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
