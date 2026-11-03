class Libro:
    def __init__(self, titulo, autor, precio, disponible):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponibile else "No disponible"
        return f"'{self.titulo}' de {self.autor} - ${self.precio:.2f} [{estado}]"


libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez", 25.50, True),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 30.00, False),
    Libro("1984", "George Orwell", 18.00, True),
    Libro("El principito", "Antoine de Saint-Exupéry", 12.50, True),
    Libro("Rayuela", "Julio Cortázar", 22.00, False)
]

# 2. Recorrer la lista e imprimir todos los libros
print("--- Lista Inicial de Libros ---")
for libro in libros:
    print(libro)

# 3. Calcular e imprimir el precio total de todos los libros de la lista
precio_total = sum(libro.precio for libro in libros)
print(f"\nPrecio total de los libros: ${precio_total:.2f}")

# 4. Contar e imprimir cuántos libros están marcados como disponible 
disponibles = sum(1 for libro in libros if libro.disponibile)
print(f"Cantidad de libros disponibles: {disponibles}")

# 5. Agrega un nuevo libro a la lista
nuevo_libro = Libro("Fahrenheit 451", "Ray Bradbury", 15.00, True)
libros.append(nuevo_libro)

print("\n--- Lista Actualizada (tras append) ---")
for libro in libros:
    print(libro)