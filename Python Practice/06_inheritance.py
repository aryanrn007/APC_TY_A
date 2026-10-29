# APL Practical Programs: Inheritance

# 31. Single inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

e = Employee("Amit", 21, 101, 25000)
e.display_employee_info()

# 32. Multilevel inheritance
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name, "Age:", self.age)

class Employee2(Person2):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_employee(self):
        self.show_person()
        print("Employee ID:", self.emp_id, "Salary:", self.salary)

class Manager(Employee2):
    def __init__(self, name, age, emp_id, salary, department, team_size):
        super().__init__(name, age, emp_id, salary)
        self.department = department
        self.team_size = team_size

    def show_manager(self):
        self.show_employee()
        print("Department:", self.department)
        print("Team size:", self.team_size)

m = Manager("Riya", 30, 201, 60000, "IT", 8)
m.show_manager()
