class CuentaBancaria:
    """Clase que representa una cuenta de ahorro, aplica encapsulamiento para proteger el saldo y datos del titular
    """
    def __init__(self, titular, saldo_inicial, numero_cuenta):
        #atributos privados
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__numero_cuenta = numero_cuenta
        self.__historial = []  
        
        
    #--Getters
    def obtener_saldo(self):
        return self.__saldo
    
    def obtener_titular(self):
        return self.__titular
    
    def obtener_numero_cuenta(self):
        return self.__numero_cuenta
    
    def obtener_historial(self):
        return self.__historial
        
    #Setter con validacion
    def establecer_titular(self, nuevo_nombre):
        if len(nuevo_nombre.strip()) > 0:
            self.__titular = nuevo_nombre
            return "Nombre del titular actualizado correctamente."
        
        else:
            return "Error: el nombre no puede estar vacio."
        
    #Metoods con parametros y retorno de valores
    def depositar(self, monto):
        if monto <= 0:
            return "Error: el monto a depositar debe ser positivo"
        self.__saldo += monto
        self.__registrar_movimiento("Deposito", monto) 
        return f"Deposito exitoso. Nuevo saldo: Qn{self.__saldo:2f}"      
    def retirar(self, monto):
        if monto <= 0:
            return "Error: fondos insuficientes."
        
        self.__saldo -= monto
        self.__registrar_movimiento("Retiro", monto)
        return f"Registro exitoso. Nuevo saldo: Q {self.__saldo:-2f}"
    def aplicar_intereses(self, tasa_porcentaje):
     #Reutilizacion: aplicar_interes reutliza la logica de depositar
     
     interes_ganado = self.__saldo * (tasa_porcentaje / 100)
     return self.depositar(interes_ganado)
 
 #metodo privado de uso interno(organizacion modular)
    def __registrar_movimiento(self,tipo, monto):
        self.__historial.append(f"{tipo}: Q {monto:.2f}")
    
    def mostrar_estado_cuenta(self):
        print(f"\---Estado de Cuenta ---")
        print(f"Titutlar: {self.__titulst}")
        print(f"No. Cuenta: {self.__numero_cuenta}")
        print(f"Saldo actual: {self.__saldo:.2f}")
        print(f"Historial de movimiento")
        for movimiento in self.__historial:
            print(f"  -  {movimiento}")
            
if __name__ == "__main__":
    
    cuenta_juan = CuentaBancaria("Juan", 1500.00, 'GT-00123')

    