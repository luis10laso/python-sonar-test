import requests
import random

respuesta = requests.get("https://fakestoreapi.com/products")

random_p = random.choice(respuesta.json())

print(random_p["title"], random_p["price"], random_p["description"])