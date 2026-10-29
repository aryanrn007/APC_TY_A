# 6. Method overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        sound_text = input("Enter the dog's sound: ")
        print("Dog says:", sound_text)

a = Animal()
a.sound()
d = Dog()
d.sound()
