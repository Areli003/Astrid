class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = self.validar_nombre(nombre)
        self.nota = self.validar_nota(nota)
        
    def validar_nombre(self, nombre):
          nombre = nombre.strip()
          if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
          return nombre

    def validar_nota(self, nota):
        if not 0 <= nota <=10:
            raise TypeError("La nota debe estar entre 0 y 100")
        return nota
    def actualizar_nota(self, nueva_nota):
        self.nota = self.validar_nota(nueva_nota)
        
    def solicitar_entero_positivo(mensaje):
        while True:
            entrada = input(mensaje).strip()
            if entrada:
                try:
                    valor = int(entrada)
                    if valor > 0:
                        return valor
                except ValueError:
                    pass
            print("Por favor, ingrese un número entero positivo.")
            