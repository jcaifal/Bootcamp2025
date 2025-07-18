class Estado:
    def __init__(self, auto):
        self.auto = auto

    def detenido(self):
        print(f"El vehículo {self.auto.tipo} está detenido.")
    
    def circulando(self):
        print(f"El vehículo {self.auto.tipo} está circulando.")
    
    def estacionado(self):
        print(f"El vehículo {self.auto.tipo} está estacionado.")
    
    def danado(self):
        print(f"El vehículo {self.auto.tipo} está dañado.")

class Comportamiento:
    def __init__(self, auto):
        self.auto = auto

    def arrancar(self):
        print(f"El vehículo {self.auto.tipo} está arrancando.")
    
    def frenar(self):
        print(f"El vehículo {self.auto.tipo} está frenando.")
    
    def acelerar(self):
        print(f"El vehículo {self.auto.tipo} está acelerando.")
    
    def girar(self):
        print(f"El vehículo {self.auto.tipo} está girando.")

class Auto:
    def __init__(self, color, peso, tamano, alto, largo, cantidad_ruedas, cantidad_puertas, tipo):
        self.color = color
        self.peso = peso
        self.tamano = tamano
        self.alto = alto
        self.largo = largo
        self.cantidad_ruedas = cantidad_ruedas
        self.cantidad_puertas = cantidad_puertas
        self.tipo = tipo
        self.estado = Estado(self)
        self.comportamiento = Comportamiento(self)

    def mostrar_informacion(self):
        print(f"Color: {self.color}")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamano}")
        print(f"Alto: {self.alto} m")
        print(f"Largo: {self.largo} m")
        print(f"Cantidad de ruedas: {self.cantidad_ruedas}")
        print(f"Cantidad de puertas: {self.cantidad_puertas}")
        print(f"Tipo: {self.tipo}")

# Ejemplo de uso de la clase Auto
auto1 = Auto("Rojo", 1200, "Mediano", 1.5, 4.0, 4, 4, "Sedán")
auto2 = Auto("Azul", 1500, "Grande", 1.6, 4.5, 4, 4, "SUV")

auto1.mostrar_informacion()
auto1.comportamiento.arrancar()
auto1.comportamiento.acelerar()
auto1.estado.circulando()
auto1.comportamiento.frenar()
auto1.estado.estacionado()

auto2.mostrar_informacion()
auto2.comportamiento.arrancar()
auto2.comportamiento.acelerar()
auto2.estado.circulando()
auto2.comportamiento.frenar()
auto2.estado.detenido()


   
