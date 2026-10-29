# OOP Concept 4: Instance, class, and static methods
class Demo:
    category = "OOP Demo"

    def instance_method(self):
        print("Instance method called")

    @classmethod
    def class_method(cls):
        print("Class method; category:", cls.category)

    @staticmethod
    def static_method():
        print("Static method called")

obj = Demo()
obj.instance_method()
Demo.class_method()
Demo.static_method()
