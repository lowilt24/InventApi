from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Producto(BaseModel):
    nombre: str
    cantidad: int
    precio: float

inventario: list[Producto] = []


@app.get("/")
def read_root():
    return {"message": "InventApi funcionando"}


@app.post("/productos")
def crear_producto(producto: Producto):
    inventario.append(producto)
    return producto


@app.get("/productos")
def listar_productos():
    return inventario