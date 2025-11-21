from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://sites.google.com"])

PRODUCTOS = {
    "perros": [
        {"nombre": "Alimento para perros Royal Canin", "precio": 59.99, "descripcion": "Alimento balanceado para perros adultos"},
        {"nombre": "Collar antitirones", "precio": 25.99, "descripcion": "Collar para paseos seguros"},
        {"nombre": "Juguete mordedor", "precio": 12.99, "descripcion": "Juguete resistente para perros"}
    ],
    "gatos": [
        {"nombre": "Arena sanitaria para gatos", "precio": 19.99, "descripcion": "Arena absorbente y sin polvo"},
        {"nombre": "Rascador para gatos", "precio": 35.99, "descripcion": "Rascador con plataforma y juguete"},
        {"nombre": "Alimento húmedo para gatos", "precio": 9.99, "descripcion": "Comida húmeda premium para gatos"}
    ],
    "peces": [
        {"nombre": "Comida para peces tropicales", "precio": 7.99, "descripcion": "Alimento balanceado para peces"},
        {"nombre": "Aireador de acuario", "precio": 15.99, "descripcion": "Mantiene el agua oxigenada"},
        {"nombre": "Decoración para acuario", "precio": 12.99, "descripcion": "Plantas y rocas decorativas"}
    ],
    "aves": [
        {"nombre": "Semillas para loros", "precio": 14.99, "descripcion": "Mezcla nutritiva para aves"},
        {"nombre": "Jaula para pájaros pequeña", "precio": 49.99, "descripcion": "Jaula segura y cómoda"},
        {"nombre": "Juguete colgante para aves", "precio": 9.99, "descripcion": "Entretenimiento para aves"}
    ]
}

@app.route('/')
def home():
    return jsonify({
        "mensaje": "API de Búsqueda de Productos de Mascotas",
        "uso": "Usa /buscar/<producto> para buscar precios",
        "ejemplos": [
            "/buscar/perros",
            "/buscar/gatos",
            "/buscar/peces",
            "/buscar/aves"
        ]
    })

@app.route('/buscar/<producto>')
def buscar_producto(producto):
    producto_lower = producto.lower().strip()
    
    if producto_lower in PRODUCTOS:
        return jsonify({
            "exito": True,
            "producto": producto_lower,
            "resultados": PRODUCTOS[producto_lower],
            "total": len(PRODUCTOS[producto_lower])
        })
    else:
        return jsonify({
            "exito": False,
            "producto": producto,
            "mensaje": "Producto no encontrado",
            "productos_disponibles": list(PRODUCTOS.keys())
        }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

