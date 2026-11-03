class Termometro:

    def __init__(self, ubicacion, temperatura):
        self.ubicacion = ubicacion
        self.temperatura = temperatura

    def mostrar_temperatura(self):
        print("Ubicación:", self.ubicacion)
        print("Temperatura:", self.temperatura, "°C")

    def aumentar_temperatura(self, grados):
        self.temperatura = self.temperatura + grados

    def disminuir_temperatura(self, grados):
        self.temperatura = self.temperatura - grados

        if self.temperatura < 0:
            self.temperatura = 0



termometro_aula = Termometro("Aula", 20)
termometro_aula.mostrar_temperatura()

termometro_aula.aumentar_temperatura(2)
termometro_aula.mostrar_temperatura()

termometro_aula.disminuir_temperatura(3)
termometro_aula.mostrar_temperatura()
    
