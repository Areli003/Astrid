class Titular: 
    """Representa a la persona titular de la cuenta bancaria"""
    def __init__(self, nombre: str, identificacion: str):
        self.nombre = nombre 
        self.identificacion = identificacion
        
    def mostrar_datos(self):
        return f"Titular: {self.nombre} (DPI: {self.identificacion} )"

class CuentaBancaria:
    """Representa la cuenta y maneja el estado del saldo"""
    def __init__(self,
                 numero_cuenta: str,
                 titular: Titular,
                 saldo_inicial: float = 0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo_inicial = saldo_inicial
        
    def depositar(self, monto: float):
        """Deposita una cantidad en la cuenta."""
        if monto > 0:
            self.saldo_inicial += monto
            print(f"[ok] Deposito de Q{monto:.2f} exitoso. Nuevo saldo: Q{self.saldo_inicial:.2f}")
        else:
            print("[error] El monto a depositar debe ser mayor a Q.0.")
            
    def retirar(self, monto: float):
        """Retira una cantidad de la cuenta."""
        if monto <= 0:
            print("[error] El monto a retirar debe ser mayor a Q.0.00")
        elif monto > self.saldo_inicial:
            print(
                f"[error] Fondos insuficientes. Intento de retiro: Q{monto:.2f}, "
                f"Saldo disponible: Q{self.saldo_inicial:.2f}"
            )
        else:
            self.saldo_inicial -= monto
            print(f"[ok] Retiro de Q{monto:.2f} exitoso. Nuevo saldo: Q{self.saldo_inicial:.2f}")
            
    def consultar_resumen(self):
        """Muestra el saldo actual de la cuenta."""
        print("\n -- Resumen de cuenta -- ")
        print(f"No. cuenta: {self.numero_cuenta}")
        print(self.titular.mostrar_datos())
        print(f"Saldo actual: Q{self.saldo_inicial:.2f}")
        print("------------------------\n")

if __name__ == "__main__":
    cliente = Titular("Maria Morales", "123456 78901 8701")
    cuenta = CuentaBancaria(numero_cuenta="1234567890", titular=cliente, saldo_inicial=500.00)
    
    cuenta.consultar_resumen()
    cuenta.depositar(250.25)
    cuenta.retirar(100.00)
    
    # Pruebas de casos de error
    cuenta.retirar(100000000000.00)
    cuenta.retirar(-300.00)
    cuenta.depositar(-50.00)  # Caso de error: depósito menor o igual a cero