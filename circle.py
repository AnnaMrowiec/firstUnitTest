from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError('The value must be an integer of a float number')
    if r < 0:
        raise ValueError('The value cannot be negative')
    return pi*(r**2)
