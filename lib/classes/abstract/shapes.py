
from abc import ABC, abstractmethod


class FlatShape(ABC):

    @abstractmethod
    def Area(self):
        ...
    @abstractmethod
    def Perimater(self):
        ...

class CorrectShape(FlatShape):
    def Area(self):
        print("Implemented 1 method")

    def Perimater(self):
        print("Implemented 1 method")

