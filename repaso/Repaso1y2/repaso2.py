#Sistema de Préstamo de Libros en Biblioteca
"""Este ejercicio ilustra la interacción entre dos clases: Libro y Lector. La clase Libro administra el estado de disponibilidad de un ejemplar físico, mientras que el flujo del programa valida que no se preste un libro ya prestado ni se devuelva uno que ya se encuentra en biblioteca."""
class Lector:
  """Modela a un usuario registrado en la biblioteca"""
  def __init__(self, id_lector: str, nombre: str):
    self.id_lector = id_lector
    self.nombre = nombre

  def mostrar_informacion(self) -> str:
    return f"Lector: {self.nombre} [ID: {self.id_lector}]"

"""
El ISBN (International Standard Book Number o Número Internacional Normalizado del Libro) es un código de barras numérico único de 13 dígitos que funciona como el documento de identidad de una publicación.
"""

class Libro:
  """Modela un libro y controla el flujo de prestamo y devolución"""
  def __init__(self, isbn: str, titulo: str, autor: str):
    self.isbn = isbn
    self.titulo = titulo
    self.autor = autor
    self.prestado = False
    self.prestado_a = None

  def prestar(self, lector: Lector):
    if self.prestado:
      print(f"[RECHAZADO] El libro '{self.titulo}' ya se encuentra prestado a {self.prestado_a.nombre}.")
    else:
      self.prestado = True
      self.prestado_a = lector
      print(f"[ÉXITO] Libro '{self.titulo}' prestado exitosamente a {lector.nombre}.")

  def devolver(self):
    if not self.prestado:
      print(f"[AVISO] El libro '{self.titulo}' ya está disponible en estantería (no estaba prestado).")
    else:
     usuario_anterior = self.prestado_a.nombre
     self.prestado = False
     self.prestado_a = None
     print(f"[ÉXITO] Libro '{self.titulo}' devuelto por {usuario_anterior}. Ahora disponible.")

  def mostrar_estado(self):
      estado = "DISPONIBLE" if not self.prestado else f"PRESTADO a {self.prestado_a.nombre}"
      print(f"[{self.isbn}] '{self.titulo}' - Autor: {self.autor} | Estado: {estado}")

if __name__ == "__main__":
    print("=== EJERCICIO 2: CONTROL DE BIBLIOTECA ===\n")

# Creación de instancias
    lector_a = Lector("LEC-101", "Ana Gómez")
    lector_b = Lector("LEC-102", "Mario Rivas")
    libro_poo = Libro("978-0134685991", "Java How to Program", "P. Deitel & H. Deitel")
    
# 1. Estado inicial mostrar estado de los libros
# 2. Préstamo exitoso
# 3. Validación de caso borde: intentar prestarlo nuevamente estando prestado
# 4. Devolución exitosa
# 5. Validación de caso borde: intentar devolverlo cuando ya está en biblioteca

 # 1. Estado inicial
    print("--- 1. Estado inicial ---")
    libro_poo.mostrar_estado()
    print()

    # 2. Préstamo exitoso
    print("--- 2. Préstamo exitoso ---")
    libro_poo.prestar(lector_a)
    libro_poo.mostrar_estado()
    print()

    # 3. Validación de caso borde: intentar prestarlo nuevamente estando prestado
    print("--- 3. Intentar prestar un libro ya prestado ---")
    libro_poo.prestar(lector_b)
    print()

    # 4. Devolución exitosa
    print("--- 4. Devolución exitosa ---")
    libro_poo.devolver()
    libro_poo.mostrar_estado()
    print()

    # 5. Validación de caso borde: intentar devolverlo cuando ya está en biblioteca
    print("--- 5. Intentar devolver un libro que ya está disponible ---")
    libro_poo.devolver()
    print() 