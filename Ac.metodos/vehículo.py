class Vehiculo:

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
        self.encendido = False

    def encender(self):
        self.encendido = True
        print("El vehículo está encendido.")

    def acelerar(self, aumento):
        if self.encendido:
            self.velocidad = self.velocidad + aumento
            print("Velocidad actual:", self.velocidad)
        else:
            print("Primero debe encender el vehículo.")

    def frenar(self, disminucion):
        self.velocidad = self.velocidad - disminucion

        if self.velocidad < 0:
            self.velocidad = 0

        print("Velocidad actual:", self.velocidad)

    def apagar(self):
        self.encendido = False
        print("El vehículo está apagado.")



carro = Vehiculo("Toyota", "Corolla", "Rojo")

carro.encender()
carro.acelerar(20)
carro.acelerar(30)
carro.frenar(10)
carro.apagar()