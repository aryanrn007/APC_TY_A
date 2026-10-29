# Program 1: Create student.txt and write student details
with open("student.txt", "w", encoding="utf-8") as file:
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")
    semester = input("Enter semester: ")

    file.write(f"Name: {name}\n")
    file.write(f"Roll Number: {roll_no}\n")
    file.write(f"Branch: {branch}\n")
    file.write(f"Semester: {semester}\n")

print("Student details saved to student.txt")
