class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eating...")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print("Walking...")


class Fish(Mammal):

    def swim(self):
        print("swimming...")


m = Mammal()
m.eat()
f = Fish()
print(m.age)
f.eat()
print(isinstance(Mammal, object))
