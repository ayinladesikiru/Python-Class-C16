class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        print(f"drawing from point {self.a} to {self.b}")

    @classmethod
    def point_from_one(cls):
        return cls(1, 1)

    def __str__(self):
        return f"({self.a}, {self.b})"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        return self.a > other.a and self.b > other.b


p1 = Point(3, 3)
p2 = Point(1, 2)
print(p1 < p2)
