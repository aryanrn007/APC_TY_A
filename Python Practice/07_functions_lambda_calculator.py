# APL Practical Programs: Functions, Lambda, Calculator

# Calculator using default arguments (Program 33)
class Calculator:
    def add(self, a, b, c=0, d=0):
        return a + b + c + d

obj = Calculator()
print(obj.add(10, 20))
print(obj.add(10, 20, 30))
print(obj.add(10, 20, 30, 40))

# Sort students by marks using lambda
students = [("Amit", 80), ("Riya", 95), ("Rahul", 72)]
students.sort(key=lambda item: item[1])
print(students)
