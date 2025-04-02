
class Animal:
    def __init__(self):
        print("Animal class")

class Pet(Animal):
    def __init__(self):
        super().__init__()
        print("Pets class")

class Dog(Pet):
    def __init(self):
        super().__init()
        print("Dog class")

    def Bark(self):
        print("Bow Wow")


d = Dog()
d.Bark()

    