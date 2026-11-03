class Empleado:
    def __init__(self, codigo, nombre, salario, empleado):
        self.codigo = codigo
        self.nombre = nombre
        self.salario = salario
        

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Salario: {self.salario:.2f}"
    
    #Almacenamiento inicial
    Empleado =  [
        Empleado("E01", "Juan Pérez", 2500.00),
        Empleado("E02", "María López", 3000.00),
        Empleado("E03", "Carlos García", 2800.00)
    ]
    
    empleados = []
    nuevo1 = Empleado("E01", "Juan Pérez", 2500.00)
    nuevo2 = Empleado("E02", "María López", 3000.00)
    
    empleados.append(nuevo1)
    empleados.append(nuevo2)
    
    print(f'total  de empleados: {len(empleados)}')
    
    datos_empleados = []
    {"codigo": "E01", "nombre": "Juan Pérez", "salario": 2500.00},
    {"codigo": "E02", "nombre": "María López", "salario": 3000.00},
    {"codigo": "E03", "nombre": "Carlos García", "salario": 2800.00}
     
    empleados_externos = []
    for datos in datos_empleados:
        empleado_externo = Empleado(datos["codigo"], datos["nombre"], datos["salario"])
        

    for emp in empleados_externos:
        print(emp)
        
    """Validación antes de almacenar (evitar duplicadas)"""
    def existe_empleado(empleados, codigo):
        for emp in empleados:
            if emp.codigo == codigo:
                return  True
            return False 
    nuevo_empleado = Empleado("E01", "Juan Pérez", 4500.00)
    if not existe_empleado(empleados, nuevo_empleado.codigo):
        empleados.append(nuevo_empleado)
        print(f"Empleado {nuevo_empleado.nombre} agregado exitosamente.")
    else:
        print(f"Empleado  con código {nuevo_empleado.codigo} ya existe. No se puede agregar.")
    
        