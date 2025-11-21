# API de Búsqueda de Productos - Flask

## Descripción
API REST simple construida con Python Flask que proporciona información de precios de productos a través de un endpoint de búsqueda.

## Características
- Endpoint `/buscar/<producto>` que retorna precios de productos en formato JSON
- CORS habilitado para integración con Google Sites
- Base de datos de ejemplo con productos de tecnología
- Respuestas JSON estructuradas con manejo de errores

## Estructura del Proyecto
```
.
├── app.py              # Aplicación Flask principal
├── requirements.txt    # Dependencias Python
├── pyproject.toml      # Configuración del proyecto uv
└── .gitignore         # Archivos ignorados por git
```

## Stack Tecnológico
- **Backend**: Python 3.11
- **Framework**: Flask 3.1.2
- **CORS**: Flask-CORS 6.0.1
- **Package Manager**: uv

## Endpoints

### `GET /`
Retorna información sobre la API y ejemplos de uso.

### `GET /buscar/<producto>`
Busca productos por categoría y retorna precios.

**Productos disponibles:**
- laptop
- mouse
- teclado
- monitor
- auriculares
- telefono

**Ejemplo de respuesta exitosa:**
```json
{
  "exito": true,
  "producto": "laptop",
  "resultados": [
    {
      "nombre": "Laptop Dell XPS 13",
      "precio": 1299.99,
      "descripcion": "Ultrabook potente con Intel i7"
    }
  ],
  "total": 3
}
```

**Ejemplo de respuesta con error (404):**
```json
{
  "exito": false,
  "producto": "tablet",
  "mensaje": "Producto no encontrado",
  "productos_disponibles": ["laptop", "mouse", "teclado", "monitor", "auriculares", "telefono"]
}
```

## Integración con Google Sites
La API tiene CORS habilitado, lo que permite hacer peticiones desde Google Sites usando JavaScript:

```javascript
fetch('https://tu-repl-url.repl.co/buscar/laptop')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // Procesa los datos aquí
  });
```

## Configuración
- Host: 0.0.0.0
- Puerto: 5000
- Debug: Habilitado en desarrollo

## Fecha de Creación
21 de noviembre de 2025
