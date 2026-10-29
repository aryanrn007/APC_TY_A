# 10. Shape inheritance with user input
class Shape:
    def input_dimensions(self):
        self.length = float(input("Enter length: "))
        self.width = float(input("Enter width: "))

class Rectangle(Shape):
    def area(self):
        print("Area of rectangle:", self.length * self.width)

r = Rectangle()
r.input_dimensions()
r.area()
