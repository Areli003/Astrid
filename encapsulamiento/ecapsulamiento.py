class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = 0
        self.set_saldo(saldo_inicial)

    # --- MÉTODO GETTER (get_nombre_de_metodo) --- #
    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    # --- MÉTODO SETTER --- #
    def set_saldo(self, nuevo_saldo):
        # Valida que el saldo no sea negativo antes de modificar el estado del atributo
        if isinstance(nuevo_saldo, (int, float)) and nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            self.__saldo = 0
            print(f"[Error] Asignación no es válida: {nuevo_saldo} no es un monto válido.")


if __name__ == "__main__":
    # * 1. Creación de una instancia
    cuenta = CuentaBancaria("Carlos Pérez", 500.00)

    # * 2. Lectura correcta mediante el Getter
    print(f'Titular: {cuenta.get_titular()}')
    print(f'Saldo: Q {cuenta.get_saldo()}')
    #* 3. Intento de mofificacion directa del atributo privado (no recomendado)
    cuenta.__saldo = -1000.0  
    print(f'Saldo después de intento de modificación directa: Q. {cuenta.get_saldo()}') 
    
    #* 4. Modificacioon contralada mediante SETTER (intento Invalido)
    cuenta.set_saldo(-250.0) #Ejecuta validacion y es rechazada
    print(f'Saldo tras intento invalido: Q. {cuenta.get_saldo()}')
    
    #* 5. Modicación controlada mediante SETTER (intento valido)
    cuenta.set_saldo(850.99)
    print(f'Saldo final actualizado: Q. {cuenta.get_saldo()}')
    
    
    