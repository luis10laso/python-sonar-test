import requests

respuesta = requests.get("https://fakestoreapi.com/products/categories")

print(respuesta.json())