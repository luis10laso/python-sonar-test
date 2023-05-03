import requests

respuesta = requests.get("https://fakestoreapi.com/products")

print(respuesta.json())

print(respuesta.status_code)

nuevo_producto = {
    "titulo": "PC",
    "precio": 14,
    "description": "PC description",
    "category": "Electronic"
}

respuesta = requests.post("https://fakestoreapi.com/products", json=nuevo_producto)

print(respuesta)