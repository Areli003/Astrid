class Estudiante:
    def __init__ (self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}"
    
    estudiantes = [
        Estudiante("Alice", 20, 8, 5),
        Estudiante("Bob", 20, 7, 0),
        Estudiante("Charlie",21 9, 5)
        
    ]
    """Recorrer la lista e imprimir cada objeto"""
    
    for e in estudiantes:
        print(e)
        
        
    print(estudiantes[0].nombre)
   
    print(estudiantes[1].nota)
    
    print(estudiantes[2].edad)
    
    print('') #Línea en blanco para separar La salida
    print('')
    
    """Acceder un valor agregado (promedio de notas)"""
    suma_notas = 0 #Línea en blanco para separar la salida
    for estudiantes in estudiantes:
        suma_notas += e.nota
    promedio = suma_notas / len(estudiantes)
    print(f"Promedio de notas: {promedio}")
    """len = suma todo y devuelve el total de elementos de la lista"""
    
    print(f"Promedio de notas es: {promedio}")
    print(f"Promedio de notas: {promedio}")
          
    print('') #Línea en blanco para separar la salida
    print(f"Promedio de notas: {promedio}")