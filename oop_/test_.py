class Human:
    number_of_eyes = 2

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"hello {self.name} ")

    def walk(self):
        print(f"{self.name} is walking")

    @classmethod
    def blue_eyes(cls):
        pass

    def __str__(self):
        return f"{self.name}"


human1 = Human("esther")
human2 = Human("torin")

print(human1.number_of_eyes)
print(Human.number_of_eyes)


