# Program 4: Read and display a text file line by line
filename = input("Enter file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.rstrip()}")
except FileNotFoundError:
    print("Error: File not found.")
