from math import cos

def cosinus(x):
    if type(x) not in [int, float]:
        raise TypeError('The value cannot be not a number')
    if x == 90:
        return 0
    return cos(x)


