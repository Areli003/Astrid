class CuentaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular #atributo protegido
        self._saldo
        
    @property
    def saldo(self):
        return self._saldo
    @property
    def titular(self):
        return self._titular
    
    if __name__ == "__main__":
        cuenta = CuentaBancaria("Astrid", 1234)
        print(cuenta.saldo)
        print(cuenta.titular)
        
   