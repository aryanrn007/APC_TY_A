from student.marks import total, percentage
from student.grade import calculate_grade
from student.attendance import attendance_percentage, is_eligible

name = input("Student name: ")
marks = [float(input(f"Marks for subject {i+1} (out of 100): ")) for i in range(3)]
attended = int(input("Classes attended: "))
total_classes = int(input("Total classes: "))

percent = percentage(marks)
attendance = attendance_percentage(attended, total_classes)
print("\nStudent report:", name)
print("Total marks:", total(marks), "/ 300")
print(f"Percentage: {percent:.2f}%")
print("Grade:", calculate_grade(percent))
print(f"Attendance: {attendance:.2f}%")
print("Attendance eligible:", is_eligible(attendance))
