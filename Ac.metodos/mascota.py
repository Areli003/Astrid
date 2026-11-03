class Mascota:

    # Constructor
    def __init__(self, nombre, especie, edad, energia):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.energia = energia

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Especie:", self.especie)
        print("Edad:", self.edad, "años")
        print("Energía:", self.energia)

    def jugar(self):
        self.energia = self.energia + 10
        print("La mascota jugó.")
        print("Energía actual:", self.energia)


    def dormir(self):
        self.energia = self.energia + 20
        print("La mascota durmió.")
        print("Energía actual:", self.energia)

    
    def cumplir_anios(self):
        self.edad = self.edad + 1
        print("La mascota cumplió años.")
        print("Edad actual:", self.edad)



mascota1 = Mascota("Boby", "Perro", 2, 50)

mascota1.mostrar_datos()
mascota1.jugar()
mascota1.dormir()
mascota1.cumplir_anios()
print("\nEstado final:")
mascota1.mostrar_datos()