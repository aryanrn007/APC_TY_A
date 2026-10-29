# 4. Multiple inheritance with user input
class Academics:
    def input_marks(self):
        self.marks = float(input("Enter academic marks: "))

class Sports:
    def input_score(self):
        self.score = float(input("Enter sports score: "))

class Result(Academics, Sports):
    def display(self):
        print("Academic marks:", self.marks)
        print("Sports score:", self.score)
        print("Combined total:", self.marks + self.score)

r = Result()
r.input_marks()
r.input_score()
r.display()
