from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PRODUCTOS = {
    "laptop": [
        {"nombre": "Laptop Dell XPS 13", "precio": 1299.99, "descripcion": "Ultrabook potente con Intel i7"},
        {"nombre": "Laptop HP Pavilion", "precio": 799.99, "descripcion": "Laptop versátil para uso diario"},
        {"nombre": "Laptop Lenovo ThinkPad", "precio": 1099.99, "descripcion": "Laptop empresarial duradera"}
    ],
    "mouse": [
        {"nombre": "Mouse Logitech MX Master 3", "precio": 99.99, "descripcion": "Mouse ergonómico inalámbrico"},
        {"nombre": "Mouse Razer DeathAdder", "precio": 69.99, "descripcion": "Mouse gaming de alta precisión"},
        {"nombre": "Mouse Microsoft Basic", "precio": 12.99, "descripcion": "Mouse básico con cable"}
    ],
    "teclado": [
        {"nombre": "Teclado Mecánico Keychron K2", "precio": 89.99, "descripcion": "Teclado mecánico compacto"},
        {"nombre": "Teclado Logitech K380", "precio": 39.99, "descripcion": "Teclado inalámbrico portátil"},
        {"nombre": "Teclado Corsair K95 RGB", "precio": 199.99, "descripcion": "Teclado gaming premium"}
    ],
    "monitor": [
        {"nombre": "Monitor LG UltraWide 34\"", "precio": 599.99, "descripcion": "Monitor panorámico para productividad"},
        {"nombre": "Monitor Dell 27\" 4K", "precio": 449.99, "descripcion": "Monitor 4K de alta resolución"},
        {"nombre": "Monitor ASUS Gaming 144Hz", "precio": 299.99, "descripcion": "Monitor gaming de alta tasa de refresco"}
    ],
    "auriculares": [
        {"nombre": "Auriculares Sony WH-1000XM5", "precio": 399.99, "descripcion": "Auriculares con cancelación de ruido premium"},
        {"nombre": "Auriculares HyperX Cloud II", "precio": 99.99, "descripcion": "Auriculares gaming cómodos"},
        {"nombre": "Auriculares JBL Tune 510BT", "precio": 49.99, "descripcion": "Auriculares inalámbricos económicos"}
    ],
    "telefono": [
        {"nombre": "iPhone 15 Pro", "precio": 999.99, "descripcion": "Smartphone Apple de última generación"},
        {"nombre": "Samsung Galaxy S24", "precio": 899.99, "descripcion": "Smartphone Android flagship"},
        {"nombre": "Google Pixel 8", "precio": 699.99, "descripcion": "Smartphone con Android puro y gran cámara"}
    ]
}

@app.route('/')
def home():
    return jsonify({
        "mensaje": "API de Búsqueda de Productos",
        "uso": "Usa /buscar/<producto> para buscar precios",
        "ejemplos": [
            "/buscar/laptop",
            "/buscar/mouse",
            "/buscar/teclado",
            "/buscar/monitor",
            "/buscar/auriculares",
            "/buscar/telefono"
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
