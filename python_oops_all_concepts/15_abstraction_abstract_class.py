# OOP Concept 15: Abstraction with ABC
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
rectangle = Rectangle(length, width)
print("Rectangle area:", rectangle.area())
