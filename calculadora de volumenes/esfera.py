from figura import Figura
import math


class Esfera(Figura):

    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)
