import student

name = input("Enter student name: ")
marks = [float(input(f"Enter marks for subject {i + 1} (out of 100): ")) for i in range(3)]
total = student.total_marks(marks)
percent = student.percentage(marks)

print("\nStudent:", name)
print("Total marks:", total, "/", len(marks) * 100)
print(f"Percentage: {percent:.2f}%")
print("Grade:", student.grade(percent))
