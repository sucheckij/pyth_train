from lib.classes.person import *

def demo_oop():
    p = Person()
    print(p.fname)
    print(p.birthDate["year"])
    print("Magic method usage:", p)
