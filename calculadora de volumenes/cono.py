from figura import Figura
import math


class Cono(Figura):

    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return (1/3) * math.pi * (self.radio ** 2) * self.altura
