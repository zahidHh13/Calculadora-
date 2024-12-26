# Controlador/controlador.py

from Modelo.calculador_modelo import CalculadorModelo
from Vista.vista import Vista

class Controlador:
    def __init__(self):
        self.modelo = CalculadorModelo()
        self.vista = Vista(self)

if __name__ == "__main__":
    controlador = Controlador()
