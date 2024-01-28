
from lib.classes.person import Person


class Worker(Person):
    """
    inheritance po Person
    """
    __structure = {'HP' : ['specjalista', 'kadrowa','palacz','rekruter'],
    'IT' : ['dev', 'tester', 'architekt', 'specjalista net'],
    'HW' : ["CSD", ]}

    __dept: str = ''
    __job: str = ''
    __salary: float = 0.0
    __licznik = 0

    def __init__(self, imie, nazwisko, pesel:str,
                 department:str, job:str, salary:float):
        super().__init__(imie=imie, nazwisko=nazwisko,pesel=pesel)
        self.department = department
        self.job = job
        self.salary = salary

    def __str__(self):
        return (f'{super().__str__()} pracuje w dziale {self.department} na stanowisku {self.job}')

    @property
    def department(self):
        return self.__dept

    @department.setter
    def department(self, value):
        self.__dept = value

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value: float):
        if value in self.__structure[self.department]:
            self.__job = value
        else:
            raise AttributeError(f"Nie ma takiego stanowiska w dziale {self.department}")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise AttributeError("error mniejsze od 0")


    @classmethod
    def IleWorkerow(cls):
        return cls.__licznik

    @classmethod # creating new classes instaances using parts of built in parameters
    def TesterWorker(cls, imie: str, nazwisko: str, pesel: str, pensja: float):
        return cls(nazwisko, imie, pesel, "IT", "tester", pensja)





