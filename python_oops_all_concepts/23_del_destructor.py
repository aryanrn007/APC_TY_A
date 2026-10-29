# OOP Concept 23: Object cleanup with __del__
class Demo:
    def __init__(self, name):
        self.name = name
        print("Created object:", self.name)

    def __del__(self):
        print("Cleanup for object:", self.name)

name = input("Enter object name: ")
obj = Demo(name)
del obj
print("Object reference deleted; cleanup timing can depend on Python implementation.")
