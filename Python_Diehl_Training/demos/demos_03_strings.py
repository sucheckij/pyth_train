from lib.utils.personUtils import *
from lib.utils.matma_utils import *


def demo03Strings():
    pesel = "82031701234"
    if isPeselPesel(pesel):
        print('Boy' if genderFromPesel(pesel) == 'M' else 'Girl')
        year,month, day, birthdate = BirthdayFromPesel(pesel)
        print(f"Birthday: {year} {month} {day} ")
        print(birthdate)

    osoba = "Dariusz"
    print(osoba.title())
    print(osoba.lower())
    print(osoba.upper())
    print(osoba.capitalize())

    path = "files\date.xml"
    print(path.endswith('xml'))

    dane = "Dariusz;Pieter;153244354"
    dane = dane.split(';')
    print(dane[0])
    print(dane[1])
    print(dane[2])

def countingPython():
    b = bmi(90,2.08)
    print(f"BMI data: {b} --> {bmiAnalysis(b)}")

    wa,wb,wc = 1, 3, 1
    wynik = rownanieKw(wa,wb,wc)
    if wynik is None:
        print("brak rozwiazan")
    elif isinstance(wynik, (int,float)):
        print(f"x = {wynik:.2f}")
    elif isinstance(wynik, tuple):
        print(f"x1, x2 = {wynik[0]:.2f}, {wynik[1]:.2f}")

