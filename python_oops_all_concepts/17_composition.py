# OOP Concept 17: Composition (has-a relationship)
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car is ready to move")

car = Car()
car.start()
