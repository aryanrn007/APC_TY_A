# OOP Concept 3: Instance and class variables
class Student:
    college = "ABC College"  # class variable

    def __init__(self, name):
        self.name = name      # instance variable

name = input("Enter student name: ")
s = Student(name)
print("Name:", s.name)
print("College:", Student.college)
