# Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.
import math


class Vehiculo:

    def __init__(self, velocidad_maxima: int, kilometraje: int):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

# Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:

    def punto(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

# Un método mostrar que imprima por consola las coordenadas del punto
    def mostrar(self):
        print(f"X en {self.x} Y en {self.y}")

# Un método mover que cambie las coordenadas del punto
    def mover(self, punto1: int, punto2: int, punto3: int, punto4: int):
        self.x1 = punto1 + 4
        self.y1 = punto2 + 5
        self.x2 = punto3 + 3
        self.y2 = punto4 + 1

# Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
    def calcular_distancia(self):

        distancia_en_x = self.x2 - self.x1
        distancia_en_y = self.y2 - self.y1
        return distancia_en_y, distancia_en_x



# Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas.
# Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.

class Rectangulo:

    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def perimetro_rectangulo(self):

        altura = self.y1 - self.y2
        base = self.x1 - self.x2
        perimetro = altura + altura + base + base

        return perimetro


    def area_rectangulo(self):
        base = self.x1 - self.x2
        altura = self.y1 - self.y2

        area = base*altura

        return area

    def es_cuadrado(self):
        base = self.x1 - self.x2
        altura = self.y1 - self.y2

        if(base == altura):
            print("El rectangulo es cuadrado")

        else:
            print("El rectangulo no es cuadrado")

#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor.
#Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.

class Circulo:

    def __int__(self, centro = int, radio = int):
        self.centro = centro
        self.radio = radio

    def area_circulo(self):

        area_del_circulo = math.pi*(self.radio*self.radio)
        return area_del_circulo

    def perimetro_circulo(self):

        perimetro_del_circulo = 2*math.pi * self.radio
        return perimetro_del_circulo

    def pertenece_al_circulo(self):

#Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto
#(se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.

class Carta:

    def __int__(self, valor: int, pinta: str):
        self.valor = valor
        self.pinta = pinta

#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance.
#Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
#Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.

class CuentaBancaria:

    def __int__(self,numero_cuenta,propietario,balance):
        self.numero_cuenta = numero_cuenta
        self.propietario = propietario
        self.balance = balance

    def depositar(self):

    def retirar(self):

    def aplicar_cuota_manejo(self):

        balance_cuota = (balance*0,2)+self.balance
        return balance_cuota

    def mostrar_detalles(self):

        print("La cuenta No."{self.numero_cuenta},"con el propietario"{self.propietario},"tiene un balance de",{self.balance})





