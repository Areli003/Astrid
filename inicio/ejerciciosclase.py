class estudiante:
    def __init__(self, nombre, carrera, edad): #constructor
        self.nombre = nombre
        self.carrera = carrera
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} y estudio {self.carrera} y tengo  {self.edad}")
        
estudiante1 = estudiante("Astrid", "Ingieneria en Sistemas")
estudiante1.saludar()





