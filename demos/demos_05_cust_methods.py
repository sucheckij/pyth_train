import functools

from lib.utils.personUtils import *
from lib.utils.validator import *

def demos05CustomMethods():
    guestList("cos", "cos2", "cos3")
    print(f"Circle: {shape(1,shape='Circle',what='area')}")


def sumLikeExcel(*params):  ### rekurencja

    # --sorted-- can be used instead of code below

    sumF = 0
    for elem in params:
        if isinstance(elem,(int,float)):
            sumF+= elem
        if isinstance(elem,str):
            if isNumber(elem):
                elem = float(elem)
                sumF += elem
        if isinstance(elem, (list,tuple,set,frozenset)):
            sumF = sumLikeExcel(e)
    return sumF

@functools.cache # how to cache works
def fib(n):
    if n <= 2:
        wynik = n
    else:
        wynik = fib(n-1)+fib(n-2)
    return wynik




