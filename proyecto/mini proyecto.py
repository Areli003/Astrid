# ==========================================
# MINI PROYECTO 1: INVENTARIO DE TIENDA
# ==========================================

class Producto:
    """Clase que representa un producto del inventario"""
 
    def __init__(self, codigo, nombre, precio, existencias, categoria):
        if not codigo.strip() or not nombre.strip():
            raise ValueError("El código y el nombre no pueden estar vacíos")

        # Atributos con guion bajo = encapsulados
        # El código se guarda en mayúsculas para evitar duplicados como p001 / P001
        self._codigo = codigo.strip() 
        self._nombre = nombre.strip() 
        self._precio = 0.0
        self._existencias = 0
        self._categoria = categoria.strip()  or "General" 

        # Validar y asignar usando los setters
        self.precio = precio
        self.existencias = existencias
 
    # --- Propiedades (getters) ---
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio
    

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo")

    @property 
    def existencias(self):
        return self._existencias

    @existencias.setter
    def existencias(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._existencias = nueva_cantidad
        else:
            raise ValueError("Las existencias no pueden ser negativas")

    @property
    def categoria(self):
        return self._categoria

    # --- Métodos ---
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio  # usa el setter que valida

    def agregar_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que 0")
        self._existencias += cantidad
        return True

    def reducir_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a reducir debe ser mayor que 0")
        if cantidad > self._existencias:
            raise ValueError("Cantidad insuficiente en inventario")
        self._existencias -= cantidad
        return True

    def valor_total_producto(self):
        return self._precio * self._existencias

    def mostrar_info(self):
        return (f"Código: {self._codigo} | Nombre: {self._nombre:20} | "
                f"Precio: Q{self._precio:8.2f} | Stock: {self._existencias:4} | "
                f"Categoría: {self._categoria}")


class Inventario:
    """Clase que gestiona la colección de productos"""

    def __init__(self):
        self._productos = []  # Lista de objetos Producto
        self._agregar_datos()

    def _agregar_datos(self):
        try:
            self.agregar(Producto("P001", "Arroz", 2.50, 50, "Alimentación"))
            self.agregar(Producto("P002", "Leche", 1.80, 30, "Alimentación"))
            self.agregar(Producto("P003", "Jabón", 0.95, 5, "Limpieza"))
        except ValueError as e:
            print(f"Error en precarga: {e}")

    def agregar(self, nuevo_producto):
        for p in self._productos:
            if p.codigo == nuevo_producto.codigo:
                raise ValueError(f"Ya existe un producto con el código {nuevo_producto.codigo}")
        self._productos.append(nuevo_producto)
        return True

    def buscar_por_codigo(self, codigo):
        codigo = codigo.strip().upper()  
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def buscar_por_nombre(self, nombre):
        coincidencias = []
        for producto in self._productos:
            if nombre.lower() in producto.nombre.lower():
                coincidencias.append(producto)
        return coincidencias

    def listar_todo(self):
        if not self._productos:
            print(" El inventario está vacío")
            return
        print("\n" + "=" * 70)
        print(" " * 20 + "LISTADO DE INVENTARIO")
        print("=" * 70)
        for p in self._productos:
            print(p.mostrar_info())
        print(f"\nTotal de productos: {len(self._productos)}")

    def actualizar_existencias(self, codigo, cantidad):
        producto = self.buscar_por_codigo(codigo)
        if not producto:
            return False, " Producto no encontrado"
        try:
            if cantidad >= 0:
                producto.agregar_stock(cantidad)
            else:
                producto.reducir_stock(-cantidad)
            return True, "Cantidad actualizada correctamente"
        except ValueError as e:
            return False, f" {e}"

    def calcular_valor_total(self):
        return sum(p.valor_total_producto() for p in self._productos)

    def cantidad_total(self):
        """Suma de todas las unidades en existencia"""
        return sum(p.existencias for p in self._productos)

    def precio_promedio(self):
        if not self._productos:
            return 0.0
        return sum(p.precio for p in self._productos) / len(self._productos)

    def existencias_promedio(self):
        if not self._productos:
            return 0.0
        return self.cantidad_total() / len(self._productos)

    def producto_mas_caro(self):
        
        
        if not self._productos:
            return None
        return max(self._productos, key=lambda p: p.precio)

    def reporte_resumen(self):
        """Devuelve un diccionario con los datos del reporte"""
        caro = self.producto_mas_caro()
        return {
            "productos": len(self._productos),
            "unidades": self.cantidad_total(),
            "valor_total": self.calcular_valor_total(),
            "precio_promedio": self.precio_promedio(),
            "existencias_promedio": self.existencias_promedio(),
            "mas_caro": caro.nombre if caro else "N/A",
        }

    def productos_bajos(self, limite=5):
        return [p for p in self._productos if p.existencias < limite]

    def eliminar(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto:
            self._productos.remove(producto)
            return True
        return False


# ==========================================
# FUNCIONES REUTILIZABLES DE ENTRADA
# ==========================================

def leer_entero(mensaje):
    """Devuelve un entero o None si la entrada no es válida"""
    try:
        return int(input(mensaje))
    except ValueError:
        return None


def leer_decimal(mensaje):
    """Devuelve un float o None si la entrada no es válida"""
    try:
        return float(input(mensaje))
    except ValueError:
        return None


# ==========================================
# UNA FUNCIÓN POR OPCIÓN DEL MENÚ
# ==========================================

def opcion_agregar(inv):
    print("\n--- Agregar Nuevo Producto ---")
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    precio = leer_decimal("Precio: ")
    existencias = leer_entero("Existencias: ")
    if precio is None or existencias is None:
        print(" Precio y existencias deben ser números")
        return
    categoria = input("Categoría: ").strip()
    try:
        inv.agregar(Producto(codigo, nombre, precio, existencias, categoria))
        print(" Producto agregado con éxito")
    except ValueError as e:
        print(f"{e}")


def opcion_buscar(inv):
    print("\nBuscar por: 1) Código  2) Nombre")
    tipo = input("Seleccione (1/2): ").strip()
    if tipo == "1":
        p = inv.buscar_por_codigo(input("Ingrese el código a buscar: "))
        if p:
            print("\nProducto encontrado:")
            print(p.mostrar_info())
        else:
            print("Producto no encontrado")
    elif tipo == "2":
        resultados = inv.buscar_por_nombre(input("Ingrese el nombre (o parte): ").strip())
        if resultados:
            print(f"\n{len(resultados)} coincidencia(s):")
            for p in resultados:
                print(f"   {p.mostrar_info()}")
        else:
            print(" No hay productos con ese nombre")
    else:
        print(" Opción no válida")


def opcion_existencias(inv):
    codigo = input("Código del producto: ").strip()
    cantidad = leer_entero("Cantidad (+ agregar / - restar): ")
    if cantidad is None:
        print(" Debe ingresar un número entero")
        return
    _, mensaje = inv.actualizar_existencias(codigo, cantidad)
    print(mensaje)


def opcion_precio(inv):
    p = inv.buscar_por_codigo(input("Código del producto: "))
    if not p:
        print(" Producto no encontrado")
        return
    nuevo = leer_decimal(f"Nuevo precio (actual: Q{p.precio:.2f}): ")
    if nuevo is None:
        print(" El precio debe ser un número")
        return
    try:
        p.actualizar_precio(nuevo)
        print(" Precio actualizado")
    except ValueError as e:
        print(f" {e}")


def opcion_bajos(inv):
    entrada = input("Mostrar productos con stock menor a (5): ").strip()
    limite = int(entrada) if entrada.isdigit() else 5
    bajos = inv.productos_bajos(limite)
    if bajos:
        print(f"\nProductos con bajo inventario (menos de {limite}):")
        for p in bajos:
            print(f"   {p.mostrar_info()}")
    else:
        print(" Todos los productos tienen buen stock")


def opcion_reporte(inv):
    r = inv.reporte_resumen()
    print("\n" + "=" * 40)
    print("        REPORTE DEL INVENTARIO")
    print("=" * 40)
    print(f"Productos registrados:   {r['productos']}")
    print(f"Unidades en total:       {r['unidades']}")
    print(f"Valor total:             Q{r['valor_total']:.2f}")
    print(f"Precio promedio:         Q{r['precio_promedio']:.2f}")
    print(f"Existencias promedio:    {r['existencias_promedio']:.1f}")
    print(f"Producto más caro:       {r['mas_caro']}")


def opcion_eliminar(inv):
    if inv.eliminar(input("Código del producto a eliminar: ")):
        print(" Producto eliminado")
    else:
        print(" Producto no encontrado")

# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def menu():
    print("\n" + "=" * 40)
    print("      SISTEMA DE INVENTARIO")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar inventario completo")
    print("3. Buscar producto (por código o nombre)")
    print("4. Actualizar existencias")
    print("5. Actualizar precio")
    print("6. Mostrar productos con bajo inventario")
    print("7. Mostrar valor total del inventario (reporte)")
    print("8. Eliminar producto")
    print("0. Salir")
    print("=" * 40)


def main():
    inventario = Inventario()
    acciones = {
        "1": opcion_agregar,
        "2": lambda inv: inv.listar_todo(),
        "3": opcion_buscar,
        "4": opcion_existencias,
        "5": opcion_precio,
        "6": opcion_bajos,
        "7": opcion_reporte,
        "8": opcion_eliminar,
    }

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción no válida. Intente nuevamente")
            continue
        try:
            accion(inventario)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()