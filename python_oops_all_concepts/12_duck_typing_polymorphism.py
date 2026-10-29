# OOP Concept 12: Polymorphism through duck typing
class Printer:
    def act(self):
        print("Printing a document")

class Scanner:
    def act(self):
        print("Scanning a document")

def operate(device):
    device.act()

choice = input("Choose printer or scanner: ").strip().lower()
if choice == "printer":
    operate(Printer())
elif choice == "scanner":
    operate(Scanner())
else:
    print("Unknown device")
