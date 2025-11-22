import json

ventas = []
gastos = []
stock = {"remera": 50, "pantalón": 40, "zapatilla": 30}
clientes = {}
proveedores = {}

def cargar_datos():
    global ventas, gastos, stock, clientes, proveedores
    try:
        with open("data.json", "r") as f:
            datos = json.load(f)
            ventas = datos.get("ventas", [])
            gastos = datos.get("gastos", [])
            stock = datos.get("stock", stock)
            clientes = datos.get("clientes", {})
            proveedores = datos.get("proveedores", {})
    except FileNotFoundError:
        ventas = []
        gastos = []
        clientes = {}
        proveedores = {}

def guardar_datos():
    with open("data.json", "w") as f:
        json.dump({
            "ventas": ventas,
            "gastos": gastos,
            "stock": stock,
            "clientes": clientes,
            "proveedores": proveedores
        }, f)