# 2. Single inheritance: student marks
class Student:
    def input_student(self):
        self.name = input("Enter student name: ")
        self.marks = float(input("Enter marks: "))

class Result(Student):
    def display_result(self):
        print("Student:", self.name)
        print("Marks:", self.marks)
        print("Result:", "Pass" if self.marks >= 35 else "Fail")

r = Result()
r.input_student()
r.display_result()
