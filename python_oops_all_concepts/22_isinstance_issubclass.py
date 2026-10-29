# OOP Concept 22: isinstance() and issubclass()
class Person:
    pass

class Student(Person):
    pass

obj = Student()
print("obj is a Student:", isinstance(obj, Student))
print("obj is a Person:", isinstance(obj, Person))
print("Student is subclass of Person:", issubclass(Student, Person))
