

class Study:
    __kierunek : str = ''
    __wydzial: str = ''
    __index: int = ''


    def __init__(self,wydzial: str, kierunek: str, index: str):
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.index = index

    def __str__(self):
        return (f' Student uczy sie na wydziale {self.wydzial} i kierunku {self.kierunek}. Ma indeks {self.index}')