# OOP Concept 8: Multilevel inheritance
class Grandparent:
    def family(self):
        print("Grandparent class")

class Parent(Grandparent):
    def parent_info(self):
        print("Parent class")

class Child(Parent):
    def child_info(self):
        print("Child class")

obj = Child()
obj.family()
obj.parent_info()
obj.child_info()
