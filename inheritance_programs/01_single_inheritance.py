# 1. Single inheritance with user input
class Person:
    def input_person(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

class Student(Person):
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s = Student()
s.input_person()
s.display()
