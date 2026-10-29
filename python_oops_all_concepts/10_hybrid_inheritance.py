# OOP Concept 10: Hybrid inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def student_info(self):
        print("Student:", self.name)

class Sports:
    def sports_info(self):
        print("Sports participation recorded")

class SportsStudent(Student, Sports):
    pass

obj = SportsStudent(input("Enter student name: "))
obj.student_info()
obj.sports_info()
