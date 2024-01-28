from lib.classes.study import *
from lib.classes.person import *

class Student(Person,Study):  # dziedziczenie odbywa sie na instancjach a nie na klasach
    def __init__(self, p: Person,s: Study, wiek: int):
        Person.__init__(self, p, p.imie, p.nazwisko, p.pesel)
        Study.__init__(self, s, s.wydzial, s.kierunek, s.index)
        self.wiek = wiek

    def __str__(self):
        return f'{self.wiek}'


