class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def __str__(self):
        return f"{self.nombre} ({self.edad} años ) - Nota:  {self.nota}"

# Creación de una lista de objetos Estudiante
lista_estudiantes = [
    Estudiante("Ana", 20, 85),
    Estudiante("Luis", 22, 92),
    Estudiante("Marta", 19, 78)
]

""" Recorrer la lista e imprimir cada objeto """
for est in lista_estudiantes:
    print(est)

""" Acceder a un atributo específico de un elemento """
print(lista_estudiantes[1].nombre)
print(lista_estudiantes[2].nota)

""" Calcular un valor agregado (promedio de notas) """
sumar_notas = 0
for est in lista_estudiantes:
    sumar_notas += est.nota

promedio = sumar_notas / len(lista_estudiantes)
print(f"Promedio del grupo: {promedio:.2f}")