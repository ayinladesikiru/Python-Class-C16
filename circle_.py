from math import pi


class Circle:

    def __init__(self, r):
        self.r = r
        self.pi = pi

    def area_of_circle(self):
        return f"the area of a circle with radius {self.r} is {self.pi * (self.r ** 2)}"

    def perimeter_of_circle(self):
        return f"the perimeter of circle with {self.r} is {2 * self.pi * self.r}"


c1 = Circle(7)
print(c1.area_of_circle())
print(c1.perimeter_of_circle())