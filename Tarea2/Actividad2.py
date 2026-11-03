class Estudiante:
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_promedio(self):
        promedio = round((self.nota1 + self.nota2 + self.nota3) / 3, 2)
        return promedio

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        if promedio >= 60:
             print("El promedio de", self.nombre, "es:", promedio ,"y esta aprobado")
        else:
             print("El promedio de", self.nombre, "es:", promedio ,"y esta reprobado")

# Solicitar al usuario que ingrese su nombre y sus tres notas
nombre = input("Ingrese su nombre: ")
nota11 = float(input("Ingrese la primera nota: "))
nota22 = float(input("Ingrese la segunda nota: "))
nota33 = float(input("Ingrese la tercera nota: "))

# Crear una instancia de la clase Estudiante
estudiante = Estudiante(nombre, nota11, nota22, nota33)

# Mostrar el promedio
estudiante.mostrar_promedio()