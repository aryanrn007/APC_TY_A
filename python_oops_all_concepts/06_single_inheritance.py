# OOP Concept 6: Single inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def show(self):
        print("Student name:", self.name)

name = input("Enter student name: ")
s = Student(name)
s.show()
