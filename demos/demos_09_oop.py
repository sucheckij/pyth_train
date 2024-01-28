from lib.classes.person import *
from lib.classes.worker import *
from lib.extensions.exports import *


def demo_oop():
    p1 = Person("jacek","nazw","97124580432")
    p2 = Person("milosz", "ktos", "96451245678")
    p3 = Person("erwin", "jakis", "95451265478")
    print(p1.fname)
    print(p1.birthDate["year"])
    print("Magic method usage:", p1)
    print(Person.bmi(70,1.78))

    l = []
    l.append(p1)
    l.append(p2)
    l.append(p3)
    l.sort(key= Person.sort_be_first_name)
    [print(osob) for osob in l]


    print("WWWOOORRRKKKEEERRR")
    wrk = Worker(imie="Erwin", nazwisko="Janicek", pesel="97031745768",
                 department="IT", job="tester", salary = 1300.0)
    wrk.job ='tester'
    print(wrk.job)

    tester_wrk = Worker.TesterWorker("name","surname", "95067312567", pensja=9)
    print(tester_wrk.job)

    Worker.saveHtml = exportToHtmil # dynamic creation of method class
    Worker.saveHtml(tester_wrk)

