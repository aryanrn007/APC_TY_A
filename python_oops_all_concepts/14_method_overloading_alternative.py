# OOP Concept 14: Flexible arguments (Python-style method overloading)
# Python does not support traditional signature-based method overloading.
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
use_third = input("Add a third number? (yes/no): ").strip().lower()

if use_third == "yes":
    c = float(input("Enter third number: "))
    print("Sum:", calc.add(a, b, c))
else:
    print("Sum:", calc.add(a, b))
