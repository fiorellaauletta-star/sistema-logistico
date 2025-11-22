# Sistema de gestión para pequeños negocios

ventas = []
gastos = []
stock = {}
clientes = {}
proveedores = {}

def registrar_venta(producto, cantidad, precio_unitario):
    total = cantidad * precio_unitario
    ventas.append({"producto": producto, "cantidad": cantidad, "total": total})
    stock[producto] = stock.get(producto, 0) - cantidad
    print(f"Venta registrada: {producto} x{cantidad} = ${total}")

def registrar_gasto(concepto, monto):
    gastos.append({"concepto": concepto, "monto": monto})
    print(f"Gasto registrado: {concepto} = ${monto}")

def ver_ganancia():
    ingreso = sum(v["total"] for v in ventas)
    egreso = sum(g["monto"] for g in gastos)
    print(f"Ganancia neta: ${ingreso - egreso}")

def cargar_cliente(nombre, contacto):
    clientes[nombre] = contacto
    print(f"Cliente cargado: {nombre} - {contacto}")

def cargar_proveedor(nombre, contacto):
    proveedores[nombre] = contacto
    print(f"Proveedor cargado: {nombre} - {contacto}")

# Ejemplo de uso
stock["lapicera"] = 100
registrar_venta("lapicera", 5, 50)
registrar_gasto("envío", 100)
cargar_cliente("Juan Pérez", "juan@email.com")
cargar_proveedor("Distribuidora Sur", "ventas@sur.com")
ver_ganancia()


ventas = []
gastos = []
stock = {}
clientes = {}
proveedores = {}

def registrar_venta():
    producto = input("Producto vendido: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio unitario:"))
    total = cantidad * precio
    ventas.append({"producto": producto, "cantidad": cantidad, "total": total})
    stock[producto] = stock.get(producto, 0) - cantidad
    print(f"Venta registrada: {producto} x{cantidad} = ${total}")

def registrar_gasto():
    concepto = input("Concepto del gasto: ")
    monto = float(input("Monto: "))
    gastos.append({"concepto": concepto, "monto": monto})
    print(f"Gasto registrado: {concepto} = ${monto}")

def cargar_cliente():
    nombre = input("Nombre del cliente: ")
    contacto = input("Contacto: ")
    clientes[nombre] = contacto
    print(f"Cliente cargado: {nombre} - {contacto}")

def cargar_proveedor():
    nombre = input("Nombre del proveedor: ")
    contacto = input("Contacto: ")
    proveedores[nombre] = contacto
    print(f"Proveedor cargado: {nombre} - {contacto}")

def ver_ganancia():
    ingreso = sum(v["total"] for v in ventas)
    egreso = sum(g["monto"] for g in gastos)
    print(f"Ganancia neta: ${ingreso - egreso}")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar venta")
        print("2. Registrar gasto")
        print("3. Cargar cliente")
        print("4. Cargar proveedor")
        print("5. Ver ganancia")
        print("6. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            registrar_gasto()
        elif opcion == "3":
            cargar_cliente()
        elif opcion == "4":
            cargar_proveedor()
        elif opcion == "5":
            ver_ganancia()
        elif opcion == "6":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida. Probá de nuevo.")

# Carga inicial de stock
stock["lapicera"] = 100
stock["cuaderno"] = 50

menu()