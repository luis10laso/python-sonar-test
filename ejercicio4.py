import requests

respuesta = requests.get("https://fakestoreapi.com/products/category/electronics")

tuples = [(x["title"], x["price"]) for x in respuesta.json()]

print(tuples)