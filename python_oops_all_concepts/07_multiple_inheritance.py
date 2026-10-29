# OOP Concept 7: Multiple inheritance
class Academics:
    def academic_marks(self):
        return float(input("Enter academic marks: "))

class Sports:
    def sports_marks(self):
        return float(input("Enter sports marks: "))

class Result(Academics, Sports):
    def display(self):
        total = self.academic_marks() + self.sports_marks()
        print("Combined marks:", total)

Result().display()
