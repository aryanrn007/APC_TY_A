# Program 5: Count the total number of lines in a text file
filename = input("Enter file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        line_count = sum(1 for _ in file)
    print("Total number of lines:", line_count)
except FileNotFoundError:
    print("Error: File not found.")
