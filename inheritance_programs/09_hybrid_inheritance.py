# 9. Hybrid inheritance example
class Person:
    def input_name(self):
        self.name = input("Enter name: ")

class Student(Person):
    def input_marks(self):
        self.marks = float(input("Enter marks: "))

class Sports:
    def input_sports_score(self):
        self.sports_score = float(input("Enter sports score: "))

class Result(Student, Sports):
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Sports score:", self.sports_score)
        print("Total:", self.marks + self.sports_score)

r = Result()
r.input_name()
r.input_marks()
r.input_sports_score()
r.display()
