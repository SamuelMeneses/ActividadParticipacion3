# Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehiculo:

    def __init__(self, velocidad_maxima: int, kilometraje: int):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

# Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:

    def punto(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

# Un método mostrar que imprima por consola las coordenadas del punto
    def mostrar(self):
        print(f"X en {self.x} Y en {self.y}")

# Un método mover que cambie las coordenadas del punto
    def mover(self, punto1: float, punto2: float):
        self.x = punto1
        self.y = punto2

# Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
    def calcular_distancia(self):

# Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas.
# Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.

class Rectangulo:

    def __init__(self, esquina1: float, esquina2: float):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def perimetro(self):

    def area(self):

    def es_cuadrado(self):



