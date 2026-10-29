# 7. Using super()
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll number:", self.roll)

name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
s = Student(name, roll)
s.display()
