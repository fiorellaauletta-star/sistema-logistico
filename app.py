from flask import Flask, render_template, request
from empresa import cargar_datos, guardar_datos, ventas, gastos, stock, clientes, proveedores
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
import webbrowser

app = Flask(__name__)

# Cargar datos al iniciar
cargar_datos()

@app.route('/')
def index():
    return render_template("index.html", ventas=ventas, gastos=gastos)

@app.route('/ventas', methods=["GET", "POST"])
def ver_ventas():
    if request.method == "POST":
        producto = request.form["producto"]
        cantidad = int(request.form["cantidad"])
        precio_unitario = float(request.form["precio_unitario"])
        total = cantidad * precio_unitario
        ventas.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "total": total
        })
        # Actualizar stock
        stock[producto] = stock.get(producto, 0) - cantidad
        guardar_datos()
    return render_template("ventas.html", ventas=ventas)

@app.route('/gastos', methods=["GET", "POST"])
def ver_gastos():
    if request.method == "POST":
        concepto = request.form["concepto"]
        monto = float(request.form["monto"])
        tipo = request.form.get("tipo", "variable")
        area = request.form.get("area", "general")
        gastos.append({
            "concepto": concepto,
            "monto": monto,
            "tipo": tipo,
            "area": area
        })
        guardar_datos()
    return render_template("gastos.html", gastos=gastos)

@app.route('/resumen')
def ver_resumen():
    total_ventas = sum(v["total"] for v in ventas)
    total_gastos = sum(g["monto"] for g in gastos)
    ganancia = total_ventas - total_gastos

    # Gastos por área
    areas = {}
    for g in gastos:
        area = g.get("area", "general")
        areas[area] = areas.get(area, 0) + g["monto"]

    return render_template(
        "resumen.html",
        total_ventas=total_ventas,
        total_gastos=total_gastos,
        ganancia=ganancia,
        areas=areas
    )

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)