class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    #get -> obtener
    def obtener_saldo(self):
        return self.__saldo
    #setter ->modificar
    def set_saldo(self, nuevo_saldo):
        #validacion
        if nuevo_saldo > 0:
            self.__saldo = nuevo_saldo
            print(f"Su saldo ha sido acreditado, saldo actual: ${self.__saldo}")
        else:
            print("El valor debe ser mayor a 0")

    def validar_edad(self, edad):
        return 0 <= edad <= 120
    
    try:
        numero = int(input("Ingrese un numero entero: "))
    except ValueError:
        print("Error: Debe ingresar un número valido.")
    finally:
        print("Termino de ejecutar el try o except")
        
    cuenta1 = Cuenta("Luis", 300)
    
    try:
        cuenta.retirar(200)
    except ValueError as error: 
    
    try:  
        cuenta1.retirar(200)
    except ValueError as error:
            print(f"Operación rechazada: {error}")
     
    finally:
        print("Operación finalizada.")
        
        
        