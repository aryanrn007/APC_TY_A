# OOP Concept 20: super() to call parent constructor
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)

name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
Employee(name, employee_id).display()
