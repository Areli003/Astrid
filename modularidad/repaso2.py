class CuentaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    @property
    def titular(self) -> str:
        return self._titular

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, monto: float) -> bool:
        if monto > 0:
            self._saldo += monto
            return True
        return False

    def retirar(self, monto: float) -> bool:
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            return True
        return False


class GestorTransferencias:
    def realizar_transferencia(
        self,
        origen: CuentaBancaria,
        monto: float,
        cuenta_destino: CuentaBancaria,
    ) -> bool:
        print(
            f"Realizando transferencia de {monto} desde "
            f"{origen.titular} a {cuenta_destino.titular}."
        )
        if origen.retirar(monto):
            cuenta_destino.depositar(monto)
            print("Transferencia realizada con éxito.")
            return True

        print("No se pudo realizar la transferencia. Fondos insuficientes.")
        return False

    def reportar_estado_cuenta(self, cuenta: CuentaBancaria) -> None:
        print(
            f"Estado de la cuenta de {cuenta.titular}: "
            f"Saldo actual = Q{cuenta.saldo}"
        )


if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Carlos Berríos", 1000.0)
    cuenta2 = CuentaBancaria("Giova Guerra", 500.0)

    gestor = GestorTransferencias()
    gestor.reportar_estado_cuenta(cuenta1)
    gestor.realizar_transferencia(cuenta1, 250.0, cuenta2)
    gestor.reportar_estado_cuenta(cuenta1)
    gestor.reportar_estado_cuenta(cuenta2)
        
            
            
      
    
     