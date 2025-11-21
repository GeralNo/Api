from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Product Query API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "mensaje": "API de Búsqueda de Productos",
        "uso": "Usa /buscar/<producto> para buscar precios"
    }

@app.get("/buscar/{producto}")
def buscar_producto(producto: str):
    
    productos_demo = ["laptop", "mouse", "teclado", "monitor", "auriculares", "telefono"]
    if producto.lower() in productos_demo:
        return {"producto": producto, "precio": "Precio demo"}
    else:
        return {"producto": producto, "mensaje": "Producto no encontrado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

