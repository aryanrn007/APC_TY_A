# OOP Concept 9: Hierarchical inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def show(self):
        print("Student:", self.name)

class Teacher(Person):
    def show(self):
        print("Teacher:", self.name)

student = Student(input("Enter student name: "))
teacher = Teacher(input("Enter teacher name: "))
student.show()
teacher.show()
