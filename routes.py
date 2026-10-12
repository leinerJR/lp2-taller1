import json
import os
from flask import Blueprint, render_template, abort

main = Blueprint("main", __name__)
RUTA_PRODUCTOS = os.path.join(os.path.dirname(__file__), "data", "productos.json")

def cargar_productos():
    with open(RUTA_PRODUCTOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def buscar_producto_por_sku(sku):
    for producto in cargar_productos():
        if producto["sku"] == sku:
            return producto
    return None

@main.route("/")
def index():
    return render_template("index.html", productos=cargar_productos())

@main.route("/producto/<sku>")
def detalle(sku):
    producto = buscar_producto_por_sku(sku)
    if producto is None:
        abort(404)
    return render_template("detalle.html", producto=producto)
