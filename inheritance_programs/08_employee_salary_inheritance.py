# 8. Employee salary using inheritance
class Employee:
    def input_employee(self):
        self.name = input("Enter employee name: ")
        self.basic_salary = float(input("Enter basic salary: "))

class Salary(Employee):
    def calculate(self):
        allowance = self.basic_salary * 0.10
        total = self.basic_salary + allowance
        print("Employee:", self.name)
        print("Basic salary:", self.basic_salary)
        print("Allowance (10%):", allowance)
        print("Total salary:", total)

e = Salary()
e.input_employee()
e.calculate()
