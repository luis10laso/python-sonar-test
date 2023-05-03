import requests

r1 = float(input("Primer numero: "))

r2 = float(input("Segundo numero: "))

if r2 < r1:
    y = r2
    r2 = r1
    r1 = y

respuesta = requests.get("https://fakestoreapi.com/products/category/electronics")

tuples = [(x["title"], x["price"]) for x in respuesta.json()]

for x, y in tuples:
    if y >= r1 and y<= r2:
        print(x, y)