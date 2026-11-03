class Ventilador:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def mostrar(self):
        print("Marca:", self.marca)
        print("Velocidad:", self.velocidad)

    def encender(self):
        print("El ventilador está encendido.")


class Silla:
    def __init__(self, color, material):
        self.color = color
        self.material = material

    def mostrar(self):
        print("Color:", self.color)
        print("Material:", self.material)

    def ocupar(self):
        print("La silla está ocupada.")


class Mesa:
    def __init__(self, color, tamano):
        self.color = color
        self.tamano = tamano

    def mostrar(self):
        print("Color:", self.color)
        print("Tamaño:", self.tamano)

    def limpiar(self):
        print("La mesa fue limpiada.")


class Proyector:
    def __init__(self, marca, resolucion):
        self.marca = marca
        self.resolucion = resolucion

    def mostrar(self):
        print("Marca:", self.marca)
        print("Resolución:", self.resolucion)

    def encender(self):
        print("El proyector está encendido.")


class Aula:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad

    def mostrar(self):
        print("Número del aula:", self.numero)
        print("Capacidad:", self.capacidad)

    def abrir(self):
        print("El aula está abierta.")


# Ingresar los atributos del ventilador
print("\nVENTILADOR")
marca = input("Ingrese la marca: ")
velocidad = int(input("Ingrese la velocidad: "))
ventilador1 = Ventilador(marca, velocidad)

# Ingresar los atributos de la silla
print("\nSILLA")
color = input("Ingrese el color: ")
material = input("Ingrese el material: ")
silla1 = Silla(color, material)

# Ingresar los atributos de la mesa
print("\nMESA")
color = input("Ingrese el color: ")
tamano = input("Ingrese el tamaño: ")
mesa1 = Mesa(color, tamano)

# Ingresar los atributos del proyector
print("\nPROYECTOR")
marca = input("Ingrese la marca: ")
resolucion = input("Ingrese la resolución: ")
proyector1 = Proyector(marca, resolucion)

# Ingresar los atributos del aula
print("\nAULA")
numero = int(input("Ingrese el número del aula: "))
capacidad = int(input("Ingrese la capacidad: "))
aula1 = Aula(numero, capacidad)

# Mostrar la información y utilizar los métodos
print("\n INFORMACIÓN INGRESADA :)")

print("\nVentilador:")
ventilador1.mostrar()
ventilador1.encender()

print("\nSilla:")
silla1.mostrar()
silla1.ocupar()

print("\nMesa:")
mesa1.mostrar()
mesa1.limpiar()

print("\nProyector:")
proyector1.mostrar()
proyector1.encender()

print("\nAula:")
aula1.mostrar()
aula1.abrir()