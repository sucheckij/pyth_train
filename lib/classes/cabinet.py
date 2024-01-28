from dataclasses import dataclass


@dataclass
class Cabinet:
    x: float =0
    y: float = 0
    z: float = 0

    def __add__(self,other):
        return Cabinet(x=self.x+other,y=self.y,z=self.z)

    def __str__(self):
        return str(f'{self.x}, {self.y}, {self.z}')

    def volume(self):
        return self.x * self.y * self.z


