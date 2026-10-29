def display():
    file = open("employees.txt", "r")
    for line in file:
        print(line.strip())
    file.close()

def highest():
    file = open("employees.txt", "r")
    employees = []
    for line in file:
        id, name, dept, salary = line.strip().split(",")
        employees.append([id, name, dept, float(salary)])
    file.close()
    print("Highest Paid:", max(employees, key=lambda x: x[3]))

def average():
    file = open("employees.txt", "r")
    salaries = []
    for line in file:
        salaries.append(float(line.strip().split(",")[3]))
    file.close()
    print("Average Salary:", sum(salaries) / len(salaries))

def above():
    amount = float(input("Enter salary: "))
    file = open("employees.txt", "r")
    for line in file:
        data = line.strip().split(",")
        if float(data[3]) > amount:
            print(line.strip())
    file.close()

file = open("employees.txt", "w")
file.write("101,Amit,IT,50000\n")
file.write("102,Priya,HR,60000\n")
file.write("103,Rahul,Sales,45000\n")
file.close()

display()
highest()
average()
above()