# 3. Multilevel inheritance
class Grandparent:
    def show_grandparent(self):
        print("Grandparent class method")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent class method")

class Child(Parent):
    def show_child(self):
        print("Child class method")

obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()
