def reciprocal(x):
    if type(x) not in [int, float]:
        raise TypeError('Value has to be a number')
    if x == 0:
        raise ValueError('Value cannot equal to zero')
    return 1/x


