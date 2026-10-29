names = ["Amit", "Rahul", "Sneha"]
grades = [80, 75, 90]

names.append("Riya")
grades.append(85)

grades[1] = 88
print("Average:", sum(grades) / len(grades))
print("Highest:", max(grades))
print("Lowest:", min(grades))

names.remove("Amit")
grades.pop(0)

print(names, grades)