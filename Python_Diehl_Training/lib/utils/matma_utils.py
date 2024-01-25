import math


def rownanieKw(a: float, b:float, c:float):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        return -b/ (2*a)
    elif delta >=0:
        return ((-b - math.sqrt(delta)/ (2*a)),(-b + math.sqrt(delta)/ (2*a)))

def double_number(x):
        return x*2

def isEven(x):
    return True if x %2 == 0 else False