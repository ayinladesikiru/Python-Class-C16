from math import pi


def area_calc(r):
    try:
        return pi * (r ** 2)
    except (TypeError, ValueError):
        print("Eyes dey pain you?, enter an integer")


print(area_calc('a'))