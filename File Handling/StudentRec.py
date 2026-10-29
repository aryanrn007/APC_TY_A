file = open("students.txt", "w")
file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")
file.close()

file = open("students.txt", "r")
students = []

for line in file:
    roll, name, marks = line.strip().split(",")
    students.append([roll, name, int(marks)])

file.close()

print("All Records:")
for s in students:
    print(s)

highest = max(students, key=lambda x: x[2])
print("Highest Marks:", highest)

average = sum(s[2] for s in students) / len(students)
print("Average Marks:", average)

print("Students scoring more than 80:")
for s in students:
    if s[2] > 80:
        print(s)