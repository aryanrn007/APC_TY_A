# OOP Concept 16: Property (getter/setter)
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

try:
    price = float(input("Enter product price: "))
    p = Product(price)
    print("Product price:", p.price)
except ValueError as error:
    print("Error:", error)
