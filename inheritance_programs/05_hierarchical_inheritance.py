# 5. Hierarchical inheritance
class Person:
    def input_name(self):
        self.name = input("Enter name: ")

class Student(Person):
    def show_student(self):
        print("Student name:", self.name)

class Teacher(Person):
    def show_teacher(self):
        print("Teacher name:", self.name)

s = Student()
s.input_name()
s.show_student()

t = Teacher()
t.input_name()
t.show_teacher()
