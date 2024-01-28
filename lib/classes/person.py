import datetime


class Person:
    """..."""
    # public
    frame : str = ""

    # prywatne
    __lname:str = "Such"
    __fname: str = "Jak"
    __pesel: str="95062713980"


    def __init__(self, imie:str, nazwisko: str, pesel: str):
        self.fname = imie
        self.lname = nazwisko
        self.pesel = pesel

    def __str__(self):
        return f"{self.__fname} {self.__pesel}"


    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, value: str):
        if len(value) > 0:
            self.__fname = value
        else:
            raise AttributeError("imie nie moze byc puste")

    @property
    def pesel(self):
        return self.__pesel

    @pesel.setter
    def pesel(self, value: str):
        if len(value) > 0 and value.isdigit():
            self.__pesel = value
        else:
            raise AttributeError("peselnie moze byc puste")

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, value: str):
        if len(value) > 0:
            self.__lname = value
        else:
            raise AttributeError("nazw nie moze byc puste")

    @property
    def gender(self):
        return 'M' if int(self.__pesel[7])%2 == 1 else "F"

    @property
    def birthDate(self):
        return {"year": int(self.__pesel[0:2]),
                "month": int(self.__pesel[2:4]),
                "day": int(self.__pesel[4:6])}

    def GetPesel(self):
        return self.__pesel

    def SetPesel(self, value: str):
        if len(value)==11 and value.isdigit():
            self.__pesel = value
        else:
            raise AttributeError("Wrong data")

    @staticmethod
    def bmi(waga: float, wzrost: float)->float:
        return waga/(wzrost**2)

    @staticmethod
    def sort_be_first_name(imie):
        return imie.fname

    @staticmethod
    def sort_be_last_(nazwisko):
        return nazwisko.lname


class Car:

    def __init__(self, marka: str, model: str, rok_prod: int):
        self.marka = marka
        self.model = model
        self.rok_prod = rok_prod



