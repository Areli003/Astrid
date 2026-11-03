class Departamento:
    def __init__(self,nombre):
        self.__empleados = []
        
    @property
    def nombre(self):
        return self._nombre
    
    def recibir_empleado(self, empleado):
        self._empleados.append(empleado)
        empleado.asignar_departamento(self)

class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario
        self._departamento = None
        
    @property
    def salario(self):
        return self._salario
    
    @property
    def salario(self):
        return self._salario
    
    @property.setter
    def sakario(self, nuevo_salario):
        if nuevo_salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salario = nuevo_salario
        
    def asignar_departamento(self, departamento):
        self._departamento = departamento
        print(f"{self._nombre} fue asignado al departamento {departamento.nombre}.")
        
if __name__ == "__main__":
    depto = Departamento("Recursos Humanos")
    emp = Empleado("Juan Perez", 5000)
    depto.recibir_empleado(emp)
    emp.salario = 5000.0 #usa setter con validacion{
    
    print(f"Nuevo salario: Q {emp.salario:.2f}")
    
    
    
    