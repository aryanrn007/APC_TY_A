# OOP Concept 18: Aggregation (object supplied from outside)
class Department:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name, department):
        self.name = name
        self.department = department

dept_name = input("Enter department name: ")
teacher_name = input("Enter teacher name: ")
department = Department(dept_name)
teacher = Teacher(teacher_name, department)
print("Teacher:", teacher.name)
print("Department:", teacher.department.name)
