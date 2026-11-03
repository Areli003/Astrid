class Producto:
    def __init__(self, nombre, codigo, precio, cantidad):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__precio = 0
        self.__cantidad = 0
        self.set_precio(precio)
        self.set_cantidad(cantidad)

    # Getters
    def get_codigo(self):
        return self.__codigo

    def get_precio(self):
        return self.__precio

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    # Setters
    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Error el precio debe ser mayor que cero.")

    def set_cantidad(self, nueva_cantidad):
        if isinstance(nueva_cantidad, int) and nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            print("Error: la cantidad debe ser un entero no negativo")

    # Métodos de stock
    def agregar_stock(self, cantidad):
        if isinstance(cantidad, int) and cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("Error: la cantidad a agregar debe ser un entero mayor a cero.")

    def retirar_stock(self, cantidad):
        if isinstance(cantidad, int) and cantidad > 0:
            if cantidad <= self.__cantidad:
                self.__cantidad -= cantidad
            else:
                print("Error: no hay suficiente Inventario")
        else:
            print("Error: la cantidad a retirar debe ser un entero mayor a cero.")

    def mostrar_informacion(self):
        print("Código:", self.get_codigo())
        print("Nombre:", self.get_nombre())
        print("Precio:", self.get_precio())
        print("Cantidad:", self.get_cantidad())


if __name__ == '__main__':
    # Crear instancia
    producto = Producto("Laptop", "P001", 1200.0, 10)

    # mostrar informacion
    producto.mostrar_informacion()

    # intento de agregar precio invalido
    print("\nPrueba precio inválida")
    producto.set_precio(-500)

    # intento de establecer cantidad invalida
    print("\nPrueba cantidad inválida")
    producto.set_cantidad(-5)

    # agregar producto al inventario
    print("\nAgregar stock")
    producto.agregar_stock(5)

    # Retirar producto del inventario
    print("\nRetirar stock ")
    producto.retirar_stock(3)

    # intentar retirar mas productos de los disponibles
    print("\nRetirar más del disponible")
    producto.retirar_stock(50)

    # Consultar por medio de los getters
    print("Código:", producto.get_codigo())
    print("Nombre:", producto.get_nombre())
    print("Precio:", producto.get_precio())
    print("Cantidad:", producto.get_cantidad())
    
    

#1. ¿Cuál es la diferencia técnica entre asignar un valor directamente a una variable y hacerlo a través de un método setter?
#La diferencia fundamental radica en el encapsulamiento y la validación, es que la asignación directa modifica el atributo 
#sin restricciones, y de esa manera permite la entrada de datos inconsistentes, como lo  es un precio negativo un tipo de dato 
#incorrecto. Por otro lado, el método setter actúa como un filtro que encapsula la lógica de asignación, evaluando primero si el 
#valor cumple con las reglas de negocio, como lo seria en este caso verificar que el valorsea numérico y no negativo, antes de 
#autorizar el cambio en el estado interno del objeto, protegiendo así la integridad de los datos y asegurando que el objeto se
#mantenga en un estado válido.

#2. Si en Python declaramos un atributo como__variable, ¿por qué decimos que está privatizado?
#En Python, decimos que está privatizado porque él aplica un mecanismo llamado Name Mangling, el cual transforma automáticamente el
#atributo__variable en _NombreDeLaClasr__variable para ocultarlo del exterior. Esto impide que el valor se lea o modifique por
#accidente mediante un acceso directo convencional, que forzara al programador a interactuar con el atributo únicamente a través
# de los métodos públicos definidos por la clase para proteger el estado interno del objeto.

#3. ¿En qué escenario es conveniente crear un getter pero NO un setter?
#Es conveniente crear atributos de solo lectura, como el atributo__código del ejercicio. Este patrón se aplica cuando el valor
#de una variable se asigna una sola vez al instanciar el objeto (__init__) y debe poder consultarse públicamente a lo largo del 
#programa, pero no debe modificarse bajo ninguna circunstancia para poder garantizar que los datos críticos del sistema no se 
#alteren de forma accidental o indebida.


