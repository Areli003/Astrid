class Vehiculo:
    def __init__(self, placa, marca, modelo, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"Placa: {self.placa} | Marca: {self.marca} | Modelo: {self.modelo} | Precio: ${self.precio:.2f}"


def existe_placa(lista, placa):
    """Retorna True si la placa ya existe en la lista"""
    for v in lista:
        if v.placa == placa:
            return True
    return False


# 1. Crear una lista vacía llamada 'vehiculos'
vehiculos = []

# 2. Almacenar 3 vehículos usando .append()
vehiculos.append(Vehiculo("P-123ABC", "Toyota", 2022, 18500.00))
vehiculos.append(Vehiculo("P-456DEF", "Honda", 2021, 15000.00))
vehiculos.append(Vehiculo("P-789GHI", "Mazda", 2023, 21000.00))

# 3. Simular un dataset (lista de diccionarios) con 2 vehículos adicionales
# y almacenarlos en la lista usando un bucle for
dataset_nuevos = [
    {"placa": "P-321JKL", "marca": "Nissan", "modelo": 2020, "precio": 12500.00},
    {"placa": "P-656MNO", "marca": "Hyundai", "modelo": 2024, "precio": 22000.00}
]

for item in dataset_nuevos:
    # Validamos opcionalmente también aquí por seguridad antes de cargarlos del dataset
    if not existe_placa(vehiculos, item["placa"]):
        nuevo_vehiculo = Vehiculo(
            item["placa"], item["marca"], item["modelo"], item["precio"]
        )
        vehiculos.append(nuevo_vehiculo)

# 4. Antes de agregar un nuevo vehículo, validar con existe_placa() que la placa no esté duplicada
placa_a_ingresar = "P-999XYZ"
marca_ingreso = "Kia"
modelo_ingreso = 2023
precio_ingreso = 19000.00

if existe_placa(vehiculos, placa_a_ingresar):
    print(f"Error: La placa {placa_a_ingresar} ya se encuentra registrada.")
else:
    vehiculo_nuevo = Vehiculo(placa_a_ingresar, marca_ingreso, modelo_ingreso, precio_ingreso)
    vehiculos.append(vehiculo_nuevo)
    print(f"Vehículo con placa {placa_a_ingresar} agregado exitosamente.")

# 5. Imprimir el total de vehículos almacenados
print("\n--- LISTA DE VEHÍCULOS ALMACENADOS ---")
for vehiculo in vehiculos:
    print(vehiculo)

print(f"\nTotal de vehículos en el sistema: {len(vehiculos)}")