# Program 3: Append information without deleting existing contents
filename = input("Enter file name (e.g., student.txt): ")

additional_info = input("Enter additional student information: ")

try:
    with open(filename, "a", encoding="utf-8") as file:
        file.write(additional_info + "\n")
    print("Information appended successfully.")
except OSError as error:
    print("Error:", error)
