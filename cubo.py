"""
Programa que calcula el cubo de un número
"""
__author__ = "Juan"
__copyright__ = "EduIT"
__credits__ = "curso sábado x la mañana"
__license__ = "GPLv3"
__version__ = "1.0"
__email__ = "goku@gmail.com"
__status__ = "Development"

def cubo(x):
        return x**3
if __name__ == "__main__":
        x = float(input("Ingrese un numero: "))
        y = cubo(x)
        print(f"El cubo de {x} es {y}")