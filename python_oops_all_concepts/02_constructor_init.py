# OOP Concept 2: Constructor (__init__)
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll number:", self.roll_no)

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
student = Student(name, roll_no)
student.display()
