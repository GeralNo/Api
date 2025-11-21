from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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
    
    return {
        "producto": producto,
        "mensaje": f"Resultados para '{producto}'",
        "uso": "Usa /buscar/<producto> para buscar precios"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
