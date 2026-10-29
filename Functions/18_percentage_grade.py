def percentage_grade(m1, m2, m3, m4, m5):
    percentage = (m1 + m2 + m3 + m4 + m5) / 5
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"
    return percentage, grade

marks = []
for i in range(1, 6):
    marks.append(float(input(f"Enter marks for subject {i} (out of 100): ")))

percentage, grade = percentage_grade(*marks)
print("Percentage =", percentage, "%")
print("Grade =", grade)
