# OOP Concept 13: Operator overloading
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

a = Number(float(input("Enter first number: ")))
b = Number(float(input("Enter second number: ")))
print("Sum using overloaded + operator:", a + b)
