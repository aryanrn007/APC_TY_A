# OOP Concept 21: Method Resolution Order (MRO)
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()
print("MRO:", " -> ".join(cls.__name__ for cls in D.mro()))
