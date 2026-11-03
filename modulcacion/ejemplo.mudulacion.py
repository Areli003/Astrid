#EJEMPLO DE PROGRAMACION MODULAR

def calcular_subtotal(precio_unitario, cantidad):
    """Módulo encargardo de únicamente de calcular el subtotal.
    """
    return precio_unitario * cantidad

def calcular_impuesto(subtotal, tasa_iva=0.12):
    """Múdulo encargado únicamente del calculo del impuesto."""
    return subtotal * tasa_iva

def calcular_descuento(subtotal, es_cliente_vip):
    """Modulo encargado unicamente de aplicar descuento"""
    if es_cliente_vip:
        return subtotal * 0.05
    return 0

def calcular_total(subtotal, impuesto, descuento):
    """Módulo encargado únicamente del calculo del total."""
    return subtotal + impuesto - descuento
      
def generar_factura(nombre_producto, precio_unitario, cantidad, es_cliente_vip):
    """Módulo orquestador: reutiliza y organiza las demás funcione, sin repetir su logica. Esto es organización modular"""
    if es_cliente_vip:
        return subtotal
    
    subtotal = calcular_subtotal(precio_unitario, cantidad)
    impuestos = calcular_impuesto(subtotal)
    descuento = calcular_descuento(subtotal, es_cliente_vip)
    total = calcular_total(subtotal, impuestos, descuento)
    
    print(f'\--Factura: {nombre_producto}--')
    print(f'Subtotal: Q{subtotal:.2f}')
    print(f'Impuesto: (Iva) Q{descuento:.2f}')
    print(f'Descuento: Q{descuento:.2f}')
    print(f'TOTAL A PAGAR : Q{total:.2f}')
    
    return total

generar_factura("Laptop", 4500.00, 1, es_cliente_vip=True)
generar_factura("Mouse", 80.00, 3, es_cliente_vip=False)