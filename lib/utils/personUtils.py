import math
from lib.utils.custom_decorator import *

def isPeselPesel(pesel: str)-> bool:  # validation function should return always True or False
    if len(pesel) == 11 and pesel.isdecimal():
        return True
    else:
        #raise AttributeError("Pesel must have 11 numbers")
        return False

def genderFromPesel(pesel:str):
    if isPeselPesel(pesel):
        gender = int(pesel[7])
        return 'M' if gender % 2 ==1 else 'F'
    else:
        raise AttributeError("Pesel must have 11 numbers")

def BirthdayFromPesel(pesel: str):
    if isPeselPesel(pesel):
        import datetime
        return pesel[0:2],pesel[2:4], pesel[4:6], datetime.date(int(pesel[0:2]),int(pesel[2:4]),int(pesel[4:6]))
    else:
        raise AttributeError("Pesel must have 11 numbers")

def bmi(waga: int, wzrost: float):
    return waga/(wzrost ** 2)

def bmiAnalysis(bmi:float):
    if bmi < 18:
        return "niedowaga"
    elif bmi >= 18.5 and bmi <25:
        return "waga ok"
    elif bmi >= 25 and bmi < 30:
        return "nadwaga"
    else: return "Daramat"

def guestList(*args):
    for i,g in enumerate(args,start=1):
        print(f"dla {i} jest {g}")

@decoratorMethod
def shape(*params, **typeOper):
    if typeOper.get("shape") == "Circle":
        if typeOper.get("what") == "area":
            return math.pi * math.pow(params[0],2)
    if typeOper.get("what") == "perimeter":
        return 2 *params[0]* params[1]
