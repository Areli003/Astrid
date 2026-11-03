"""
Enunciado
Una pequeña tienda necesita un programa para adiministrar sus productos.
--la informacion debe protegerse de la siguiente manera:
"""
class Producto:
    def __init__(self, nombre,  codigo, precio, cantidad):
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
    
    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0:
                self.__precio = nuevo_precio
        else:
                print('Error el precio debe ser mayor que cero. ')     
    
    def set_cantidad(self, nueva_cantidad):
        if isinstance(nueva_cantidad, int) and nueva_cantidad >= 0:
                self.__cantidad = nueva_cantidad
        else:
                print('Error: la cantidad debe ser un entero no negativo')
                
    def agregar_stock(self, cantidad):
        if isinstance(cantidad, int) and cantidad > 0:
            if cantidad <= self.__cantidad:
                self.__cantidad -= cantidad
            else:
                print("Error: no hay suficiente Inventario")
        else:
            print("Error: la cantidad  a retirar debe ser un enterio mayor a cero.")
            
    def mostrar_informacion(self):
        print("Código: ", self.get_codigo())
        print("Nombre: ", self.get_nombre())
        print("Precio: ", self.get_precio())
        print("Cantidad: ", self.get_cantidad())
        

if __name__ == '__main__':
    # Crear instancia
    producto = Producto("Cuaderno", "P001", 1200.0, 10)

    # Mostrar información
    print("Información inicial")
    producto.mostrar_informacion()

    # Intento de agregar precio inválido
    print("\nPrueba precio inválido")
    producto.set_precio(-500)

    # Intento de establecer cantidad inválida
    print("\nPrueba cantidad inválida")
    producto.set_cantidad(-5)

    # Agregar producto al inventario
    print("\nAgregar stock")
    producto.agregar_stock(5)

    # Retirar producto del inventario
    print("\nRetirar stock ")
    producto.retirar_stock(3)

    # Intentar retirar más productos de los disponibles
    print("\nRetirar más del disponible")
    producto.retirar_stock(50)

    # Consultar por medio de los getters
    print("Código:", producto.get_codigo())
    print("Precio:", producto.get_precio())
    print("Cantidad:", producto.get_cantidad())

#R