from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


productos = [
    {"id": 1, "nombre": "Comida para perro", "categoria": "perro", "precio": 50},
    {"id": 2, "nombre": "Juguete para gato", "categoria": "gato", "precio": 20},
    {"id": 3, "nombre": "Collar para perro", "categoria": "perro", "precio": 15},
    {"id": 4, "nombre": "Rascador para gato", "categoria": "gato", "precio": 40},
    {"id": 5, "nombre": "Comida para gato", "categoria": "gato", "precio": 45}
]

@app.route('/')
def home():
    return "API de productos de mascotas funcionando correctamente"


@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

@app.route('/buscar/<categoria>', methods=['GET'])
def buscar_producto(categoria):
    resultados = [p for p in productos if p["categoria"].lower() == categoria.lower()]
    if resultados:
        return jsonify(resultados)
    else:
        return jsonify({"mensaje": f"No se encontraron productos para la categoría '{categoria}'"}), 404

@app.route('/productos', methods=['POST'])
def agregar_producto():
    nuevo_producto = request.get_json()
    if "nombre" in nuevo_producto and "categoria" in nuevo_producto and "precio" in nuevo_producto:
        nuevo_producto["id"] = len(productos) + 1
        productos.append(nuevo_producto)
        return jsonify(nuevo_producto), 201
    else:
        return jsonify({"mensaje": "Datos incompletos"}), 400

if __name__ == '__main__':
    app.run(debug=True)

      

